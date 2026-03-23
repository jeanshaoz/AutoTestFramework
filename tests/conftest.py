import pytest
from selenium import webdriver
@pytest.fixture(scope="function")
def driver():
    # 初始化浏览器
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    # 测试结束后关闭
    driver.quit()
