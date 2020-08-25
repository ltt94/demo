# -*- coding: utf-8 -*-
"""
===========================
   File Name：     handle_request
   Description :
   Author :       lintt
   date：          2020/7/27
===========================
"""

import requests
#header中，"Content-Type":"multipart/form-data"
from requests_toolbelt import MultipartEncoder


def send_requests(method,url,data=None):
    """
    封装了request方法
    :param method:根据请求类型，调用请求方法
    :param url:得到完整的url - 拼接url
    :param data:请求数据的处理 - 如果是字符串，则转换成字典对象
    :param token:
    :return:
    """
    # header = __pre_header(token)
    # url = __pre_url(url)
    #请求地址
    base_url = "http://139.9.119.10:9000"
    url = base_url + url
    #请求参数
    data = eval(data)
    Data = MultipartEncoder(fields=data)

    header = {
        "Content-Type": Data.content_type
    }
    if method.upper() == "GET":
        respon = requests.get(url,Data,headers=header)
    else:
        respon = requests.post(url,Data,headers=header)

    return respon


if __name__ == '__main__':
    send_requests("get", "/kvp_mps/v1/users/users/info", data=None)
