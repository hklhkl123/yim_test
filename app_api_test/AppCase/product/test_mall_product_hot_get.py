
import unittest
from pprint import pprint

import requests
from app_api_test.common.setting import baseurl

url1 = baseurl


class Test(unittest.TestCase):

    def setUp(self):
        print("开始")

    # 获取热销商品【缓存】
    def test_1(self):
        # 调用登录函数获取最新token
        # token = login1.test_login_code()
        # # 请求头
        headers = {
            # "token": token

        }

        payload = {
            # "thumb_image_width": "300"

        }
        # 请求地址
        url = url1 + '/mall/api/v1/product/spu/recommend/hot'
        # 发起请求
        response = requests.request("GET", url, headers=headers, params=payload)
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
