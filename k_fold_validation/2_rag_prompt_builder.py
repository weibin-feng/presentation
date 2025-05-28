import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import json
import os
from typing import List, Dict
import logging
from datetime import datetime
from sklearn.model_selection import StratifiedKFold

class RAGPromptBuilder:
    def __init__(self, model_name='all-mpnet-base-v2', fold=0):
        """Initialize RAG prompt builder"""
        # Set directories first
        self.base_dir = os.path.dirname(os.path.abspath(__file__))  # Get current directory
        self.data_dir = os.path.join(self.base_dir, 'processed_data')
        self.logs_dir = os.path.join(self.base_dir, 'logs')
        self.prompts_dir = os.path.join(self.base_dir, 'prompts')
        os.makedirs(self.data_dir, exist_ok=True)
        os.makedirs(self.logs_dir, exist_ok=True)
        os.makedirs(self.prompts_dir, exist_ok=True)
        
        # Setup logging
        self.setup_logging()
        
        # Initialize text encoder
        self.logger.info("\n=== Initializing RAG Prompt Builder ===")
        self.logger.info("\n1. Initializing text encoder...")
        self.encoder = SentenceTransformer(model_name)
        self.logger.info("Text encoder initialization completed")
        
        # Set fold
        self.fold = fold
        
        # Load data
        self.load_data()
        
        # Prepare training and test sets
        self.prepare_folds()
        
    def setup_logging(self):
        """Setup logging configuration"""
        # Generate log filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = os.path.join(self.logs_dir, f'rag_prompt_builder_{timestamp}.log')
        
        # Configure logger
        self.logger = logging.getLogger('RAGPromptBuilder')
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
    
    def load_data(self):
        """Load data"""
        self.logger.info("\n2. Loading data...")
        
        # Load processed data
        processed_data_path = os.path.join(self.data_dir, 'processed_data.json')
        if not os.path.exists(processed_data_path):
            raise FileNotFoundError(f"Processed data file not found: {processed_data_path}")
            
        with open(processed_data_path, 'r', encoding='utf-8') as f:
            processed_data = json.load(f)
            
        # Convert to DataFrame
        self.df = pd.DataFrame(processed_data['data'])
        self.embeddings = np.array(processed_data['embeddings']).astype('float32')
        
        # L2 normalize embeddings
        faiss.normalize_L2(self.embeddings)
        
        self.logger.info(f"Successfully loaded {len(self.df)} items")
        
        # Load FAISS index
        self.logger.info(f"\n3. Loading FAISS index (fold {self.fold})...")
        index_path = os.path.join(self.data_dir, f'faiss_index_fold_{self.fold}.index')
        if not os.path.exists(index_path):
            raise FileNotFoundError(f"Index file not found: {index_path}")
        self.index = faiss.read_index(index_path)
        self.logger.info("FAISS index loaded successfully")
    
    def prepare_folds(self):
        """Prepare training and test sets"""
        self.logger.info(f"\n4. Preparing data split (fold {self.fold})...")
        
        # Use same random seed as data_preparation.py
        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        
        # Get current fold split
        for fold_idx, (train_idx, test_idx) in enumerate(skf.split(self.df, self.df['Score'])):
            if fold_idx == self.fold:
                # Training set
                self.train_df = self.df.iloc[train_idx]
                self.train_embeddings = self.embeddings[train_idx].copy()  # Create copy
                
                # Test set
                self.test_df = self.df.iloc[test_idx]
                self.test_embeddings = self.embeddings[test_idx].copy()  # Create copy
                break
        
        # Ensure embeddings are normalized
        faiss.normalize_L2(self.train_embeddings)
        faiss.normalize_L2(self.test_embeddings)
        
        self.logger.info(f"Training set: {len(self.train_df)} items")
        self.logger.info(f"Test set: {len(self.test_df)} items")
    
    def get_similar_cases(self, policy, k=2):
        """Get similar cases (only from training set)"""
        self.logger.info("\n=== Getting similar cases ===")
        try:
            # Encode target policy
            self.logger.info("Encoding target policy...")
            query_text = policy['Type'] + " " + policy['Description']
            query_embedding = self.encoder.encode([query_text])[0].astype('float32')
            
            # L2 normalize query vector
            faiss.normalize_L2(query_embedding.reshape(1, -1))
            
            # Search similar cases (using dot product)
            similarities, indices = self.index.search(query_embedding.reshape(1, -1), k)
            
            # Build similar cases list
            similar_cases = []
            for i, (similarity, idx) in enumerate(zip(similarities[0], indices[0])):
                if idx != -1:  # Ensure index is valid
                    case = self.train_df.iloc[idx].to_dict()
                    case['similarity'] = float(similarity)  # Use dot product as similarity
                    similar_cases.append(case)
                    self.logger.info(f"Found similar case {i+1}: {case['Policy_ID']} (similarity: {similarity:.4f})")
            
            return similar_cases
        except Exception as e:
            self.logger.error("Error getting similar cases: %s", str(e))
            raise
    
    def build_prompt(self, policy, similar_cases):
        """Build prompt"""
        self.logger.info("\n=== Building prompt ===")
        try:
            # Build base prompt
            prompt = f"""You are an expert legal-policy analyst evaluating the **bindingness** of climate or environmental policies. Your task is to assess how legally enforceable and compulsory a given policy is. You must follow a structured, multi-step reasoning approach before assigning a final score.

---

Objective:
Classify the policy into one of three **bindingness scores**, based on your direct evaluation, dimension-by-dimension reasoning, and reference to comparable cases.


---

### Scoring Categories:

- **Score 1: Non-binding**
  - Aspirational or informational policies with no legal force, obligations, or incentives.
  - Often appear as reports, plans, advisory boards, or descriptive indexes.
  - **Common keywords**: may, encourage, develop, planning goals

- **Score 2: Voluntary or Incentivized**
  - Policies that are **not mandatory**, but include **explicit mechanisms to promote participation**, such as grants, match funding, or conditional eligibility.
  - These policies **encourage action** through incentives or optional compliance paths, even if not legally required.
  - Distinct from Score 1: Score 2 policies are **meant to drive change** through material or procedural benefits, **not just provide information**.
  - **Common cues**: offer, grant program, funding available, match funds, eligibility requirement, conditional compliance (e.g., "where practicable")
  
- **Score 3: Mandatory**
  - Legally binding measures from statute, regulation, or executive order with enforceable obligations.
  - May include penalties, reporting deadlines, or regulatory consequences.
  - **Common keywords**: must, shall, is required to, mandate, penalty, enforce

---

### Evaluation Dimensions (Used for Explanation):

For each of the five dimensions, answer both components:

1. **Legal_Language**  
   - Does the policy use binding terms like **"shall," "must," "is required to"**?  
   - Or does it use non-binding terms like **"may," "encourage," "help," "support," "goal"**?

2. **Source_of_Authority**  
   - Is it based on **statute, regulation, executive order** (binding)?  
   - Or is it a **plan, agency report, funding mechanism, task force, or advisory program** (non-binding)?

3. **Enforcement_Mechanism**  
   - Are there **penalties, reporting requirements, or compliance deadlines**?  
   - Or is it **aspirational** with **no consequence** for failure to comply?

4. **Obligations**  
   - Who is obligated to act?  
   - Are responsibilities assigned and legally enforceable, or **left to discretion**?

5. **Optionality_or_Incentives**  
   - Does the policy offer **grants, rebates, tax credits**, or **non-compulsory incentives** to encourage action?


### Step-by-step Procedure:

1. **Analyze the Current Policy**
   - Examine each of the five dimensions.
   - Describe what is directly observed in the policy language and structure.

2. **Retrieve and Compare Similar Cases**
   - Review the two retrieved cases below.
   - Compare their language, structure, and bindingness to the current policy.

3. **Synthesize and Resolve**
   - Discuss agreement or divergence between direct analysis and retrieved cases.
   - Highlight any ambiguous elements or borderline scores.

4. **Assign Final Score and Confidence**
   - Score: - You should assign the final score based primarily on your direct analysis. Retrieved cases serve as contextual benchmarks.
   - Confidence (0–10): High = strong signals; Medium = partial alignment; Low = ambiguous.

---

### Current Policy for Evaluation:

Policy ID: {policy['Policy_ID']}  
Policy Name: {policy['Policy_Name']}  
Type: {policy['Type']}  
Description:  
{policy['Description']}

---

### Retrieved Reference Cases:

Below are the **two most semantically similar reference policies**, retrieved using a language model encoder.  
They are not labeled as "similar" or "contrasting" — both are provided to support your reasoning.

You should **prioritize direct analysis** of the current policy, using these cases as comparative reference points only.



"""
            
            # Add similar cases
            for i, case in enumerate(similar_cases, 1):
                prompt += f"\nCase {i}:\n"
                prompt += f"Similarity: {case['similarity']:.2f}\n"
                prompt += f"Policy ID: {case['Policy_ID']}\n"
                prompt += f"Name: {case['Policy_Name']}\n"
                prompt += f"Score: {case['Score']}\n"
                prompt += f"Type: {case['Type']}\n"
                prompt += f"Description: {case['Description']}\n\n"
                prompt += f"Explanation: {case.get('Explanation', '')}\n\n"
            
            # Add target policy
            prompt += f"""---


            
### Final Output Format (JSON Only):

{{
  "Score": <1 | 2 | 3>, 
  "Confidence": <0–10>, 
  "Explanation": {{
    "Legal_Language": "Explain what kind of language the current policy uses (e.g., 'shall', 'may', 'encourage').",
    "Source_of_Authority": "Explain whether this policy stems from law, regulation, or advisory source.",
    "Enforcement_Mechanism": "Explain if there are penalties, deadlines, or if it is purely aspirational.",
    "Obligations": "Explain who is required to act, and whether responsibilities are enforceable.",
    "Optionality_or_Incentives": "Explain whether the policy provides incentives or is fully mandatory."
  }},
  "Inference_Chain": [
    "Step 1: Direct analysis of the current policy shows <binding/non-binding> terms ('<term>') and <source of authority>.",
    "Step 2: Retrieved <CASE_A_Name> (sim=<CASE_A_Similarity>, Score <CASE_A_Score>) has similar features.",
    "Step 3: Retrieved <CASE_B_Name> (sim=<CASE_B_Similarity>, Score <CASE_B_Score>) shares some elements but lacks <feature>.",
    "Step 4: Current policy aligns more with <CASE_A_Name> due to <reason>.",
    "Step 5: Direct analysis has priority; retrieved cases provide additional support weighted by their similarity scores.",
    "Step 6: Final judgment: Score <Final_Score>, Confidence <Confidence_Score>."
  ],
  "Comparable_Cases": [
    {{
      "Policy_ID": "<CASE_1_ID>",
      "Case_Name": "<CASE_1_NAME>",
      "Score": <SCORE_1>,
      "Reason": "Summarize why this case is highly similar and informative for the current policy evaluation."
    }},
    {{
      "Policy_ID": "<CASE_2_ID>",
      "Case_Name": "<CASE_2_NAME>",
      "Score": <SCORE_2>,
      "Reason": "Summarize why this case is also relevant and comparable to the current policy."
    }}
  ]
}}

Note: The above is a structural JSON template.

You must:
- Replace <...> placeholders with actual values from your analysis.
- Derive both cases from the two retrieved examples.
- These should be the top 2 most semantically similar reference policies.
- Do not copy this template literally.

---

Please evaluate the bindingness of the current policy following the structured approach above."""
            
            self.logger.info("Prompt built successfully")
            return prompt
            
        except Exception as e:
            self.logger.error("Error building prompt: %s", str(e))
            raise

def main():
    # Process all folds
    for fold in range(5):
        print(f"\nProcessing fold {fold}...")
        
        # Create RAG prompt builder
        builder = RAGPromptBuilder(fold=fold)
        
        # Generate prompts for each policy in test set
        for idx, test_policy in builder.test_df.iterrows():
            try:
                # Get similar cases
                similar_cases = builder.get_similar_cases(test_policy.to_dict())
                
                # Build prompt
                prompt = builder.build_prompt(test_policy.to_dict(), similar_cases)
                
                # Clean Policy_ID
                policy_id = test_policy["Policy_ID"].replace('/', '_')
                output_file = os.path.join(builder.prompts_dir, f'prompt_fold_{fold}_{policy_id}.txt')
                
                # Save prompt
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(prompt)
                
                print(f"Generated prompt: {output_file}")
                
            except Exception as e:
                print(f"Error processing policy {test_policy['Policy_ID']}: {str(e)}")
                continue
    
    print("\nAll folds processed!")
    print(f"Prompt files saved to {builder.prompts_dir} directory")

if __name__ == "__main__":
    main() 