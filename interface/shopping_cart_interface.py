from common.sendmethod import SendMethod
from common.getkeyword import get_keywords
from common.getkeyword import get_keyword

from interface.login_interface import LoginInterface


class ShoppingCart:
    def __init__(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/"

    def create_cart(self, url, data):
        """添加购物车接口"""
        url = self.url + url
        return SendMethod.sendmethod(url=url, data=data)

    def get_cart(self, url, data):
        """查看购物车"""
        url = self.url + url
        return SendMethod.sendmethod(url=url, data=data)

    def upcart(self, url, data):
        """更新购物车接口"""
        url = self.url + url
        return SendMethod.sendmethod(url=url, data=data)

    def delcart(self, url, data):
        """移除购物车"""
        url = self.url + url
        return SendMethod.sendmethod(url=url, data=data)

    def get_goods_succeed(self,url,data):
        """获取商品的goods_succeed"""
        response = self.get_cart(url=url,data=data)
        return get_keyword(response, "succeed")

    def get_goods_goods_list(self,url,data):
        """获取商品的goods_list"""
        response = self.get_cart(url=url,data=data)
        return get_keywords(response, "goods_list")


if __name__ == '__main__':
    login = LoginInterface()
    login_data = {"name": "user11", "password": "123456"}
    session = login.get_session(data=login_data)
    # print(session)
    cart =ShoppingCart()


    # 添加购物车
    url="?url=/cart/create"
    create_da={"spec":[],"session":session,"goods_id":84,"number":1}
    print(cart.create_cart(url=url, data=create_da))
    # 查看购物车
    url = "?url=/cart/list"
    getcat_data = {"session": session}
    print(cart.get_goods_goods_list(url=url, data=getcat_data))








