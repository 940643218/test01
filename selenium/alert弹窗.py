#coding:utf-8
from selenium import webdriver
driver=webdriver.Firefox()
import time
driver.get("file:///D:/test2.html")
time.sleep(3)
driver.find_element_by_xpath("/html/body/input").click()
time.sleep(3)
al=driver.switch_to_alert()
al.accept()