import streamlit as st

st.set_page_config(
    page_title="Research Background - PolicyBindScoreRAG",
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
    


st.title("Research Background")

st.markdown("""
### Climate Policy Landscape

Climate policies play a crucial role in addressing global environmental challenges. However, the effectiveness of these policies often depends on their bindingness - the degree to which they create legally enforceable obligations. Current policy assessments primarily rely on qualitative analysis, which can lead to:

- Inconsistent evaluation methods
- Subjective interpretations
- Limited comparability across policies
- Lack of standardized metrics

### Research Gap

The existing literature reveals several key gaps in policy bindingness assessment:

1. **Methodological Limitations**
   - Heavy reliance on expert judgment
   - Lack of quantitative measures
   - Inconsistent evaluation frameworks

2. **Technical Challenges**
   - Complex legal language interpretation
   - Diverse policy structures
   - Varying enforcement mechanisms

3. **Practical Constraints**
   - Time-consuming manual analysis
   - Limited scalability
   - Resource-intensive evaluation process

### Research Objectives

This study aims to address these gaps by developing a novel framework that:

1. **Quantifies Policy Bindingness**
   - Establishes standardized scoring criteria
   - Provides numerical measures of bindingness
   - Enables comparative analysis

2. **Leverages Advanced Technologies**
   - Utilizes Large Language Models (LLMs)
   - Implements Retrieval-Augmented Generation (RAG)
   - Automates policy analysis

3. **Ensures Practical Applicability**
   - Offers scalable solutions
   - Provides interpretable results
   - Supports decision-making processes

### Significance

This research contributes to the field by:

- Developing a novel quantitative framework for policy bindingness assessment
- Providing a standardized methodology for policy evaluation
- Enabling more objective and consistent policy analysis
- Supporting evidence-based policy development and implementation

### Research Questions

1. How can policy bindingness be effectively quantified?
2. What are the key dimensions of policy bindingness?
3. How can LLM and RAG technologies enhance policy analysis?
4. What are the practical implications of automated policy bindingness assessment?
""") 