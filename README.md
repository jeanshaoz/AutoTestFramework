# AutoTestFramework
### 🚀 项目介绍
这是一个基于 **Python + Pytest + Selenium + Allure** 的自动化测试框架。
旨在解决 UI 自动化稳定性差、接口测试数据难以维护、测试报告不直观等痛点。
### ✨ 核心特性
- **PO 模式封装**：采用 Page Object 设计模式，实现元素定位与业务逻辑分离。
- **多环境支持**：通过配置文件切换测试/预发/生产环境。
- **失败重试**：集成 `pytest-rerunfailures`，失败用例自动重跑。
- **日志监控**：封装日志模块，支持控制台彩色输出与文件记录。
- **Allure 报告**：生成美观的可视化测试报告，自动截图。
### 🛠 技术栈
- **测试框架**: Pytest
- **Web 自动化**: Selenium 4
- **接口自动化**: Requests
- **报告展示**: Allure
- **CI/CD**: Jenkins (待集成)
### 📂 目录结构
- `config/`: 存放环境配置、数据库连接信息。
- `pages/`: 封装页面元素定位和操作步骤。
- `tests/`: 存放测试用例。
- `utils/`: 封装日志、数据库、文件读取等工具类。
- `reports/`: 存放生成的测试报告。
### ⚡️ 快速开始
1. 安装依赖：`pip install -r requirements.txt`
2. 运行测试：`pytest tests/ --alluredir=reports`
3. 查看报告：`allure serve reports`
