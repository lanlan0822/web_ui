from page.page_my import PageMy
from base.driver import GetDriver
from page.page_login import PageLogin
from tool.logger import GegLogger
from base.base_option import BaseOption
import os
import page
import time
import unittest
log=GegLogger().get_logger()
class TestMy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        log.info("--------------------开始执行用例：%s---------------------",cls.__name__)
        cls.dr=GetDriver().get_driver()
        PageLogin(cls.dr).page_login("15117998520","123456")
        time.sleep(2)
        cls.base=BaseOption(cls.dr)
        cls.my=PageMy(cls.dr)
        cls.my.page_home_to_personal()
    @classmethod
    def tearDownClass(cls):
        GetDriver().close_driver()

    def test_personal_change_address(self):
        cur=self.my.page_get_current_province()
        if cur=="北京市":
            self.my.page_personal_change_address("天津市","河西区")
        elif cur=="天津市":
            self.my.page_personal_change_address("北京市","西城区")
        else:
            self.my.page_personal_change_address("北京市","西城区")
        self.my.page_personal_change_submit()
        time.sleep(3)
        cur_now=self.my.page_get_current_province()
        self.assertTrue(self.base.base_assert_notequal(cur,cur_now))
    # 原测试头像上传用例   采用的是非input标签  用autoit3对windows窗口进行操作
    # def test_change_userimg(self):
    #     path1=os.path.dirname(os.path.dirname(__file__))+"/test_data/push_userimg1.exe"
    #     path2=os.path.dirname(os.path.dirname(__file__))+"/test_data/push_userimg1.exe"
    #     path_list=[path1,path2]
    #     for path in path_list:
    #         self.my.page_change_userimg(path)
    #     采用input标签测试头像  点击头像位置  然后加载js显示勾选框等元素  直接用send_keys上传
    def test_change_userimg(self):
        path1=os.path.dirname(os.path.dirname(__file__))+"/test_data/userimg1.jpeg"
        path2=os.path.dirname(os.path.dirname(__file__))+"/test_data/userimg2.jpg"
        path_list=[path1,path2]
        for path in path_list:
            self.my.page_change_userimg_new(path)

if __name__ == '__main__':
    unittest.main()