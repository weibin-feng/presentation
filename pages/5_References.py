import streamlit as st

st.set_page_config(
    page_title="References - PolicyBindScoreRAG",
    page_icon="📖",
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

st.title("References")

st.markdown("""


- D’Orazio, P. (2021). *Climate-related financial policy index: A composite index to compare the engagement in green financial policymaking at the global level*. Ecological Economics, 193, 107308. https://doi.org/10.1016/j.ecolind.2022.109065

- DeepSeek AI. (2024). *DeepSeek-V3: Open LLM for reasoning, coding, and knowledge tasks*. https://github.com/deepseek-ai/DeepSeek-V3

- Lewis, M., Liu, Y., Goyal, N., et al. (2020). *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*. NeurIPS 33, 9459–9474. https://arxiv.org/abs/2005.11401

- Reimers, N., & Gurevych, I. (2019). *Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks*. EMNLP 2019. https://arxiv.org/abs/1908.10084

- Johnson, J., Douze, M., & Jégou, H. (2019). *Billion-scale similarity search with GPUs*. IEEE Transactions on Big Data, 7(3), 535–547. https://doi.org/10.1109/TBDATA.2019.2921572

- Kohavi, R. (1995). *A study of cross-validation and bootstrap for accuracy estimation and model selection*. IJCAI 14(2), 1137–1143.

- Chen, Z. Z., Ma, J., Zhang, X., Hao, N., Yan, A., Nourbakhsh, A., Yang, X., McAuley, J., Petzold, L., & Wang, W. Y. (2024). A Survey on Large Language Models for Critical Societal Domains: Finance, Healthcare, and Law. arXiv preprint. https://arxiv.org/abs/2405.01769
            
- Cheng, Q., Liu, L., Zhu, Q., Yu, R., Jin, Z., Xie, Y., & Jia, X. (2025). LLM-based Evaluation Policy Extraction for Ecological Modeling. arXiv preprint. https://arxiv.org/abs/2505.13794
""")
