from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.config_utils import config
from utils.log_utils import log


class LoginPage(BasePage):
    # SahiTest 登录页定位器
    USERNAME_INPUT = (By.NAME, "user")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//input[@type='submit']")

    def __init__(self, driver):
        super().__init__(driver)
        # 从配置文件读取 URL
        self.url = config.get('ui', 'base_url')

    def load(self):
        log.info(f"访问登录页面: {self.url}")
        self.driver.get(self.url)

    def login(self, username, password):
        log.info(f"执行登录操作: 用户名={username}")
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)