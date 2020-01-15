from common.sendmethod import SendMethod

from interface.login_interface import LoginInterface


class Upcart:
    def __init__(self):
        """初始化请求地址"""
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/cart/update"

    def upcart(self, data):
        """更新购物车接口"""
        return SendMethod.sendmethod(url=self.url, data=data)


if __name__ == '__main__':
    login = LoginInterface()
    login_data = {"name": "user11", "password": "123456"}
    session = login.get_session(login_data)
    upcart_data = {"new_number": 3, "session": session, "rec_id": 21140}  #更新购物车请求参数
    upcart = Upcart()
    print(upcart.upcart(upcart_data))
