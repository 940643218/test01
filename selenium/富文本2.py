#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
profileDir=r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\zf4klf5g.default'
profile=webdriver.FirefoxProfile(profileDir)
driver=webdriver.Firefox(profile)
blogurl="http://www.cnblogs.com/"
yoyoblog=blogurl+"yoyoketang"
driver.get(yoyoblog)
driver.find_element_by_id("blog_nav_newpost").click()
time.sleep(3)
edittile = u"Selenium2+python�Զ���-���ı�"
editbody = u"�����Ƿ���������"
driver.find_element_by_id("Editor_Edit_txbTitle").send_keys(edittile)
driver.switch_to_frame("Editor_Edit_EditorBody_ifr")
driver.find_element_by_id("tinymce").send_keys(Keys.TAB)
driver.find_element_by_id("tinymce").send_keys(editbody)
