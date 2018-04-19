#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
url="https://www.baidu.com"
driver.get(url)
driver.implicitly_wait(10)
mouse=driver.find_element_by_link_text(u"设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text(u"搜索设置").click()
# s = driver.find_element_by_xpath("//td[@id='se-setting-3']/select")
s=driver.find_element_by_id("nr")
# Select(s).select_by_value("20")
Select(s).select_by_visible_text("每页显示20条").click()