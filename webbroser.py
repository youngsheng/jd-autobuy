# -*- coding: UTF-8 -*- 
from splinter.browser import Browser 
import time 
def login(b): 
    b.click_link_by_text("账户登录") 
    time.sleep(1) 
    b.fill("loginname","XXXXXXXXXXX") #京东用户名 
    time.sleep(1) 
    b.fill("nloginpwd","XXXXXXXXXXX ") #登陆密码 
    time.sleep(1) 
    b.find_by_id("loginsubmit").click() 
    print(b) 
    return b 
#订单页 
def loop(b): #循环点击 
    try: 
        if b.title=="订单结算页 -京东商城": 
            b.find_by_text("保存收货人信息").click() 
            b.find_by_text("保存支付及配送方式").click() 
            b.find_by_id("order-submit").click() 
            return b 
        else: #多次抢购操作后，有可能会被转到京东首页，所以要再打开手机主页 
            b.visit("https://item.jd.com/100003434260.html") #荣耀V9的URL 
            #b.find_by_xpath('//*[@id="area1"]/div[2]/div[1]/a[1]').first.click()
            b.find_by_id("choose-btn-ko").click() 
            time.sleep(1) 
            loop(b) #递归操作 
    except Exception: #异常情况处理，以免中断程序 
        b.reload() #重新刷新当前页面，此页面为订单提交页 
        time.sleep(1) 
        loop(b) #重新调用自己 

b = Browser('chrome') 
b.visit("https://item.jd.com/100003434260.html") 
time.sleep(10) 
b.click_link_by_text("你好，请登录") 
time.sleep(5) 
b = login(b) #登录 
time.sleep(1) 
while True: 
    loop(b) 
    if b.is_element_present_by_id("tryBtn"): #订单提交后显示“再次抢购”的话 
        b.find_by_id("tryBtn").click() #点击再次抢购，进入读秒5，跳转订单页 
        time.sleep(6.5) 
    elif b.title=="订单结算页 -京东商城": #如果还在订单结算页 
        b.find_by_id("order-submit").click() 
    else: 
        print('恭喜你，抢购成功') 
        break 