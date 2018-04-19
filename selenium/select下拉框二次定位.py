#encoding=utf-8
from selenium import webdriver
import time 
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome()
url="https://www.baidu.com"
driver.get(url)
driver.implicitly_wait(3)
mouse=driver.find_element_by_link_text(u"设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text(u"搜索设置").click()
# s=driver.find_element_by_id("nr")
# s.find_element_by_xpath("//option[@value='20']").click()
driver.find_element_by_id("nr").find_element_by_xpath("//option[@value='20']").click()
driver.find_element_by_link_text(u"保存设置").click()
