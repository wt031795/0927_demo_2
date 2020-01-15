from common.sendmethod import SendMethod
from interface.login_interface import LoginInterface


class GetCart:
    def __init__(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/cart/list"

    def get_cart(self, data):
        """查看购物车"""
        return SendMethod.sendmethod(url=self.url, data=data)


if __name__ == '__main__':
    login = LoginInterface()
    login_data = {"name": "user11", "password": "123456"}
    session = login.get_session(login_data)
    getcart = GetCart()
    getcat_data = {"session": session}   #查看购物车请求参数
    print(getcart.get_cart(getcat_data))
