# 飞书意图助手（Feishu Intent Assistant）

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![飞书API](https://img.shields.io/badge/飞书API-v1.4.15-green.svg)](https://open.feishu.cn/)
[![Hugging Face](https://img.shields.io/badge/Hugging%20Face-Transformers-orange.svg)](https://huggingface.co/)

## 项目简介
基于 **Hugging Face 中文意图识别** 和 **飞书 API** 的轻量级智能助手，支持将用户输入文本识别为设备报修、合同审查等意图，并通过飞书发送结构化通知。适用于企业内部客服、工单系统等场景。


## 核心功能
1. **多意图识别**：支持4种中文业务意图（设备报修、合同审查、订单查询、通用咨询）。  
2. **飞书通知**：通过飞书API发送文本/富文本/卡片消息，支持用户自定义模板。  
3. **模块化设计**：配置集中管理，模型与通知模块解耦，便于扩展新功能。  


## 技术栈
- **意图识别**：Hugging Face Transformers（BERT 模型）  
- **消息通知**：飞书开放平台 API（`lark-oapi` SDK）  
- **配置管理**：Python 字典集中管理超参数  
- **环境**：Python 3.10，支持 CPU/GPU 自动检测  


## 配置
# config.py（关键参数）
python
```
FEISHU_CONFIG = {
    "app_id": "你的飞书App ID",        # 从开放平台获取
    "app_secret": "你的飞书App Secret",  # 从开放平台获取
    "receive_id_type": "user_id",       # 固定值（用户ID类型）
    "default_user_id": "你的飞书User ID"  # 格式：ou_xxxxxxxx
}

HUGGINGFACE_CONFIG = {
    "model_name": "bert-base-chinese",  # 中文预训练模型（可替换为其他分类模型）
}
```





## 本地输入
![b4ad15e5-8279-4243-90e3-61a2f67196f7](https://github.com/user-attachments/assets/cc28aebd-b45b-4f21-ac40-eb91fb82627b)
## 飞书端机器人传达
![f6405dc6-102e-49ff-a589-1e07146cd581](https://github.com/user-attachments/assets/b078b021-8846-4ac3-a147-14dba3a2d42a)
