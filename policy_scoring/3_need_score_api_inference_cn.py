import os
import json
import time
import logging
from datetime import datetime
from typing import Dict, List, Optional
import pandas as pd
from tqdm import tqdm
from openai import OpenAI
import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import partial

class NeedScorePolicyScorer:
    def __init__(self, api_key: str, model_name: str = "deepseek-chat", batch_size: int = 5, max_workers: int = 4):
        """初始化政策评分器"""
        # 设置日志
        self.setup_logging()
        
        self.logger.info("\n=== 初始化政策评分器 ===")
        
        # 初始化API客户端
        self.logger.info("\n1. 初始化API客户端...")
        try:
            self.client = OpenAI(
                api_key=api_key,
                base_url="https://api.deepseek.com"
            )
            self.model_name = model_name
            self.batch_size = batch_size
            self.max_workers = max_workers
            self.logger.info(f"API客户端初始化完成，使用模型: {model_name}")
            self.logger.info(f"批处理大小: {batch_size}, 最大工作线程数: {max_workers}")
        except Exception as e:
            self.logger.error(f"API客户端初始化失败: {str(e)}")
            raise
        
        # 创建输出目录
        self.output_dir = 'policy_scoring/evaluation_results'
        os.makedirs(self.output_dir, exist_ok=True)
        self.logger.info(f"输出目录已创建: {self.output_dir}")
        
    def setup_logging(self):
        """设置日志记录"""
        # 创建logs目录
        logs_dir = 'policy_scoring/logs'
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)
            
        # 生成日志文件名
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = f'{logs_dir}/need_score_api_inference_{timestamp}.log'
        
        # 配置日志记录器
        self.logger = logging.getLogger('NeedScorePolicyScorer')
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
    
    def extract_json_from_response(self, response: str) -> Optional[Dict]:
        """从API响应中提取JSON"""
        try:
            # 查找JSON开始和结束的位置
            start_idx = response.find('{')
            end_idx = response.rfind('}') + 1
            
            if start_idx == -1 or end_idx == 0:
                self.logger.error("未找到JSON响应")
                return None
            
            # 提取JSON字符串
            json_str = response[start_idx:end_idx]
            
            # 解析JSON
            result = json.loads(json_str)
            
            # 验证必需字段
            required_fields = ['Score', 'Confidence', 'Explanation', 'Inference_Chain', 'Comparable_Cases']
            missing_fields = [field for field in required_fields if field not in result]
            if missing_fields:
                self.logger.error(f"缺少必需字段: {missing_fields}")
                return None
            
            # 验证并转换字段类型
            try:
                # 验证Score
                if not isinstance(result['Score'], int):
                    result['Score'] = int(result['Score'])
                if result['Score'] not in [1, 2, 3]:
                    self.logger.error(f"无效的评分: {result['Score']}")
                    return None
                
                # 验证Confidence
                if not isinstance(result['Confidence'], (int, float)):
                    result['Confidence'] = float(result['Confidence'])
                if not (0 <= result['Confidence'] <= 10):
                    self.logger.error(f"无效的置信度: {result['Confidence']}")
                    return None
                
                # 验证Explanation
                if not isinstance(result['Explanation'], dict):
                    if isinstance(result['Explanation'], str):
                        try:
                            result['Explanation'] = json.loads(result['Explanation'])
                        except:
                            self.logger.error("Explanation无法转换为字典类型")
                            return None
                    else:
                        self.logger.error("Explanation必须是字典类型")
                        return None
                
                # 验证Inference_Chain
                if not isinstance(result['Inference_Chain'], list):
                    if isinstance(result['Inference_Chain'], str):
                        try:
                            result['Inference_Chain'] = json.loads(result['Inference_Chain'])
                        except:
                            self.logger.error("Inference_Chain无法转换为列表类型")
                            return None
                    else:
                        self.logger.error("Inference_Chain必须是列表类型")
                        return None
                
                # 验证Comparable_Cases
                if not isinstance(result['Comparable_Cases'], list):
                    if isinstance(result['Comparable_Cases'], str):
                        try:
                            result['Comparable_Cases'] = json.loads(result['Comparable_Cases'])
                        except:
                            self.logger.error("Comparable_Cases无法转换为列表类型")
                            return None
                    else:
                        self.logger.error("Comparable_Cases必须是列表类型")
                        return None
                
                return result
                
            except (ValueError, TypeError) as e:
                self.logger.error(f"字段类型转换失败: {str(e)}")
                return None
            
        except json.JSONDecodeError as e:
            self.logger.error(f"JSON解析错误: {str(e)}")
            return None
        except Exception as e:
            self.logger.error(f"提取JSON时发生错误: {str(e)}")
            return None
    
    def score_policy(self, prompt: str) -> Optional[Dict]:
        """评分单个政策"""
        try:
            # 调用API
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are a professional policy evaluation assistant. Your task is to assess the bindingness of policies and return the result strictly in JSON format."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                max_tokens=2000,
                stream=False
            )
            
            # 提取响应内容
            content = response.choices[0].message.content
            
            # 提取JSON
            result = self.extract_json_from_response(content)
            if result is None:
                return None
            
            return result
            
        except Exception as e:
            self.logger.error(f"评分过程中发生错误: {str(e)}")
            return None
    
    def process_batch(self, batch: List[tuple], batch_num: int, total_batches: int, original_df: pd.DataFrame, processed_count: int) -> tuple:
        """处理一批政策"""
        results = []
        self.logger.info(f"处理批次 {batch_num}/{total_batches}，共 {len(batch)} 个文件")
        
        for i, (file, prompt) in enumerate(batch, 1):
            try:
                result = self.score_policy(prompt)
                if result is not None:
                    results.append((file, result))
                    # 立即更新数据框
                    policy_id = f"policy/{file.replace('prompt_policy_', '').replace('.txt', '')}"
                    mask = original_df['Policy_ID'] == policy_id
                    if mask.any():
                        # 更新基本字段
                        original_df.loc[mask, 'Predicted_Score'] = result['Score']
                        original_df.loc[mask, 'Confidence'] = result['Confidence']
                        
                        # 解析Explanation
                        explanation = result['Explanation']
                        original_df.loc[mask, 'Explanation'] = json.dumps(explanation, ensure_ascii=False)
                        original_df.loc[mask, 'Legal_Language'] = explanation.get('Legal_Language', '')
                        original_df.loc[mask, 'Source_of_Authority'] = explanation.get('Source_of_Authority', '')
                        original_df.loc[mask, 'Enforcement_Mechanism'] = explanation.get('Enforcement_Mechanism', '')
                        original_df.loc[mask, 'Obligations'] = explanation.get('Obligations', '')
                        original_df.loc[mask, 'Optionality_or_Incentives'] = explanation.get('Optionality_or_Incentives', '')
                        
                        # 解析Inference_Chain
                        inference_chain = result['Inference_Chain']
                        original_df.loc[mask, 'Inference_Chain'] = json.dumps(inference_chain, ensure_ascii=False)
                        original_df.loc[mask, 'Inference_Steps'] = '\n'.join(inference_chain)
                        
                        # 解析Comparable_Cases
                        comparable_cases = result['Comparable_Cases']
                        original_df.loc[mask, 'Comparable_Cases'] = json.dumps(comparable_cases, ensure_ascii=False)
                        
                        # 提取相似案例信息
                        if len(comparable_cases) >= 1:
                            case1 = comparable_cases[0]
                            original_df.loc[mask, 'Similar_Case_1'] = case1.get('Case_Name', '')
                            original_df.loc[mask, 'Similar_Case_1_Score'] = case1.get('Score', '')
                            original_df.loc[mask, 'Similar_Case_1_Similarity'] = case1.get('Similarity', '')
                        
                        if len(comparable_cases) >= 2:
                            case2 = comparable_cases[1]
                            original_df.loc[mask, 'Similar_Case_2'] = case2.get('Case_Name', '')
                            original_df.loc[mask, 'Similar_Case_2_Score'] = case2.get('Score', '')
                            original_df.loc[mask, 'Similar_Case_2_Similarity'] = case2.get('Similarity', '')
                        
                        # 更新处理计数
                        processed_count += 1
                        
                        # 每处理100个文件保存一次
                        if processed_count % 100 == 0:
                            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                            output_file = os.path.join(self.output_dir, f'need_score_with_predictions_{timestamp}.xlsx')
                            original_df.to_excel(output_file, index=False)
                            self.logger.info(f"已处理 {processed_count} 个文件，保存结果: {output_file}")
                    else:
                        self.logger.error(f"未找到政策ID: {policy_id}")
            except Exception as e:
                self.logger.error(f"处理文件 {file} 时发生错误: {str(e)}")
        
        self.logger.info(f"批次 {batch_num}/{total_batches} 完成，成功: {len(results)}/{len(batch)}")
        return results, processed_count

    def process_policies(self, prompts_dir: str = 'policy_scoring/prompts'):
        """处理所有政策"""
        self.logger.info("=== 开始处理政策 ===")
        try:
            # 检查提示目录是否存在
            if not os.path.exists(prompts_dir):
                self.logger.error(f"提示目录不存在: {prompts_dir}")
                raise FileNotFoundError(f"提示目录不存在: {prompts_dir}")
            
            # 获取所有提示文件
            prompt_files = [f for f in os.listdir(prompts_dir) if f.startswith('prompt_') and f.endswith('.txt')]
            if not prompt_files:
                self.logger.error(f"在目录 {prompts_dir} 中未找到任何提示文件")
                raise FileNotFoundError(f"在目录 {prompts_dir} 中未找到任何提示文件")
            
            total_files = len(prompt_files)
            self.logger.info(f"找到 {total_files} 个提示文件")
            
            # 读取原始数据文件
            original_df = pd.read_excel('policy_scoring/need_score.xlsx')
            
            # 添加预测结果列
            original_df['Predicted_Score'] = None
            original_df['Confidence'] = None
            original_df['Explanation'] = None
            original_df['Inference_Chain'] = None
            original_df['Comparable_Cases'] = None
            
            # 添加详细解析列
            original_df['Legal_Language'] = None
            original_df['Source_of_Authority'] = None
            original_df['Enforcement_Mechanism'] = None
            original_df['Obligations'] = None
            original_df['Optionality_or_Incentives'] = None
            original_df['Inference_Steps'] = None
            original_df['Similar_Case_1'] = None
            original_df['Similar_Case_2'] = None
            original_df['Similar_Case_1_Score'] = None
            original_df['Similar_Case_2_Score'] = None
            original_df['Similar_Case_1_Similarity'] = None
            original_df['Similar_Case_2_Similarity'] = None
            
            # 准备批处理数据
            batches = []
            current_batch = []
            
            for i, file in enumerate(prompt_files, 1):
                try:
                    with open(os.path.join(prompts_dir, file), 'r', encoding='utf-8') as f:
                        prompt = f.read()
                    current_batch.append((file, prompt))
                    
                    if len(current_batch) >= self.batch_size:
                        batches.append(current_batch)
                        current_batch = []
                except Exception as e:
                    self.logger.error(f"读取文件 {file} 时发生错误: {str(e)}")
            
            if current_batch:
                batches.append(current_batch)
            
            total_batches = len(batches)
            self.logger.info(f"批处理数据准备完成，共 {total_batches} 批")
            
            # 使用线程池处理批次
            processed_files = 0
            successful_files = 0
            processed_count = 0
            
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = [
                    executor.submit(self.process_batch, batch, i+1, total_batches, original_df, processed_count)
                    for i, batch in enumerate(batches)
                ]
                
                for future in tqdm(as_completed(futures), total=len(futures), desc="处理批次"):
                    try:
                        batch_results, processed_count = future.result()
                        processed_files += len(batch_results)
                        successful_files += len(batch_results)
                        self.logger.info(f"进度: {processed_files}/{total_files}，成功: {successful_files}/{processed_files}")
                    except Exception as e:
                        self.logger.error(f"处理批次时发生错误: {str(e)}")
            
            self.logger.info(f"所有批次处理完成，共处理 {processed_files}/{total_files} 个文件")
            
            # 生成最终输出文件名
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            final_output_file = os.path.join(self.output_dir, f'need_score_with_predictions_final_{timestamp}.xlsx')
            
            # 保存最终结果
            original_df.to_excel(final_output_file, index=False)
            self.logger.info(f"最终结果已保存到: {final_output_file}")
            
            return original_df
            
        except Exception as e:
            self.logger.error(f"处理政策时发生错误: {str(e)}")
            raise

def main():
    try:
        # 设置API密钥
        api_key = "sk-d77ee9363560463b9c8c6eb2adca3704"
        
        # 创建评分器并处理政策
        scorer = NeedScorePolicyScorer(
            api_key=api_key,
            batch_size=10,  # 每批处理5个文件
            max_workers=5  # 使用4个线程
        )
        
        # 确保提示目录存在
        prompts_dir = 'policy_scoring/prompts'
        if not os.path.exists(prompts_dir):
            os.makedirs(prompts_dir)
            print(f"已创建提示目录: {prompts_dir}")
            print("请将提示文件放入该目录后重新运行程序")
            return
        
        # 处理政策
        results = scorer.process_policies()
        
        if results is not None:
            print(f"\n成功处理 {len(results)} 个政策")
            print(f"结果已保存到 policy_scoring/evaluation_results 目录")
        else:
            print("\n处理失败，请查看日志文件了解详细信息")
            
    except Exception as e:
        print(f"\n程序执行出错: {str(e)}")
        print("请查看日志文件了解详细信息")

if __name__ == "__main__":
    main() 