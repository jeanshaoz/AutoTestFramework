import json
import os


def read_json(file_path):
    """
    读取 JSON 文件并返回数据列表
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_dir, file_path)
    with open(full_path, encoding='utf-8') as f:
        return json.load(f)