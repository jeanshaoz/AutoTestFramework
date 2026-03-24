from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    # 1. 定义元素定位器 (国外网站)
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    # 国外网站的成功和失败提示都在 .flash 这个 class 下
    ALERT_MSG = (By.CSS_SELECTOR, ".flash")
    # 2. 页面 URL
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

    # 【改造】通用获取提示信息方法
    def get_alert_message(self):
        """
        获取页面顶部的提示信息（包含成功和失败）
        使用 .text 获取文本，会自动去掉末尾的 "×" 符号
        """
        # 这里的 find_element 继承自 BasePage，自带显式等待
        element = self.find_element(self.ALERT_MSG)
        # 获取文本并去除首尾空格
        return element.text.strip()