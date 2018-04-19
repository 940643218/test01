#encoding=utf-8
from selenium import webdriver
import random
import time
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(3)
driver.find_element_by_id("kw").send_keys(u"测试部落")
driver.find_element_by_id("kw").submit()
s=driver.find_elements_by_css_selector("h3.t>a")
t=random.randint(0,9)
a=s[t].get_attribute("href")
print(a)
driver.get(a)
time.sleep(20)
driver.quit()
