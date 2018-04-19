#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Firefox()
url="https://www.baidu.com"
driver.get(url)
time.sleep(3)
# mouse=driver.find_element("link text",u"设置")
mouse=driver.find_element_by_link_text(u"设置")
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(3)
# driver.find_element("link text",u"搜索设置").click()
driver.find_element_by_link_text(u"搜索设置").click()
time.sleep(3)
# s=driver.find_element("id","nr")
s=driver.find_element_by_id("nr")
Select.select_by_visible_text(u"每页显示50条")
#方法一：先点父元素
# driver.find_element("id","gxszButton").click()
# driver.find_element("class name","prefpanelgo").click()
driver.find_element_by_id("gxszButton").click()
driver.find_element_by_name("prefpanelgo").click()
