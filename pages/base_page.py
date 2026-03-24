from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.log_utils import log


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        """
        显式等待封装：等待元素可见并返回
        locator 格式：(By.ID, "username")
        """
        try:
            log.info(f"正在定位元素: {locator}")
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except Exception as e:
            log.error(f"元素定位失败: {locator}, 错误: {e}")
            # 失败时截图（扩展功能，后续可加）
            raise e

    def click(self, locator):
        """点击元素"""
        element = self.find_element(locator)
        log.info(f"点击元素: {locator}")
        element.click()

    def send_keys(self, locator, text):
        """输入文本"""
        element = self.find_element(locator)
        log.info(f"向元素 {locator} 输入文本: {text}")
        element.clear()
        element.send_keys(text)