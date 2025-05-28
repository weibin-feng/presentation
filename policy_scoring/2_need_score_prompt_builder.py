import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss
import json
import os
from typing import List, Dict
import logging
from datetime import datetime

class NeedScorePromptBuilder:
    def __init__(self, model_name='all-mpnet-base-v2'):
        """Initialize RAG prompt builder"""
        self.setup_logging()
        self.logger.info("\n=== Initializing RAG Prompt Builder ===")
        
        # Initialize text encoder
        self.logger.info("\n1. Initializing text encoder...")
        self.encoder = SentenceTransformer(model_name)
        self.logger.info("Text encoder initialization complete")
        
        # Setup directories
        self.processed_data_dir = 'policy_scoring/need_score_processed'
        self.prompts_dir = 'policy_scoring/prompts'
        os.makedirs(self.prompts_dir, exist_ok=True)
        
        # Load data
        self.load_data()
        
    def setup_logging(self):
        """Setup logging configuration"""
        logs_dir = 'policy_scoring/logs'
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = f'{logs_dir}/need_score_prompt_builder_{timestamp}.log'
        
        self.logger = logging.getLogger('NeedScorePromptBuilder')
        self.logger.setLevel(logging.INFO)
        
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
        self.logger.info(f"Log file created: {log_file}")
    
    def load_data(self):
        """Load data"""
        self.logger.info("\n2. Loading data...")
        
        # Load processed data
        processed_data_path = os.path.join(self.processed_data_dir, 'processed_data.json')
        if not os.path.exists(processed_data_path):
            raise FileNotFoundError(f"Processed data file not found: {processed_data_path}")
            
        with open(processed_data_path, 'r', encoding='utf-8') as f:
            processed_data = json.load(f)
            
        # Convert to DataFrame
        self.reference_df = pd.DataFrame(processed_data['reference_data'])
        self.reference_embeddings = np.array(processed_data['reference_embeddings']).astype('float32')
        
        self.target_df = pd.DataFrame(processed_data['target_data'])
        self.target_embeddings = np.array(processed_data['target_embeddings']).astype('float32')
        
        # L2 normalize embedding vectors
        faiss.normalize_L2(self.reference_embeddings)
        faiss.normalize_L2(self.target_embeddings)
        
        self.logger.info(f"Successfully loaded reference data: {len(self.reference_df)} records")
        self.logger.info(f"Successfully loaded target data: {len(self.target_df)} records")
        
        # Load FAISS index
        self.logger.info("\n3. Loading FAISS index...")
        index_path = os.path.join(self.processed_data_dir, 'faiss_index.index')
        if not os.path.exists(index_path):
            raise FileNotFoundError(f"Index file not found: {index_path}")
        self.index = faiss.read_index(index_path)
        self.logger.info("FAISS index loaded")
    
    def get_similar_cases(self, policy, k=2):
        """Get similar cases (from reference data)"""
        self.logger.info("\n=== Getting Similar Cases ===")
        try:
            # Encode target policy
            self.logger.info("Encoding target policy...")
            query_text = policy['Type'] + " " + policy['Description']
            query_embedding = self.encoder.encode([query_text])[0].astype('float32')
            
            # L2 normalize query vector
            faiss.normalize_L2(query_embedding.reshape(1, -1))
            
            # Search for similar cases (using dot product)
            similarities, indices = self.index.search(query_embedding.reshape(1, -1), k)
            
            # Build similar cases list
            similar_cases = []
            for i, (similarity, idx) in enumerate(zip(similarities[0], indices[0])):
                if idx != -1:  # Ensure index is valid
                    case = self.reference_df.iloc[idx].to_dict()
                    case['similarity'] = float(similarity)  # Use dot product directly as similarity
                    similar_cases.append(case)
                    self.logger.info(f"Found similar case {i+1}: {case['Policy_ID']} (similarity: {similarity:.4f})")
            
            return similar_cases
        except Exception as e:
            self.logger.error("Error getting similar cases: %s", str(e))
            raise
    
    def build_prompt(self, policy, similar_cases):
        """Build prompt"""
        self.logger.info("\n=== Building Prompt ===")
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

> Note: Use judgment based on overall context, not just keywords.
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
                prompt += f"Policy ID: {case['Policy_ID']}\n"
                prompt += f"Name: {case['Policy_Name']}\n"
                prompt += f"Similarity: {case['similarity']:.4f}\n"
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
      "Similarity": <CASE_1_SIMILARITY>,
      "Score": <SCORE_1>,
      "Reason": "Summarize why this case is highly similar and informative for the current policy evaluation."
    }},
    {{
      "Policy_ID": "<CASE_2_ID>",
      "Case_Name": "<CASE_2_NAME>",
      "Similarity": <CASE_2_SIMILARITY>,
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
            
            self.logger.info("Prompt building complete")
            return prompt
            
        except Exception as e:
            self.logger.error("Error building prompt: %s", str(e))
            raise

def main():
    try:
        # Create prompt builder
        builder = NeedScorePromptBuilder()
        
        # Generate prompts for each target policy
        for idx, target_policy in builder.target_df.iterrows():
            try:
                # Get similar cases
                similar_cases = builder.get_similar_cases(target_policy.to_dict())
                
                # Build prompt
                prompt = builder.build_prompt(target_policy.to_dict(), similar_cases)
                
                # Clean Policy_ID slashes
                policy_id = target_policy["Policy_ID"].replace('/', '_')
                output_file = os.path.join(builder.prompts_dir, f'prompt_{policy_id}.md')
                
                # Save prompt
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(prompt)
                
                print(f"Generated prompt: {output_file}")
                
            except Exception as e:
                print(f"Error processing policy {target_policy['Policy_ID']}: {str(e)}")
                continue
        
        print("\nAll prompts generated!")
        print(f"Prompt files saved to {builder.prompts_dir} directory")
    except Exception as e:
        print(f"Program execution error: {str(e)}")

if __name__ == "__main__":
    main() 