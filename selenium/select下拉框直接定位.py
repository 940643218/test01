#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(3)
mouse=driver.find_element_by_link_text(u"设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text(u"搜索设置").click()
driver.find_element_by_xpath(".//*[@id='nr']/option[2]").click()