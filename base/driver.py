from base.driver_option import DriverOption
import page
from tool.logger import GegLogger
log=GegLogger().get_logger()
# 单例模式思想  确保程序运行过程中只有一个driver实例对象
class GetDriver:
    dr=None
    # 用于普通调用  正常测试套件执行调用  默认启动谷歌浏览器
    @classmethod
    def get_driver(cls,browser="C",url=page.url):
        if cls.dr==None:
            cls.dr=DriverOption().get_driver(browser)
            log.info("打开浏览器地址：%s"%url)
            cls.dr.get(url)
            log.info("浏览器最大化")
            cls.dr.maximize_window()
            return cls.dr
    # 用于多进程启动浏览器时调用
    @classmethod
    def multi_get_driver(cls,url=page.url):
        if cls.dr==None:
            cls.dr=DriverOption().multi_getdriver()
            log.info("打开浏览器地址：%s"%url)
            cls.dr.get(url)
            log.info("浏览器最大化")
            cls.dr.maximize_window()
            return cls.dr

    @classmethod
    def close_driver(cls):
        if cls.dr:
            cls.dr.quit()
            log.info("关闭浏览器")
            cls.dr=None
    @classmethod
    def get_new_url(cls,url):
        cls.dr.get(url)
if __name__ == '__main__':
    url="https://www.itougu.com/"
    # GetDriver().get_driver("C",page.url)
    GetDriver().multi_get_driver(url)





