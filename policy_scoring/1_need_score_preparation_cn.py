import os
import json
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import logging
from datetime import datetime

class NeedScorePreparator:
    def __init__(self, model_name='all-mpnet-base-v2'):
        """初始化数据准备器"""
        # 设置日志
        self.setup_logging()
        
        # 初始化文本编码器
        self.logger.info("初始化文本编码器...")
        self.encoder = SentenceTransformer(model_name)
        
        # 设置目录
        self.data_dir = 'policy_scoring/need_score_processed'
        os.makedirs(self.data_dir, exist_ok=True)
        
    def setup_logging(self):
        """设置日志记录"""
        # 创建logs目录
        logs_dir = 'policy_scoring/logs'
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
            
        # 生成日志文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = f'{logs_dir}/need_score_preparation_{timestamp}.log'
        
        # 配置日志记录器
        self.logger = logging.getLogger('NeedScorePreparator')
        self.logger.setLevel(logging.INFO)
        
        # 文件处理器
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        
        # 控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # 设置日志格式
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        # 添加处理器
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
        self.logger.info(f"日志文件已创建: {log_file}")
    
    def load_data(self, reference_file: str = 'policy_scoring/policy_score.xlsx', target_file: str = 'policy_scoring/need_score.xlsx') -> tuple:
        """加载参考数据和目标数据"""
        self.logger.info(f"加载参考数据: {reference_file}")
        reference_df = pd.read_excel(reference_file)
        
        self.logger.info(f"加载目标数据: {target_file}")
        target_df = pd.read_excel(target_file)
        
        # 验证必需列
        required_columns = ['Policy_ID', 'Policy_Name', 'Type', 'Description']
        for df, name in [(reference_df, '参考数据'), (target_df, '目标数据')]:
            missing_columns = [col for col in required_columns if col not in df.columns]
            if missing_columns:
                raise ValueError(f"{name}缺少必需列: {missing_columns}")
            
            # 检查空值
            for col in required_columns:
                null_count = df[col].isna().sum()
                if null_count > 0:
                    self.logger.warning(f"{name}中{col}列有{null_count}个空值")
                    # 显示空值的Policy_ID
                    null_ids = df[df[col].isna()]['Policy_ID'].tolist()
                    self.logger.warning(f"空值的Policy_ID: {null_ids}")
            
            # 检查空字符串
            for col in ['Type', 'Description']:
                empty_count = (df[col] == '').sum()
                if empty_count > 0:
                    self.logger.warning(f"{name}中{col}列有{empty_count}个空字符串")
                    # 显示空字符串的Policy_ID
                    empty_ids = df[df[col] == '']['Policy_ID'].tolist()
                    self.logger.warning(f"空字符串的Policy_ID: {empty_ids}")
        
        # 显示数据分布
        self.logger.info(f"\n参考数据: {len(reference_df)} 条")
        if 'Score' in reference_df.columns:
            score_dist = reference_df['Score'].value_counts().sort_index()
            self.logger.info("参考数据评分分布:")
            for score, count in score_dist.items():
                self.logger.info(f"Score {score}: {count} 条 ({count/len(reference_df)*100:.1f}%)")
        
        self.logger.info(f"\n目标数据: {len(target_df)} 条")
        
        return reference_df, target_df
    
    def create_embeddings(self, df: pd.DataFrame) -> np.ndarray:
        """创建文本嵌入"""
        self.logger.info("创建文本嵌入...")
        
        try:
            # 组合Type和Description
            texts = df['Type'] + ' ' + df['Description']
            self.logger.info(f"文本数量: {len(texts)}")
            
            # 检查文本是否为空
            empty_texts = texts[texts.isna() | (texts == '')]
            if not empty_texts.empty:
                self.logger.warning(f"发现 {len(empty_texts)} 个空文本")
                self.logger.warning(f"空文本的索引: {empty_texts.index.tolist()}")
            
            # 生成嵌入
            self.logger.info("开始生成嵌入...")
            try:
                # 分批处理，每批100条
                batch_size = 100
                all_embeddings = []
                
                for i in range(0, len(texts), batch_size):
                    batch_texts = texts[i:i+batch_size]
                    self.logger.info(f"处理第 {i//batch_size + 1} 批，包含 {len(batch_texts)} 条文本")
                    
                    batch_embeddings = self.encoder.encode(batch_texts.tolist(), show_progress_bar=True)
                    all_embeddings.append(batch_embeddings)
                
                # 合并所有批次的嵌入
                embeddings = np.vstack(all_embeddings)
                self.logger.info(f"嵌入生成完成，类型: {type(embeddings)}")
                
            except Exception as e:
                self.logger.error(f"生成嵌入时出错: {str(e)}")
                raise
            
            # 确保是numpy数组
            if not isinstance(embeddings, np.ndarray):
                self.logger.info("转换嵌入为numpy数组...")
                embeddings = np.array(embeddings)
            
            # 确保向量是float32类型
            self.logger.info("转换向量为float32类型...")
            embeddings = embeddings.astype('float32')
            
            self.logger.info(f"成功创建 {len(embeddings)} 个嵌入向量，形状: {embeddings.shape}")
            return embeddings
            
        except Exception as e:
            self.logger.error(f"创建嵌入时发生错误: {str(e)}")
            raise
    
    def create_faiss_index(self, embeddings: np.ndarray) -> tuple:
        """创建FAISS索引"""
        self.logger.info("创建FAISS索引...")
        
        # 添加调试日志
        self.logger.info(f"embeddings类型: {type(embeddings)}")
        self.logger.info(f"embeddings形状: {embeddings.shape}")
        
        # 确保向量是float32类型并进行L2归一化
        embeddings = embeddings.astype('float32')
        self.logger.info("向量已转换为float32类型")
        
        faiss.normalize_L2(embeddings)
        self.logger.info("向量已完成L2归一化")
        
        # 创建索引（使用点积）
        dimension = embeddings.shape[1]
        self.logger.info(f"向量维度: {dimension}")
        
        index = faiss.IndexFlatIP(dimension)  # 使用点积
        self.logger.info("FAISS索引已创建")
        
        # 添加向量
        index.add(embeddings)
        self.logger.info("向量已添加到索引")
        
        # 保存索引
        index_path = os.path.join(self.data_dir, 'faiss_index.index')
        faiss.write_index(index, index_path)
        
        self.logger.info(f"FAISS索引已保存到: {index_path}")
        return index, embeddings
    
    def process_data(self):
        """处理数据主函数"""
        try:
            # 加载数据
            reference_df, target_df = self.load_data()
            
            # 创建嵌入
            reference_embeddings = self.create_embeddings(reference_df)
            target_embeddings = self.create_embeddings(target_df)
            
            # 保存处理后的数据
            processed_data = {
                'reference_data': reference_df.to_dict(orient='records'),
                'reference_embeddings': reference_embeddings.tolist(),
                'target_data': target_df.to_dict(orient='records'),
                'target_embeddings': target_embeddings.tolist()
            }
            
            with open(os.path.join(self.data_dir, 'processed_data.json'), 'w', encoding='utf-8') as f:
                json.dump(processed_data, f, ensure_ascii=False, indent=2)
            
            # 创建FAISS索引
            self.create_faiss_index(reference_embeddings)
            
            self.logger.info("\n数据处理完成")
            
        except Exception as e:
            self.logger.error(f"数据处理过程中发生错误: {str(e)}")
            raise

def main():
    try:
        preparator = NeedScorePreparator()
        preparator.process_data()
        print("\n数据处理完成！")
        print("处理后的数据已保存到 policy_scoring/need_score_processed 目录")
        print("请查看日志文件了解详细的数据分布情况")
        
    except Exception as e:
        print(f"\n程序执行出错: {str(e)}")
        print("请查看日志文件了解详细信息")

if __name__ == "__main__":
    main() 