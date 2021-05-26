import sys, os

from appium.webdriver.common.touch_action import TouchAction

sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class MessagePage(BaseAction):

    group1 = By.XPATH, "//*[contains(@text,'智能云官方交流群')]"
    group2 = By.XPATH, "//*[contains(@text,'唐凯丽PK群')]"
    group3 = By.XPATH, "//*[contains(@text,'云聊官方交流群') and contains(@resource-id,'com.yidejia.yim.test:id/tv_name')]"
    smartrobot_button = By.XPATH,"//*[contains(@resource-id,'com.yidejia.yim.test:id/iv_assist')]"
    more_button = By.XPATH,"//*[contains(@resource-id,'com.yidejia.yim.test:id/base_iv_right')]"
    search_button = By.XPATH,"//*[contains(@text,'搜索')]"
    back_button = By.XPATH, "//*[contains(@resource-id,'com.yidejia.yim.test:id/base_tv_left')]"
    chat_input_button = By.XPATH, "//*[contains(@resource-id,'com.yidejia.yim.test:id/et_chat_input')]"
    chat_send_button = By.XPATH, "//*[contains(@resource-id,'com.yidejia.yim.test:id/iv_send')]"

    def __init__(self,driver):
        BaseAction.__init__(self,driver)
        #这个下面其实一般会加上其他固定步骤，比如我只要测试message，但是我需要先进入这里A点击B，就可以放这

    def click_group1(self):
        self.click(self.group1)

    def click_group2(self):
        self.click(self.group2)

    def click_group3(self):
        self.click(self.group3)

    def click_search_button(self):
        self.click(self.search_button)

    #把2移动到1的位置
    def roll_group(self):
        self.ele1 = self.find_element(self.group1)
        self.ele2 = self.find_element(self.group2)
        self.driver.scroll(self.ele2, self.ele1)

    def roll_xy(self):
        TouchAction(self.driver).press(x=200, y=260).wait(100).move_to(x=200, y=1800).release().perform()
        # self.driver.swipe(200, 259, 200, 848, 1000)
    def click_smartrobot_button(self):
        self.click(self.smartrobot_button)

    def click_more_button(self):
        self.click(self.more_button)

    def input_text(self,type,text):
        if type == 'chat':
            self.input(self.chat_input_button,text)
        if type == 'search':
            self.input(self.search_button,text)

    def send_message(self):
        self.click(self.chat_send_button)

    def click_back(self):
        self.click(self.back_button)