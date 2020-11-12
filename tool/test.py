from base.driver import GetDriver
from selenium.webdriver.common.keys import Keys
from page.page_login import PageLogin
from base.base_option import BaseOption
from selenium.webdriver.common.by import By
import page
import time
# dr=webdriver.Chrome()
# dr.get("http://itougu.jrj.com.cn/view/261999.jspa")
# time.sleep(5)
# # dr.find_element_by_css_selector('[class="switchable-triggers"]>li:nth-child(1)').click()
# el=dr.find_element_by_css_selector("[class='itg-comment-box']>div:nth-child(1)>div>div>p:nth-child(2)")
# print(el.text)


dr = GetDriver().get_driver("C")
base=BaseOption(dr)
# dr.get("https://www.itougu.com/live/index.html")
login = PageLogin(dr)
login.page_login('15117998520','123456')
time.sleep(3)
# loc=By.CLASS_NAME,"userop-msg-newmsg"
# base.base_move_to_element(loc)
# time.sleep(3)
key=Keys.CONTROL,'v'
base.base_keybox_option(page.home_search_input,Keys.CONTROL,'v')
# time.sleep(4)
# dr.get("http://i.jrj.com.cn/home/userSetting/profile")



# 多个进程执行所有测试用例  执行结果：多条用例启动多个浏览器  具体并发执行的数量取决于电脑cpu内核
# 且生成的报告没写到同一个报告中
import unittest,os,time,multiprocessing
from tool import HTMLTestRunner
import time

curpath = os.path.dirname(os.path.realpath(__file__))
casepath = curpath
reportpath = os.path.dirname(os.path.dirname(__file__))+"/report"

def add_case(case_path=casepath, rule="test*.py"):
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    return discover

def htmlrun(filename,testut):
    #改写、前模式是wb或w+结果都只是一个进程写进了报告，另外一个进程未写入，改成a+后，貌似也不行  哎
    with open(filename,'ab+') as fp:
        runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况：')
        runner.run(testut)

def mutiRunCase(suite):
    now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    #把当前时间加到报告中
    filename="../report/"+now+'result.html'
    proclist=[]
    j=0
    for i in suite:
        proc=multiprocessing.Process(target=htmlrun,args=(filename,i))
        proclist.append(proc)
        lens=len(proclist)
        for p in proclist: p.start()
        for p in proclist: p.join()
