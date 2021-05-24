import pytest
import os,sys
sys.path.append(os.getcwd())

# a= os.getcwd()
# sys.path.append(a)
# sys.path.append("C:\\Users\\admin\\PycharmProjects\\pythonPO")

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from base.base_driver import init_driver


class Test_move(object):
    def setup(self):
        self.driver = init_driver()

    def test_move1(self):
        #scroll滑动数据，从一个元素到另一元素位置【有惯性】
        ele1 = WebDriverWait(self.driver, 10, 1).until(lambda x:x.find_element_by_xpath("//*[contains(@text,'工作助手')]"))
        ele2 = WebDriverWait(self.driver, 10, 1).until(lambda x:x.find_element_by_xpath("//*[contains(@text,'智能云官方交流群')]"))
        self.driver.scroll(ele1,ele2)

    def teardown(self):
        self.driver.quit()

@pytest.mark.skipif(True,reason="已经玩过了")
class Test_chat(object):
    def setup(self):
        self.driver = init_driver()

    def test_chat1(self):
        ele1 = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element_by_xpath("//*[contains(@text,'工作助手')]"))
        ele1.click()

    def teardown(self):
        self.driver.quit()


if __name__ == "__main__":
    pytest.main(["-s","pre_test_move.py"])