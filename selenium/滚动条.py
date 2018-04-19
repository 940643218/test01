#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
url1="https://www.weibo.com"
driver.get(url1)
time.sleep(3)
# js1='var q=document.documentElement.scrollTop=10000'
# driver.execute_script(js1)
# time.sleep(3)
# js2="var q=document.getElementById('id').scrollTop=0"
# driver.execute_script(js2)
# js = "window.scrollTo(100,400)"
# driver.execute_script(js)
js="var q=document.body.scrollTop=10000"
driver.execute_script(js)
time.sleep(20)
driver.quit()
