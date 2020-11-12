# 利用cmd直接执行python文件  可以不修改path  直接在根路径下新建要执行的文件  直接执行
from tool.HTMLTestRunner import HTMLTestRunner
import unittest
from script.test_login import Login
# from script.test_tougu_live import TouguLive
# from script.test_allhome_link import AllhomeLick
import time
import os,sys
# 从类中加载测试用例
# suit=unittest.defaultTestLoader.loadTestsFromTestCase(AllhomeLick)
# 从文件中加载测试用例
suit=unittest.defaultTestLoader.discover("script",pattern="test_*.py")
file_path=os.path.dirname(os.path.dirname(__file__))
file_name=file_path+"/itougu_po/report/"+time.strftime("%Y_%m_%d_%H_%M_%S")+".html"
with open(file_name,"wb") as f:
    HTMLTestRunner(stream=f, verbosity=1, title="爱投顾网站功能测试报告", description="测试报告描述").run(suit)

