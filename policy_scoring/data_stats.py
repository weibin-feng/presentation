import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import os

def get_data_stats():
    # 读取数据
    reference_df = pd.read_excel('policy_scoring/policy_score.xlsx')
    target_df = pd.read_excel('policy_scoring/need_score.xlsx')
    
    # 获取参考数据的评分分布
    score_dist = reference_df['Score'].value_counts().sort_index()
    
    # 获取目标数据的类型分布
    type_dist = target_df['Type'].value_counts()
    
    # 计算文本长度统计
    reference_df['text_length'] = (reference_df['Type'] + ' ' + reference_df['Description']).str.len()
    target_df['text_length'] = (target_df['Type'] + ' ' + target_df['Description']).str.len()
    
    # 获取一些示例
    first_policy = target_df.iloc[0]
    last_policy = target_df.iloc[-1]
    
    # 获取一些参考案例
    example_references = reference_df.sample(2)
    
    stats = {
        'reference_count': len(reference_df),
        'target_count': len(target_df),
        'score_distribution': score_dist.to_dict(),
        'type_distribution': type_dist.to_dict(),
        'reference_text_stats': {
            'mean': reference_df['text_length'].mean(),
            'std': reference_df['text_length'].std(),
            'min': reference_df['text_length'].min(),
            'max': reference_df['text_length'].max()
        },
        'target_text_stats': {
            'mean': target_df['text_length'].mean(),
            'std': target_df['text_length'].std(),
            'min': target_df['text_length'].min(),
            'max': target_df['text_length'].max()
        },
        'first_policy': first_policy.to_dict(),
        'last_policy': last_policy.to_dict(),
        'example_references': example_references.to_dict('records')
    }
    
    return stats

if __name__ == "__main__":
    stats = get_data_stats()
    print("\nData Statistics:")
    print(f"Reference policies: {stats['reference_count']}")
    print(f"Target policies: {stats['target_count']}")
    print("\nScore Distribution:")
    for score, count in stats['score_distribution'].items():
        print(f"Score {score}: {count} policies")
    print("\nText Length Statistics:")
    print("Reference policies:")
    print(f"Mean: {stats['reference_text_stats']['mean']:.1f}")
    print(f"Std: {stats['reference_text_stats']['std']:.1f}")
    print(f"Min: {stats['reference_text_stats']['min']}")
    print(f"Max: {stats['reference_text_stats']['max']}") 