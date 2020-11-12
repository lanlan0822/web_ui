from base.base_option import BaseOption
from base.driver import GetDriver
import time
from page.page_login import PageLogin
import page
class PageHome(BaseOption):
    def page_click_search_input_shares(self):
        self.base_input(page.home_search_input,page.home_search_shares)
    def page_click_search_input_tougu(self):
        self.base_input(page.home_search_input,page.home_search_tougu)
    def page_click_search_button(self):
        self.base_click(page.home_click_search_button)
    def page_view_bigdata(self):
        return self.base_find_element(page.home_view_bigdata).text
    def page_click_recommend_view(self):
        self.base_click(page.home_recommend_view)
    def page_click_banner(self):
        self.base_click(page.home_click_first_banner)
        self.base_click(page.home_click_banner)
    def page_click_live_more(self):
        self.base_click(page.home_click_live_more)
    def page_click_live_join(self):
        self.base_click(page.home_click_live_join)
    def page_get_live_join_name(self):
        names=self.base_find_element(page.home_live_join_name).text
        name=names.split(" ")
        return name[0]
    def page_click_ask_more(self):
        self.base_click(page.home_click_ask_more)
    def page_click_ask_join(self):
        self.base_click(page.home_click_ask_join)
    def page_click_ask_close(self):
        self.base_click(page.home_cick_ask_close)
    def page_click_find_tougu_more(self):
        self.base_click(page.home_click_find_tougu_more)

    # 组合业务，首页输入股票编码点击搜索
    def page_search_sharse(self):
        self.page_click_search_input_shares()
        self.page_click_search_button()

    # 组合业务  首页输入投顾进行搜索
    def page_search_tougu(self):
        self.page_click_search_input_tougu()
        self.page_click_search_button()
    # 组合业务  页面滑动到底部  点击查看更多投顾
    def page_find_tougu_more(self):
        self.base_slip_to_position(1000)
        self.page_click_find_tougu_more()

    # 组合业务  页面滑到到底部  点击问股 在弹窗中点击关闭
    def page_ask_join(self):
        self.base_slip_to_position(900)
        self.page_click_ask_join()
        self.page_click_ask_close()







if __name__ == '__main__':
    dr = GetDriver().get_driver("C")
    login = PageLogin(dr)
    login.page_login('15117998520','123456')
    time.sleep(4)
    hh=PageHome(dr)
    hh.page_search_tougu()
    hh.page_search_sharse()
