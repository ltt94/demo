# -*- coding: utf-8 -*-
"""
===========================
   File Name：     handle_excel
   Description :
   Author :       lintt
   date：          2020/7/27
===========================
"""
import pandas as pd
from common.handle_path import datas_path


class HandleFile:
    def __init__(self,file_path):
        self.file_path = file_path
    def get_excel_data(self):
        """
        把Excel里的数据转换成列表嵌字典的格式
        每一行（每一条用例）为一个字典，字典格式标题：内容
        如：
        [
            { 标题1:值1,标题2:值2,标题3:值3 },
            { 标题1:值1,标题2:值2,标题3:值3 },
            { 标题1:值1,标题2:值2,标题3:值3 },
        ]
        :return:
        """
        lines = pd.read_excel(self.file_path)
        cases = []
        for i in range(len(lines)):
            dict1 = {}
            for line in lines:
                dict1[line] = lines[line][i]
            cases.append(dict1)
            i += 1
        return cases



if __name__ == '__main__':
    # file_path = os.path.join(datas_path + "\\intent\\andrology","andrology_intent.csv")
    # exc = HandleExcel(file_path,"andrology_intent")
    # exc = HandleExcel(datas_path + "\\login_cases.xlsx", "登陆")
    # cases = exc.read_data()
    # exc.close_file()
    # print(cases)
    file_path = datas_path + "\\login_cases.xlsx"
    print(HandleFile(file_path).get_excel_data())
    print("test test")
