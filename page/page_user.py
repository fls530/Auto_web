from common.base_page import BasePage
from locator.user_locator import UserLocator as loc


class UserPage(BasePage):
    def get_user_amount(self):
        """获取用户的余额"""
        amount = self.get_element_text(loc.user_amount_ele, '用户页面_获取余额')
        amount = amount.replace('元', '')
        return amount
