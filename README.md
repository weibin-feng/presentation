# Environmental Policy Bindingness Classification System

This is an environmental policy bindingness classification system based on RAG (Retrieval-Augmented Generation) and LLM.

## Project Structure

```
.
├── k_fold_validation/           # K-fold cross-validation scripts
│   ├── 1_data_preparation.py    # Data preprocessing script
│   ├── 2_rag_prompt_builder.py  # RAG prompt generation script
│   ├── 3_api_inference.py       # API inference script
│   ├── 4_metrics_calculation.py # Metrics calculation script
│   ├── policy score.xlsx        # Original data file
│   ├── processed_data/          # Processed data directory
│   ├── prompts/                 # Generated prompts directory
│   ├── logs/                    # Log files directory
│   ├── evaluation_results/      # Evaluation results directory
│   └── metrics_results/         # Metrics results directory
├── policy_scoring/             # Policy scoring scripts
│   ├── 1_need_score_preparation.py    # Data preparation script
│   ├── 2_need_score_prompt_builder.py # RAG prompt builder script
│   ├── 3_need_score_api_inference.py  # API inference script
│   ├── need_score.xlsx         # Original need score data
│   ├── policy_score.xlsx       # Original policy score data
│   ├── need_score_processed/   # Processed need score data
│   ├── prompts/                # Generated prompts directory
│   ├── logs/                   # Log files directory
│   └── evaluation_results/     # Evaluation results directory
├── environment.yml             # Conda environment configuration
└── requirements.txt            # pip dependencies (optional)
```

## Environment Setup

### Using Conda (Recommended)

1. Create and activate environment:
```bash
conda env create -f environment.yml
conda activate policy-classifier
```

### Using pip (Alternative)

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### K-fold Cross Validation

1. Data Preparation:
```bash
python k_fold_validation/1_data_preparation.py
```
This will:
- Load the original Excel data
- Create five-fold cross-validation splits
- Generate text embeddings using sentence-transformers
- Create FAISS indices for each fold
- Save processed data to the `processed_data` directory

2. RAG Prompt Generation:
```bash
python k_fold_validation/2_rag_prompt_builder.py
```
This will:
- Generate RAG prompts for each policy in the test set
- Save prompts to the `prompts` directory

3. API Inference:
```bash
python k_fold_validation/3_api_inference.py
```
This will:
- Process each prompt using the API
- Save evaluation results to the `evaluation_results` directory

4. Metrics Calculation:
```bash
python k_fold_validation/4_metrics_calculation.py
```
This will:
- Calculate evaluation metrics
- Generate ROC curves and confusion matrices
- Save results to the `metrics_results` directory

### Policy Scoring

1. Data Preparation:
```bash
python policy_scoring/1_need_score_preparation.py
```
This will:
- Load the original Excel data (need_score.xlsx and policy_score.xlsx)
- Process and prepare the data for scoring
- Save processed data to the `need_score_processed` directory

2. RAG Prompt Generation:
```bash
python policy_scoring/2_need_score_prompt_builder.py
```
This will:
- Generate RAG prompts for policy scoring
- Save prompts to the `prompts` directory

3. API Inference:
```bash
python policy_scoring/3_need_score_api_inference.py
```
This will:
- Process each prompt using the API
- Save evaluation results to the `evaluation_results` directory

## Data Format

### Policy Score Data (policy_score.xlsx)
The input data should contain the following columns:
- Policy_ID: Unique identifier for each policy
- Policy_Name: Name of the policy
- Type: Policy type (Standard/Program etc.)
- Description: Policy content
- Score: Human-annotated classification (1/2/3)
- Explanation: Human explanation

### Need Score Data (need_score.xlsx)
The input data should contain the following columns:
- Policy_ID: Unique identifier for each policy
- Policy_Name: Name of the policy
- Type: Policy type
- Description: Policy content
- Need_Score: Human-annotated need score
- Explanation: Human explanation

## Notes

- Ensure column names in the Excel files exactly match the format above
- Processed data will be saved in their respective directories
- FAISS indices are saved separately for each fold to avoid data leakage
- Log files are saved in the `logs` directory for debugging
- Evaluation results are saved in the `evaluation_results` directory
- Metrics and visualizations are saved in the `metrics_results` directory 