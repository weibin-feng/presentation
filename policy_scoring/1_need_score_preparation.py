import os
import json
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import logging
from datetime import datetime

class NeedScorePreparator:
    def __init__(self, model_name='all-mpnet-base-v2'):
        """Initialize data preparator"""
        # Setup logging
        self.setup_logging()
        
        # Initialize text encoder
        self.logger.info("Initializing text encoder...")
        self.encoder = SentenceTransformer(model_name)
        
        # Setup directories
        self.data_dir = 'policy_scoring/need_score_processed'
        os.makedirs(self.data_dir, exist_ok=True)
        
    def setup_logging(self):
        """Setup logging configuration"""
        # Create logs directory
        logs_dir = 'policy_scoring/logs'
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
            
        # Generate log filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = f'{logs_dir}/need_score_preparation_{timestamp}.log'
        
        # Configure logger
        self.logger = logging.getLogger('NeedScorePreparator')
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
    
    def load_data(self, reference_file: str = 'policy_scoring/policy_score.xlsx', target_file: str = 'policy_scoring/need_score.xlsx') -> tuple:
        """Load reference and target data"""
        self.logger.info(f"Loading reference data: {reference_file}")
        reference_df = pd.read_excel(reference_file)
        
        self.logger.info(f"Loading target data: {target_file}")
        target_df = pd.read_excel(target_file)
        
        # Validate required columns
        required_columns = ['Policy_ID', 'Policy_Name', 'Type', 'Description']
        for df, name in [(reference_df, 'Reference data'), (target_df, 'Target data')]:
            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                raise ValueError(f"{name} missing required columns: {missing_columns}")
            
            # Check for null values
            for col in required_columns:
                null_count = df[col].isna().sum()
                if null_count > 0:
                    self.logger.warning(f"{name} has {null_count} null values in {col} column")
                    # Show Policy_IDs with null values
                    null_ids = df[df[col].isna()]['Policy_ID'].tolist()
                    self.logger.warning(f"Policy_IDs with null values: {null_ids}")
            
            # Check for empty strings
            for col in ['Type', 'Description']:
                empty_count = (df[col] == '').sum()
                if empty_count > 0:
                    self.logger.warning(f"{name} has {empty_count} empty strings in {col} column")
                    # Show Policy_IDs with empty strings
                    empty_ids = df[df[col] == '']['Policy_ID'].tolist()
                    self.logger.warning(f"Policy_IDs with empty strings: {empty_ids}")
        
        # Show data distribution
        self.logger.info(f"\nReference data: {len(reference_df)} records")
        if 'Score' in reference_df.columns:
            score_dist = reference_df['Score'].value_counts().sort_index()
            self.logger.info("Reference data score distribution:")
            for score, count in score_dist.items():
                self.logger.info(f"Score {score}: {count} records ({count/len(reference_df)*100:.1f}%)")
        
        self.logger.info(f"\nTarget data: {len(target_df)} records")
        
        return reference_df, target_df
    
    def create_embeddings(self, df: pd.DataFrame) -> np.ndarray:
        """Create text embeddings"""
        self.logger.info("Creating text embeddings...")
        
        try:
            # Combine Type and Description
            texts = df['Type'] + ' ' + df['Description']
            self.logger.info(f"Number of texts: {len(texts)}")
            
            # Check for empty texts
            empty_texts = texts[texts.isna() | (texts == '')]
            if not empty_texts.empty:
                self.logger.warning(f"Found {len(empty_texts)} empty texts")
                self.logger.warning(f"Indices of empty texts: {empty_texts.index.tolist()}")
            
            # Generate embeddings
            self.logger.info("Starting embedding generation...")
            try:
                # Process in batches of 100
                batch_size = 100
                all_embeddings = []
                
                for i in range(0, len(texts), batch_size):
                    batch_texts = texts[i:i+batch_size]
                    self.logger.info(f"Processing batch {i//batch_size + 1}, containing {len(batch_texts)} texts")
                    
                    batch_embeddings = self.encoder.encode(batch_texts.tolist(), show_progress_bar=True)
                    all_embeddings.append(batch_embeddings)
                
                # Combine all batch embeddings
                embeddings = np.vstack(all_embeddings)
                self.logger.info(f"Embedding generation complete, type: {type(embeddings)}")
                
            except Exception as e:
                self.logger.error(f"Error generating embeddings: {str(e)}")
                raise
            
            # Ensure numpy array
            if not isinstance(embeddings, np.ndarray):
                self.logger.info("Converting embeddings to numpy array...")
                embeddings = np.array(embeddings)
            
            # Ensure float32 type
            self.logger.info("Converting vectors to float32 type...")
            embeddings = embeddings.astype('float32')
            
            self.logger.info(f"Successfully created {len(embeddings)} embedding vectors, shape: {embeddings.shape}")
            return embeddings
            
        except Exception as e:
            self.logger.error(f"Error creating embeddings: {str(e)}")
            raise
    
    def create_faiss_index(self, embeddings: np.ndarray) -> tuple:
        """Create FAISS index"""
        self.logger.info("Creating FAISS index...")
        
        # Add debug logs
        self.logger.info(f"embeddings type: {type(embeddings)}")
        self.logger.info(f"embeddings shape: {embeddings.shape}")
        
        # Ensure float32 type and L2 normalization
        embeddings = embeddings.astype('float32')
        self.logger.info("Vectors converted to float32 type")
        
        faiss.normalize_L2(embeddings)
        self.logger.info("Vectors L2 normalized")
        
        # Create index (using dot product)
        dimension = embeddings.shape[1]
        self.logger.info(f"Vector dimension: {dimension}")
        
        index = faiss.IndexFlatIP(dimension)  # Using dot product
        self.logger.info("FAISS index created")
        
        # Add vectors
        index.add(embeddings)
        self.logger.info("Vectors added to index")
        
        # Save index
        index_path = os.path.join(self.data_dir, 'faiss_index.index')
        faiss.write_index(index, index_path)
        
        self.logger.info(f"FAISS index saved to: {index_path}")
        return index, embeddings
    
    def process_data(self):
        """Main data processing function"""
        try:
            # Load data
            reference_df, target_df = self.load_data()
            
            # Create embeddings
            reference_embeddings = self.create_embeddings(reference_df)
            target_embeddings = self.create_embeddings(target_df)
            
            # Save processed data
            processed_data = {
                'reference_data': reference_df.to_dict(orient='records'),
                'reference_embeddings': reference_embeddings.tolist(),
                'target_data': target_df.to_dict(orient='records'),
                'target_embeddings': target_embeddings.tolist()
            }
            
            with open(os.path.join(self.data_dir, 'processed_data.json'), 'w', encoding='utf-8') as f:
                json.dump(processed_data, f, ensure_ascii=False, indent=2)
            
            # Create FAISS index
            self.create_faiss_index(reference_embeddings)
            
            self.logger.info("\nData processing complete")
            
        except Exception as e:
            self.logger.error(f"Error during data processing: {str(e)}")
            raise

def main():
    try:
        preparator = NeedScorePreparator()
        preparator.process_data()
        print("\nData processing complete!")
        print("Processed data saved to policy_scoring/need_score_processed directory")
        print("Please check the log file for detailed data distribution information")
        
    except Exception as e:
        print(f"\nProgram execution error: {str(e)}")
        print("Please check the log file for details")

if __name__ == "__main__":
    main() 