# -*- coding: utf-8 -*-

"""
配置参数信息
"""

Config = {
    "model_path": r"F:\motrix\新建文件夹\深度学习\第八周文本匹配\week8 文本匹配问题\model_path",
    "schema_path": r"F:\motrix\新建文件夹\深度学习\第八周文本匹配\week8 文本匹配问题\data\schema.json",
    "train_data_path": r"F:\motrix\新建文件夹\深度学习\第八周文本匹配\week8 文本匹配问题\data\train.json",
    "valid_data_path": r"F:\motrix\新建文件夹\深度学习\第八周文本匹配\week8 文本匹配问题\data\valid.json",
    "vocab_path": r"F:\motrix\新建文件夹\深度学习\第八周文本匹配\week8 文本匹配问题\chars.txt",
    "max_length": 20,
    "hidden_size": 128,
    "epoch": 10,
    "batch_size": 32,
    "epoch_data_size": 200,     #每轮训练中采样数量
    "positive_sample_rate":0.5,  #正样本比例
    "optimizer": "adam",
    "learning_rate": 1e-3,
}
