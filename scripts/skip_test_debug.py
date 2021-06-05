import time
import os,sys
import pytest
import allure

sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.message_page import MessagePage
from base.base_yaml import Read_Data

class TestDebug(object):
    def setup(self):
        self.driver = init_driver()
        self.message_page = MessagePage(self.driver)

    def test_debug_1(self):
        assert True

    def test_debug_2(self):
        assert False

    def teardown(self):
        self.driver.quit()



if __name__ == "__main__":
    pytest.main(["-s","skip_test_debug.py"])