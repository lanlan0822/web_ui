import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import page
import os
from tool.logger import GegLogger
log=GegLogger().get_logger()
path=os.path.dirname(os.path.dirname(__file__))



'''闭包  检测程序执行异常时截图'''
def get_image_fail(func):
    def get_image2(self,*args,**kwargs):
        if func(self,*args,**kwargs)==True:
            return True
        else:
            BaseOption(self.dr).base_get_image(func.__name__)
            return False
    return get_image2


class BaseOption:
    def __init__(self,dr):
        self.dr=dr

    '''基本页面操作'''
    # 查找页面元素
    def base_find_element(self,loc,timeout=20,poll_frequency=0.5):
        log.info("开始查找元素{}".format(loc))
        el= WebDriverWait(self.dr,timeout=timeout,poll_frequency=poll_frequency).until(lambda x:x.find_element(*loc))
        return el

    # 点击操作
    def base_click(self,loc):
        log.info("点击click元素:{}".format(loc))
        self.base_find_element(loc).click()

    # 输入内容操作
    def base_input(self,loc,content):
        el=self.base_find_element(loc)
        log.info("清空输入框默认内容")
        el.clear()
        log.info("输入内容:{}".format(content))
        el.send_keys(content)
    # 获取截图
    def base_get_image(self,fun_name):
        file_path=path+"/image/"+fun_name+"_"+time.strftime("%Y-%m-%d_%H_%M_%S")+".png"
        log.info("开始屏幕截图并保存,保存地址:{}".format(file_path))
        self.dr.get_screenshot_as_file(file_path)
    # 添加cookie
    def base_add_cookie(self,name,value):
        log.info("开始添加cookie信息__{}:{}".format(name,value))
        self.dr.add_cookie({"name":name,"value":value})
    # 切换 iframe
    def base_switch_to_iframe(self,frame):
        log.info("开始切换到iframe:%s"%frame)
        self.dr.switch_to.frame(frame)
    # 从iframe中切换返回默认页面
    def base_swtich_to_iframe_back(self):
        log.info("开始从ifrome中返回原网页")
        self.dr.switch_to.default_content()
    # 切换浏览器窗口
    def base_switch_to_handle(self,title):
        for handle in self.dr.window_handles:
            self.dr.switch_to.window(handle)
            if self.dr.title==title:
                log.info("切换到titl为%s的window窗口"%title)
                break
    # 获取浏览器打开窗口数
    def base_get_windows_num(self):
        return len(self.dr.window_handles)
    # js执行 无返回
    def base_excute_js(self,js):
        log.info("执行js：%s"%js)
        self.dr.execute_script(js)
    # js执行 有返回值
    def base_excute_js_return(self,js):
        log.info("执行js：%s"%js)
        return self.dr.execute_script(js)

    #基本操作 页面滑动 1000表示滑动到底部  0表示滑动到顶部（页面底部根据实际比例填写   可能大于1000）
    def base_slip_to_position(self,position):
        js="var q=document.documentElement.scrollTop="+str(position)
        self.base_excute_js(js)
    # 上传  loc为点击上传的icon元素位置信息  file_path为要上传的文件路径
    def base_file_push(self,loc,file_path):
        log.info("上传文件")
        self.base_find_element(loc).send_keys(file_path)
    # 下载
    def base_file_pull(self,path):
        options=webdriver.ChromeOptions()
        # 必须是绝对路径
        # path=r"D:\project\web\ma_student_test\reports"
        # 第一个参数的意思是下载时隐藏下载提示弹窗
        pref={'profile.default_content_setting.popups':0,'download.default_directory':path}
        options.add_experimental_option("prefs",pref)
        log.info("下载文件")
        self.dr=webdriver.Chrome(chrome_options=options)
    # 获取当前页面url
    def base_get_current_url(self):
        return self.dr.current_url
    # 下拉选择框操作  通过index进行选择
    def base_select_by_index(self,loc,index):
        el=self.base_find_element(loc)
        Select(el).select_by_index(index)
    # 下拉选择框操作  通过value进行选择
    def base_select_by_indexid(self,loc,value):
        el=self.base_find_element(loc)
        Select(el).select_by_value(value)
    # 下拉选择框操作  通过bisible_text进行选择
    def base_select_by_indexid(self,loc,text):
        el=self.base_find_element(loc)
        Select(el).select_by_visible_text(text)

    # 页面刷新操作  用于一般初始化、删除后也刷新等用例场景
    def base_refresh(self):
        self.dr.refresh()


    '''基本断言方式'''
    # 页面源码是否包含关键字  返回True False
    @get_image_fail
    def base_assert_pagesource(self,content):
        log.info("开始断言，断言内容：%s"%content)
        if content in self.dr.page_source:
            return True
        else:
            return False
    # 页面是否能查找到某个元素  返回True False
    # 读取代码中配置文件 比如page __init__中的配置文件  默认格式为元组  直接解包即可  如果读取excel文件 参数默认是str类型  需要用eval函数
    @get_image_fail
    def base_assert_elemtexist(self,loc):
        log.info("开始断言页面是否存在该元素，元素：{}".format(loc))
        try:
            self.base_find_element(loc)
            return True
        except:
            return False

    # 基本断言 断言点击某个链接后  页面是否正常打开
    def base_assert_url_isopen(self,title):
        log.info("开始断言，查看title包含：%s的页面是否被打开???"%title)
        try:
            for handle in self.dr.window_handles:
                self.dr.switch_to.window(handle)
                titles=self.dr.title
                if title in titles:
                    return True
        except:
            return False
    #基本断言  断言俩个值是否相等
    @get_image_fail
    def base_assert_equal(self,guys1,guys2):
        log.info("开始断言，查看俩元素是否相等:%s==%s???"%(guys1,guys2))
        try:
            if guys1==guys2:
                return True
        except Exception as e:
            print("断言失败",e)
            return False
    # 基本断言  断言俩个值是否不相等
    @get_image_fail
    def base_assert_notequal(self,guys1,guys2):
        log.info("开始断言，查看俩元素是否不相等:%s!=%s???"%(guys1,guys2))
        try:
            if guys1!=guys2:
                return True
        except Exception as e:
            print(e)
            return False

    '''鼠标键盘操作'''
    # 鼠标双击
    def base_dubble_click(self,loc):
        action=ActionChains(self.dr)
        el=self.base_find_element(loc)
        action.double_click(el).perform()
    # 鼠标悬停
    def base_move_to_element(self,loc):
        action=ActionChains(self.dr)
        el=self.base_find_element(loc)
        action.move_to_element(el).perform()

    # 键盘操作封装  参数示例：key=Keys.CONTROL,'v'  base_keybox_option(loc,key)
    # def base_keybox_option(self,loc,opt):
    #     el=self.base_find_element(loc)
    #     el.send_keys(*opt)
    # 键盘操作封装  调用直接输入参数base_keybox_option(loc,CONTROL,'v')
    def base_keybox_option(self,loc,*args):
        el=self.base_find_element(loc)
        el.send_keys(*args)


    '''基本页面初始化操作  方便用例执行'''
    def base_get_new_page(self,url):
        self.dr.get(url)
        log.info('打开页面：%s'%url)




if __name__ == '__main__':
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    dr=webdriver.Chrome()
    dr.get("http://121.42.15.146:9090/mtx/")
    time.sleep(3)
    BaseOption(dr).base_get_image("login")
    dr.find_element()
    # print(BaseOption(dr).base_assert_elemtexist(page.login_link))
    # loc=By.PARTIAL_LINK_TEXT, '登录'
    # el=BaseOption(dr).base_find_element(loc)
    # el.click()




