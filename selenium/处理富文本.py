#coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
url="https://passport.cnblogs.com/user/signin"
driver.get(url)
time.sleep(3)
driver.find_element_by_xpath("//input[@id='input1']").send_keys("18617093687")
driver.find_element_by_xpath("//input[@id='input2']").send_keys("1qw2!QW@")
driver.find_element_by_xpath("//input[@id='signin']").click()
driver.find_element_by_xpath("//div[@class='geetest_wait']").click()
time.sleep(3)