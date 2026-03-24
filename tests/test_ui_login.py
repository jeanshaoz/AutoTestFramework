import pytest
from pages.login_page import LoginPage
from utils.log_utils import log


class TestLoginUI:
    def test_login_success(self, driver):
        """测试登录成功场景"""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("test", "secret")
        # 验证：登录成功后会跳转到 books 页面
        log.info("验证是否跳转到购物页")
        assert "books.htm" in driver.current_url, "登录失败，未跳转到预期页面"
        log.info("测试通过：登录成功并正确跳转")

    def test_login_fail(self, driver):
        """测试登录失败场景"""
        login_page = LoginPage(driver)
        login_page.load()
        login_page.login("test", "wrong_password")
        # 验证：登录失败应停留在登录页，或 URL 不变
        log.info("验证是否停留在登录页")
        assert "login.htm" in driver.current_url or "books.htm" not in driver.current_url
        # 也可以验证页面上是否有错误提示文本（如果有显示的话）
        # 这里简单以 URL 未跳转作为验证标准