import requests
from utils.log_utils import log
import json


class BaseAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        # 【关键修复】模拟浏览器请求头，绕过服务器 403 拦截
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive'
        })

    def request(self, method, endpoint, **kwargs):
        """
        统一请求封装
        """
        url = f"{self.base_url}{endpoint}"
        # 日志记录
        log.info(f"REQUEST -> {method} {url}")
        if 'json' in kwargs:
            log.debug(f"BODY: {json.dumps(kwargs['json'], ensure_ascii=False)}")
        if 'params' in kwargs:
            log.debug(f"PARAMS: {kwargs['params']}")
        try:
            # 发送请求
            response = self.session.request(method, url, **kwargs)
            # 响应日志
            log.info(f"RESPONSE <- Status: {response.status_code}")
            try:
                log.debug(f"DATA: {json.dumps(response.json(), indent=2, ensure_ascii=False)}")
            except:
                log.debug(f"DATA: {response.text}")
            return response
        except Exception as e:
            log.error(f"请求异常: {e}")
            raise e