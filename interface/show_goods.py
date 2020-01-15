from common.sendmethod import SendMethod
from common.getkeyword import get_keyword
from interface.login_interface import LoginInterface


class ShowGoodsList:
    def __init__(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/goods"

    def goodsList(self, session):
        '''查看商品列表'''
        showgoods_data = {"goods_id": 1072, "session": session}  # 商品详情请求参数
        return SendMethod.send_post(url=self.url, data=showgoods_data)

    def get_goodsList(self, data):
        '''获取商品列表中的返回值'''
        response = self.goodsList(data)
        return get_keyword(response, "id")



if __name__ == '__main__':
    login = LoginInterface()
    login_data = {"name": "yehong", "password": "yehong123"}
    session = LoginInterface().get_session(data=login_data)
    show = ShowGoodsList()
    result = show.goodsList(session)
    print(result)
