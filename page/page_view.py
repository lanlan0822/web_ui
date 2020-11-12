import time
import random
from base.base_option import BaseOption
import page
from page.page_login import PageLogin
from base.driver import GetDriver

class PageView(BaseOption):
    content=""
    # 点击观点详情页关注投顾icon
    def page_click_focus_on(self):
        self.base_click(page.view_focus_on)
    # 点击投顾头像  跳转到投顾个人页
    def page_click_tougu_name(self):
        self.base_click(page.view_tougu_name)
    # 点击相关股票
    def page_click_about_stock(self):
        self.base_click(page.view_about_stock)
    # 点击相关来源
    def page_click_about_source(self):
        self.base_click(page.view_about_source)
    # 点击右侧更多观点  跳转到投顾个人页面观点列表
    def page_click_more_view(self):
        self.base_click(page.view_more_view)
    #点击打赏按钮
    def page_click_reward(self):
        self.base_click(page.view_click_reward)
    # 弹窗中提交要打赏的金额
    def page_click_reward_submit(self):
        self.base_click(page.view_reward_submit)
    # 点击支付跳转到支付页面
    def page_click_reward_pay(self):
        self.base_click(page.view_reward_pay)
    # 观点评论  输入内容
    def page_click_comment(self):
        self.base_slip_to_position(3000)
        num=random.randint(0,2)
        PageView.content=page.view_comment_content[num]
        self.base_input(page.view_comment,PageView.content)
    # 观点评论 提交内容
    def page_click_comment_submit(self):
        self.base_click(page.view_comment_submit)
    # 观点评论 删除评论
    def page_click_comment_delate(self):
        self.base_click(page.view_comment_delate)
    def page_click_comment_delate_sure(self):
        self.base_click(page.view_comment_delate_sure)
    # 观点评论  对评论点赞
    def page_click_comment_thumbs(self):
        self.base_click(page.view_comment_thumb)




    # 组合业务  点击观点详情页中投顾名称  进入投顾个人页
    def page_tougu_name(self):
        self.page_click_tougu_name()


    # 组合业务  观点详情点击关注投顾  然后取消关注
    def page_focus_on(self):
        self.page_click_focus_on()

    # 组合业务 查看相关股票
    def page_about_stock(self):
        self.page_click_about_stock()

    # 组合业务  点击相关来源
    def page_about_source(self):
        self.page_click_about_source()

    # 组合业务 打赏
    def page_reward(self):
        self.page_click_reward()
        self.page_click_reward_submit()
        self.page_click_reward_pay()
        self.base_switch_to_handle("支付")
        time.sleep(2)

    # 组合业务 观点评论
    def page_comment(self):
        self.page_click_comment()
        self.page_click_comment_submit()

    # 组合业务 观点评论删除
    def page_comment_delate(self):
        self.page_click_comment_delate()
        self.page_click_comment_delate_sure()
        self.base_refresh()
        time.sleep(2)
    # 组合业务  对用户评论的内容点赞
    def page_comment_thumb(self):
        self.page_click_comment_thumbs()

if __name__ == '__main__':
    dr = GetDriver().get_driver("C")
    login = PageLogin(dr)
    login.page_login('15117998520','123456')
    time.sleep(4)
    dr.get(page.view_url)
    hh=PageView(dr)
    # hh.page_focus_on()
    # hh.page_tougu_name()
    # hh.page_about_stock()
    # hh.page_about_source()
    # hh.page_reward()
    hh.page_comment()
    hh.page_comment_delate()

