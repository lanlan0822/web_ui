
from tool.HTMLTestRunner import HTMLTestRunner
import unittest
from script.test_login import Login
# from script.test_tougu_live import TouguLive
# from script.test_allhome_link import AllhomeLick
import time
import os
from tool.change_unittest import ChangeUnitest
from script.test_home_grid import Home
from script.test_login_grid import Login
from multiprocessing.pool import Pool
# 从类中加载测试用例
# suit=unittest.defaultTestLoader.loadTestsFromTestCase(AllhomeLick)

# 从文件中加载测试用例
lists = {
    'http://127.0.0.1:4003/wd/hub': 'firefox',
    'http://127.0.0.1:4002/wd/hub': 'chrome'
}
def runner_pool():
    devices_Pool ={
    'http://127.0.0.1:4003/wd/hub': 'chrome',
    'http://127.0.0.1:4002/wd/hub': 'firefox'
}
    pool = Pool(2)
    for host,browser in devices_Pool.items():
        pool.apply_async(run,(host,browser))
    pool.close()
    pool.join()

def run(host,browser):
    suite = unittest.TestSuite()
    suite.addTest(ChangeUnitest.parametrize(Home, host=host,browser=browser))
    suite.addTest(ChangeUnitest.parametrize(Login, host=host,browser=browser))
    file_path=os.path.dirname(os.path.dirname(__file__))
    file_name=file_path+"/report/"+time.strftime("%Y_%m_%d_%H_%M_%S")+browser+".html"
    with open(file_name,"wb") as f:
        HTMLTestRunner(stream=f, verbosity=1, title="爱投顾网站功能测试报告", description="测试浏览器"+browser).run(suite)

if __name__ == '__main__':
    runner_pool()