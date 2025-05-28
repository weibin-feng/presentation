import os
import json
import time
import logging
from datetime import datetime
from typing import Dict, List, Optional
import pandas as pd
from tqdm import tqdm
from openai import OpenAI

class PolicyScorer:
    def __init__(self, api_key: str, model_name: str = "deepseek-chat"):
        """Initialize policy scorer"""
        # Set directories first
        self.base_dir = os.path.dirname(os.path.abspath(__file__))  # Get current directory
        self.data_dir = os.path.join(self.base_dir, 'processed_data')
        self.logs_dir = os.path.join(self.base_dir, 'logs')
        self.prompts_dir = os.path.join(self.base_dir, 'prompts')
        self.output_dir = os.path.join(self.base_dir, 'evaluation_results')
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.logs_dir, exist_ok=True)
        os.makedirs(self.prompts_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)
        
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
            self.logger.info(f"API client initialized successfully, using model: {model_name}")
        except Exception as e:
            self.logger.error(f"API client initialization failed: {str(e)}")
            raise
        
        self.logger.info(f"Output directory created: {self.output_dir}")
        
    def setup_logging(self):
        """Setup logging configuration"""
        # Generate log filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(self.logs_dir, f'api_inference_{timestamp}.log')
        
        # Configure logger
        self.logger = logging.getLogger('PolicyScorer')
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
        self.logger.info("\n=== Extracting JSON Response ===")
        try:
            # Find JSON start and end positions
            start_idx = response.find('{')
            end_idx = response.rfind('}') + 1
            
            if start_idx == -1 or end_idx == 0:
                self.logger.error("No JSON response found")
                self.logger.error(f"Original response content: {response}")
                return None
            
            # Extract JSON string
            json_str = response[start_idx:end_idx]
            self.logger.info("Successfully extracted JSON string")
            self.logger.info(f"Extracted JSON string: {json_str}")
            
            # Parse JSON
            result = json.loads(json_str)
            self.logger.info("Successfully parsed JSON")
            self.logger.info(f"Parsed JSON object: {json.dumps(result, ensure_ascii=False, indent=2)}")
            
            # Validate required fields
            required_fields = ['Score', 'Confidence', 'Explanation', 'Inference_Chain', 'Comparable_Cases']
            missing_fields = [field for field in required_fields if field not in result]
            if missing_fields:
                self.logger.error(f"Missing required fields: {missing_fields}")
                self.logger.error(f"Current fields: {list(result.keys())}")
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
                            self.logger.error(f"Cannot convert Explanation to dictionary, current value: {result['Explanation']}")
                            return None
                    else:
                        self.logger.error(f"Explanation must be dictionary type, current type: {type(result['Explanation'])}")
                        return None
                
                # Validate Inference_Chain
                if not isinstance(result['Inference_Chain'], list):
                    if isinstance(result['Inference_Chain'], str):
                        try:
                            result['Inference_Chain'] = json.loads(result['Inference_Chain'])
                        except:
                            self.logger.error(f"Cannot convert Inference_Chain to list, current value: {result['Inference_Chain']}")
                            return None
                    else:
                        self.logger.error(f"Inference_Chain must be list type, current type: {type(result['Inference_Chain'])}")
                        return None
                
                # Validate Comparable_Cases
                if not isinstance(result['Comparable_Cases'], (dict, list)):
                    self.logger.info(f"Comparable_Cases current type: {type(result['Comparable_Cases'])}")
                    self.logger.info(f"Comparable_Cases current value: {result['Comparable_Cases']}")
                    
                    if isinstance(result['Comparable_Cases'], str):
                        try:
                            # Try direct parsing
                            result['Comparable_Cases'] = json.loads(result['Comparable_Cases'])
                        except:
                            try:
                                # If direct parsing fails, try fixing common format issues
                                fixed_str = result['Comparable_Cases'].replace("'", '"')
                                result['Comparable_Cases'] = json.loads(fixed_str)
                            except:
                                self.logger.error(f"Cannot convert Comparable_Cases to dictionary or list, current value: {result['Comparable_Cases']}")
                                return None
                    else:
                        self.logger.error(f"Comparable_Cases must be dictionary or list type, current type: {type(result['Comparable_Cases'])}")
                        return None
                
                # If Comparable_Cases is list, convert to dictionary format
                if isinstance(result['Comparable_Cases'], list):
                    comparable_cases_dict = {
                        "similar_cases": [],
                        "contrasting_cases": []
                    }
                    
                    for case in result['Comparable_Cases']:
                        if isinstance(case, dict):
                            if case.get('Score', 0) >= result['Score']:
                                comparable_cases_dict["similar_cases"].append(case)
                            else:
                                comparable_cases_dict["contrasting_cases"].append(case)
                    
                    result['Comparable_Cases'] = comparable_cases_dict
                
                self.logger.info("JSON response validation passed")
                self.logger.info(f"Final processed JSON object: {json.dumps(result, ensure_ascii=False, indent=2)}")
                return result
                
            except (ValueError, TypeError) as e:
                self.logger.error(f"Field type conversion failed: {str(e)}")
                return None
            
        except json.JSONDecodeError as e:
            self.logger.error(f"JSON parsing error: {str(e)}")
            self.logger.error(f"Original response content: {response}")
            return None
        except Exception as e:
            self.logger.error(f"Error extracting JSON: {str(e)}")
            return None
    
    def score_policy(self, prompt: str) -> Optional[Dict]:
        """Score a single policy"""
        self.logger.info("\n=== Scoring Policy ===")
        try:
            # Call API
            self.logger.info("Calling API...")
            self.logger.debug(f"Prompt content: {prompt[:200]}...")  # Only log first 200 characters
            
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
            self.logger.info("Successfully received API response")
            self.logger.debug(f"API response content: {content[:200]}...")  # Only log first 200 characters
            
            # Extract JSON
            result = self.extract_json_from_response(content)
            if result is None:
                self.logger.error("Cannot extract valid JSON response")
                return None
            
            self.logger.info(f"Score: {result['Score']}, Confidence: {result['Confidence']}")
            return result
            
        except Exception as e:
            self.logger.error(f"Error during scoring: {str(e)}")
            return None
    
    def process_policies(self):
        """Process all policies"""
        self.logger.info("\n=== Starting Policy Processing ===")
        try:
            # Check if prompts directory exists
            if not os.path.exists(self.prompts_dir):
                self.logger.error(f"Prompts directory not found: {self.prompts_dir}")
                raise FileNotFoundError(f"Prompts directory not found: {self.prompts_dir}")
            
            # Get all prompt files
            prompt_files = [f for f in os.listdir(self.prompts_dir) if f.startswith('prompt_') and f.endswith('.txt')]
            if not prompt_files:
                self.logger.error(f"No prompt files found in directory {self.prompts_dir}")
                raise FileNotFoundError(f"No prompt files found in directory {self.prompts_dir}")
            
            self.logger.info(f"Found {len(prompt_files)} prompt files")
            
            # Read original data file
            original_df = pd.read_excel(os.path.join(self.base_dir, 'policy score.xlsx'))
            
            # Add prediction result columns
            original_df['Predicted_Score'] = None
            original_df['Confidence'] = None
            original_df['Explanation'] = None
            original_df['Inference_Chain'] = None
            original_df['Comparable_Cases'] = None
            
            # Process each policy
            for file in tqdm(prompt_files, desc="Processing policies"):
                self.logger.info(f"\nProcessing file: {file}")
                
                try:
                    # Read prompt
                    with open(os.path.join(self.prompts_dir, file), 'r', encoding='utf-8') as f:
                        prompt = f.read()
                    
                    # Score policy
                    result = self.score_policy(prompt)
                    if result is None:
                        self.logger.error(f"Cannot score policy: {file}")
                        continue
                    
                    # Extract policy ID and fold number
                    # File name format: prompt_fold_0_policy_444.txt
                    parts = file.replace('prompt_', '').replace('.txt', '').split('_')
                    fold = parts[1]  # Get fold number
                    policy_num = parts[3]  # Get policy number
                    policy_id = f"policy/{policy_num}"  # Format as policy/XXXX
                    
                    # Update original dataframe
                    mask = original_df['Policy_ID'] == policy_id
                    if mask.any():
                        original_df.loc[mask, 'Predicted_Score'] = result['Score']
                        original_df.loc[mask, 'Confidence'] = result['Confidence']
                        original_df.loc[mask, 'Explanation'] = json.dumps(result['Explanation'], ensure_ascii=False)
                        original_df.loc[mask, 'Inference_Chain'] = json.dumps(result['Inference_Chain'], ensure_ascii=False)
                        original_df.loc[mask, 'Comparable_Cases'] = json.dumps(result['Comparable_Cases'], ensure_ascii=False)
                        
                        # Save results in real-time
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        output_file = os.path.join(self.output_dir, f'policy_score_with_predictions_{timestamp}.xlsx')
                        original_df.to_excel(output_file, index=False)
                        
                        self.logger.info(f"Successfully processed policy: {policy_id} (Fold {fold})")
                    else:
                        self.logger.error(f"Policy ID not found: {policy_id}, please check file name format")
                        self.logger.error(f"Current file name: {file}")
                        self.logger.error(f"Available Policy_IDs: {original_df['Policy_ID'].tolist()[:5]}...")
                    
                except Exception as e:
                    self.logger.error(f"Error processing file {file}: {str(e)}")
                    continue
                
                # Wait to avoid API rate limits
                time.sleep(1)
            
            # Generate final output filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            final_output_file = os.path.join(self.output_dir, f'policy_score_with_predictions_final_{timestamp}.xlsx')
            
            # Save final results
            original_df.to_excel(final_output_file, index=False)
            self.logger.info(f"\nFinal results saved to: {final_output_file}")
            
            return original_df
            
        except Exception as e:
            self.logger.error(f"Error processing policies: {str(e)}")
            raise

def main():
    try:
        # Set API key
        api_key = "sk-d77ee9363560463b9c8c6eb2adca3704"
        
        # Create scorer and process policies
        scorer = PolicyScorer(api_key=api_key)
        
        # Process policies
        results = scorer.process_policies()
        
        if results is not None:
            print(f"\nSuccessfully processed {len(results)} policies")
            print(f"Results saved to evaluation_results directory")
        else:
            print("\nProcessing failed, please check log file for details")
            
    except Exception as e:
        print(f"\nProgram execution error: {str(e)}")
        print("Please check log file for details")

if __name__ == "__main__":
    main() 