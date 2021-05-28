import time
import os,sys
import pytest
import allure

sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.message_page import MessagePage
from base.read_yaml import Read_Data


def package_param_data():
    list_data = []  # 存储参数值列表，格式[(用例编号1,输入内容2),(用例编号1,输入内容2)...]
    yaml_data = Read_Data("test1.yaml").return_data()  # 返回yaml文件读取数据
    print(yaml_data)
    for i in yaml_data.keys():
        list_data.append((i, yaml_data.get(i).get('search_test_001')))  # list_data中添加参数值
    print(list_data)
    return list_data

# package_param_data()

#类的名字不需要下划线，就这个就可以
class TestSpeak(object):

    def setup(self):
        self.driver = init_driver()
        self.message_page = MessagePage(self.driver)

    # @pytest.mark.skipif(True, reason="已经玩过了")
    # @pytest.mark.parametrize("type,content",package_param_data())
    @allure.step(title="测试步骤001")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_click_speak(self):
        allure.attach('描述', '我是测试步骤001的描述～～～')
        self.message_page.click_group1()
        self.message_page.input_text("chat","大家好")
        self.message_page.send_message()
        time.sleep(3)
        self.message_page.click_back()

    # @pytest.mark.skipif(True, reason="已经玩过了")
    @allure.step(title="测试步骤002")
    def test_roll_click_speak(self):
        self.message_page.roll_group()
        self.message_page.click_group2()
        self.message_page.input_text("chat","第二个和大家好了")
        self.message_page.send_message()
        time.sleep(3)
        self.message_page.click_back()

    # @pytest.mark.skipif(True, reason="已经玩过了")
    @allure.step(title="测试步骤003")
    def test_search_click_speak(self):
        self.message_page.roll_xy()
        self.message_page.click_search_button()
        time.sleep(3)
        self.message_page.input_text("search","云聊官方交流群")
        self.message_page.click_group3()
        self.message_page.input_text("chat","终于到云聊官方了")
        self.message_page.send_message()
        time.sleep(3)
        self.message_page.click_back()

    # @pytest.mark.parametrize('test_id,input_text', package_param_data())  # 参数传递三组参数，会运行三次
    # def test_search(self, test_id, input_text):
    #     # 示例化页面封装类
    #     sp = Search_Page(self.driver)
    #     # 调用操作类
    #     print("test_id:", test_id)
    #     sp.input_search_text(input_text)
    #     # 退出driver对象

    def teardown(self):
        self.driver.quit()

if __name__ == "__main__":
    pytest.main(["-s","test_speak.py"])