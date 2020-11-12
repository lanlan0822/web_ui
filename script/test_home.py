'''首页各功能模块测试用例
Created on 2020-08-10
@author:xiaolan.gao
'''
import unittest
from base.driver import GetDriver
from base.base_option import BaseOption
from page.page_login import PageLogin
from page.page_home import PageHome
from tool.logger import GegLogger
import page
import time
log=GegLogger().get_logger()
class Home(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info("--------------------开始执行用例：%s---------------------",cls.__name__)
        cls.dr=GetDriver().get_driver()
        PageLogin(cls.dr).page_login("15117998520","123456")
        cls.base=BaseOption(cls.dr)
        cls.Home=PageHome(cls.dr)
        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        GetDriver().close_driver()
    # 每次用例结束后都重新回到首页
    def tearDown(self):
        self.dr.get("http://itougu.jrj.com.cn/")
    # 首页输入股票编码点击搜索
    def test_search_sharse(self):
        self.Home.page_search_sharse()
    #
    # # 首页输入投顾进行搜索
    # def test_search_tougu(self):
    #     self.Home.page_search_tougu()
    # # 判断首页左上角是否加载显示上证指数行情数据
    # def test_view_bigdata(self):
    #     el_text=self.Home.page_view_bigdata()
    #     self.assertIn(el_text,"上证指数创业板")
    # # 点击左上角推荐观点  跳转到详情页
    # def test_click_recommend_view(self):
    #     self.Home.page_click_recommend_view()
    # # 点击首页banner跳转
    # def test_click_banner(self):
    #     self.Home.page_click_banner()
    # # 点击查看更多直播
    # def test_click_live_more(self):
    #     self.Home.page_click_live_more()
    # # 点击立即参与  跳转到投顾直播间
    # def test_click_live_join(self):
    #     self.Home.page_click_live_join()
    #     self.base.base_assert_url_isopen(self.Home.page_get_live_join_name())
    # def test_click_ask_more(self):
    #     self.Home.page_click_ask_more()
    # def test_ask_join(self):
    #     self.Home.page_ask_join()
    # def test_find_tougu_more(self):
    #     self.Home.page_find_tougu_more()
    # # 最后执行 判断个链接打开页面数目是否正确
    # def test_z_window_number(self):
    #     num=self.base.base_get_windows_num()
    #     self.assertEqual(num,7)
if __name__ == '__main__':
    unittest.main()
