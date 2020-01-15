from common.sendmethod import SendMethod

from interface.login_interface import LoginInterface


class DelCart:
    def __init__(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/cart/delete"

    def delcart(self, data):
        """移除购物车"""
        return SendMethod.sendmethod(url=self.url, data=data)


if __name__ == '__main__':
    login = LoginInterface()
    login_data = {"name": "user11", "password": "123456"}
    session = login.get_session(data=login_data)
    delcart = DelCart()
    delcart_data = {"session": session, "rec_id": 21140}  # 移除购物车请求参数
    print(delcart.delcart(delcart_data))
