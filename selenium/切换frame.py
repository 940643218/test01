#encoding=utf-8
from selenium import webdriver
import time
import random
driver=webdriver.Chrome()
driver.get("https://www.mail.163.com")
time.sleep(3)
# driver.switch_to_frame("x-URS-iframe")
iframe=driver.find_element_by_tag_name("iframe")
driver.switch_to_frame(iframe)
driver.find_element_by_name("email").send_keys("18617093687")
driver.find_element_by_name("password").send_keys("315021")
driver.find_element_by_id("dologin").click()
driver.switch_to_default_content()#回到主页面
time.sleep(20)
driver.quit()
