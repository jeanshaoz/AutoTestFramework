import requests
class BaseAPI:
    def __init__(self, base_url):
        self.session = requests.Session()
        self.base_url = base_url
    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        # 这里可以添加日志记录和响应断言
        return response
