#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.get("file:///D:/Rat.html")
# driver.find_element_by_id("c1").click()
checkboxs=driver.find_elements_by_xpath(".//*[@type='checkbox']")
for i in checkboxs:
    i.click()
