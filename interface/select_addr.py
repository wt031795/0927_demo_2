from common.sendmethod import SendMethod
from common.getkeyword import get_keyword
from interface.login_interface import LoginInterface


class AddrListInter:
    def __init__(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/list"

    def addr_list(self, data):
        """请求查看收货地址列表"""
        return SendMethod.send_post(url=self.url, data=data)

    def get_addr_id(self, data):
        """获取收货地址id"""
        response = self.addr_list(data=data)
        return get_keyword(response, "id")

    def get_addr_name(self, data):
        """获取收货人姓名"""
        response = self.addr_list(data=data)
        return get_keyword(response, "consignee")

    def get_status(self, data):
        """获取status"""
        response = self.addr_list(data=data)
        return get_keyword(response, "status")


if __name__ == '__main__':
    login = LoginInterface()
    login_data = {"name": "a123", "password": "123123"}
    data = login.get_session(login_data)
    addr = AddrListInter()
    addr_data = {"session": data}
    # addr.addr_list(addr_data)
    # print(addr.addr_list(addr_data))
    id = addr.get_addr_id(addr_data)
    print(id)
    name = addr.get_addr_name(addr_data)
    print(name)
