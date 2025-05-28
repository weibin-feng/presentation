import streamlit as st

# 页面配置
st.set_page_config(
    page_title="PolicyBindScoreRAG",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.image("university-of-southampton-text.svg", width=300)


# 居中主标题 & 副标题
st.markdown("""
<div style='text-align: center; padding-top: 10px; padding-bottom: 10px'>
    <h1 style='font-size: 50px;'>PolicyBindScoreRAG</h1>
    <h3 style='font-size: 24px; font-weight: normal;'>A Bindingness Evaluation Framework for Climate Policies via LLM + Retrieval-Augmented Generation</h3>
</div>
""", unsafe_allow_html=True)

# 项目信息（居中 + 大字号）
st.markdown("""
<div style='text-align: center; font-size: 18px; padding-bottom: 30px'>
    <p><strong>Author:</strong> Yini Ma</p>
    <p><strong>Supervisor:</strong> Dr. Mohamed Bakoush, Professor Woon Sau Leung</p>
    <p><strong>Affiliation:</strong> Southampton Business School, University of Southampton</p>
    <p><strong>Date:</strong> May 2025</p>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div style='text-align: center; font-size: 14px; color: gray; padding-top: 20px'>
    <p>The Accounting and Banking & Finance, PhD Symposium 2025 | University of Southampton</p>
</div>
""", unsafe_allow_html=True)
