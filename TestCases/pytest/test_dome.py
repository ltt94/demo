# -*- coding: utf-8 -*-
"""
===========================
   File Name：     test_dome
   Description :
   Author :       lintt
   date：          2020/8/11
===========================
"""

from common.handle_request import send_requests
from common.handle_excel import HandleFile
from common.handle_path import datas_path
import pytest
import json

cases = HandleFile(datas_path + "\\login_cases.xlsx").get_excel_data()

@pytest.mark.parametrize("case",cases)
class TestLogin:
    def test_login(self,case):
        print("执行第{}条用例：{}".format(case["id"], case["title"]))
        print("测试数据为：",case)
        respon = send_requests(case["method"], case["url"], data=case["request_data"])
        print("测试结果为：", respon.json())
        expect_data = json.loads(case["expect_data"])
        try:
            assert respon.json()["code"]==expect_data["code"]
            assert respon.json()["msg"]==expect_data["msg"]
            # self.assertEqual(respon.json()["code"], expect_data["code"])
            # self.assertEqual(respon.json()["msg"], expect_data["msg"])
        except:
            print("断言失败")
            raise

# if __name__ == '__main__':
#     pytest.main(["-s","-v",
#                  "--html=Outputs/reports/pytest.html",
#                  "--alluredir=Outputs/allure"])