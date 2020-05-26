from locator.invest_locator import InvestLocator as loc
from common.base_page import BasePage


class InvestPage(BasePage):
    """投资页面"""

    def get_user_amount(self):
        """获取用户投资前的余额"""
        return self.get_element_attribute(loc.invest_amount_ele, 'data-amount', '投资_获取投资前余额')

    def input_invest_money(self, money):
        """输入投资金额"""
        # 清空输入框
        self.driver.find_element(*loc.invest_amount_ele).clear()
        self.input_text(loc.invest_amount_ele, money, '投资_输入投资金额')

    def click_invest(self):
        """点击投资"""
        # time.sleep(1)
        self.click_element(loc.invest_btn_ele, '投资_点击投资')

    def get_invest_info(self):
        """获取投资成功提示信息"""
        ele = self.wait_element_visibility(loc.invest_success, '投资页面_获取投资成功的信息')
        return ele.text

    def click_invest_success(self):
        """点击投资成功更多信息"""
        ele = self.wait_element_clickable(loc.click_success_info, '投资页面_点击投资成功')
        ele.click()

    def get_btn_error_info(self):
        """获取按钮上的提示信息"""
        # time.sleep(0.5)
        return self.get_element_text(loc.invest_btn_ele, '投资_获取按钮错误提示')

    def get_window_error_info(self):
        """获取弹框的错误信息"""
        ele = self.wait_element_visibility(loc.invest_error_info, '投资_获取弹框错误提示')
        return ele.text

    def page_refresh(self):
        """刷新页面"""
        self.driver.refresh()

    def click_close_error_popup(self):
        """点击关闭错误弹框"""
        self.click_element(loc.close_popup_btn, '投资_关闭错误弹框')
