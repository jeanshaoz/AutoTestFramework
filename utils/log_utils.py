import logging
import os
from utils.config_utils import config


def setup_logger():
    # 1. 读取配置
    log_path = config.get('log', 'log_path')
    # 2. 创建日志目录
    log_dir = os.path.dirname(log_path)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    # 3. 设置格式
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s'
    )
    # 4. 初始化 Logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 5. 控制台输出
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    # 6. 文件输出
    fh = logging.FileHandler(log_path, encoding='utf-8')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


# 全局日志对象
log = setup_logger()