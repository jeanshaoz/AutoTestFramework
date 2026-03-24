import configparser
import os


class ConfigReader:
    def __init__(self, config_file='config/config.ini'):
        self.config = configparser.ConfigParser()
        # 获取项目根目录
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        full_path = os.path.join(base_dir, config_file)
        self.config.read(full_path, encoding='utf-8')

    def get(self, section, option):
        return self.config.get(section, option)

    def getint(self, section, option):
        return self.config.getint(section, option)

    def getboolean(self, section, option):
        return self.config.getboolean(section, option)


# 全局实例
config = ConfigReader()