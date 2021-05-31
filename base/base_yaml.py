import yaml

def yml_data_with_filename_and_key(file_name, key):
    with open("./data/" + file_name + ".yaml", "r",encoding ="utf-8" ) as f:
        data = yaml.load(f,Loader = yaml.FullLoader)[key]
        # case_data_list = list()
        # for case_data in data.values():
        #     case_data_list.append(case_data)

        return data

# data1 = {'Search_Data': {
# 'search_test_002': {'expect': {'value': '你好'}, 'value': '你好'},
# 'search_test_001': {'expect': [4, 5, 6], 'value': 456}}}
# 'search_test_003':{111,222,333}
#
# with open("data/test1.yaml", 'w', encoding ="utf-8") as f:
#     #必须用allow_unicode=True才可以不乱码
#     yaml.dump(data1, f,allow_unicode=True)