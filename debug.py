import time
import os,sys
import pytest
import yaml

sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.message_page import MessagePage
from base.base_yaml import yml_data_with_filename_and_key

a =  yml_data_with_filename_and_key("test_speak", "test_click_speak")
print(a)
@pytest.mark.parametrize("name,content", yml_data_with_filename_and_key("test_speak", "test_click_speak"))
def test_001(name,content):
    print(name+' and '+str(content))



# @pytest.mark.parametrize('name,age',[('rob',22),('lisa',28)])
# def test_def2(name,age):
#     print(name+'+'+str(age))

data1 = {'Search_Data': {
'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
'search_test_001': {'expect': [4, 5, 6], 'value': 456},
'search_test_003': [("ccc",111),222,333]}}

# with open("data/test_speak.yaml", 'w', encoding ="utf-8") as f:
#     #必须用allow_unicode=True才可以不乱码
#     yaml.dump(data1, f,allow_unicode=True)

# with open("data/test_speak.yaml", "r",encoding ="utf-8" ) as f:
#     data = yaml.load(f,Loader = yaml.FullLoader)["test_login1"]
#     print(data)