import streamlit as st

# 页面配置
st.set_page_config(
    page_title="Research Background",
    page_icon="📚",
    layout="wide"
)

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

# 页面主标题
st.title("Research Background & Motivation")

# 正文内容
st.markdown("""
### Background: ESG Fund Flows and Policy Signals

In recent years, U.S. ESG mutual funds have shifted from rapid growth to significant net outflows.  
While macroeconomic drivers such as interest rate hikes and market sentiment shifts are widely acknowledged,  
**a less explored factor is the changing stance of the U.S. government on climate and sustainability.**

This research proposes a **more responsive, higher-frequency policy indicator** to capture national-level climate policy signals  
and investigate their potential explanatory power for ESG capital flows.

---

### Motivation: Limitations of Existing Indices

We build on the Climate-related Financial Policy Index (CRFPI) developed by D’Orazio & Thole (2022),  
which attempts to quantify policy bindingness across more than 70 countries.  
However, the CRFPI suffers from several serious limitations:

- Covers only ~200 country-year observations, with many missing entries  
- Ends in 2020, with annual frequency — insufficient for fast-evolving contexts  
- Lacks a transparent or reproducible evaluation methodology  
- Not well-suited for focused empirical analysis in a single country like the U.S.

These issues **limit its utility** for understanding the role of policy in dynamic capital markets.

---

### Contribution: Method, Data, and Scope

This study introduces several key innovations:

- **Methodological Advancement**:  
  A novel scoring framework using **Large Language Models (LLMs)** and **Retrieval-Augmented Generation (RAG)** to automate policy bindingness evaluation

- **Enhanced Data Resolution**:  
  A monthly U.S.-specific climate policy dataset extended through **Jan 2025**, enabling more granular empirical research

- **Research Enabler**:  
  A transparent, scalable, and reproducible indicator to support future analysis of **ESG fund behavior and policy impact**

---

### Scope of This Presentation

This presentation focuses on the **first half of the project**:  
the design and implementation of the LLM+RAG-based policy scoring method,  
and the construction of the high-frequency policy bindingness dataset for the U.S.
""")
