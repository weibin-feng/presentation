import streamlit as st

st.set_page_config(
    page_title="Scoring System - PolicyBindScoreRAG",
    page_icon="📊",
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

# 添加校徽
st.image("university-of-southampton-text.svg", width=200)

st.title("Scoring System")

st.markdown("""
## Scoring Categories

Our system evaluates policy bindingness using a three-level scoring framework:
""")

# Score 1
with st.expander("Score 1: Non-binding", expanded=True):
    st.markdown("""
    - **Definition**: Aspirational or informational policies with no legal force, obligations, or incentives
    - **Common Forms**: Reports, plans, advisory boards, or descriptive indexes
    - **Key Indicators**:
        - Use of non-binding language
        - Absence of enforcement mechanisms
        - Focus on information sharing or guidance
    - **Common Keywords**: may, encourage, develop, planning goals
    """)

# Score 2
with st.expander("Score 2: Voluntary or Incentivized", expanded=True):
    st.markdown("""
    - **Definition**: Policies that are **not mandatory**, but include **explicit mechanisms to promote participation**
    - **Key Characteristics**:
        - Voluntary participation with incentives
        - Optional compliance paths
        - Material or procedural benefits
    - **Common Cues**: offer, grant program, funding available, match funds, eligibility requirement
    - **Distinction**: Unlike Score 1, these policies actively drive change through benefits
    """)

# Score 3
with st.expander("Score 3: Mandatory", expanded=True):
    st.markdown("""
    - **Definition**: Legally binding measures with enforceable obligations
    - **Key Characteristics**:
        - Clear legal authority
        - Enforceable requirements
        - Defined consequences for non-compliance
    - **Common Keywords**: must, shall, is required to, mandate, penalty, enforce
    - **Typical Sources**: Statute, regulation, or executive order
    """)

st.markdown("""
## Evaluation Dimensions

Each policy is evaluated across five key dimensions:
""")

# 使用卡片样式展示评估维度
dimensions = {
    "Legal Language": "Binding terms vs. non-binding terms",
    "Source of Authority": "Statute/regulation vs. advisory program",
    "Enforcement Mechanism": "Penalties vs. no consequences",
    "Obligations": "Enforceable vs. discretionary",
    "Optionality/Incentives": "Mandatory vs. incentive-based"
}

for dim, desc in dimensions.items():
    with st.expander(dim, expanded=True):
        st.markdown(f"""
        - **Definition**: {desc}
        - **Evaluation Focus**:
            - Identify key terms and phrases
            - Assess bindingness indicators
            - Consider contextual factors
        """)

st.markdown("""
## Evaluation Process

Our evaluation follows a structured four-step process:
""")

# 使用列布局展示评估过程
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    ### 1. Policy Analysis
    - Examine each dimension
    - Document observed features
    - Identify key indicators
    """)
    
    st.markdown("""
    ### 2. Case Comparison
    - Review similar cases
    - Compare language and structure
    - Assess bindingness patterns
    """)

with col2:
    st.markdown("""
    ### 3. Synthesis
    - Compare direct analysis with cases
    - Identify agreements/disagreements
    - Note ambiguous elements
    """)
    
    st.markdown("""
    ### 4. Scoring
    - Assign bindingness score (1-3)
    - Determine confidence level (0-10)
    - Provide detailed justification
    """)

st.markdown("""
> **Note**: The final score is based primarily on direct analysis, with similar cases serving as contextual benchmarks.
""")