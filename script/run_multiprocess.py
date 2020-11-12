# 多个进程执行所有测试用例  执行结果：多条用例启动多个浏览器  具体并发执行的数量取决于电脑cpu内核
# 且生成的报告没写到同一个报告中
import unittest,os,time,multiprocessing
from multiprocessing import Pool
from tool import HTMLTestRunner
import time

curpath = os.path.dirname(os.path.realpath(__file__))
casepath = curpath
reportpath = os.path.dirname(os.path.dirname(__file__))+"/report"

def add_case(case_path=casepath, rule="test*.py"):
    discover = unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    return discover

def htmlrun(filename,testut):
    #改写、前模式是wb或w+结果都只是一个进程写进了报告，另外一个进程未写入，改成ab+后，成功
    print(("%s开始执行，进程号为%d" % (testut, os.getpid())))
    with open(filename,'ab+') as fp:
        runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况：')
        runner.run(testut)
    print("%s执行完成"%testut)
#多进程执行测试套件  遍历测试套件生成进程池  多进程执行
def mutiRunCase(suite,po_num=2):
    now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    #把当前时间加到报告中
    filename="../report/"+now+'pool_result.html'
    po=Pool(po_num)
    for i in suite:
        po.apply_async(htmlrun,(filename,i))
    po.close()
    po.join()
if __name__=='__main__':
    cases = add_case()
    mutiRunCase(cases,2)


