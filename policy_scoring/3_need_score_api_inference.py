import os
import json
import logging
from datetime import datetime
from typing import Dict, List, Optional
import pandas as pd
from tqdm import tqdm
from openai import OpenAI
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial

class NeedScorePolicyScorer:
    def __init__(self, api_key: str, model_name: str = "deepseek-chat", batch_size: int = 5, max_workers: int = 4):
        """Initialize policy scorer"""
        # Setup logging
        self.setup_logging()
        
        self.logger.info("\n=== Initializing Policy Scorer ===")
        
        # Initialize API client
        self.logger.info("\n1. Initializing API client...")
        try:
            self.client = OpenAI(
                api_key=api_key,
                base_url="https://api.deepseek.com"
            )
            self.model_name = model_name
            self.batch_size = batch_size
            self.max_workers = max_workers
            self.logger.info(f"API client initialized, using model: {model_name}")
            self.logger.info(f"Batch size: {batch_size}, Max workers: {max_workers}")
        except Exception as e:
            self.logger.error(f"API client initialization failed: {str(e)}")
            raise
        
        # Create output directory
        self.output_dir = 'policy_scoring/evaluation_results'
        os.makedirs(self.output_dir, exist_ok=True)
        self.logger.info(f"Output directory created: {self.output_dir}")
        
    def setup_logging(self):
        """Setup logging configuration"""
        # Create logs directory
        logs_dir = 'policy_scoring/logs'
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
            
        # Generate log filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = f'{logs_dir}/need_score_api_inference_{timestamp}.log'
        
        # Configure logger
        self.logger = logging.getLogger('NeedScorePolicyScorer')
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
    
    def extract_json_from_response(self, response: str) -> Optional[Dict]:
        """Extract JSON from API response"""
        try:
            # Find JSON start and end positions
            start_idx = response.find('{')
            end_idx = response.rfind('}') + 1
            
            if start_idx == -1 or end_idx == 0:
                self.logger.error("No JSON response found")
                return None
            
            # Extract JSON string
            json_str = response[start_idx:end_idx]
            
            # Parse JSON
            result = json.loads(json_str)
            
            # Validate required fields
            required_fields = ['Score', 'Confidence', 'Explanation', 'Inference_Chain', 'Comparable_Cases']
            missing_fields = [field for field in required_fields if field not in result]
            if missing_fields:
                self.logger.error(f"Missing required fields: {missing_fields}")
                return None
            
            # Validate and convert field types
            try:
                # Validate Score
                if not isinstance(result['Score'], int):
                    result['Score'] = int(result['Score'])
                if result['Score'] not in [1, 2, 3]:
                    self.logger.error(f"Invalid score: {result['Score']}")
                    return None
                
                # Validate Confidence
                if not isinstance(result['Confidence'], (int, float)):
                    result['Confidence'] = float(result['Confidence'])
                if not (0 <= result['Confidence'] <= 10):
                    self.logger.error(f"Invalid confidence: {result['Confidence']}")
                    return None
                
                # Validate Explanation
                if not isinstance(result['Explanation'], dict):
                    if isinstance(result['Explanation'], str):
                        try:
                            result['Explanation'] = json.loads(result['Explanation'])
                        except:
                            self.logger.error("Explanation cannot be converted to dictionary type")
                            return None
                    else:
                        self.logger.error("Explanation must be dictionary type")
                        return None
                
                # Validate Inference_Chain
                if not isinstance(result['Inference_Chain'], list):
                    if isinstance(result['Inference_Chain'], str):
                        try:
                            result['Inference_Chain'] = json.loads(result['Inference_Chain'])
                        except:
                            self.logger.error("Inference_Chain cannot be converted to list type")
                            return None
                    else:
                        self.logger.error("Inference_Chain must be list type")
                        return None
                
                # Validate Comparable_Cases
                if not isinstance(result['Comparable_Cases'], list):
                    if isinstance(result['Comparable_Cases'], str):
                        try:
                            result['Comparable_Cases'] = json.loads(result['Comparable_Cases'])
                        except:
                            self.logger.error("Comparable_Cases cannot be converted to list type")
                            return None
                    else:
                        self.logger.error("Comparable_Cases must be list type")
                        return None
                
                return result
                
            except (ValueError, TypeError) as e:
                self.logger.error(f"Field type conversion failed: {str(e)}")
                return None
            
        except json.JSONDecodeError as e:
            self.logger.error(f"JSON parsing error: {str(e)}")
            return None
        except Exception as e:
            self.logger.error(f"Error extracting JSON: {str(e)}")
            return None
    
    def score_policy(self, prompt: str) -> Optional[Dict]:
        """Score a single policy"""
        try:
            # Call API
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are a professional policy evaluation assistant. Your task is to assess the bindingness of policies and return the result strictly in JSON format."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                max_tokens=2000,
                stream=False
            )
            
            # Extract response content
            content = response.choices[0].message.content
            
            # Extract JSON
            result = self.extract_json_from_response(content)
            if result is None:
                return None
            
            return result
            
        except Exception as e:
            self.logger.error(f"Error during scoring: {str(e)}")
            return None
    
    def process_batch(self, batch: List[tuple], batch_num: int, total_batches: int, original_df: pd.DataFrame, processed_count: int) -> tuple:
        """Process a batch of policies"""
        results = []
        self.logger.info(f"Processing batch {batch_num}/{total_batches}, {len(batch)} files")
        
        for i, (file, prompt) in enumerate(batch, 1):
            try:
                result = self.score_policy(prompt)
                if result is not None:
                    results.append((file, result))
                    # Update DataFrame immediately
                    policy_id = f"policy/{file.replace('prompt_policy_', '').replace('.txt', '')}"
                    mask = original_df['Policy_ID'] == policy_id
                    if mask.any():
                        # Update basic fields
                        original_df.loc[mask, 'Predicted_Score'] = result['Score']
                        original_df.loc[mask, 'Confidence'] = result['Confidence']
                        
                        # Parse Explanation
                        explanation = result['Explanation']
                        original_df.loc[mask, 'Explanation'] = json.dumps(explanation, ensure_ascii=False)
                        original_df.loc[mask, 'Legal_Language'] = explanation.get('Legal_Language', '')
                        original_df.loc[mask, 'Source_of_Authority'] = explanation.get('Source_of_Authority', '')
                        original_df.loc[mask, 'Enforcement_Mechanism'] = explanation.get('Enforcement_Mechanism', '')
                        original_df.loc[mask, 'Obligations'] = explanation.get('Obligations', '')
                        original_df.loc[mask, 'Optionality_or_Incentives'] = explanation.get('Optionality_or_Incentives', '')
                        
                        # Parse Inference_Chain
                        inference_chain = result['Inference_Chain']
                        original_df.loc[mask, 'Inference_Chain'] = json.dumps(inference_chain, ensure_ascii=False)
                        original_df.loc[mask, 'Inference_Steps'] = '\n'.join(inference_chain)
                        
                        # Parse Comparable_Cases
                        comparable_cases = result['Comparable_Cases']
                        original_df.loc[mask, 'Comparable_Cases'] = json.dumps(comparable_cases, ensure_ascii=False)
                        
                        # Extract similar case information
                        if len(comparable_cases) >= 1:
                            case1 = comparable_cases[0]
                            original_df.loc[mask, 'Similar_Case_1'] = case1.get('Case_Name', '')
                            original_df.loc[mask, 'Similar_Case_1_Score'] = case1.get('Score', '')
                            original_df.loc[mask, 'Similar_Case_1_Similarity'] = case1.get('Similarity', '')
                        
                        if len(comparable_cases) >= 2:
                            case2 = comparable_cases[1]
                            original_df.loc[mask, 'Similar_Case_2'] = case2.get('Case_Name', '')
                            original_df.loc[mask, 'Similar_Case_2_Score'] = case2.get('Score', '')
                            original_df.loc[mask, 'Similar_Case_2_Similarity'] = case2.get('Similarity', '')
                        
                        # Update processed count
                        processed_count += 1
                        
                        # Save every 100 files
                        if processed_count % 100 == 0:
                            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                            output_file = os.path.join(self.output_dir, f'need_score_with_predictions_{timestamp}.xlsx')
                            original_df.to_excel(output_file, index=False)
                            self.logger.info(f"Processed {processed_count} files, saved results: {output_file}")
                    else:
                        self.logger.error(f"Policy ID not found: {policy_id}")
            except Exception as e:
                self.logger.error(f"Error processing file {file}: {str(e)}")
        
        self.logger.info(f"Batch {batch_num}/{total_batches} complete, successful: {len(results)}/{len(batch)}")
        return results, processed_count

    def process_policies(self, prompts_dir: str = 'policy_scoring/prompts'):
        """Process all policies"""
        self.logger.info("=== Starting Policy Processing ===")
        try:
            # Check if prompts directory exists
            if not os.path.exists(prompts_dir):
                self.logger.error(f"Prompts directory not found: {prompts_dir}")
                raise FileNotFoundError(f"Prompts directory not found: {prompts_dir}")
            
            # Get all prompt files
            prompt_files = [f for f in os.listdir(prompts_dir) if f.startswith('prompt_') and f.endswith('.txt')]
            if not prompt_files:
                self.logger.error(f"No prompt files found in directory {prompts_dir}")
                raise FileNotFoundError(f"No prompt files found in directory {prompts_dir}")
            
            total_files = len(prompt_files)
            self.logger.info(f"Found {total_files} prompt files")
            
            # Read original data file
            original_df = pd.read_excel('policy_scoring/need_score.xlsx')
            
            # Add prediction result columns
            original_df['Predicted_Score'] = None
            original_df['Confidence'] = None
            original_df['Explanation'] = None
            original_df['Inference_Chain'] = None
            original_df['Comparable_Cases'] = None
            
            # Add detailed analysis columns
            original_df['Legal_Language'] = None
            original_df['Source_of_Authority'] = None
            original_df['Enforcement_Mechanism'] = None
            original_df['Obligations'] = None
            original_df['Optionality_or_Incentives'] = None
            original_df['Inference_Steps'] = None
            original_df['Similar_Case_1'] = None
            original_df['Similar_Case_2'] = None
            original_df['Similar_Case_1_Score'] = None
            original_df['Similar_Case_2_Score'] = None
            original_df['Similar_Case_1_Similarity'] = None
            original_df['Similar_Case_2_Similarity'] = None
            
            # Prepare batch data
            batches = []
            current_batch = []
            
            for i, file in enumerate(prompt_files, 1):
                try:
                    with open(os.path.join(prompts_dir, file), 'r', encoding='utf-8') as f:
                        prompt = f.read()
                    current_batch.append((file, prompt))
                    
                    if len(current_batch) >= self.batch_size:
                        batches.append(current_batch)
                        current_batch = []
                except Exception as e:
                    self.logger.error(f"Error reading file {file}: {str(e)}")
            
            if current_batch:
                batches.append(current_batch)
            
            total_batches = len(batches)
            self.logger.info(f"Batch data preparation complete, {total_batches} batches")
            
            # Process batches using thread pool
            processed_files = 0
            successful_files = 0
            processed_count = 0
            
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = [
                    executor.submit(self.process_batch, batch, i+1, total_batches, original_df, processed_count)
                    for i, batch in enumerate(batches)
                ]
                
                for future in tqdm(as_completed(futures), total=len(futures), desc="Processing batches"):
                    try:
                        batch_results, processed_count = future.result()
                        processed_files += len(batch_results)
                        successful_files += len(batch_results)
                        self.logger.info(f"Progress: {processed_files}/{total_files}, successful: {successful_files}/{processed_files}")
                    except Exception as e:
                        self.logger.error(f"Error processing batch: {str(e)}")
            
            self.logger.info(f"All batches processed, total: {processed_files}/{total_files} files")
            
            # Generate final output filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            final_output_file = os.path.join(self.output_dir, f'need_score_with_predictions_final_{timestamp}.xlsx')
            
            # Save final results
            original_df.to_excel(final_output_file, index=False)
            self.logger.info(f"Final results saved to: {final_output_file}")
            
            return original_df
            
        except Exception as e:
            self.logger.error(f"Error processing policies: {str(e)}")
            raise

def main():
    try:
        # Set API key
        api_key = "sk-d77ee9363560463b9c8c6eb2adca3704"
        
        # Create scorer and process policies
        scorer = NeedScorePolicyScorer(
            api_key=api_key,
            batch_size=10,  # Process 10 files per batch
            max_workers=5  # Use 5 threads
        )
        
        # Ensure prompts directory exists
        prompts_dir = 'policy_scoring/prompts'
        if not os.path.exists(prompts_dir):
            os.makedirs(prompts_dir)
            print(f"Created prompts directory: {prompts_dir}")
            print("Please place prompt files in this directory and run the program again")
            return
        
        # Process policies
        results = scorer.process_policies()
        
        if results is not None:
            print(f"\nSuccessfully processed {len(results)} policies")
            print(f"Results saved to policy_scoring/evaluation_results directory")
        else:
            print("\nProcessing failed, please check the log file for details")
            
    except Exception as e:
        print(f"\nProgram execution error: {str(e)}")
        print("Please check the log file for details")

if __name__ == "__main__":
    main() 