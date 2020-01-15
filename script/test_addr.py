from interface.add_addr import Add_Addr
from interface.login_interface import LoginInterface
import unittest
from interface.select_addr import AddrListInter
from interface.update_addr import Updateaddr
from interface.delete_addr import Delete_Addr


class Test_Add_Addr(unittest.TestCase):

    def test_add_addr(self):
        """测试添加收货地址"""
        login = LoginInterface()
        login_data = {"name": "a123", "password": "123123"}
        session = login.get_session(login_data)
        add = Add_Addr()
        add_data = {"address": {"default_address": 0, "consignee": "土豆粉", "tel": "1888065189", "zipcode": "610000",
                                "country": "1", "city": "271", "id": 0, "email": "7871@qq.com", "address": "天府新谷",
                                "province": "24",
                                "district": "2716", "mobile": ""}, "session": session}
        # print(add.add_addr(add_data))
        """断言"""
        expect = {'succeed': 1}
        # status_1 = {"session": session}
        status = add.get_status(add_data)
        actual = status
        self.assertEqual(expect, actual)
        # 断言收货人姓名
        addr = AddrListInter()
        name1 = "土豆粉"
        name2 = addr.get_addr_name(add_data)
        self.assertEqual(name1, name2)

    def test_select_addr(self):
        """测试查看收货地址"""
        login = LoginInterface()
        login_data = {"name": "a123", "password": "123123"}
        session = login.get_session(login_data)
        select = AddrListInter()
        data = {"session": session}
        print(select.addr_list(data))
        """断言"""
        expect = {'succeed': 1}
        status = select.get_status(data)
        actual = status
        self.assertEqual(expect, actual)

    def test_update_addr(self):
        """测试修改收货地址"""
        login = LoginInterface()
        login_data = {"name": "a123", "password": "123123"}
        session = login.get_session(login_data)
        add_list = AddrListInter()
        addr_id = {"session": session}
        id = add_list.get_addr_id(addr_id)
        update = Updateaddr()
        update_data = {
            "address": {"default_address": 0, "consignee": "陈良", "tel": "151", "zipcode": "610000", "country": "1",
                        "city": "271", "id": 0, "email": "yang90@li.cn", "address": "广西壮族自治区淮安县大兴王街z座 892317",
                        "province": "24",
                        "district": "2714", "mobile": ""}, "address_id": id, "session": session}
        print(update.update_addr(update_data))
        """断言"""
        expect = {'succeed': 1}
        status = update.get_status(update_data)
        actual = status
        self.assertEqual(expect, actual)

    def test_delete_addr(self):
        """测试删除收货地址"""
        login = LoginInterface()
        login_data = {"name": "a123", "password": "123123"}
        data = login.get_session(login_data)
        delete = Delete_Addr()
        add_list = AddrListInter()
        addr_id = {"session": data}
        id = add_list.get_addr_id(addr_id)
        delete_data = {"address_id": id, "session": data}
        print(delete.delete_addr(delete_data))
        """断言"""
        expect = {'succeed': 1}
        status = delete.get_status(delete_data)
        actual = status
        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
