'''
投顾个人直播间核心用例
Created on 2020-08-17
@author:xiaolan.gao
'''
from page.page_tougu_live import PageTouguLive
from base.driver import GetDriver
from page.page_login import PageLogin
from tool.logger import GegLogger
from base.base_option import BaseOption
import page
import time
import unittest
log=GegLogger().get_logger()
class TouguLive(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info("--------------------开始执行用例：%s---------------------",cls.__name__)
        cls.dr=GetDriver().get_driver()
        PageLogin(cls.dr).page_login("15117998520","123456")
        time.sleep(2)
        cls.base=BaseOption(cls.dr)
        cls.base.base_get_new_page(page.tougu_live_url)
        cls.tougulive=PageTouguLive(cls.dr)
    @classmethod
    def tearDownClass(cls):
        GetDriver().close_driver()

    # 点赞
    def test_thumbs_up(self):
        num_begin=self.tougulive.page_get_thumbs_num()
        self.tougulive.page_click_thumbs_up()
        time.sleep(2)
        num_middle=self.tougulive.page_get_thumbs_num()
        self.assertTrue(self.base.base_assert_equal(int(num_middle),int(num_begin)+1))
        self.tougulive.page_click_thumbs_up()
        time.sleep(2)
        num_end=self.tougulive.page_get_thumbs_num()
        self.assertTrue(self.base.base_assert_equal(int(num_begin),int(num_end)))
    # 点击关注投顾 然后取消关注  初始状态为未关注状态
    def test_focus_on(self):
        self.tougulive.page_focus_on()
        time.sleep(1)
        self.assertTrue(self.base.base_assert_equal("已关注",self.base.base_find_element(page.tougu_live_focus_on).text))
        self.tougulive.page_focus_on()
        time.sleep(1)
        self.assertTrue(self.base.base_assert_equal("关注",self.base.base_find_element(page.tougu_live_focus_on).text))
    # 点击问股  向投顾单独提问  问股内容不包含股票
    def test_ask_tougu(self):
        self.tougulive.page_ask_tougu()
        time.sleep(2)
        self.assertTrue(self.base.base_assert_equal(page.tougu_live_assert_ask_success_text,self.base.base_find_element(page.tougu_live_assert_ask_success).text))
        self.tougulive.page_click_ask_success_close()
    # 点击右侧投顾内参查看更多
    def test_adviser(self):
        self.tougulive.page_adviser()
        time.sleep(2)
        self.assertTrue(self.base.base_assert_elemtexist(page.tougu_live_assert_adviser_success))
        self.base.base_get_new_page(page.tougu_live_url)
    # 点击打赏 默认金额提交  判断能正常跳转到支付页面
    def test_gifts(self):
        self.tougulive.page_gifts()
        self.assertTrue(self.base.base_assert_equal(self.base.base_find_element(page.tougu_live_assert_gifts_success).text,"直播打赏"))
        self.base.base_get_new_page(page.tougu_live_url)
    # 直播间发言  输入发言内容后提交
    def test_speak(self):
        self.tougulive.page_speak()
    #   通过获取页面最后一条评论  判断是否为刚发表的内容  获取方式dr.find_element_by_xpath("//*[@contype='51'][last()]/div/div").text

    # 直播间发言输入框上方勾选框勾选功能正常
    def test_base_select(self):
        self.tougulive.page_base_select()
    # 直播间字体大小设置  默认选中小  依次点击大、中、小后  判断当前勾选的是否为小
    def test_fontsize(self):
        self.tougulive.page_fontsize()
        self.assertTrue(self.base.base_assert_equal(self.base.base_find_element(page.tougu_live_fontsize_small).text,"小"))
if __name__ == '__main__':
    unittest.main()