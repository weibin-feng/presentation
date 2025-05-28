import streamlit as st
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import os
from sklearn.model_selection import StratifiedKFold

# 页面配置
st.set_page_config(
    page_title="Methodology - PolicyBindScoreRAG",
    page_icon="🔬",
    layout="wide"
)



with st.sidebar:
    st.image("university-of-southampton-text.svg", width=200)
    st.markdown("""
<div style='text-align: font-size: 10px; padding-bottom: 30px'>
    <p><strong>Title:</strong> PolicyBindScoreRAG</p> 
                <p> A Bindingness Evaluation Framework for Climate Policies via LLM + RAG</p>        
    <p><strong>Author:</strong> Yini Ma</p>
    <p><strong>Date:</strong> May 2025</p>
</div>
""", unsafe_allow_html=True)

# 标题
st.title("Methodology")

# 主要内容
st.markdown("""
## 1. Method Overview

Our approach combines Large Language Models (LLM) with Retrieval-Augmented Generation (RAG) to evaluate the bindingness of climate policies. 

### 1.1 Large Language Model
We utilize DeepSeek Chat V3, a state-of-the-art language model that demonstrates exceptional capabilities in:
- Understanding complex policy language
- Analyzing legal and regulatory contexts
- Providing structured reasoning
- Generating consistent evaluations

### 1.2 Retrieval-Augmented Generation (RAG)
RAG enhances LLM performance by:
- Retrieving relevant reference cases from a knowledge base
- Providing contextual information for better decision-making
- Reducing hallucinations through factual grounding
- Supporting consistent evaluation across similar policies

In our project, RAG is specifically applied to:
- Find semantically similar policies from our annotated dataset
- Provide comparative context for bindingness evaluation
- Ensure consistent scoring across similar policy types
- Support structured reasoning through case-based analysis

### 1.3 Methodlogy Pipelines:

1. **Data Preparation**: Preparing and encoding policy texts for similarity search
2. **Prompt Building**: Generating structured prompts with retrieved similar cases
3. **API Inference**: Using LLM to analyze policies and assign bindingness scores

## 2. Data Preparation

The data preparation process involves several key steps:

### 2.1 Data Overview
Our dataset contains climate policies with the following structure:
""")

# 数据展示
df = pd.read_excel('policy_scoring/need_score.xlsx')
st.dataframe(df.head(3), use_container_width=True)

st.markdown("""
### 2.2 Text Processing
- Combining `Type` and `Description` fields to create comprehensive text representations
- Excluding policy names to prevent overfitting
- Preserving semantic information needed for bindingness evaluation

### 2.3 Text Embedding
- Using the `all-mpnet-base-v2` model from Sentence Transformers
- Converting policy texts into 768-dimensional vectors
- Capturing semantic relationships between policies

### 2.4 Vector Normalization and Similarity Search
- Normalizing vectors using L2 normalization
- Calculating cosine similarity between vectors
- Finding the most similar reference cases

The cosine similarity between two vectors A and B is calculated as:

$$\\cos(\\theta) = \\frac{\\mathbf{A} \\cdot \\mathbf{B}}{\\|\\mathbf{A}\\| \\|\\mathbf{B}\\|}$$

Where:
- A · B is the dot product of vectors A and B
- ||A|| and ||B|| are the L2 norms (magnitudes) of vectors A and B

After L2 normalization, the cosine similarity simplifies to the dot product:

```python
# Vector normalization
faiss.normalize_L2(embeddings)

# Similarity calculation (dot product after normalization)
similarities = np.dot(query_embedding, reference_embeddings.T)
```

## 3. Prompt Building

The prompt building process enhances the LLM's evaluation capabilities through RAG:

### 3.1 Similar Case Retrieval
- Encoding target policy text
- Finding the two most similar reference cases
- Using semantic similarity for case selection

### 3.2 Prompt Structure
- Task definition and objective
- Scoring categories and criteria
- Evaluation dimensions
- Step-by-step analysis procedure
- Output format specification

### 3.3 Context Integration
- Including retrieved similar cases
- Providing comparative context
- Supporting structured reasoning

## 4. API Inference

The inference process uses the LLM to analyze policies:

- Using DeepSeek Chat model
- Extracting structured JSON responses
- Validating required fields

```python
# API call
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}],
    temperature=0.1
)
```
""")