from common.base_page import BasePage
from locator.login_locator import LoginLocator as loc
from selenium.webdriver.remote.webdriver import WebDriver
from common.handle_config import conf


class LoginPage(BasePage):
    """登陆页面"""
    # 登陆的url地址
    url = conf.get('env', 'base_url') + conf.get('url', 'login_url')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.url)
        self.driver.implicitly_wait(15)

    def login(self, user, pwd):
        """输入账户密码点击登录"""
        self.input_text(loc.mobile_loc, user, '登录_账户输入')
        # 输入密码
        self.input_text(loc.pwd_loc, pwd, '登录_密码输入')
        # 点击登录
        self.click_element(loc.login_loc, '登陆_点击元素')

    def get_error_info(self):
        """获取登陆失败的提示信息"""
        return self.get_element_text(loc.error_info, '登陆_失败提示信息')

    def get_alert_error_info(self):
        """获取页面弹窗的错误信息"""
        ele = self.wait_element_visibility(loc.alert_error_info, '登录_页面弹窗错误提示')
        return ele.text

    def page_refresh(self):
        """刷新页面"""
        self.driver.get(url=self.url)

    def click_re_mobile(self):
        """取消记住手机号"""
        self.click_element(loc.re_mobile, "登录_点击取消记住手机号")
