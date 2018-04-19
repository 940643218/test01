#encoding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
url1="https://www.baidu.com"
driver.implicitly_wait(10)
driver.get(url1)
time.sleep(3)
title=driver.title
print(title)
text=driver.find_element_by_xpath("//a[@id='setf']").text
print(text)
tag=driver.find_element_by_id("kw").tag_name
print(tag)
name=driver.find_element_by_id("kw").get_attribute("class")
print(name)
driver.find_element_by_id("kw").send_keys("yoyoketang")
driver.find_element_by_xpath("//input[@type='submit']").click()
value=driver.find_element_by_id("kw").get_attribute("value")
print(value)
print(driver.name)
time.sleep(20)
driver.quit()
