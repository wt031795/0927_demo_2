import unittest
import ddt
from interface.login_interface import LoginInterface
from interface.show_goods import ShowGoodsList


@ddt.ddt
class Test_show_goods(unittest.TestCase):
    def setUp(self):
        self.show = ShowGoodsList()  # 实例化商品详情
        self.login = LoginInterface()  # 实例化登录

    def test_show(self):
        login_data = {"name": "yehong", "password": "yehong123"}
        session = LoginInterface().get_session(data=login_data)
        show = ShowGoodsList()
        result = show.goodsList("id")
        self.assertTrue(result, show.get_goodsList("id"))


if __name__ == '__main__':
    unittest.main()
