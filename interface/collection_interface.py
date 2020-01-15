from common.sendmethod import SendMethod
from common.getkeyword import get_keyword
from interface.login_interface import LoginInterface


class CollectionList:
    def __init__(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/"

    def add_collection(self, url, session):
        '''添加收藏'''
        url = self.url + url
        add_collection_data = {"session": session, "goods_id": 1087}
        return SendMethod.send_post(url=url, data=add_collection_data)

    def collection_list(self, url, session):
        '''查看收藏列表'''
        url = self.url + url
        collection_list_data = {"session": session,
                                "pagination": {"count": 10, "page": 1}, "rec_id": 0}
        return SendMethod.send_post(url=url, data=collection_list_data)

    def get_rec_id(self, url, session):
        '''获取收藏列表中的rec_id'''
        response = self.collection_list(url=url, session=session)
        recid = get_keyword(response, keyword="rec_id")
        return recid

    def collection_news(self, url, session):
        '''收藏商品详情'''
        url = self.url + url
        collection_news_data = {"goods_id": 1087, "session": session}
        return SendMethod.send_post(url=url, data=collection_news_data)

    # def get_id(self, url, session):
    #     '''获取商品id'''
    #     response = self.collection_news(url=url, session=session)
    #     id = get_keyword(response, keyword="id")
    #     return id

    def delect_collection(self, url, rec_id, session):
        '''删除收藏'''
        url = self.url + url
        delect_collection_data = {"session": session,
                                  "rec_id": rec_id}
        return SendMethod.send_post(url=url, data=delect_collection_data)


if __name__ == '__main__':
    login = LoginInterface()
    login_data = {"name": "yehong", "password": "yehong123"}
    session = LoginInterface().get_session(data=login_data)
    collection = CollectionList()

    # 添加收藏
    url = "?url=/user/collect/create"
    result = collection.add_collection(url=url, session=session)
    print(result)

    # 查看商品列表
    url = "?url=/user/collect/list"
    result = collection.get_rec_id(url=url, session=session)
    print(result)

    # 查看收藏商品详情
    url = "?url=/goods"
    result = collection.collection_news(url=url, session=session)
    print(result)

    # 删除收藏
    url = "?url=/user/collect/delete"
    result = collection.delect_collection(url=url, session=session, rec_id=result)
    print(result)
