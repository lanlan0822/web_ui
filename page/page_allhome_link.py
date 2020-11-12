from base.base_option import BaseOption
import page
from base.driver import GetDriver
from page.page_login import PageLogin
import time
class PageAllhome(BaseOption):
    # 点击首页链接：我的
    def page_allhome_click_my(self):
        self.base_click(page.allhome_click_my)
        time.sleep(2)
    # 点击首页链接：找投顾

    def page_allhome_click_find_tougu(self):
        self.base_click(page.allhome_click_find_tougu)
        time.sleep(2)
    # 点击首页链接：观点
    def page_allhome_click_view(self):
        self.base_click(page.allhome_click_view)
        time.sleep(2)
    # 点击首页链接：问股
    def page_allhome_click_ask(self):
        self.base_click(page.allhome_click_ask)
        time.sleep(2)
    # 点击首页链接：直播
    def page_allhome_click_live(self):
        self.base_click(page.allhome_click_live)
        time.sleep(2)
    # 点击首页链接：首页
    def page_allhome_click_home(self):
        self.base_click(page.allhome_click_home)
        time.sleep(2)

    # 没有组合业务  基本页面操作为点击各页面查看页面是否正常显示
if __name__ == '__main__':
    dr = GetDriver().get_driver("C")
    login = PageLogin(dr)
    login.page_login('15117998520','123456')
    time.sleep(4)
    dr.find_element_by_xpath("//*[@data-type='itougu']").click()


