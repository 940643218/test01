#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("http://sh.xsjedu.org/")
time.sleep(3)
js='document.getElementById("doyoo_monitor").style.display="none";'
driver.execute_script(js)