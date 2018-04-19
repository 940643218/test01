#encoding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(3)
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").send_keys(Keys.ENTER)