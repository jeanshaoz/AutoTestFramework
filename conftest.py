import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    # 自动下载并配置 Chrome 驱动
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    # 隐式等待：全局设置，查找元素时最多等待 5 秒
    driver.implicitly_wait(5)
    # 最大化窗口
    driver.maximize_window()
    yield driver  # 测试用例执行前运行到这里
    # 测试用例执行完毕后关闭浏览器
    driver.quit()