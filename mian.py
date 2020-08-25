# -*- coding: utf-8 -*-
"""
===========================
   File Name：     mian
   Description :
   Author :       lintt
   date：          2020/7/29
===========================
"""
from common.handle_path import datas_path,cases_path,reports_path,now
#unittest
# import unittest
# from HTMLTestRunnerNew import HTMLTestRunner
# from common.handle_path import cases_path,reports_path,now
# s = unittest.TestLoader().discover(cases_path+"\\unittest")
# with open( "Outputs/reports/" + now +"_unittest.html","wb") as fs:
#     runner = HTMLTestRunner(fs,title="登录测试报告",tester="lintt")
#     runner.run(s)



#pytest
import pytest
pytest.main(["TestCases/pytest/test_dome.py",
             "-s","-v",
             "--html","Outputs/reports/" + now + "_pytest.html",
             "--clean-alluredir",
             "--alluredir","Outputs/allure"])
# # pytest.main(["-s","-v",
#              "--html=Outputs/reports/pytest.html",
#              "--alluredir=Outputs/allure"])   # allure文件生成的目录