# #coding=utf-8
# import time
# from selenium import webdriver
# #浏览器数组
# lists=['firefox','firefox']
# #通过不同的浏览器执行脚本
# for browser in lists:
#     driver = webdriver.Remote(
#         command_executor='http://10.66.81.210:39179/wd/hub',
#         desired_capabilities={'platform': 'ANY', 'browserName':browser, 'version': '', 'javascriptEnabled': True })
#     driver.get("http://www.youdao.com")
#     time.sleep(5)
#     driver.close()


from selenium.webdriver import Remote
import time
from threading import Thread
def search_baidu(host,browser):
    driver = Remote(
        command_executor=host,
        desired_capabilities={
            'platform': 'ANY',
            'browserName': browser,
            'version': '',
            'javascriptEnabled': 'True'
        })
    driver.get('https://www.baidu.com/')
    driver.find_element_by_id('kw').send_keys(browser)
    driver.find_element_by_id('su').click()
    time.sleep(4)
    driver.close()
if __name__=='__main__':
    lists = {
        'http://127.0.0.1:4003/wd/hub': 'firefox',
        'http://127.0.0.1:4002/wd/hub': 'chrome'
    }
    threads=[]
    for host,browser in lists.items():
        print(host,browser)
        #driver=start_driver(host,browser)
        t=Thread(target=search_baidu,args=(host,browser))
        threads.append(t)

    for thr in threads:
        thr.start()
