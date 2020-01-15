from common.sendmethod import SendMethod
from interface.login_interface import LoginInterface
from common.getkeyword import get_keyword


class Add_Addr:
    def __init__(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/add"

    def add_addr(self, data):
        """添加收货地址"""
        return SendMethod.send_post(url=self.url, data=data)

    def get_status(self, data):
        """获取status"""
        response = self.add_addr(data=data)
        return get_keyword(response, "status")


if __name__ == '__main__':
    login = LoginInterface()
    login_data = {"name": "a123", "password": "123123"}
    data = login.get_session(login_data)
    add = Add_Addr()
    add_data = {
        "address": {"default_address": 0, "consignee": "张飞飞", "tel": "1888065189", "zipcode": "610000", "country": "1",
                    "city": "271", "id": 0, "email": "7871@qq.com", "address": "天府新谷", "province": "24",
                    "district": "2716", "mobile": ""}, "session": data}
    print(add.add_addr(add_data))
    status_1 = {"session": data}
    status = add.get_status(status_1)
    print(status)
