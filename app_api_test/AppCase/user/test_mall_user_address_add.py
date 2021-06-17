
import unittest
from pprint import pprint

import requests
from app_api_test.common import login1

from app_api_test.common.setting import baseurl

url1 = baseurl


class Test(unittest.TestCase):

    def setUp(self):
        print("开始")

    # 新增地址【token】
    def test_address(self):
        # 调用登录函数获取最新token
        token = login1.test_login_code()
        # # 请求头
        headers = {
            "token": token
        }

        payload = {
            "customer_name": "ceshi1",
            "handset": "12222222222",
            "telephone": "020-12345678",
            "province": "广东省",
            "city": "广州市",
            "district": "番禺区",
            "address": "哈哈哈",
            "is_default": "is_default",

        }
        # 请求地址
        url = url1 + '/api/v1/user/address'
        # 发起请求
        response = requests.request("POST", url, headers=headers, params=payload)
        # 接口返结果处理
        result = response.json()
        pprint(result)
        print(result["code"])
        print(result["message"])

        # 接口返回200，并且返回结果中code=0,message=成功，
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, result["code"])
        self.assertEqual('success', result["message"])

    def tearDown(self):
        print("结束")
