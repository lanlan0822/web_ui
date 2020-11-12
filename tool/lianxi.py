import time
from selenium import webdriver
dr=webdriver.Chrome()
dr.maximize_window()
dr.get("https://www.itougu.com/live/9")
# print(dr.find_element_by_xpath("//*[@contype='51'][last()-2]/div/div").text)

# 获取直播间指定行指定列的表情 i表示行  j标示列
def send_image(i,j):
    xpath="//*[@class='layer-content']/table/tbody/tr[%s]/td[%s]"%(i,j)
    return xpath
dr.find_element_by_xpath('//*[@title="表情"]').click()
time.sleep(1)
dr.find_element_by_xpath(send_image(1,2)).click()