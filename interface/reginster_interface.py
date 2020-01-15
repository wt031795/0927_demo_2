"""
1.测试登录接口方法
2.获取session方法
"""
from common.sendmethod import SendMethod
from common.getkeyword import get_keyword


class Register:
    def __init__(self, tel, email, name, password):
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signup"
        self.register_data = {"field": [{"id": 5, "value": tel}], "email": email, "name": name, "password": password}

    def register(self):
        """请求注册接口"""
        return SendMethod.send_post(url=self.url, data=self.register_data)
    # def get_succeed(self):


if __name__ == "__main__":
    register = Register(tel=14555555555, email="123@qq.co", name="hsb4349u238", password="8764836")
    re = register.register()
    print(re)
