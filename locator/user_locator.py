from selenium.webdriver.common.by import By


class UserLocator:
    """用户页面的元素定位"""
    user_amount_ele = (By.XPATH, '//li[@class="color_sub"]')
