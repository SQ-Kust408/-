from MultiAgent.config import FEISHU_CONFIG, HUGGINGFACE_CONFIG, SYSTEM_CONFIG

def get_config(section: str) -> dict:
    """获取指定模块的配置"""
    config_map = {
        "feishu": FEISHU_CONFIG,
        "huggingface": HUGGINGFACE_CONFIG,
        "system": SYSTEM_CONFIG
    }
    return config_map.get(section, {})