'''点击各导航栏 浏览页面 通过pagesource判断页面关键模块是否加载正常
Created on 2020-08-10
@author:xiaolan.gao
'''
from tool.logger import GegLogger
import unittest
from base.driver import GetDriver
from base.base_option import BaseOption
from page.page_allhome_link import PageAllhome
from page.page_login import PageLogin
import page
import time
log=GegLogger().get_logger()
class AllhomeLick(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info("--------------------开始执行用例：%s---------------------",cls.__name__)
        cls.dr=GetDriver().get_driver("C")
        PageLogin(cls.dr).page_login("15117998520","123456")
        cls.base=BaseOption(cls.dr)
        cls.Allhome=PageAllhome(cls.dr)
        time.sleep(3)
    @classmethod
    def tearDownClass(cls):
        GetDriver().close_driver()

    def test_allhome_click_my(self):
        self.Allhome.page_allhome_click_my()

        for content in page.allhome_assert_my:
            self.assertTrue(self.base.base_assert_pagesource(content))
    # 点击首页链接：找投顾
    def test_allhome_click_find_tougu(self):
        self.Allhome.page_allhome_click_find_tougu()
        time.sleep(3)
        for content in page.allhome_assert_find_tougu:
            self.assertTrue(self.base.base_assert_pagesource(content))
    # 点击首页链接：观点
    def test_allhome_click_view(self):
        self.Allhome.page_allhome_click_view()
        time.sleep(3)
        for content in page.allhome_assert_view:
            self.assertTrue(self.base.base_assert_pagesource(content))
    # 点击首页链接：问股
    def test_allhome_click_ask(self):
        self.Allhome.page_allhome_click_ask()
        time.sleep(3)
        for content in page.allhome_assert_ask:
            self.assertTrue(self.base.base_assert_pagesource(content))
    # 点击首页链接：直播
    def test_allhome_click_live(self):
        self.Allhome.page_allhome_click_live()
        time.sleep(3)
        for content in page.allhome_assert_live:
            self.assertTrue(self.base.base_assert_pagesource(content))
    # 点击首页链接：首页
    def test_allhome_click_home(self):
        self.Allhome.page_allhome_click_home()
        time.sleep(3)
        for content in page.allhome_assert_home:
            self.assertTrue(self.base.base_assert_pagesource(content))
if __name__ == '__main__':
    unittest.main()
