from appium import webdriver

def init_driver():
    # server 启动参数
    desired_caps = {}
    # 设备信息
    # desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '6.0'
    # desired_caps['deviceName'] = '0123456789ABCDEF'

    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.1.0'
    desired_caps['deviceName'] = 'e1a3da18'

    # app信息
    desired_caps['appPackage'] = 'com.yidejia.yim.test'
    desired_caps['appActivity'] = 'com.yidejia.yim.SplashActivity'
    #启动环境，解决输入中文和不重置数据
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    desired_caps['noReset'] =True
    desired_caps['dontStopAppOnReset'] =True

    # toast
    desired_caps['automationName'] = 'Uiautomator2'

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver