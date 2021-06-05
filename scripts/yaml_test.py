import yaml

data1 = {'Search_Data': {
'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}

data2 = {"test_click_speak" : [('chat',666),('chat',888)]}



with open("../data/test_speak_data.yaml", 'w', encoding ="utf-8") as f:
    #必须用allow_unicode=True才可以不乱码
    yaml.dump(data1, f,allow_unicode=True)

with open("../data/test_speak_data.yaml", 'r', encoding ="utf-8") as f:
    #这个是老方法会提示警告
    # data = yaml.load(f)
    #这个是新的，也可以用SafeLoader，会更加安全
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(type(data))  # 打印data类型
    print(data)  # 打印data返回值