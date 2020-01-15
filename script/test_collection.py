import unittest
import ddt
from interface.login_interface import LoginInterface
from interface.collection_interface import CollectionList


@ddt.ddt
class Test_Collection(unittest.TestCase):
    def setUp(self):
        self.login = LoginInterface()  # 实例化登录
        self.collection = CollectionList()  # 实例化收藏

    def test_add_collection(self):
        '''测试添加收藏'''
        login_data = {"name": "yehong", "password": "yehong123"}
        session = self.login.get_session(data=login_data)
        url = "?url=/user/collect/create"
        result = self.collection.add_collection(url=url, session=session)
        self.assertTrue(result, login_data)

    def test_show_list(self):
        '''测试查看收藏列表'''
        login_data = {"name": "yehong", "password": "yehong123"}
        session = self.login.get_session(data=login_data)
        url = "?url=/user/collect/list"
        result = self.collection.collection_list(url=url, session=session)
        self.assertTrue(result, session)

    def test_collection_news(self):
        '''测试查看收藏商品详情'''
        login_data = {"name": "yehong", "password": "yehong123"}
        session = self.login.get_session(data=login_data)
        url = "?url=/goods"
        result = self.collection.collection_news(url=url, session=session)
        self.assertTrue(result, session)

    def test_delete_collection(self):
        '''测试删除收藏'''
        login_data = {"name": "yehong", "password": "yehong123"}
        session = self.login.get_session(data=login_data)
        url = "?url=/user/collect/delete"
        urll = "?url=/user/collect/list"
        rec_id = self.collection.get_rec_id(url=urll, session=session)
        result = self.collection.delect_collection(url=url, session=session,
                                                   rec_id=rec_id)
        self.assertTrue(result, self.collection.get_rec_id)


if __name__ == '__main__':
    unittest.main()
