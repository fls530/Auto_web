import pytest
from selenium import webdriver
from data.case_data import LoginCase
from page.page_index import IndexPage
from page.page_login import LoginPage
from common.handle_logging import log


@pytest.fixture(scope='class')
def login_fixture():
    """登录功能的前置后置"""
    # 前置条件
    log.info("开始执行登录的用例")
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    index_page = IndexPage(driver)
    yield login_page, index_page
    # 后置条件
    driver.quit()
    log.info("登录的用例执行完毕")


class TestLogin:
    """测试登录"""

    @pytest.mark.slow
    @pytest.mark.parametrize("case", LoginCase.success_case_data)
    def test_login_pass(self, case, login_fixture):
        """正常登录的用例"""
        login_page, index_page = login_fixture
        login_page.click_re_mobile()
        # 进行登录的操作
        login_page.login(case['mobile'], case['pwd'])
        # 获取登录之后的用户信息
        res = index_page.get_my_user_info()
        # 断言用例执行是否通过
        try:
            assert '登录成功' == res
        except AssertionError as e:
            log.error("用例执行失败")
            log.exception(e)
            raise e
        else:
            log.info("用例执行通过")
            # 退出登录，重新访问登录页面
            index_page.click_quit()
            # 重新进入登录页面
            login_page.page_refresh()

    @pytest.mark.parametrize('case', LoginCase.error_case_data)
    def test_login_error_case(self, case, login_fixture):
        """异常用例，窗口上有提示"""
        login_page, index_page = login_fixture
        # 刷新页面
        login_page.page_refresh()
        # 执行登录操作
        login_page.login(case['mobile'], case['pwd'])
        # 获取实际提示结果
        result = login_page.get_error_info()
        # 断言
        try:
            assert case['expected'] == result
        except AssertionError as e:
            log.error("用例执行失败")
            log.exception(e)
            raise e
        else:
            log.info("用例执行通过")

    @pytest.mark.parametrize('case', LoginCase.error_alert_data)
    def test_login_error_alert(self, case, login_fixture):
        """异常用例，错误信息弹窗提示"""
        login_page, index_page = login_fixture
        # 刷新页面
        login_page.page_refresh()
        # 执行登录操作
        login_page.login(case['mobile'], case['pwd'])
        # 获取实际提示结果
        result = login_page.get_alert_error_info()

        # 断言
        try:
            assert case['expected'] == result
        except AssertionError as e:
            log.error("用例执行失败")
            log.exception(e)
            raise e
        else:
            log.info("用例执行通过")