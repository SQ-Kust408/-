import logging
from MultiAgent.src.utils.config_loader import get_config

config = get_config("system")


def get_logger(name: str) -> logging.Logger:
    """初始化日志器"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG if config["debug_mode"] else logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # 控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # 文件处理器
    file_handler = logging.FileHandler(config["log_path"])
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger


logger = get_logger(__name__)