'''
观点详情页核心用例
Created on 2020-08-19
@author:xiaolan.gao
'''
from page.page_view import PageView
from base.driver import GetDriver
from page.page_login import PageLogin
from base.base_option import BaseOption
from tool.logger import GegLogger
import page
import time
import unittest
log=GegLogger().get_logger()
class TouguView(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info("--------------------开始执行用例：%s---------------------",cls.__name__)
        cls.dr=GetDriver().get_driver()
        PageLogin(cls.dr).page_login("15117998520","123456")
        time.sleep(2)
        cls.base=BaseOption(cls.dr)
        cls.base.base_get_new_page(page.view_url)
        cls.view=PageView(cls.dr)
    @classmethod
    def tearDownClass(cls):
        GetDriver().close_driver()
    # 点击观点详情页中投顾名称  进入投顾个人页
    def test_tougu_name(self):
        self.view.page_tougu_name()
        self.assertTrue(self.base.base_assert_url_isopen(page.view_assert_tougu_name_success))
        self.base.base_get_new_page(page.view_url)
    # # 观点详情点击关注投顾  然后取消关注
    # def test_focus_on(self):
    #     self.view.page_focus_on()
    #     time.sleep(1)
    #     self.assertTrue(self.base.base_assert_equal("取消关注",self.base.base_find_element(page.view_focus_on).text))
    #     self.view.page_focus_on()
    #     time.sleep(1)
    #     self.assertTrue(self.base.base_assert_equal("关注",self.base.base_find_element(page.view_focus_on).text))
    # # 查看相关股票
    # def test_about_stock(self):
    #     self.view.page_about_stock()
    #     self.assertTrue(self.base.base_assert_url_isopen(page.view_assert_about_stock_success))
    #     self.base.base_get_new_page(page.view_url)
    # # 点击相关来源
    # def test_about_source(self):
    #     self.view.page_about_stock()
    # # 打赏
    # def test_reward(self):
    #     self.view.page_reward()
    #     self.assertTrue(self.base.base_assert_elemtexist(page.view_assert_reward_success))
    #     self.base.base_get_new_page(page.view_url)
    # # 观点评论后点赞并删除评论
    # def test_comment(self):
    #     # 先发表评论
    #     self.view.page_comment()
    #     time.sleep(3)
    #     # 评论成功后查看下方第一条评论是否为刚发表的
    #     self.assertTrue(self.base.base_assert_equal(PageView.content,self.base.base_find_element(page.view_assert_comment_success).text))
    #     # 点赞前查看点赞数
    #     num=self.base.base_find_element(page.view_comment_thumb).text
    #     # 点赞操作
    #     self.view.page_comment_thumb()
    #     time.sleep(2)
    #     # 点赞完成后查看点赞数是否加1
    #     self.assertTrue(self.base.base_assert_equal(int(num)+1,int(self.base.base_find_element(page.view_comment_thumb).text)))
    #     # 删除操作
    #     self.view.page_comment_delate()
    #     # 删除后确认第一条评论不是刚发表的内容
    #     self.assertTrue(self.base.base_assert_notequal(PageView.content,self.base.base_find_element(page.view_assert_comment_success).text))

if __name__ == '__main__':
    unittest.main()


