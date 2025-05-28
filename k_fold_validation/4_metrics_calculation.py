import os
import pandas as pd
import numpy as np
from sklearn.metrics import (
    roc_auc_score, confusion_matrix, classification_report,
    accuracy_score, precision_score, recall_score, f1_score,
    roc_curve
)
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import logging

class MetricsCalculator:
    def __init__(self):
        """Initialize metrics calculator"""
        # Set directories first
        self.base_dir = os.path.dirname(os.path.abspath(__file__))  # Get current directory
        self.data_dir = os.path.join(self.base_dir, 'processed_data')
        self.logs_dir = os.path.join(self.base_dir, 'logs')
        self.output_dir = os.path.join(self.base_dir, 'metrics_results')
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.logs_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Setup logging
        self.setup_logging()
        
        self.logger.info("\n=== Initializing Metrics Calculator ===")
        self.logger.info(f"Output directory created: {self.output_dir}")
        
    def setup_logging(self):
        """Setup logging configuration"""
        # Generate log filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(self.logs_dir, f'metrics_calculation_{timestamp}.log')
        
        # Configure logger
        self.logger = logging.getLogger('MetricsCalculator')
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
    
    def plot_roc_curves(self, y_true_onehot, y_pred_onehot, timestamp):
        """Plot ROC curves"""
        plt.figure(figsize=(10, 8))
        
        # Plot ROC curve for each score
        for i in range(3):  # 3 scores
            fpr, tpr, _ = roc_curve(y_true_onehot.iloc[:, i], y_pred_onehot.iloc[:, i])
            roc_auc = roc_auc_score(y_true_onehot.iloc[:, i], y_pred_onehot.iloc[:, i])
            plt.plot(fpr, tpr, label=f'Score {i+1} (AUC = {roc_auc:.2f})')
        
        # Plot diagonal line
        plt.plot([0, 1], [0, 1], 'k--')
        
        # Set plot properties
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('ROC Curves')
        plt.legend(loc="lower right")
        
        # Save plot
        plt.savefig(os.path.join(self.output_dir, f'roc_curves_{timestamp}.png'))
        plt.close()
    
    def calculate_metrics(self, input_file: str):
        """Calculate evaluation metrics"""
        self.logger.info("\n=== Starting Metrics Calculation ===")
        try:
            # Read data
            self.logger.info(f"Reading file: {input_file}")
            df = pd.read_excel(input_file)
            
            # Check required columns
            required_columns = ['Score', 'Predicted_Score']
            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                raise ValueError(f"Missing required columns: {missing_columns}")
            
            # Get true and predicted labels
            y_true = df['Score']
            y_pred = df['Predicted_Score']
            
            # Calculate confusion matrix
            cm = confusion_matrix(y_true, y_pred)
            self.logger.info("\nConfusion Matrix:")
            self.logger.info(cm)
            
            # Plot confusion matrix heatmap
            plt.figure(figsize=(10, 8))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                       xticklabels=['Score 1', 'Score 2', 'Score 3'],
                       yticklabels=['Score 1', 'Score 2', 'Score 3'])
            plt.title('Confusion Matrix')
            plt.xlabel('Predicted Score')
            plt.ylabel('True Score')
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            plt.savefig(os.path.join(self.output_dir, f'confusion_matrix_{timestamp}.png'))
            plt.close()
            
            # Calculate classification report
            report = classification_report(y_true, y_pred, output_dict=True)
            self.logger.info("\nClassification Report:")
            self.logger.info(classification_report(y_true, y_pred))
            
            # Calculate ROC AUC (convert labels to one-hot encoding)
            y_true_onehot = pd.get_dummies(y_true)
            y_pred_onehot = pd.get_dummies(y_pred)
            roc_auc = roc_auc_score(y_true_onehot, y_pred_onehot, multi_class='ovr')
            self.logger.info(f"\nROC AUC: {roc_auc:.4f}")
            
            # Plot ROC curves
            self.plot_roc_curves(y_true_onehot, y_pred_onehot, timestamp)
            
            # Calculate other metrics
            accuracy = accuracy_score(y_true, y_pred)
            precision = precision_score(y_true, y_pred, average='weighted')
            recall = recall_score(y_true, y_pred, average='weighted')
            f1 = f1_score(y_true, y_pred, average='weighted')
            
            self.logger.info(f"\nAccuracy: {accuracy:.4f}")
            self.logger.info(f"Weighted Precision: {precision:.4f}")
            self.logger.info(f"Weighted Recall: {recall:.4f}")
            self.logger.info(f"Weighted F1 Score: {f1:.4f}")
            
            # Save results to Excel
            results = {
                'Metric': ['ROC AUC', 'Accuracy', 'Precision', 'Recall', 'F1 Score'],
                'Value': [roc_auc, accuracy, precision, recall, f1]
            }
            results_df = pd.DataFrame(results)
            
            # Add metrics for each score
            for score in range(1, 4):
                results_df = pd.concat([results_df, pd.DataFrame({
                    'Metric': [f'Precision (Score {score})', f'Recall (Score {score})', f'F1 (Score {score})'],
                    'Value': [
                        report[str(score)]['precision'],
                        report[str(score)]['recall'],
                        report[str(score)]['f1-score']
                    ]
                })])
            
            # Save results
            output_file = os.path.join(self.output_dir, f'metrics_results_{timestamp}.xlsx')
            results_df.to_excel(output_file, index=False)
            self.logger.info(f"\nResults saved to: {output_file}")
            
            return results_df
            
        except Exception as e:
            self.logger.error(f"Error calculating metrics: {str(e)}")
            raise

def main():
    try:
        # Create metrics calculator
        calculator = MetricsCalculator()
        
        # Find the latest evaluation results file
        evaluation_dir = os.path.join(calculator.base_dir, 'evaluation_results')
        evaluation_files = [f for f in os.listdir(evaluation_dir) if f.startswith('policy_score_with_predictions_final_')]
        if not evaluation_files:
            raise FileNotFoundError("No evaluation results found")
        
        # Get the latest file
        latest_file = max(evaluation_files)
        input_file = os.path.join(evaluation_dir, latest_file)
        
        # Calculate metrics
        results = calculator.calculate_metrics(input_file)
        
        print("\nCalculation complete! Results saved to metrics_results directory")
        
    except Exception as e:
        print(f"\nProgram execution error: {str(e)}")
        print("Please check the log file for details")

if __name__ == "__main__":
    main() 