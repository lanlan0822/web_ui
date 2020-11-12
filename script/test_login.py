'''登录核心用例  登录成功及登录失败
Created on 2020-07-20
@author:xiaolan.gao
'''
from base.driver import GetDriver
from base.base_option import *
from tool.excel_option import Openxl
from page.page_login import PageLogin
from tool.logger import GegLogger
import time
from selenium.webdriver.common.by import By
from base import add_base

import os
import unittest
import ddt
log=GegLogger().get_logger()
file_path=os.path.dirname(os.path.dirname(__file__))+"/test_data/login.xlsx"
data_success=Openxl(file_path,"user_success").read_xl_list(2,1,2,3)
data_fail=Openxl(file_path,"user_fail").read_xl_list(2,1,7,3)

@ddt.ddt
class Login(unittest.TestCase):
    dr = None
    login = None
    @classmethod
    def setUpClass(cls):
        log.info("--------------------开始执行用例：%s---------------------",cls.__name__)
        cls.dr = GetDriver().get_driver()
        cls.login = PageLogin(cls.dr)

    @classmethod
    def tearDownClass(cls):
        GetDriver().close_driver()
    def tearDown(self):
        self.dr.refresh()

    @ddt.data(*data_success)
    def test_login_success(self,data_success):
        self.login.page_login(data_success[0],data_success[1])
        if BaseOption(self.dr).base_assert_elemtexist(page.login_assert_success)==True:
                PageLogin(self.dr).page_click_logout_button()

    @ddt.data(*data_fail)
    # 用例执行完成截图
    # @add_base.get_image
    def test_login_fail(self,data_fail):
        self.login.page_login(data_fail[0],data_fail[1])
        time.sleep(1)
        temp=eval(data_fail[2])
        self.assertTrue(PageLogin(self.dr).base_assert_elemtexist(temp))


if __name__ == '__main__':
    unittest.main()

