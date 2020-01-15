"""
1.测试登录接口方法
2.获取session方法

"""
from common.sendmethod import SendMethod
from common.getkeyword import get_keyword


class LoginInterface:
    def __init__(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
        self.data={"name":"jing123","password":"jing123"}

    def login(self):
        """请求登录接口"""
        return SendMethod.send_post(url=self.url,data=self.data)

    def get_session(self):
        """获取登录后的session"""
        response = self.login()
        return get_keyword(response,"session")

if __name__ == '__main__':
    login = LoginInterface()
    session = login.get_session()
    print(session)
    # url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/info"  # 个人中心请求地址
    # userinfo_data = {"session":session}  # 个人中心请求参数
    # print(SendMethod.send_post(url, userinfo_data))




