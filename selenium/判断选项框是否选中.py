#encoding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("file:///D:/Rat.html")
time.sleep(3)
driver.find_element_by_id("girl").click()
time.sleep(3)
s=driver.find_element_by_id("boy").is_selected()
print(s)
driver.find_element_by_id("boy").click()
r=driver.find_element_by_id("boy").is_selected()
print(r)