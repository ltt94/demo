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
from common.handle_path import datas_path,cases_path,reports_path,now

from ddt import ddt,data
import json
import unittest

cases = HandleFile(datas_path + "\\login_cases.xlsx").get_excel_data()
@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUp(self) -> None:
        print("=========【测试开始】=每个用例执行开始前都会执行【setUp】=========")
    @classmethod
    def tearDown(self) -> None:
        print("=========【测试结束】=每个用例执行结束后都会执行【tearDown】=========")

    @classmethod
    def setUpClass(cls) -> None:
        print("=========【测试开始】=每个测试类执行开始前都会执行【setUpClass】=========")

    @classmethod
    def tearDownClass(cls) -> None:
        print("=========【测试结束】=每个测试类执行结束后都会执行【tearDownClass】=========")


    @data(*cases)
    def test_login(self,case):
        print("执行第{}条用例：{}".format(case["id"],case["title"]))
        # send_requests() 在后续的文章有详细说明
        respon = send_requests(case["method"],case["url"],data=case["request_data"])
        print("测试结果为：",respon.json())
        expect_data = json.loads(case["expect_data"])
        try:
            # self.assertNotEquals(respon.json()["code"],expect_data["code"])
            self.assertEqual(respon.json()["code"],expect_data["code"])
            self.assertEqual(respon.json()["msg"], expect_data["msg"])
        except:
            print("断言失败")
            raise

