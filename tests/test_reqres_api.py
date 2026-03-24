import pytest
from api.base_api import BaseAPI

# 【修改】更换为稳定的测试地址：httpbin.org
BASE_URL = "https://httpbin.org"


class TestReqresAPI:
    def setup_class(self):
        """初始化 API 客户端"""
        self.api = BaseAPI(BASE_URL)

    def test_get_request(self):
        """测试 GET 请求"""
        # 1. 发送请求
        response = self.api.request("GET", "/get", params={"name": "AutoTest", "status": "success"})
        # 2. 断言状态码
        assert response.status_code == 200
        # 3. 断言业务数据 (httpbin 会返回我们发送的参数)
        data = response.json()
        assert data['args']['name'] == "AutoTest"
        assert data['args']['status'] == "success"
        print(f"\nGET 测试通过，返回数据: {data['args']}")

    def test_post_request(self):
        """测试 POST 请求"""
        # 1. 准备数据
        payload = {
            "username": "admin",
            "password": "123456"
        }
        # 2. 发送请求
        response = self.api.request("POST", "/post", json=payload)
        # 3. 断言
        assert response.status_code == 200
        # 4. 断言返回数据 (httpbin 会返回我们发送的 JSON)
        data = response.json()
        assert data['json']['username'] == "admin"
        assert data['json']['password'] == "123456"
        print(f"\nPOST 测试通过，返回数据: {data['json']}")