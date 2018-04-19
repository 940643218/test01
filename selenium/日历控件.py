#coding:utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
driver.get("https://kyfw.12306.cn/otn/index/init")
time.sleep(3)
#去掉元素的readonly属性
js='document.getElementById("train_date").removeAttribute("readonly");'
driver.execute_script(js)
#清空文本后输入值
# driver.find_element_by_id("train_date").clear()
# driver.find_element_by_id("train_date").send_keys("2018-04-05")
#用js方法输入值
js_value='document.getElementById("train_date").value="2018-04-06"'
driver.execute_script(js_value)