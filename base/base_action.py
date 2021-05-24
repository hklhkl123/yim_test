from selenium.webdriver.support.wait import WebDriverWait
class BaseAction(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, time=15, poll=1):
        return WebDriverWait(self.driver, time, poll).until(lambda x: x.find_element(loc[0], loc[1]))
        # return self.driver.find_element(by, value)

    def find_elements(self, loc, time=10, poll=1):
        return WebDriverWait(self.driver, time, poll).until(lambda x: x.find_elements(loc[0], loc[1]))
        # return self.driver.find_elements(by, value)

    def click(self, loc):
        self.find_element(loc).click()

    def input(self, loc, text):
        self.find_element(loc).send_keys(text)