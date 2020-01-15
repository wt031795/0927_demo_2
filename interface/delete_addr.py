from common.sendmethod import SendMethod
from interface.login_interface import LoginInterface
from interface.select_addr import AddrListInter
from common.getkeyword import get_keyword

class Delete_Addr:

    def __init__(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/delete"

    def delete_addr(self,data):
        """删除收货地址"""
        return SendMethod.send_post(url=self.url,data=data)
    
    def get_status(self,data):
        """获取status"""
        response = self.delete_addr(data=data)
        return get_keyword(response,"status")


if __name__ == '__main__':
    login = LoginInterface()
    login_data = {"name":"a123","password":"123123"}
    data = login.get_session(login_data)
    delete = Delete_Addr()
    add_list = AddrListInter()
    addr_id = {"session": data}
    id = add_list.get_addr_id(addr_id)
    delete_data ={"address_id":id,"session":data}
    print(delete.delete_addr(delete_data))