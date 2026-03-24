import pytest
import allure
from pages.login_page import LoginPage
from utils.file_utils import read_json
from utils.log_utils import log

# 读取测试数据
login_data = read_json("data/login_data.json")


@allure.feature("登录模块")
class TestLoginUI:
    @allure.story("用户登录")
    @allure.severity(allure.severity_level.NORMAL)
    # 使用参数化，ids 用于在报告中显示测试用例名称
    @pytest.mark.parametrize("data", login_data, ids=[d['desc'] for d in login_data])
    def test_login_flow(self, driver, data):
        """
        参数化登录测试
        """
        log.info(f"开始执行测试场景: {data['desc']}")
        # 步骤1：打开页面
        with allure.step(f"打开登录页面"):
            login_page = LoginPage(driver)
            login_page.load()
        # 步骤2：输入用户名密码并点击登录
        with allure.step(f"输入用户名: {data['username']}, 密码: {data['password']}"):
            login_page.login(data['username'], data['password'])
        # 步骤3：验证结果
        with allure.step("验证登录结果"):
            current_url = driver.current_url
            log.info(f"当前 URL: {current_url}, 预期包含: {data['expected_url']}")
            assert data['expected_url'] in current_url, \
                f"断言失败: 预期 URL 包含 {data['expected_url']}, 实际为 {current_url}"