import time
import random
from base.base_option import BaseOption
import page
from page.page_login import PageLogin
from base.driver import GetDriver
class PageTouguLive(BaseOption):
    # 点击投顾个人页面点赞按钮 然后再次点击取消点赞
    def page_get_thumbs_num(self):
        return self.base_find_element(page.tougu_live_thumbs_up).text
    def page_click_thumbs_up(self):
        self.base_click(page.tougu_live_thumbs_up)
    def page_click_focus_on(self):
        self.base_click(page.tougu_live_focus_on)
    def page_click_ask_tougu(self):
        self.base_click(page.tougu_live_ask_tougu)
    def page_click_ask_input(self):
        num=random.randint(0,2)
        self.base_input(page.tougu_live_ask_input,page.tougu_live_input_content[num])
    def page_click_ask_submit(self):
        self.base_click(page.tougu_live_ask_submit)
    def page_click_ask_success_close(self):
        self.base_click(page.tougu_live_ask_success_close)
    def page_click_adviser(self):
        self.base_click(page.tougu_live_adviser)
    def page_click_gifts(self):
        self.base_click(page.tougu_live_gifts)
    def page_click_gifts_submit(self):
        self.base_click(page.tougu_live_gifts_submit)
    def page_click_switch_speak_iframe(self):
        frame=self.base_find_element(page.tougu_live_speak_iframe)
        self.base_switch_to_iframe(frame)
    def page_click_input_speak(self):
        num=random.randint(0,2)
        self.base_input(page.tougu_live_input_speak,page.tougu_live_input_content[num])
    def page_click_speak_submit(self):
        self.base_click(page.tougu_live_speak_submit)
    def page_click_only_tougu_select(self):
        self.base_click(page.tougu_live_only_tougu_select)
    def page_click_voice_tips_select(self):
        self.base_click(page.tougu_live_voice_tips_select)
    def page_click_fontsize_big_select(self):
        self.base_click(page.tougu_live_fontsize_big)
    def page_click_fontsize_small_select(self):
        self.base_click(page.tougu_live_fontsize_small)
    def page_click_fontsize_middle_select(self):
        self.base_click(page.tougu_live_fontsize_middle)



    # 组合业务 用户开始未关注投顾  点击关注后查看关注数是否自动加1  然后取消关注 判断关注数与开始一致
    def page_thumbs_up(self):
        self.page_click_thumbs_up()

    # 点击关注投顾 然后取消关注  初始状态为未关注状态
    def page_focus_on(self):
        self.page_click_focus_on()
    # 点击问股  向投顾单独提问  问股内容不包含股票
    def page_ask_tougu(self):
        self.page_click_ask_tougu()
        self.page_click_ask_input()
        self.page_click_ask_submit()
    def page_ask_uccess_close(self):
        self.page_click_ask_success_close()
    # 点击右侧投顾内参查看更多
    def page_adviser(self):
        self.page_click_adviser()

    # 点击打赏 默认金额提交  判断能正常跳转到支付页面
    def page_gifts(self):
        self.base_slip_to_position(800)
        self.page_click_gifts()
        self.page_click_gifts_submit()
        self.base_switch_to_handle("支付")

    # 直播间发言  输入发言内容后提交
    def page_speak(self):
        self.base_slip_to_position(900)
        self.page_click_switch_speak_iframe()
        self.page_click_input_speak()
        self.base_swtich_to_iframe_back()
        self.page_click_speak_submit()
    # 直播间发言输入框上方勾选框勾选功能正常
    def page_base_select(self):
        self.base_slip_to_position(900)
        self.page_click_only_tougu_select()
        self.page_click_only_tougu_select()
        self.page_click_voice_tips_select()
        self.page_click_voice_tips_select()
    # 直播间字体大小设置  默认选中小  依次点击大、中、小后  判断当前勾选的是否为小
    def page_fontsize(self):
        self.base_slip_to_position(800)
        self.page_click_fontsize_big_select()
        self.page_click_fontsize_middle_select()
        self.page_click_fontsize_small_select()



if __name__ == '__main__':
    dr = GetDriver().get_driver("C")
    login = PageLogin(dr)
    login.page_login('15117998520','123456')
    time.sleep(4)
    dr.get(page.tougu_live_url)
    hh=PageTouguLive(dr)
    hh.page_base_select()
    hh.page_fontsize()

