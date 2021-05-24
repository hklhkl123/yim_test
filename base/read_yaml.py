import yaml, os

class Read_Data(object):
    def __init__(self, file_name):
        '''
        	使用pytest运行在项目的根目录下运行，即App_Project目录
        	期望路径为：项目所在目录/App_Project/Data/file_name
        '''
        self.file_path = os.getcwd() + os.sep + "data" + os.sep + file_name

    def return_data(self):
        with open(self.file_path, 'r',encoding="utf-8") as f:
            data = yaml.load(f,Loader = yaml.FullLoader)  # 读取文件内容
            return data

    # data:{"search_test_001":{"input_text": "你好"},"search_test_002":{"input_text": "1234"},"search_test_003":{"input_text": "*&^%"}}