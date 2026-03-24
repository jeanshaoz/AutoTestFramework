import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 定义截图保存目录
SCREENSHOT_DIR = "screenshots"


@pytest.fixture(scope="function")
def driver():
    # 自动下载并配置 Chrome 驱动
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest 钩子函数：在测试执行结束后获取报告状态
    """
    outcome = yield
    report = outcome.get_result()
    # 仅在测试失败且处于“调用”阶段时进行截图
    if report.when == "call" and report.failed:
        # 获取 driver 对象
        # 注意：这里的 driver 是 fixture 返回的，item.funcargs 可以获取 fixture 返回值
        if "driver" in item.funcargs:
            driver = item.funcargs["driver"]
            # 创建截图目录
            if not os.path.exists(SCREENSHOT_DIR):
                os.makedirs(SCREENSHOT_DIR)
            # 生成截图文件名：时间_用例名.png
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{timestamp}_{item.name}.png"
            file_path = os.path.join(SCREENSHOT_DIR, file_name)
            # 截图并保存
            driver.save_screenshot(file_path)
            print(f"\n测试失败，已自动截图: {file_path}")
            # 【关键】将截图路径写入 extra_html，嵌入到 HTML 报告中
            if hasattr(report, "extra"):
                report.extra.append(pytest_html.extras.image(file_path))
            else:
                report.extra = [pytest_html.extras.image(file_path)]


# 确保引用 pytest_html 模块
import pytest_html