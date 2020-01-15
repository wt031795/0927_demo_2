import unittest
from interface.shopping_cart_interface import ShoppingCart
from interface.login_interface import LoginInterface


class TestShopping(unittest.TestCase):
    def setUp(self):
        """购物前先登录"""
        self.login = LoginInterface()
        login_data = {"name": "user11", "password": "123456"}
        self.session = self.login.get_session(data=login_data)
        self.shoppingcart = ShoppingCart()

    def test_create_cart(self):
        """测试添加购物车"""
        url = "?url=/cart/create"
        create_data = {"spec": [], "session": self.session, "goods_id": 84, "number": 1}
        self.shoppingcart.create_cart(url=url, data=create_data)
        """断言"""
        succeed = self.shoppingcart.get_goods_succeed(url=url, data=create_data)
        self.assertEqual(succeed, 1)

    def test_get_cart(self):
        """测试查看购物车"""
        url = "?url=/cart/list"
        get_cart_data = {"session": self.session}
        self.shoppingcart.get_cart(url=url, data=get_cart_data)

        """断言"""
        self.shoppingcart.get_goods_goods_list(url=url,data=get_cart_data)



    def test_upcart(self):
        """测试更新购物车"""
        url = "?url=/cart/update"
        upcart_data = {"new_number": 3, "session": self.session, "rec_id": 21819}
        self.shoppingcart.upcart(url=url, data=upcart_data)


    def test_del_cart(self):
        """测试删除购物车"""
        url = "?url=/cart/delete"
        delcart_data = {"session": self.session, "rec_id": 11385}
        self.shoppingcart.delcart(url=url, data=delcart_data)


if __name__ == '__main__':
    unittest.main()
