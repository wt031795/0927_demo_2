from interface.shopping_interface import Shopping
# from common.database import Database
import unittest

# sql = "select * FROM ecs_order_goods where goods_id='73'"
# db = Database()  # 实例化Database


class Test_Shopping(unittest.TestCase):

    def setUp(self):
        # 实例化
        self.shopping = Shopping()

    def test_01_shopping(self):
        """验证有商品点击去结算的正确性"""
        # 添加购物车
        self.shopping.addcart()
        # 查看商品列表
        self.shopping.show_cart_list()
        # 去结算,并获取状态返回值
        status = self.shopping.get_check_status()
        # """断言"""
        # self.assertTrue(status,msg="没有商品")

    def test_02_shopping(self):
        """验证有商品提交订单的正确性"""
        # 添加购物车
        self.shopping.addcart()
        # 查看商品列表
        self.shopping.show_cart_list()
        # 去结算
        self.shopping.check_order()
        # 提交订单
        order_status = self.shopping.get_order_status()
        # """断言"""
        # self.assertTrue(order_status,msg="提交订单失败")

    def test_03_shopping(self):
        """验证购物正向流程的正确性"""
        # 添加购物车
        self.shopping.addcart()
        # 查看商品列表
        self.shopping.show_cart_list()
        # 去结算
        self.shopping.check_order()
        order_id1 = self.shopping.get_order_id()  # 请求提交订单接口返回的order_id
        # 支付
        result = self.shopping.buy()
        print(result)
        """断言"""
        # goods_order= db.readone(sql)
        # order_id2 = goods_order["order_id"] #数据库查询订单表中最新订单的order_id
        # print(order_id2)
        # self.assertTrue(order_id1==order_id2)


if __name__ == '__main__':
    unittest.main()
