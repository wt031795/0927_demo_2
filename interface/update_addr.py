from common.sendmethod import SendMethod
from common.getkeyword import get_keyword
from interface.login_interface import LoginInterface


class Updateaddr:
    def __init__(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/update"

    def update_addr(self, data):
        """更新收货地址"""
        return SendMethod.send_post(url=self.url, data=data)

    def get_status(self, data):
        """获取status"""
        response = self.update_addr(data=data)
        return get_keyword(response, "status")


if __name__ == '__main__':
    login = LoginInterface()
    login_data = {"name": "a123", "password": "123123"}
    data = login.get_session(login_data)
    update = Updateaddr()
    up_data = {"address": {"default_address": 0, "consignee": "宽粉", "tel": "151", "zipcode": "610000", "country": "1",
                           "city": "271", "id": 0, "email": "yang90@li.cn", "address": "广西壮族自治区淮安县大兴王街z座 892317",
                           "province": "24", "district": "2714", "mobile": ""}, "address_id": "8723", "session": data}
    print(update.update_addr(up_data))
