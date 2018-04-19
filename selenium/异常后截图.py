#encoding:utf-8
from selenium import webdriver
import time
url_login="https://passport.cnblogs.com/user/signin"
driver=webdriver.Firefox()
driver.get(url_login)
try:
    driver.find_element_by_id("input1").send_keys("18617093687")
    driver.find_element_by_id("input2").send_keys("1qw2!QW@")
    driver.find_element_by_id("signin1").click()
except Exception as msg:
    print(u"异常原因：%s" % msg)
    nowtime=time.strftime("%Y%m%d.%H.%M.%S")
    t=driver.get_screenshot_as_file("%s.png" % nowtime)
    print(u"截图结果：%s" % t)
    