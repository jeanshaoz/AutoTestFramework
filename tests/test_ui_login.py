import pytest
from pages.login_page import LoginPage
from utils.data_utils import load_json_data

# 1. 加载测试数据
test_data = load_json_data("data/login_data.json")


class TestLoginUI:
    @pytest.mark.parametrize("data", test_data, ids=[d['case_name'] for d in test_data])
    def test_login_scenarios(self, driver, data):
        """
        数据驱动测试：覆盖国外网站登录场景
        """
        # 1. 初始化页面
        login_page = LoginPage(driver)
        login_page.load()
        # 2. 执行登录
        login_page.login(data['username'], data['password'])
        # 3. 获取提示信息
        actual_msg = login_page.get_alert_message()
        # 4. 断言 (使用 in 判断，因为实际文本可能包含多余字符)
        assert data['expected_text'] in actual_msg
        print(f"\n用例 [{data['case_name']}] 执行通过 -> 提示信息: {actual_msg}")