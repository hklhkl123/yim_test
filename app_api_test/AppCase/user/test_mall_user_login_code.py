import unittest
from pprint import pprint

import jsonpath
import requests


from app_api_test.common.setting import baseurl

url1 = baseurl


class TestLoginCode(unittest.TestCase):

    def setUp(self):
        print("开始")

    # 使用短信验证码登录
    def test_login_code(self):
        # 请求头
        headers = {

        }
        # 请求体

        payload = {
            "phone": "18820787573",
            "area_code": "+86",
            "code": "1234",
            "sign": "7f6d0ffc-b0e2-495e-b438-6ac0a7f4155a",
            "app_version": "1.0",

        }
        # 请求地址
        url = url1 + '/user/login/code'
        # 发起请求
        response = requests.request("POST", url, headers=headers, params=payload)
        # 接口返结果处理
        result = response.json()
        pprint(result)
        print(result["code"])
        print(result["message"])

        # 获取token
        token1 = jsonpath.jsonpath(result, '$..token')
        # 格式化token
        token2 = "".join(token1)
        # 返回token
        print(token2)

        # 接口返回200，并且返回结果中code=0,message=成功，
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, result["code"])
        self.assertEqual('成功', result["message"])
        return token2

    def tearDown(self):
        print("结束")
