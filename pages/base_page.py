from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self, driver):
        self.driver = driver
    def find_element(self, locator, timeout=10):
        """显式等待封装"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    def js_input(self, locator, text):
        """使用JS强制输入，解决遮挡问题"""
        element = self.find_element(locator)
        self.driver.execute_script(f"arguments[0].value='{text}';", element)
