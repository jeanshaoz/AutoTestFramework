import pytest
from pages.login_page import LoginPage


class TestLoginUI:
    def test_login_success(self, driver):
        # 1. 初始化页面对象
        login_page = LoginPage(driver)
        # 2. 访问页面
        login_page.load()
        # 3. 执行登录操作
        login_page.login("tomsmith", "SuperSecretPassword!")
        # 4. 断言结果
        success_msg = login_page.get_success_message()
        assert "You logged into a secure area!" in success_msg
        print(f"\n登录成功提示: {success_msg}")