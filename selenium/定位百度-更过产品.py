#coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
time.sleep(3)
mouse=driver.find_element_by_link_text(u"更多产品")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_elements("css selector",".bdbriimgitem_1")[0].click()