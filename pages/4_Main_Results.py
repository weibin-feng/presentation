import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sentence_transformers import SentenceTransformer
import os
from sklearn.model_selection import StratifiedKFold
import plotly.express as px
import plotly.graph_objects as go
from sklearn.metrics import roc_auc_score, roc_curve, precision_recall_curve, average_precision_score
from sklearn.preprocessing import label_binarize
from scipy.stats import gaussian_kde
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix

st.set_page_config(
    page_title="Main Results - PolicyBindScoreRAG",
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



st.title("Main Results")

st.markdown("""
## 1. K-Fold Cross Validation Results

To validate our approach, we conducted a 5-fold cross-validation study using our manually annotated dataset. This process helps us:
- Assess the robustness of our methodology
- Ensure balanced representation across all bindingness levels
- Validate the effectiveness of our similarity-based retrieval approach

### 1.1 Dataset Overview

Our validation dataset consists of 30 manually annotated policies with the following distribution:
""")

# 读取数据
df = pd.read_excel('k_fold_validation/policy score.xlsx')
score_dist = df['Score'].value_counts().sort_index()

# 创建评分分布表格
score_dist_df = pd.DataFrame({
    'Score': score_dist.index,
    'Count': score_dist.values,
    'Percentage': (score_dist.values / len(df) * 100).round(1)
})
score_dist_df['Score Type'] = score_dist_df['Score'].map({
    1: 'Non-binding',
    2: 'Voluntary/Incentivized',
    3: 'Mandatory'
})

st.table(score_dist_df)

# 绘制评分分布图
fig = px.pie(
    score_dist_df,
    values='Count',
    names='Score Type',
    title='Distribution of Bindingness Scores in Validation Dataset'
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("""
### 1.2 K-Fold Split Strategy

We implemented a stratified 5-fold cross-validation approach to ensure:
- Balanced representation of each bindingness level in both training and test sets
- Consistent distribution across all folds
- Comprehensive evaluation of our methodology

#### Fold Distribution
""")

# 创建5折交叉验证
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# 收集每个折的统计信息
fold_stats = []
for fold_idx, (train_idx, test_idx) in enumerate(skf.split(df, df['Score'])):
    train_df = df.iloc[train_idx]
    test_df = df.iloc[test_idx]
    
    fold_stats.append({
        'Fold': fold_idx + 1,
        'Train Size': len(train_df),
        'Test Size': len(test_df),
        'Train Score 1': len(train_df[train_df['Score'] == 1]),
        'Train Score 2': len(train_df[train_df['Score'] == 2]),
        'Train Score 3': len(train_df[train_df['Score'] == 3]),
        'Test Score 1': len(test_df[test_df['Score'] == 1]),
        'Test Score 2': len(test_df[test_df['Score'] == 2]),
        'Test Score 3': len(test_df[test_df['Score'] == 3])
    })

# 创建折统计表格
fold_stats_df = pd.DataFrame(fold_stats)
st.table(fold_stats_df)

# 绘制折分布图
fig = go.Figure()
for score in [1, 2, 3]:
    fig.add_trace(go.Bar(
        name=f'Score {score}',
        x=fold_stats_df['Fold'],
        y=fold_stats_df[f'Test Score {score}'],
        text=fold_stats_df[f'Test Score {score}'],
        textposition='auto',
    ))
fig.update_layout(
    title='Score Distribution Across Folds',
    xaxis_title='Fold',
    yaxis_title='Count',
    barmode='group',
    showlegend=True,
    legend_title='Score Type'
)
st.plotly_chart(fig, use_container_width=True)

# 添加k折过程可视化
st.markdown("### K-Fold Cross Validation Process")

# 基本参数
num_samples = 30
num_folds = 5
samples_per_fold = num_samples // num_folds
colors = ['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A']

# 选择当前验证折
selected_fold = st.slider("Select Current Validation Fold (0-4)", 0, 4, 0)

# 构造每个样本对应的折编号
sample_fold_mapping = {}
for i in range(num_folds):
    start = i * samples_per_fold
    end = start + samples_per_fold
    for j in range(start, end):
        sample_fold_mapping[j] = i

# 构造图表数据：每个样本一条 bar
data = []
for sample_id in range(num_samples):
    fold_id = sample_fold_mapping[sample_id]
    data.append(dict(
        Sample=sample_id,
        Fold=f"Fold {fold_id}",
        Color=colors[fold_id] if fold_id == selected_fold else 'lightgray'
    ))

# 转为 DataFrame
plot_df = pd.DataFrame(data)

# 创建图表
fig = go.Figure()
fig.add_trace(go.Bar(
    x=plot_df['Sample'],
    y=[1]*len(plot_df),
    marker_color=plot_df['Color'],
    text=plot_df['Fold'],
    hovertext=[f"Sample {i} (Fold {sample_fold_mapping[i]})" for i in plot_df['Sample']],
    orientation='v',
    showlegend=False
))

fig.update_layout(
    title=f"Fold {selected_fold} as Validation Set, Others as Reference Set",
    xaxis_title="Sample Index",
    yaxis=dict(showticklabels=False, range=[0, 2]),
    height=200,
    margin=dict(l=40, r=40, t=40, b=20),
)
st.plotly_chart(fig, use_container_width=True)



st.markdown("""
### 1.3 Evaluation Results

For each fold, we evaluate:
- Accuracy of bindingness scoring
- Confidence level distribution
- Similarity of retrieved cases
- Consistency of evaluation across folds
""")

# 读取k折验证结果
kfold_results = pd.read_excel('k_fold_validation/evaluation_results/policy_score_with_predictions_final_20250527_044812.xlsx')

# 计算评估指标
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix

# 计算准确率
accuracy = accuracy_score(kfold_results['Score'], kfold_results['Predicted_Score'])

# 计算每个类别的精确率、召回率和F1分数
precision, recall, f1, _ = precision_recall_fscore_support(
    kfold_results['Score'], 
    kfold_results['Predicted_Score'],
    average=None
)

# 计算宏平均和加权平均
macro_precision, macro_recall, macro_f1, _ = precision_recall_fscore_support(
    kfold_results['Score'], 
    kfold_results['Predicted_Score'],
    average='macro'
)

weighted_precision, weighted_recall, weighted_f1, _ = precision_recall_fscore_support(
    kfold_results['Score'], 
    kfold_results['Predicted_Score'],
    average='weighted'
)

# 显示评估指标
st.markdown("### 1.3 Evaluation Metrics")

# 创建指标表格
metrics_df = pd.DataFrame({
    'Score': ['Score 1', 'Score 2', 'Score 3', 'Macro Avg', 'Weighted Avg'],
    'Precision': np.append(precision, [macro_precision, weighted_precision]),
    'Recall': np.append(recall, [macro_recall, weighted_recall]),
    'F1-Score': np.append(f1, [macro_f1, weighted_f1])
})

# 格式化数值
metrics_df = metrics_df.round(3)
st.table(metrics_df)

# 创建两列布局
col1, col2 = st.columns(2)

with col1:
    # 混淆矩阵
    cm = confusion_matrix(kfold_results['Score'], kfold_results['Predicted_Score'])
    cm_normalized = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    
    fig = go.Figure(data=go.Heatmap(
        z=cm_normalized,
        x=['Predicted 1', 'Predicted 2', 'Predicted 3'],
        y=['Actual 1', 'Actual 2', 'Actual 3'],
        colorscale='YlOrRd',
        text=[[f'{val:.2%}' for val in row] for row in cm_normalized],
        texttemplate='%{text}',
        textfont={"size": 14},
        colorbar=dict(title='Normalized Count')
    ))
    
    fig.update_layout(
        title='Confusion Matrix (Normalized)',
        height=400,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # ROC曲线
    y_true = kfold_results['Score']
    y_pred = kfold_results['Predicted_Score']
    y_score = kfold_results['Confidence']
    
    # 将标签转换为one-hot编码
    y_true_bin = label_binarize(y_true, classes=[1, 2, 3])
    y_pred_bin = label_binarize(y_pred, classes=[1, 2, 3])
    
    # 计算每个类别的ROC曲线
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(3):
        y_score_bin = (y_pred == i+1).astype(int)
        fpr[i], tpr[i], _ = roc_curve(y_true_bin[:, i], y_score_bin)
        roc_auc[i] = roc_auc_score(y_true_bin[:, i], y_score_bin)
    
    fig = go.Figure()
    for i in range(3):
        fig.add_trace(go.Scatter(
            x=fpr[i],
            y=tpr[i],
            name=f'Score {i+1} (AUC = {roc_auc[i]:.2f})'
        ))
    fig.add_trace(go.Scatter(
        x=[0, 1],
        y=[0, 1],
        name='Random',
        line=dict(dash='dash')
    ))
    
    fig.update_layout(
        title='ROC Curves for Each Score',
        xaxis_title='False Positive Rate',
        yaxis_title='True Positive Rate',
        yaxis=dict(range=[0, 1.05]),
        xaxis=dict(range=[0, 1.05]),
        height=400,
        margin=dict(l=20, r=20, t=40, b=20)
    )
    st.plotly_chart(fig, use_container_width=True)

# 删除置信度分布部分，直接进入完整数据集结果
st.markdown("""
## 2. Full Dataset Deployment Results

We applied our validated methodology to the complete dataset of 846 policies. The results provide comprehensive insights into policy bindingness patterns.
""")

# 读取完整数据集结果
full_results = pd.read_excel('policy_scoring/evaluation_results/need_score_with_predictions_final_20250527_081756.xlsx')

# 2.1 评分和置信度分析
st.markdown("### 2.1 Score and Confidence Analysis")

# 创建两列布局
col1, col2 = st.columns(2)

with col1:
    # 计算评分分布
    score_dist = full_results['Predicted_Score'].value_counts().sort_index()
    score_dist_pct = (score_dist / len(full_results) * 100).round(1)
    
    # 创建评分分布图表
    fig = px.bar(
        x=score_dist.index,
        y=score_dist.values,
        text=score_dist_pct.apply(lambda x: f'{x}%'),
        labels={'x': 'Score', 'y': 'Count'},
        title='Distribution of Bindingness Scores'
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # 计算每个评分的平均置信度
    confidence_by_score = full_results.groupby('Predicted_Score')['Confidence'].agg(['mean', 'std']).round(2)
    
    # 创建置信度箱线图
    fig = px.box(
        full_results,
        x='Predicted_Score',
        y='Confidence',
        title='Confidence Distribution by Score',
        points='all'
    )
    fig.update_layout(height=400)
    st.plotly_chart(fig, use_container_width=True)

# 2.2 相似度分析
st.markdown("### 2.2 Similarity Analysis")

# 计算相似度统计
similarity_cols = [col for col in full_results.columns if 'Similarity' in col]
if similarity_cols:
    # 计算相似度统计（包括分位数）
    similarity_stats = full_results[similarity_cols].describe(percentiles=[.25, .5, .75]).round(3)
    st.table(similarity_stats)
    
    # 创建相似度分布图
    fig = go.Figure()
    for col in similarity_cols:
        fig.add_trace(go.Histogram(
            x=full_results[col],
            name=col,
            opacity=0.7
        ))
    
    fig.update_layout(
        title='Distribution of Similarity Scores',
        xaxis_title='Similarity Score',
        yaxis_title='Count',
        barmode='overlay',
        height=400
    )
    st.plotly_chart(fig, use_container_width=True)
