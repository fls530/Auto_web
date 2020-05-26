import time
import pytest
from decimal import Decimal
from page.page_user import UserPage
from selenium.webdriver import Chrome
from common.handle_config import conf
from common.handle_logging import log
from data.case_data import InvestData
from page.page_index import IndexPage
from page.page_login import LoginPage
from page.page_invest import InvestPage


@pytest.fixture(scope='class')
def invest_fixture():
    # 前置条件
    driver = Chrome()
    driver.implicitly_wait(15)
    # 创建登录页面
    login_page = LoginPage(driver)
    # 登录
    login_page.login(user=conf.get('test_data', 'mobile'), pwd=conf.get('test_data', 'pwd'))
    # 创建首页对象
    index_page = IndexPage(driver)
    # 点击抢标
    index_page.click_bid()
    # 创建投资页面
    invest_page = InvestPage(driver)
    # 创建用户页面
    user_page = UserPage(driver)
    yield invest_page, user_page
    # 后置条件
    driver.quit()


class TestInvest:
    @pytest.mark.parametrize('case', InvestData.error_data)
    def test_invest_error(self, case, invest_fixture):
        """投资失败，按钮上出现提示的用例"""
        invest_page = invest_fixture[0]
        # 输入投资金额
        invest_page.input_invest_money(case['money'])
        # 获取按钮的提示信息
        res = invest_page.get_btn_error_info()
        try:
            assert case['expected'] == res
        except AssertionError as e:
            log.error("用例--{}---执行未通过".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}---执行通过".format(case['title']))

    @pytest.mark.parametrize('case', InvestData.error_popup_data)
    def test_invest_error_window(self, case, invest_fixture):
        """投资失败，弹框上出现提示信息的用例"""
        # 用例：投资金额为0
        invest_page = invest_fixture[0]
        # 输入投资金额
        invest_page.input_invest_money(case['money'])
        # 点击投资
        invest_page.click_invest()
        # 获取页面弹框的提示
        res = invest_page.get_window_error_info()
        # 手动关闭弹框
        invest_page.click_close_error_popup()
        try:
            assert case['expected'] == res
        except AssertionError as e:
            log.error("用例--{}---执行未通过".format(case['title']))
            log.exception(e)
            raise e
        else:
            log.info("用例--{}---执行通过".format(case['title']))

    @pytest.mark.parametrize('case', InvestData.success_data)
    def test_invest_success(self, case, invest_fixture):
        """投资成功的用例"""
        # 用例：投资金额为200
        invest_page, user_page = invest_fixture
        # 获取用户的余额（投资前）
        start_amount = invest_page.get_user_amount()
        # 输入投资金额
        invest_page.input_invest_money(case['money'])
        # 点击投资
        invest_page.click_invest()
        # 获取页面弹框的提示成功的信息
        res = invest_page.get_invest_info()
        # 点击查看投资成功的信息，跳转到用户页面
        invest_page.click_invest_success()
        # 获取用户页面的用户余额(投资后)
        end_amount = user_page.get_user_amount()
        try:
            assert case["expected"] == res
            assert Decimal(start_amount) - Decimal(end_amount) == Decimal(case['money'])
        except AssertionError as e:
            log.error("用例--{}---执行未通过".format('投资金额为0'))
            log.exception(e)
            time.sleep(10)
            raise e
        else:
            log.info("用例--{}---执行通过".format('投资金额为0'))
