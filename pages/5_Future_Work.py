import streamlit as st
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import os

# 页面配置
st.set_page_config(
    page_title="Future Work - PolicyBindScoreRAG",
    page_icon="🔮",
    layout="wide"
)

# 自定义CSS样式
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stMarkdown h1 {
        padding-bottom: 1rem;
        border-bottom: 2px solid #E5E7EB;
    }
    .stMarkdown h2 {
        margin-top: 2rem;
    }
    .stDataFrame {
        border: 1px solid #E5E7EB;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .stMarkdown blockquote {
        border-left: 4px solid #3B82F6;
        padding-left: 1rem;
        margin: 1rem 0;
        background-color: #F8FAFC;
    }
    </style>
""", unsafe_allow_html=True)

# 侧边栏
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
st.title("Future Work")

# 主要内容
st.markdown("""
## Research Background

Over the past decade, sustainable investing has gained increasing importance in global capital markets.

Recently, U.S. ESG mutual funds have seen notable outflows.

While concerns over greenwashing and higher interest rates are well-known factors, another possible explanation is the changing stance of the U.S. government toward sustainability.

This makes the U.S. an ideal context to study how policy attitudes influence ESG fund flows.

## Research Objective

To capture the national stance on sustainability, we use a climate-related policy index.

This index reflects bindingness of climate-related financial policies.
""") 