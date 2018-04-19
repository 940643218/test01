#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
url1="https://www.weibo.com"
driver.get(url1)
print(driver.get_cookies())
time.sleep(5)
driver.find_element_by_xpath("//input[@id='loginname']").send_keys("18677236149")
driver.find_element_by_xpath("//input[@tabindex='2']").send_keys("lifeng")
driver.find_element_by_xpath("//a[@tabindex='6']").click()
print(driver.get_cookies())
time.sleep(3)
driver.delete_all_cookies()
print(driver.get_cookies())
time.sleep(20)
driver.quit()
