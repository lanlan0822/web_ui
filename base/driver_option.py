# coding=utf-8
from selenium import webdriver
from tool.logger import GegLogger
from multiprocessing import Pool
from selenium.webdriver import Remote
from multiprocessing import Manager
log=GegLogger().get_logger()
class DriverOption:
    def get_driver(self,browser):
        log.info("启动driver,打开浏览器")
        if browser=="chrom" or browser=="C":
            return webdriver.Chrome()
        elif browser=="firefox" or browser=="F":
            return webdriver.Firefox()
        elif browser=="ie" or browser=="I":
            return webdriver.Ie()
        elif browser=="edge" or browser=="E":
            return webdriver.Edge()
        elif browser=="safari" or browser=="S":
            return webdriver.Safari()
        else:
            raise NameError('Not found %s browser:you must input "firefox","edge","chrome","ie","safari"'%browser)

    # 多进程执行 涉及到返回值问题无法序列化  目前这种方式运行多浏览器失败  还需要继续研究
    def multi_getdriver(self):
        # manage=Manager().Queue()
        # return_list=manage.dict()
        list=["C","F"]
        po=Pool(2)
        list1=[]
        for i in list:
            re=po.apply_async(self.get_driver,(i,))
            list1.append(re)
        po.close()
        po.join()
        for j in list1:
            print(j.dump(j))

    # grid 多进程生成浏览器driver
    def grid_getdriver(self,host,browser):
        driver = Remote(
            command_executor=host,
            desired_capabilities={
                'platform': 'ANY',
                'browserName': browser,
                'version': '',
                'javascriptEnabled': 'True'
        })
        return driver

if __name__ == '__main__':
   DriverOption().multi_getdriver()

