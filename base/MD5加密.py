# MD5加密，32位小写
import hashlib
import time
from datetime import date


def md5vale(key):
    input_name = hashlib.md5()

    input_name.update(key.encode("utf-8"))

    sign = input_name.hexdigest()

    print(key, "  ---->  ", sign)
    # 返回加密后的sign
    return sign


if __name__ == "__main__":
    # 参数sign，获取当前时间转化格式为2020-12-10，拼接参数值给MD5加密
    date = time.strftime("%Y-%m-%d", time.localtime())
    sign = md5vale(date + "-ybs-247")
    print(sign)
