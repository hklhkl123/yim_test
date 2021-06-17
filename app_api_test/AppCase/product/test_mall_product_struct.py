
import time
import unittest
from pprint import pprint

import requests
from app_api_test.common import login1

from app_api_test.common.setting import baseurl

url1 = baseurl


class TestStruct(unittest.TestCase):

    def setUp(self):
        print("开始")

    # 商品结构【缓存】
    def test_struct(self):

        # 调用登录函数获取最新token
        # token = login1.test_login_code()
        # 请求头
        headers = {}
        # 请求体

        payload = {
                   'cat_ids': "[148,16,25,33,37,2,7,12,87,46,53,133,61,64,73,78,84,130]",

                   'thumb_image_width': "750"

                   }
        # 请求地址
        url = url1 + '/mall/api/v1/product/spu/struct'
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
        time.sleep(2)



    def tearDown(self):
        print("结束")
