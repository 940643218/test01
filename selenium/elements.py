#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
time.sleep(3)
#这里定位多个class
# elements=driver.find_elements_by_class_name("mnav")
# elements[1].click()
#这里使用css语法
# driver.find_elements("css selector",".mnav")[3].click()
s=driver.find_elements("css selector",".mnav")
print(s[2].text)
s[2].click()