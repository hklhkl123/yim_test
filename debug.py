import time
import os,sys
import pytest

sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.message_page import MessagePage
from base.read_yaml import Read_Data


def package_param_data():
    list_data = []  # 存储参数值列表，格式[(用例编号1,输入内容2),(用例编号1,输入内容2)...]
    yaml_data = Read_Data("test1.yaml").return_data()  # 返回yaml文件读取数据
    print(yaml_data)
    for i in yaml_data.keys():
        list_data.append((i, yaml_data.get(i).get('speak_test_002')))  # list_data中添加参数值
    print("--------------")
    print(list_data)
    return list_data

package_param_data()
print("come on66666")