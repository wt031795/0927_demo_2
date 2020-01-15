"""
封装sendmethod.py
根据ECShop的接口特点,封装对应的方法:
请求方式:POST
请求参数类型:urlencoded格式
"""
import requests
import json


class SendMethod:
    @staticmethod
    def send_post(url=None, data=None):
        # 对请求参数格式化
        ruqest_data = {
            "json": json.dumps(data)
        }
        response = requests.post(url=url, data=ruqest_data)
        return response.json()  # 接口返回值为json格式

    @staticmethod
    def sendmethod(url=None, data=None):
        """封装请求参数和请求方式"""

        request_data = {

            "json": json.dumps(data)

        }

        response = requests.post(url=url, data=request_data)

        return response.json()


if __name__ == '__main__':
    import json

    url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin"
    data = {"name": "yuanma", "password": "123456"}
    res = SendMethod.send_post(url=url, data=data)
    print(res)
