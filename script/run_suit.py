import os,sys
# 用cmd执行py文件时需要手动添加变量  不然执行时找不到路径下的包  提示导包失败
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

from tool.HTMLTestRunner import HTMLTestRunner
import unittest
from script.test_login import Login
# from script.test_tougu_live import TouguLive
# from script.test_allhome_link import AllhomeLick
import time

# 从类中加载测试用例
# suit=unittest.defaultTestLoader.loadTestsFromTestCase(AllhomeLick)

# 从文件中加载测试用例
suit=unittest.defaultTestLoader.discover("script",pattern="test_*.py")
file_path=os.path.dirname(os.path.dirname(__file__))
file_name=file_path+"/report/"+time.strftime("%Y_%m_%d_%H_%M_%S")+".html"
with open(file_name,"wb") as f:
    HTMLTestRunner(stream=f, verbosity=1, title="爱投顾网站功能测试报告", description="测试报告描述").run(suit)

