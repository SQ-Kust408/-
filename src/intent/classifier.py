import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from MultiAgent.src.utils.config_loader import get_config
from MultiAgent.src.utils.logger import logger

config = get_config("huggingface")
system_config = get_config("system")

class ChineseIntentClassifier:
    def __init__(self):
        self.model_name = config["model_name"]
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            config["model_name"],
            num_labels=len(config["intent_mapping"])  # 动态获取类别数
        )
        self.model.to(system_config["device"])  # 模型加载到指定设备（CPU/GPU）
        self.intent_mapping = config["intent_mapping"]

    def preprocess(self, text: str) -> dict:
        """文本预处理并转换为模型输入"""
        inputs = self.tokenizer(
            text,
            padding=True,
            truncation=True,
            return_tensors="pt",
            max_length=config["max_length"]
        )
        # 数据移动到目标设备
        inputs = {k: v.to(system_config["device"]) for k, v in inputs.items()}
        return inputs

    def predict(self, text: str) -> str:
        """意图预测主函数"""
        try:
            inputs = self.preprocess(text)
            with torch.no_grad():
                outputs = self.model(**inputs)
                logits = outputs.logits
                predicted_class = torch.argmax(logits, dim=1).item()
            return self.intent_mapping[predicted_class]
        except Exception as e:
            logger.error(f"意图识别失败：{str(e)}")
            return self.intent_mapping[3]  # 默认返回通用咨询