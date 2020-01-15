"""封装购物模块的接口及接口的返回值"""

from common.sendmethod import SendMethod
from common.getkeyword import get_keyword
from interface.login_interface1 import LoginInterface


class Shopping:
    def __init__(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/"
        # 先登录
        self.session = LoginInterface().get_session()

    def addcart(self):
        """请求添加购物车接口"""
        url = self.url + "?url=/cart/create"
        add_cart_data = {"spec": [], "session": self.session, "goods_id": 73, "number": 1}
        return SendMethod.send_post(url=url, data=add_cart_data, )

    def show_cart_list(self):
        """请求查看购物车列表接口"""
        # self.addcart()
        url = self.url + "?url=/cart/list"
        cart_list_data = {"session": self.session}
        return SendMethod.send_post(url=url, data=cart_list_data)

    def check_order(self):
        """请求去结算接口"""
        url = self.url + "?url=/flow/checkOrder"
        check_data = {"session": self.session}
        return SendMethod.send_post(url=url, data=check_data)

    def get_shipping_id(self):
        """从结算返回值中获取shipping_id"""
        response = self.check_order()
        return get_keyword(response, "shipping_id")

    def get_pay_id(self):
        """从结算返回值中获取pay_id"""
        response = self.check_order()
        return get_keyword(response, "pay_id")

    def get_check_status(self):
        """从结算返回值中获取status"""
        response = self.check_order()
        return get_keyword(response, "succeed")

    def submitoder(self):
        """请求提交订单接口"""
        url = self.url + "?url=/flow/done"
        shipping_id = self.get_shipping_id()  # 获取shipping_id
        pay_id = self.get_pay_id()  # 获取pay_id
        submitoder_data = {"shipping_id": shipping_id, "session": self.session, "pay_id": pay_id}
        return SendMethod.send_post(url=url, data=submitoder_data)

    def get_order_id(self):
        """从提交订单接口返回值中获取order_id"""
        response = self.submitoder()
        order_id = get_keyword(response, "order_id")
        print(order_id)
        return order_id

    def get_order_status(self):
        """从提交订单接口返回值中获取order_id"""
        response = self.submitoder()
        order_status = get_keyword(response, "succeed")
        print(order_status)
        return order_status

    def buy(self):
        """请求支付接口"""
        url = self.url + "?url=/order/pay"
        order_id = self.get_order_id()  # 获取order_id
        buy_data = {"session": self.session, "order_id": order_id}
        return SendMethod.send_post(url=url, data=buy_data)


if __name__ == '__main__':
    # 实例化
    shopping = Shopping()
    # 添加购物车
    shopping.addcart()
    # 查看商品列表
    shopping.show_cart_list()
    # 去结算
    shopping.check_order()
    # 支付
    re = shopping.buy()
    print(re)
