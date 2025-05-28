import streamlit as st

# 页面配置
st.set_page_config(
    page_title="Future Work - PolicyBindScoreRAG",
    page_icon="🔮",
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

# 标题
st.title("Future Work")

# 主要内容
# Future Work 内容
st.markdown("""

#### From Policy to Markets  
Next, we’ll test whether the strength of climate policy—captured by our bindingness scores—can help explain the flow of money into or out of U.S. ESG mutual funds.

#### Quarterly Analysis  
Using our policy scores, we’ll construct a quarterly panel combining ESG fund flows with government policy signals, and apply fixed-effects regressions to explore the relationship.

#### Main Hypothesis  
We expect that stronger, more binding climate policies increase investor confidence, leading to more stable or positive ESG fund flows.

#### Controlling for Other Factors  
To isolate the effect of policy, we’ll include controls for interest rates, market volatility, and investor sentiment.

#### Why It Matters  
If policy strength truly influences capital flows, this would offer valuable insights into how public commitments drive private investment in sustainable finance.
""")
