import time
import os,sys
import pytest
import allure

sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.message_page import MessagePage
from base.base_yaml import yml_data_with_filename_and_key


#类的名字不需要下划线，就这个就可以
class TestSpeak(object):

    def setup(self):
        self.driver = init_driver()
        self.message_page = MessagePage(self.driver)

    @pytest.mark.skipif(True, reason="已经玩过了")
    @allure.step(title="测试步骤001")
    #这里是设置用例的级别，会显示到allure报告中
    @allure.severity(allure.severity_level.CRITICAL)
    #想要的效果("type,content",[('chat',111111),('chat',222222)])
    #这个也可以写成(("type","content"),data)
    @pytest.mark.parametrize("type,content",yml_data_with_filename_and_key("test_speak_data","test_click_speak"))
    def test_click_speak(self,type,content):
        allure.attach('描述', '我是测试步骤001的描述～～～')
        self.message_page.click_group1()
        self.message_page.input_text(type,content)
        self.message_page.send_message()
        time.sleep(2)
        self.message_page.click_back()

    #这个用来点击群时判断toast提示不在群了
    def test_click_toast(self):
        self.message_page.click_group4()
        assert self.message_page.is_toast_exist('你已经不在群内')
        print("的确不在群了")
        #这个也是返回
        self.driver.keyevent(4)
        # self.message_page.click_back()

    #这个用来点击被踢群时后发言，判断toast提示不在群不能发言
    def test_click_speak_toast(self):
        self.message_page.click_group4()
        time.sleep(3)
        self.message_page.input_text("chat", "随便说句话")
        self.message_page.send_message()
        assert self.message_page.is_toast_exist('无法发送消息')
        print("不在群，不能发言")
        # 这个也是返回，因为这个有个标志挡住了，不能正常点击，用系统的返回处理
        self.driver.keyevent(4)
        # self.message_page.click_back()

    @pytest.mark.skipif(True, reason="已经玩过了")
    @allure.step(title="测试步骤002")
    #这个是用来滚动一下列表，然后点击第二个群发言
    def test_roll_click_speak(self):
        self.message_page.roll_group()
        self.message_page.click_group2()
        self.message_page.input_text("chat","第二个和大家好了")
        self.message_page.send_message()
        time.sleep(2)
        self.message_page.click_back()

    @pytest.mark.skipif(True, reason="已经玩过了")
    @allure.step(title="测试步骤003")
    #这个是用来滚动一下列表，然后搜索群进行发言
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


    def teardown(self):
        self.driver.quit()

if __name__ == "__main__":
    pytest.main(["-s","test_speak.py"])