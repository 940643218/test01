#coding=utf-8
from selenium import webdriver
import time
import re
driver=webdriver.Chrome()
print(driver.get_cookies())
# url1="https://home.cnblogs.com/u/lifeng315021/"
# driver.get(url1)
# print(driver.get_cookies())
# time.sleep(20)
# driver.quit()

url2="https://passport.cnblogs.com/user/signin"
driver.get(url2)
time.sleep(3)
driver.find_element_by_xpath("//input[@id='input1']").send_keys("18617093687")
driver.find_element_by_xpath("//input[@id='input2']").send_keys("1qw2!QW@")
driver.find_element_by_xpath("//input[@id='signin']").click()
time.sleep(2)
# print(driver.get_cookies())
print(driver.get_cookie(name='AspxAutoDetectCookieSupport'))
