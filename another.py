import requests, pickle
import time
import json
import datetime

class JD:
    headers = {
        'referer': '',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    }

    def __init__(self):
        self.index = 'https://www.jd.com/'
        self.user_url = 'https://passport.jd.com/user/petName/getUserInfoForMiniJd.action?&callback=jsonpUserinfo&_=' + \
            str(int(time.time() * 1000))  # 检测用户信息
        self.buy_url = 'https://cart.jd.com/gate.action?pid={}&pcount=1&ptype=1'    # 添加到购物车
        self.pay_url = 'https://cart.jd.com/gotoOrder.action'   # 提交订单
        self.pay_success = 'https://trade.jd.com/shopping/order/submitOrder.action'  # 付款页面
        self.goods_id = ''  # 商品id
        self.thor = ''	# 用户的cookie
        self.session = requests.session()

    def login(self):  # 直接加上cookie访问用户信息。
        JD.headers['referer'] = 'https://cart.jd.com/cart.action'
        #c = requests.cookies.RequestsCookieJar()
        #c.set('thor', self.thor)  # 添加用户的thor
        with open('cookie', 'rb') as f:
            c = requests.utils.cookiejar_from_dict(pickle.load(f))
        self.session.cookies.update(c)
        response = self.session.get(
            url=self.user_url, headers=JD.headers).text.strip('jsonpUserinfo()\n')
        user_info = json.loads(response)
        print('账号：', user_info.get('nickName'))
        if user_info.get('nickName'):
            self.shopping()

    def shopping(self):
        goods_url = input('商品链接：')
        self.goods_id = goods_url[
            goods_url.rindex('/') + 1:goods_url.rindex('.')]
        #self.goods_id = '100003434260'
        JD.headers['referer'] = goods_ur
        buy_url = self.buy_url.format(self.goods_id)


        #Panic_time = datetime.datetime(2019, 2, 26, 10, 0)
        Panic_time = datetime.datetime(2019, 2, 25, 22, 40)

        Remaining_time = (Panic_time - datetime.datetime.now()).second
        while Remaining_time > 2:
            print('剩余', Remaining_time, '秒')
            time.sleep(1)
            Remaining_time = (datetime.datetime.now() - Panic_time).second
        
        while((Panic_time - datetime.datetime.now()).second > 0):
            pass


        self.session.get(url=buy_url, headers=JD.headers)  # 添加到购物车

        order_id = None
        count = 0
        while(order_id == None):
            self.session.get(url=self.pay_url, headers=JD.headers)  # 提交订单
            response = self.session.post(
                url=self.pay_success, headers=JD.headers)     # 提交订单
            order_id = json.loads(response.text).get('orderId')
            count = count + 1
            if count > 3:
                break
            time.sleep(0.5)
        if order_id:
            print('抢购成功订单号:', order_id)
        else:
            print('抢购失败')
        print('count:', count)

if __name__ == "__main__":
    jd = JD()
    jd.login()	# http://loghb.com
