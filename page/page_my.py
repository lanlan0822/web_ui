from base.base_option import BaseOption
import page
import time
from base.driver import GetDriver
from page.page_login import PageLogin
import os
class PageMy(BaseOption):
    # 点击首页用户头像  进入用户个人页面
    def page_click_home_userimg(self):
        self.base_click(page.my_home_userimg)
    # 个人页面点击头像  跳转到个人信息设置页面
    def page_click_personal_userimg(self):
        self.base_click(page.my_personal_userimg)
    # 切换到基本消息页面  执行用例顺序可能先执行头像照片页面  所以需要提前切换
    def page_click_personal_baseinfo(self):
        self.base_click(page.my_personal_change_baseinfo)
    # 获取当前选中的城市信息
    def page_get_current_province(self):
        return self.base_excute_js_return(page.my_get_current_provice)
    # 修改用户住址  选择省份
    def page_click_select_province(self,province):
        self.base_select_by_indexid(page.my_select_province,province)
    # 修改用户住址  选择城市
    def page_click_select_city(self,city):
        self.base_select_by_indexid(page.my_select_city,city)
    # 点击保存
    def page_click_personal_submit(self):
        self.base_click(page.my_personal_submit)
    # 保存后弹窗提示提交成功  点击确定  关闭弹窗
    def page_click_personal_submit_sure(self):
        self.base_click(page.my_personal_submit_sure)
    # 点击tap 切换到个人信息—头像照片页面
    def page_click_change_userimg(self):
        self.base_click(page.my_personal_change_userimg)
    # 点击上传照片
    def page_click_push_userimg(self):
        self.base_click(page.my_personal_push_userimg)
    # 执行系统命令  运行.exe文件  上传相应图片
    def page_os_syetem_push(self,path):
        os.system(path)
    # 上传成功后点击勾选icon 确认上传
    def page_click_push_userimg_sure(self):
        self.base_click(page.my_personal_push_userimg_sure)

    # 组合业务  从首页点击跳转到个人中心
    def page_home_to_personal(self):
        self.page_click_home_userimg()
        time.sleep(2)
        self.base_switch_to_handle(page.my_personal_title)
        time.sleep(3)
        self.page_click_personal_userimg()
    # 组合业务  修改用户住址  修改市区
    def page_personal_change_address(self,province,city):
        self.page_click_personal_baseinfo()
        self.page_click_select_province(province)
        self.page_click_select_city(city)
    # 组合业务  保存修改的个人信息
    def page_personal_change_submit(self):
        self.page_click_personal_submit()
        self.page_click_personal_submit_sure()

    # 组合业务  修改用户头像
    def page_change_userimg(self,path):
        self.page_click_change_userimg()
        time.sleep(3)
        self.page_click_push_userimg()
        time.sleep(5)
        os.system(path)
        time.sleep(3)
        self.page_click_push_userimg_sure()

    # 组合业务  修改用户头像  用input标签直接上传
    def page_change_userimg_new(self,path):
        self.page_click_change_userimg()
        self.base_refresh()
        time.sleep(3)
        self.base_file_push(page.my_personal_input,path)
        time.sleep(5)
        #执行js 让勾选框icon显示
        js="document.querySelector('.imgBtn').style='position: relative; display: block;'"
        self.base_excute_js(js)
        time.sleep(2)
        self.page_click_push_userimg_sure()
        time.sleep(3)

if __name__ == '__main__':
    dr = GetDriver().get_driver("C")
    login = PageLogin(dr)
    login.page_login('15117998520','123456')
    time.sleep(4)
    hh=PageMy(dr)
    hh.page_click_home_userimg()
    time.sleep(5)
    BaseOption(dr).base_switch_to_handle(page.my_personal_title)
    hh.page_click_personal_userimg()
    time.sleep(3)
    # el=dr.execute_script("$('#s_province Option:selected').text()")
    # print(el)
    # print(hh.page_get_current_province())
    # hh.page_click_select_province("天津市")
    # hh.page_click_select_city("和平区")
    # hh.page_click_personal_submit()
    # hh.page_click_personal_submit_sure()

    hh.page_click_change_userimg()
    time.sleep(3)
    # hh.page_click_push_userimg()
    # time.sleep(5)
    # os.system(r"..\test_data\push_image1.exe")
    hh.page_change_userimg_new(r"D:\project\web\itougu_po\test_data\userimg2.jpg")
    hh.page_change_userimg_new(r"D:\project\web\itougu_po\test_data\userimg1.jpeg")
    time.sleep(3)

