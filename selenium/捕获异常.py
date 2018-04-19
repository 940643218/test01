#coding:utf-8
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
driver=webdriver.Firefox()
driver.get("https://passport.cnblogs.com/user/signin")
try:
    element=driver.find_element("id","blog_nav_newpostxx")
except NoSuchElementException as msg:
    print(u"查找元素异常%s" % msg)
else:
    element.click()