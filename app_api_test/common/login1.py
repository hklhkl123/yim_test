import jsonpath
import requests
import hashlib

# 这里是接口地址，必填
from app_api_test.common.setting import baseurl

url1 = baseurl


# app登录接口获取token
def test_login_code():
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
    # print(result)
    # print(result["code"])
    # print(result["message"])

    # 获取token
    token1 = jsonpath.jsonpath(result, '$..token')
    # 格式化token
    token2 = "".join(token1)
    # 返回token
    print(token2)
    return token2


# 云聊登录接口获取token
def getToken():
    payload = {'account': '张英波',
               'password': 'test888888',
               'sign': 'f9a69c19-25c7-4ebf-ae96-468f80c487db',
               'app_version': '1.17.3'
               }

    url = url1 + '/staff/signin'
    response = requests.request("POST", url, data=payload)
    result = response.json()
    # 获取token
    token1 = jsonpath.jsonpath(result, '$..token')
    # 格式化token
    token2 = "".join(token1)
    # 返回token
    return token2


# MD5加密，32位小写
def md5vale(key):
    input_name = hashlib.md5()

    input_name.update(key.encode("utf-8"))

    sign = input_name.hexdigest()

    print(key, "  ---->  ", sign)
    # 返回加密后的sign
    return sign


if __name__ == '__main__':
    print(getToken())
