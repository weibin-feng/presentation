import os
import json
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedKFold
from sentence_transformers import SentenceTransformer
import faiss
import logging
from datetime import datetime
from collections import defaultdict

class DataPreparator:
    def __init__(self, model_name='all-mpnet-base-v2'):
        """Initialize data preparator"""
        # Set directories first
        self.base_dir = os.path.dirname(os.path.abspath(__file__))  # Get current directory
        self.data_dir = os.path.join(self.base_dir, 'processed_data')
        self.logs_dir = os.path.join(self.base_dir, 'logs')
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.logs_dir, exist_ok=True)
        
        # Setup logging
        self.setup_logging()
        
        # Initialize text encoder
        self.logger.info("Initializing text encoder...")
        self.encoder = SentenceTransformer(model_name)
        
    def setup_logging(self):
        """Setup logging configuration"""
        # Generate log filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(self.logs_dir, f'data_preparation_{timestamp}.log')
        
        # Configure logger
        self.logger = logging.getLogger('DataPreparator')
        self.logger.setLevel(logging.INFO)
        
        # File handler
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Set log format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # Add handlers
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
        self.logger.info(f"Log file created: {log_file}")
    
    def load_data(self, file_path: str = None) -> pd.DataFrame:
        """Load data"""
        if file_path is None:
            file_path = os.path.join(self.base_dir, 'policy score.xlsx')
            
        self.logger.info(f"Loading data: {file_path}")
        df = pd.read_excel(file_path)
        
        # Validate required columns
        required_columns = ['Policy_ID', 'Policy_Name', 'Type', 'Description', 'Score']
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
        
        # Display original data distribution
        score_dist = df['Score'].value_counts().sort_index()
        self.logger.info("\nOriginal data score distribution:")
        for score, count in score_dist.items():
            self.logger.info(f"Score {score}: {count} items ({count/len(df)*100:.1f}%)")
        
        self.logger.info(f"Successfully loaded {len(df)} items")
        return df
    
    def create_embeddings(self, df: pd.DataFrame) -> np.ndarray:
        """Create text embeddings"""
        self.logger.info("Creating text embeddings...")
        
        # Combine Type and Description
        texts = df['Type'] + ' ' + df['Description']
        
        # Generate embeddings
        embeddings = self.encoder.encode(texts, show_progress_bar=True)
        
        # Ensure vectors are float32 type
        embeddings = embeddings.astype('float32')
        
        self.logger.info(f"Successfully created {len(embeddings)} embedding vectors")
        return embeddings
    
    def create_folds(self, df: pd.DataFrame, n_folds: int = 5) -> list:
        """Create stratified k-fold splits"""
        self.logger.info(f"\nCreating {n_folds}-fold stratified splits...")
        
        # Use Score for stratification
        skf = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=42)
        
        # Create splits
        folds = []
        total_dist = defaultdict(lambda: defaultdict(int))
        
        for fold_idx, (train_idx, test_idx) in enumerate(skf.split(df, df['Score'])):
            fold = {
                'train': df.iloc[train_idx],
                'test': df.iloc[test_idx]
            }
            folds.append(fold)
            
            # Calculate distribution
            train_dist = fold['train']['Score'].value_counts().sort_index()
            test_dist = fold['test']['Score'].value_counts().sort_index()
            
            # Update total distribution
            for score, count in train_dist.items():
                total_dist['train'][score] += count
            for score, count in test_dist.items():
                total_dist['test'][score] += count
            
            # Log fold distribution
            self.logger.info(f"\nFold {fold_idx + 1} distribution:")
            self.logger.info("Training set:")
            for score, count in train_dist.items():
                self.logger.info(f"  Score {score}: {count} items ({count/len(fold['train'])*100:.1f}%)")
            self.logger.info("Test set:")
            for score, count in test_dist.items():
                self.logger.info(f"  Score {score}: {count} items ({count/len(fold['test'])*100:.1f}%)")
        
        # Display overall distribution
        self.logger.info("\nOverall distribution:")
        self.logger.info("Total training set:")
        for score in sorted(total_dist['train'].keys()):
            count = total_dist['train'][score]
            self.logger.info(f"  Score {score}: {count} items ({count/(len(df)*(n_folds-1)/n_folds)*100:.1f}%)")
        self.logger.info("Total test set:")
        for score in sorted(total_dist['test'].keys()):
            count = total_dist['test'][score]
            self.logger.info(f"  Score {score}: {count} items ({count/(len(df)/n_folds)*100:.1f}%)")
        
        return folds
    
    def create_faiss_index(self, embeddings: np.ndarray, fold_idx: int) -> tuple:
        """Create FAISS index"""
        self.logger.info(f"Creating FAISS index for fold {fold_idx + 1}...")
        
        # Ensure vectors are float32 type and L2 normalized
        embeddings = embeddings.astype('float32')
        faiss.normalize_L2(embeddings)
        
        # Create index (using dot product)
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatIP(dimension)  # Use dot product
        
        # Add vectors
        index.add(embeddings)
        
        # Save index
        index_path = os.path.join(self.data_dir, f'faiss_index_fold_{fold_idx}.index')
        faiss.write_index(index, index_path)
        
        self.logger.info(f"FAISS index saved to: {index_path}")
        return index, embeddings
    
    def process_data(self):
        """Main data processing function"""
        try:
            # Load data
            df = self.load_data()
            
            # Create embeddings
            embeddings = self.create_embeddings(df)
            
            # Create folds
            folds = self.create_folds(df)
            
            # Save processed data
            processed_data = {
                'data': df.to_dict(orient='records'),
                'embeddings': embeddings.tolist()
            }
            
            with open(os.path.join(self.data_dir, 'processed_data.json'), 'w', encoding='utf-8') as f:
                json.dump(processed_data, f, ensure_ascii=False, indent=2)
            
            # Create FAISS index for each fold
            for fold_idx, fold in enumerate(folds):
                # Get training set indices
                train_indices = fold['train'].index
                
                # Create FAISS index for this fold
                self.create_faiss_index(embeddings[train_indices], fold_idx)
            
            self.logger.info("\nData processing completed")
            
        except Exception as e:
            self.logger.error(f"Error during data processing: {str(e)}")
            raise

def main():
    try:
        preparator = DataPreparator()
        preparator.process_data()
        print("\nData processing completed!")
        print("Processed data saved to k_fold_validation/processed_data directory")
        print("Please check the log file for detailed score distribution information")
        
    except Exception as e:
        print(f"\nProgram execution error: {str(e)}")
        print("Please check the log file for details")

if __name__ == "__main__":
    main() 