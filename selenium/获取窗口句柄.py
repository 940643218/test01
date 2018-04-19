#encoding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("http://sz.ganji.com/")
driver.implicitly_wait(30)
h=driver.current_window_handle
print(h)
driver.find_element_by_link_text("深圳招聘").click()
all_h=driver.window_handles
print(all_h)
# for i in all_h:
#     if i != h:
#         driver.switch_to_window(i)
#         print(driver.title)
driver.switch_to_window(all_h[1])
print(driver.title)
time.sleep(5)
driver.close()
driver.switch_to.window(h)
print(driver.title)
time.sleep(10)
driver.quit()