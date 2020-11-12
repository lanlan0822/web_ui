from base.base_option import BaseOption
import page
from base.driver import GetDriver
from base.add_base import get_image_all

from selenium.webdriver.common.by import By

class PageLogin(BaseOption):
    # 点击登录链接前缀page 页面层 见名知意  loc元素定位的东西
    def page_click_login_link(self):
        self.base_click(page.login_link)

    # 输入用户名
    def page_input_username(self, username):
        self.base_input(page.login_input_username, username)

    # 输入密码
    def page_input_password(self,password):
        self.base_input(page.login_input_password, password)

    # 点击登录  修改超时时间和频率
    def page_click_login_button(self):
        self.base_click(page.login_click_login_button )

    # 点击退出
    def page_click_logout_button(self):
        self.base_click(page.login_click_logout_button)

    # 组合业务逻辑->跟你做功能测试一样的一个组合的动作，动作顺序一样
    # 添加装饰器  在每个登录用例结束后截图
    # @get_image_all
    def page_login(self, username, password):
        # 点击登录链接
        self.page_click_login_link()
        # 输入用户名
        if username!=None:
            self.page_input_username(username)
        # 输入密码
        if password!=None:
            self.page_input_password(password)
        # 点击登录
        self.page_click_login_button()

if __name__ == '__main__':
    dr = GetDriver().get_driver("C")
    login = PageLogin(dr)
    login.page_login('15117998520','123456')
    # BaseOption(dr).base_assert_elemtexist(page.login_assert_success)==True
