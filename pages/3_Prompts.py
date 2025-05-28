import streamlit as st
import os
import json

st.set_page_config(
    page_title="Prompts - PolicyBindScoreRAG",
    page_icon="💬",
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



st.title("Prompts")

# 使用列布局
col1, col2 = st.columns([2,1])

with col1:
    st.markdown("""
    ### Prompt Templates

    This page displays the prompt templates used for policy bindingness evaluation. Each prompt is structured to guide the LLM through a systematic analysis of policy bindingness, incorporating both direct analysis and comparison with similar cases.

    The prompts follow a consistent structure:
    1. Task definition and objectives
    2. Scoring categories and criteria
    3. Evaluation dimensions
    4. Step-by-step analysis procedure
    5. Output format specification
    """)

    # 获取所有提示词文件
    prompts_dir = "policy_scoring/prompts"
    prompt_files = [f for f in os.listdir(prompts_dir) if f.endswith('.md')]

    # 提取政策ID
    policy_ids = [f.replace('prompt_policy_', '').replace('.md', '') for f in prompt_files]
    policy_ids.sort(key=int)  # 按数字排序

    # 创建下拉列表
    selected_policy_id = st.selectbox(
        "Select Policy ID",
        policy_ids
    )

    # 读取并显示选中的提示词
    if selected_policy_id:
        prompt_file = f"prompt_policy_{selected_policy_id}.md"
        prompt_path = os.path.join(prompts_dir, prompt_file)
        
        try:
            with open(prompt_path, 'r', encoding='utf-8') as f:
                prompt_content = f.read()
                
            st.markdown("### Prompt Content")
            st.code(prompt_content, language="markdown")
            
        except Exception as e:
            st.error(f"Error reading prompt file: {str(e)}")

with col2:
    st.markdown("""
    ### Output JSON Template

    The LLM's response follows a structured JSON format:
    """)
    
    # JSON模板
    json_template = {
        "Score": "[1 | 2 | 3]",
        "Confidence": "[0-10]",
        "Explanation": {
            "Legal_Language": "[Explain what kind of language the current policy uses (e.g., 'shall', 'may', 'encourage')]",
            "Source_of_Authority": "[Explain whether this policy stems from law, regulation, or advisory source]",
            "Enforcement_Mechanism": "[Explain if there are penalties, deadlines, or if it is purely aspirational]",
            "Obligations": "[Explain who is required to act, and whether responsibilities are enforceable]",
            "Optionality_or_Incentives": "[Explain whether the policy provides incentives or is fully mandatory]"
        },
        "Inference_Chain": [
            "Step 1: Direct analysis of the current policy shows [binding/non-binding] terms ('[term]') and [source of authority]",
            "Step 2: Retrieved [CASE_A_Name] (sim=[CASE_A_Similarity], Score [CASE_A_Score]) has similar features",
            "Step 3: Retrieved [CASE_B_Name] (sim=[CASE_B_Similarity], Score [CASE_B_Score]) shares some elements but lacks [feature]",
            "Step 4: Current policy aligns more with [CASE_A_Name] due to [reason]",
            "Step 5: Direct analysis has priority; retrieved cases provide additional support weighted by their similarity scores",
            "Step 6: Final judgment: Score [Final_Score], Confidence [Confidence_Score]"
        ],
        "Comparable_Cases": [
            {
                "Policy_ID": "[CASE_1_ID]",
                "Case_Name": "[CASE_1_NAME]",
                "Score": "[SCORE_1]",
                "Reason": "[Summarize why this case is highly similar and informative for the current policy evaluation]"
            },
            {
                "Policy_ID": "[CASE_2_ID]",
                "Case_Name": "[CASE_2_NAME]",
                "Score": "[SCORE_2]",
                "Reason": "[Summarize why this case is also relevant and comparable to the current policy]"
            }
        ]
    }
    
    # 显示格式化的JSON
    st.json(json_template)
    
    st.markdown("""
    ### Key Components:
    
    1. **Score**: Bindingness level (1-3)
    2. **Confidence**: Evaluation certainty (0-10)
    3. **Explanation**: Detailed analysis of each dimension
    4. **Inference_Chain**: Step-by-step reasoning process
    5. **Comparable_Cases**: Similar reference policies
    """) 