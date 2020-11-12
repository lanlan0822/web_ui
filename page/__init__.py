# 项目配置信息
from selenium.webdriver.common.by import By
# 页面url
url="http://itougu.jrj.com.cn/"

# page_login登录流程页面配置信息
login_link = By.XPATH, '//*[text()="登录"]'
login_input_username = By.CSS_SELECTOR, '#dl_blur'
login_input_password = By.CSS_SELECTOR, '#pwd'
login_click_login_button = By.XPATH, '//*[text()="登 录"]'
login_click_logout_button = By.XPATH,'//*[text()="退出"]'
login_assert_success=By.XPATH,'//*[text()="金融街一姐"]'



# page_all_home_link首页各导航栏配置信息
allhome_click_my=By.XPATH,"//*[@data-type='itougu']"
allhome_click_find_tougu=By.XPATH,"//*[@data-type='account']"
allhome_click_view=By.XPATH,"//*[@data-type='viewpoint']"
allhome_click_ask=By.XPATH,"//*[@data-type='ques']"
allhome_click_live=By.XPATH,"//*[@data-type='live']"
allhome_click_home=By.XPATH,"//*[@data-type='index']"

allhome_assert_my=["投资内参","全部动态","消费记录","我的优惠劵"]
allhome_assert_find_tougu=["投资顾问排名","观点最热排名","回答最佳排名","擅长领域"]
allhome_assert_view=["获赏之星","大盘","题材","股票学堂"]
allhome_assert_ask=["值班投顾","免费提问","热问股票","精彩回答"]
allhome_assert_live=["直播动态","资深直播","人气榜","资深直播"]
allhome_assert_home=["看直播","精彩回答","直播最火","实时解盘"]



#page_homes首页各功能点配置文件
home_search_input=By.ID,"txtSearchBox"
home_search_shares="600002"
home_search_tougu="涨停王者"
home_click_search_button=By.ID,"btnSearchBox"
home_view_bigdata=By.CSS_SELECTOR,"[class='stockindex clearfix']>li:nth-child(1)>h4"
home_recommend_view=By.CSS_SELECTOR,'[class="news"]>li:nth-child(1)>a'
home_click_first_banner=By.CSS_SELECTOR,'[class="switchable-triggers"]>li:nth-child(1)'
home_click_banner=By.CSS_SELECTOR,'[class="switchable-content"]>ul>li:nth-child(1)'
home_click_live_more=By.CSS_SELECTOR,"[href='http://itougu.jrj.com.cn/live/index.html']"
home_click_live_join=By.XPATH,"(//*[text()='立即参与'])[1]"
home_click_ask_more=By.CSS_SELECTOR,"[href='http://itougu.jrj.com.cn/ques/']"
home_click_ask_join=By.XPATH,"(//*[text()='问股'])[3]"
home_cick_ask_close=By.CSS_SELECTOR,"[title='关闭']"
home_click_find_tougu_more=By.XPATH,"(//*[text()='更多>>'])[1]"
home_live_join_name=By.XPATH,"(//*[@class='userinfo'])[1]"



# page_tougu_live投顾个人直播间配置信息
# 产品经理的直播间地址  方便测试数据发表等
tougu_live_url="http://itougu.jrj.com.cn/live/141125010090996822"
tougu_live_thumbs_up =By.ID,'superLike'
tougu_live_focus_on =By.ID,'focusId'
tougu_live_ask_tougu =By.XPATH,"//*[text()='提问']"
tougu_live_ask_input=By.ID,"TextArea1"
tougu_live_ask_content="老师好  帮忙分析下今天大盘走势  谢谢"
tougu_live_ask_submit=By.XPATH,"(//*[text()='提交'])[2]"
tougu_live_ask_success_close=By.XPATH,"//*[text()='关闭']"
tougu_live_adviser=By.XPATH,"//*[text()='查看详情']"
tougu_live_order_adviser_adviser=By.ID,"orderNoLimit"
# tougu_live_gifts_id=By.XPATH,"//*[@gid='1']"
tougu_live_gifts_submit=By.ID,"btnCouponPay"
tougu_live_gifts=By.XPATH,"(//*[text()='立即赠送'])[1]"
tougu_live_speak_iframe=By.ID,"FoolEditor_iframeeditor1"
tougu_live_input_speak=By.CSS_SELECTOR,"[spellcheck='false']"
tougu_live_input_content=["老师好 帮忙分析下今日大盘走势 谢谢","老师好 目前大盘考虑持仓比例为多少比较合适？","老师好 帮忙分析下今日券商股走势情况"]
tougu_live_speak_submit=By.ID,"usrsubmit"
tougu_live_only_tougu_select=By.ID,"checkBtn2"
tougu_live_voice_tips_select=By.ID,"checkBtn"
tougu_live_fontsize_big=By.XPATH,"//*[text()='大']"
tougu_live_fontsize_small=By.XPATH,"//*[text()='小']"
tougu_live_fontsize_middle=By.XPATH,"//*[text()='中']"

tougu_live_assert_ask_success=By.XPATH,"(//*[@class='tit-2 clearfix']/p)[1]"
tougu_live_assert_ask_success_text="您的问题已经提交"
tougu_live_assert_adviser_success=By.ID,"orderNoLimit"
tougu_live_assert_gifts_success=By.XPATH,"(//*[@class='orderDesc'])[1]"



# page_view观点详情页配置信息
view_url="http://itougu.jrj.com.cn/view/261999.jspa"
view_tougu_name=By.XPATH,"(//*[text()='产品经理'])[1]"
view_about_stock=By.XPATH,"//*[text()='光大银行']"
view_about_source=By.XPATH,"//*[text()='来源：']/a"
view_click_reward=By.XPATH,"//*[@class='btn-award']"
view_reward_submit=By.XPATH,"//*[@id='reward']"
view_reward_pay=By.XPATH,"//*[@id='btnCouponPay']"
view_comment=By.CSS_SELECTOR,"[id='txtComment']"
view_comment_submit=By.CSS_SELECTOR,"[id='btnPost']"
view_comment_content=["点赞","棒棒哒","不错 老师的观点很好","支持老师"]
view_more_view=By.XPATH,"(//*[text()='更多'])[2]"
view_focus_on=By.CSS_SELECTOR,"[class='vp-profile-bottom']>a"
view_comment_delate=By.CSS_SELECTOR,"[class='itg-comment-box']>div:nth-child(1)>div>div>div>i:nth-child(3)"
view_comment_delate_sure=By.CSS_SELECTOR,"[value='确定']"
view_comment_thumb=By.CSS_SELECTOR,"[class='itg-comment-box']>div:nth-child(1)>div>div>div>i:nth-child(2)"

view_assert_about_stock_success="光大银行(601818)-爱投顾-金融界"
view_assert_reward_success=By.XPATH,"//*[text()='观点打赏']"
view_assert_more_view_success="产品经理的观点-爱投顾-金融界"
view_assert_tougu_name_success="产品经理的个人主页-爱投顾-金融界"
# 发表成功后   确认第一条评论是否为发表的内容
view_assert_comment_success=By.CSS_SELECTOR,"[class='itg-comment-box']>div:nth-child(1)>div>div>p:nth-child(2)"



# page_my配置文件  我的个人页
my_home_userimg=By.CSS_SELECTOR,"[class='site-top-v2-inner fr after-login']>a:nth-child(1)"
my_personal_userimg=By.CLASS_NAME,"user_big_img"
my_personal_title="我的金融界-个人中心"
my_select_province=By.ID,"s_province"
my_personal_change_baseinfo=By.XPATH,"//*[text()='基本消息']"
my_select_city=By.ID,"s_city"
my_select_content={"北京市":"西城区","天津市":"和平区"}
my_personal_submit=By.ID,"updateBtn"
my_personal_submit_sure=By.XPATH,"//*[text()='确定']"
my_personal_change_userimg=By.XPATH,"//*[text()='头像照片']"
my_personal_push_userimg=By.XPATH,"//*[text()='上传本地照片']"
my_personal_push_imgname=["userimg1.jpeg","userimg2.jpg"]
my_personal_push_userimg_sure=By.XPATH,"//*[@src='/home/static/img/duihao_white.png']"
my_personal_input=By.XPATH,"//*[@type='file']"

my_assert_click_home_userimg="个人中心-资产概览"
# 获取城市信息的js  执行后返回当前选中的城市信息  用于对比省市是否正常修改
my_get_current_provice="return $('#s_province Option:selected').text();"

# ls=self.driver.execute_script('return $("#hid_new_tagno").text();')
# js1 = "var options=$('#province option:selected');var text=options.text(); return text;"
# text = driver.execute_script(js1)
# print(f'选中的option的值是:{text}')



# 内参支付流程配置信息
adviser_order_adviser_agree=By.ID,"chkAgreement"
adviser_order_adviser_pay=By.ID,"btnCouponPay"