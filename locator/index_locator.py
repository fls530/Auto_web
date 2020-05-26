from selenium.webdriver.common.by import By


class IndexLocator:
    """首页的元素定位"""
    # 用户信息
    user_info= (By.XPATH, "//a[contains(text(),'我的账户')]")
    # 退出登陆
    quit_btn = (By.XPATH, "//a[text()='退出']")
    # 项目抢投标的节点
    bid_btn_ele = (By.XPATH, "(//a[text()='抢投标'])[1]")