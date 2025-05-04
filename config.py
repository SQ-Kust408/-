# 飞书配置
import torch

FEISHU_CONFIG = {
    "app_id": "",        # 飞书应用App ID
    "app_secret": "",  # App Secret
    "receive_id_type": "user_id",           # 接收者ID类型（user_id/email/chat_id）
    "default_user_id": "" # 默认测试用户ID
}

# Hugging Face配置
HUGGINGFACE_CONFIG = {
    "model_name": "bert-base-chinese",       # 预训练模型名称
    "max_length": 512,                       # 输入文本最大长度
    "intent_mapping": {                      # 意图标签映射
        0: "设备报修",
        1: "合同审查",
        2: "订单查询",
        3: "通用咨询"
    }
}

# 系统配置
SYSTEM_CONFIG = {
    "log_path": "app.log",                   # 日志文件路径
    "device": "cuda" if torch.cuda.is_available() else "cpu",  # 设备类型（自动检测GPU）
    "debug_mode": True                       # 调试模式（开启详细日志）
}