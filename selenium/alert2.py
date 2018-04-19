#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
url="https://www.baidu.com"
driver.get(url)
driver.implicitly_wait(10)
mouse=driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
driver.find_element_by_link_text("搜索设置").click()
s=driver.find_element_by_id("nr")
Select(s).select_by_visible_text("每页显示20条")
time.sleep(3)
s.click()
driver.find_element_by_link_text(u"保存设置").click()
time.sleep(5)
t=driver.switch_to_alert()
print(t.text)
t.accept()