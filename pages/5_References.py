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
### Academic Literature

1. **Policy Bindingness Assessment**
   - Bodansky, D. (2016). The Legal Character of the Paris Agreement. *Review of European, Comparative & International Environmental Law*, 25(2), 142-150.
   - Falkner, R. (2016). The Paris Agreement and the new logic of international climate politics. *International Affairs*, 92(5), 1107-1125.

2. **Climate Policy Analysis**
   - Jordan, A., et al. (2018). Governing climate change polycentrically: setting the scene. *Climate Policy*, 18(5), 545-557.
   - Ostrom, E. (2010). Polycentric systems for coping with collective action and global environmental change. *Global Environmental Change*, 20(4), 550-557.

3. **Legal Language Processing**
   - Chalkidis, I., et al. (2020). LEGAL-BERT: The Muppets straight out of Law School. *Findings of EMNLP*, 2898-2904.
   - Niklaus, J., et al. (2021). Swiss-Judgment-Prediction: A Multilingual Legal Judgment Prediction Benchmark. *ACL-IJCNLP 2021*.

4. **LLM and RAG Technologies**
   - Lewis, M., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. *NeurIPS 2020*.
   - Brown, T., et al. (2020). Language Models are Few-Shot Learners. *NeurIPS 2020*.

### Technical Resources

1. **Vector Databases and Similarity Search**
   - Johnson, J., et al. (2019). Billion-scale similarity search with GPUs. *IEEE Transactions on Big Data*.
   - Malkov, Y. A., & Yashunin, D. A. (2020). Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs. *IEEE transactions on pattern analysis and machine intelligence*.

2. **Natural Language Processing**
   - Devlin, J., et al. (2019). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. *NAACL 2019*.
   - Reimers, N., & Gurevych, I. (2019). Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks. *EMNLP 2019*.

### Policy Documents

1. **International Climate Agreements**
   - United Nations Framework Convention on Climate Change (1992)
   - Paris Agreement (2015)
   - Glasgow Climate Pact (2021)

2. **National Climate Policies**
   - European Union Climate Action Plan
   - United States Climate Action Plan
   - China's National Climate Change Program

### Tools and Frameworks

1. **Machine Learning Libraries**
   - PyTorch
   - Transformers
   - Sentence-Transformers

2. **Vector Search**
   - FAISS
   - Annoy
   - HNSW

3. **Web Development**
   - Streamlit
   - Plotly
   - Pandas
""") 