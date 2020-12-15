import unittest
from base.driver import GetDriver
class ChangeUnitest(unittest.TestCase):
    def __init__(self,methodName='runTest',host=None,browser=None):
        super(ChangeUnitest, self).__init__(methodName)
        global host1,browser1
        host1=host
        browser1=browser

    @classmethod
    def setUpClass(cls):
        pass
        cls.driver = GetDriver.gird_get_driver(host1,browser1)
        return cls.driver
        # cls.logTest = myLog().getLog("chrome")  # 每个设备实例化一个日志记录器

    def setup(self):
        pass
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        pass

    def tearDown(self):
        pass

    @staticmethod
    def parametrize(testcase_klass, host=None,browser=None):
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, host=host,browser=browser))
        return suite