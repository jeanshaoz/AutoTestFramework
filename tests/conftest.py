import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.config_utils import config
from utils.log_utils import log

SCREENSHOT_DIR = "screenshots"


@pytest.fixture(scope="function")
def driver():
    log.info("======== 开始测试：初始化浏览器 ========")
    # 解决国内驱动下载网络问题
    os.environ['WDM_CHROME_DRIVER_MIRROR'] = "https://registry.npmmirror.com/-/binary/chromedriver"
    os.environ['WDM_SSL_VERIFY'] = "0"
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # 读取配置：是否无头模式
    if config.getboolean('ui', 'headless'):
        options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(service=service, options=options)
    # 读取配置：隐式等待时间
    driver.implicitly_wait(config.getint('ui', 'implicit_wait'))
    driver.maximize_window()
    log.info("浏览器启动成功")
    yield driver
    log.info("测试结束：关闭浏览器")
    driver.quit()


# 失败截图钩子
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        if "driver" in item.funcargs:
            driver = item.funcargs["driver"]
            if not os.path.exists(SCREENSHOT_DIR):
                os.makedirs(SCREENSHOT_DIR)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_name = item.name.replace("::", "_").replace("[", "_").replace("]", "_")
            file_path = os.path.join(SCREENSHOT_DIR, f"{timestamp}_{safe_name}.png")
            try:
                driver.save_screenshot(file_path)
                log.error(f"用例失败，已截图: {file_path}")
                import pytest_html
                if hasattr(report, "extra"):
                    report.extra.append(pytest_html.extras.image(file_path))
            except Exception as e:
                log.error(f"截图失败: {e}")