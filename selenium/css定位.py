#encoding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("https://www.baidu.com")
time.sleep(3)
# driver.find_element_by_css_selector("#kw").send_keys("python")
# driver.find_element_by_css_selector(".s_ipt").send_keys("python")
# driver.find_element_by_css_selector("input").send_keys("python")
# driver.find_element_by_css_selector("[name='wd']").send_keys("python")
# driver.find_element_by_css_selector("[autocomplete='off']").send_keys("python")
# driver.find_element_by_css_selector("input[id='kw']").send_keys("python")
# driver.find_element_by_css_selector("input.s_ipt").send_keys("python")
# driver.find_element_by_css_selector("form#form>span>input").send_keys("python")
# driver.find_element_by_css_selector("form.fm>span>input").send_keys("python")
driver.find_element_by_css_selector("input[id='kw'][name='wd']").send_keys("python")
driver.find_element_by_id("su").click()
time.sleep(20)
driver.quit()
