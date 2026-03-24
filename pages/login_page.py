from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # 1. 定义元素定位器
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MSG = (By.CSS_SELECTOR, ".flash.success")
    # 2. 定义页面 URL
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, driver):
        super().__init__(driver)

    def load(self):
        """打开页面"""
        self.driver.get(self.URL)

    def login(self, username, password):
        """登录操作流程"""
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_success_message(self):
        """获取登录成功后的提示信息"""
        return self.find_element(self.SUCCESS_MSG).text