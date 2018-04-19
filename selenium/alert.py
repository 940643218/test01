#encoding=utf-8
from selenium import webdriver
import time
url="file://D:/test2.html"
driver=webdriver.Chrome()
driver.get(url)
time.sleep(3)
driver.find_element_by_id("confirm").click()
time.sleep(3)
t=driver.switch_to_alert()
print(t.text)
t.accept()