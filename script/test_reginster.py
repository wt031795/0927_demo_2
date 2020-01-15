from common.operation_data import OperationFile
import unittest
from interface.reginster_interface import Register
import ddt

register_data = OperationFile("python注册.xlsx").get_data_to_dict()


@ddt.ddt
class TestRegister(unittest.TestCase):

    @ddt.data(*register_data)
    def test_register(self, data):
        """测试注册"""
        register = Register(str(data["tel"]), data["email"], data["name"], data["password"])
        re = register.register()
        """断言"""
        status_code = re["status"]["succeed"]
        if status_code == "1":
            self.assertTrue(status_code, msg="注册成功")
        else:
            self.assertFalse(status_code, msg="注册失败")


if __name__ == "__main__":
    unittest.main()
