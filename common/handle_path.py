# -*- coding: utf-8 -*-
"""
===========================
   File Name：     handle_path
   Description :
   Author :       lintt
   date：          2020/7/27
===========================
"""
import os
import datetime
#base_dir = os.path.dirname(os.path.dirname(__file__))
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cases_path = os.path.join(base_dir,"TestCases")
datas_path = os.path.join(base_dir,"TestDatas")
reports_path = base_dir+"\\Outputs\\reports"
logs_dir = os.path.join(base_dir,"Outputs\\logs")
result_dir = os.path.join(base_dir,"Outputs\\results")
conf_dir = os.path.join(base_dir,"Conf")
now = str(datetime.datetime.now().strftime('%Y-%m-%d-%H_%M'))
