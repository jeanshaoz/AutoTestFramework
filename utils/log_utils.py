import logging
import sys


class Logger:
    # 定义日志颜色
    COLORS = {
        'DEBUG': '\033[94m',  # 蓝色
        'INFO': '\033[92m',  # 绿色
        'WARNING': '\033[93m',  # 黄色
        'ERROR': '\033[91m',  # 红色
        'CRITICAL': '\033[91m',  # 红色
    }
    RESET = '\033[0m'

    def __init__(self, name="AutoTest"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        # 避免重复添加 handler
        if not self.logger.handlers:
            # 控制台输出
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.setLevel(logging.DEBUG)
            # 设置格式
            formatter = logging.Formatter(
                '%(asctime)s | %(levelname)-8s | %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def debug(self, msg):
        self.logger.debug(f"{self.COLORS['DEBUG']}{msg}{self.RESET}")

    def info(self, msg):
        self.logger.info(f"{self.COLORS['INFO']}{msg}{self.RESET}")

    def error(self, msg):
        self.logger.error(f"{self.COLORS['ERROR']}{msg}{self.RESET}")


# 全局实例，方便直接调用
log = Logger()