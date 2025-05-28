import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold
import os

def get_kfold_stats():
    # 读取数据
    df = pd.read_excel('k_fold_validation/policy score.xlsx')
    
    # 创建5折交叉验证
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    
    # 收集每个折的统计信息
    fold_stats = []
    for fold_idx, (train_idx, test_idx) in enumerate(skf.split(df, df['Score'])):
        train_df = df.iloc[train_idx]
        test_df = df.iloc[test_idx]
        
        # 计算每个折的分布
        train_dist = train_df['Score'].value_counts().sort_index()
        test_dist = test_df['Score'].value_counts().sort_index()
        
        # 获取一些示例
        train_examples = train_df.sample(2)
        test_examples = test_df.sample(2)
        
        fold_stats.append({
            'fold': fold_idx + 1,
            'train_size': len(train_df),
            'test_size': len(test_df),
            'train_distribution': train_dist.to_dict(),
            'test_distribution': test_dist.to_dict(),
            'train_examples': train_examples.to_dict('records'),
            'test_examples': test_examples.to_dict('records')
        })
    
    # 计算总体统计
    total_stats = {
        'total_policies': len(df),
        'score_distribution': df['Score'].value_counts().sort_index().to_dict(),
        'type_distribution': df['Type'].value_counts().to_dict(),
        'text_length_stats': {
            'mean': (df['Type'] + ' ' + df['Description']).str.len().mean(),
            'std': (df['Type'] + ' ' + df['Description']).str.len().std(),
            'min': (df['Type'] + ' ' + df['Description']).str.len().min(),
            'max': (df['Type'] + ' ' + df['Description']).str.len().max()
        }
    }
    
    return {
        'fold_stats': fold_stats,
        'total_stats': total_stats
    }

if __name__ == "__main__":
    stats = get_kfold_stats()
    print("\nTotal Statistics:")
    print(f"Total policies: {stats['total_stats']['total_policies']}")
    print("\nScore Distribution:")
    for score, count in stats['total_stats']['score_distribution'].items():
        print(f"Score {score}: {count} policies")
    print("\nFold Statistics:")
    for fold in stats['fold_stats']:
        print(f"\nFold {fold['fold']}:")
        print(f"Train size: {fold['train_size']}")
        print(f"Test size: {fold['test_size']}")
        print("Train distribution:")
        for score, count in fold['train_distribution'].items():
            print(f"  Score {score}: {count} policies")
        print("Test distribution:")
        for score, count in fold['test_distribution'].items():
            print(f"  Score {score}: {count} policies") 