#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
url1="https://weibo.com/"
driver=webdriver.Chrome()
driver.get(url1)
time.sleep(5)
driver.find_element_by_xpath("//div[@class='tab clearfix']/a").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@id='loginname']").send_keys("18677236149")
driver.find_element_by_xpath("//input[@type='password']").send_keys("lifeng")
driver.find_element_by_xpath("//a[@tabindex='6']").click()
time.sleep(4)
url2=u"我来签到啦！^_^"
driver.find_element_by_xpath("//textarea[@title='微博输入框']").send_keys(url2)
time.sleep(2)
mouse1=driver.find_element_by_xpath("//form[@id='pic_upload']/input")
ActionChains(driver).move_to_element(mouse1).perform()
driver.find_element_by_xpath("//form[@id='pic_upload']/input").send_keys(r"E:\IMG_0171.JPG")
time.sleep(10)
mouse2=driver.find_element_by_xpath("//a[@node-type='submit']")
ActionChains(driver).move_to_element(mouse2).perform()
mouse2.click()