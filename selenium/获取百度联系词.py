#coding:utf-8
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
time.sleep(3)
driver.find_element_by_id("kw").send_keys("python")
time.sleep(3)
bd=driver.find_elements_by_class_name("bdsug-overflow")
# for i in bd:
#     print(i.get_attribute("data-key"))
time.sleep(3)
if len(bd)>1:
    bd[1].click()
    print(driver.current_url)
else:
    print(u"未获取到匹配的词")