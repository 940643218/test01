from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get("file:///D:/table.html")
t=driver.find_element_by_xpath("//table[@id='myTable']/tbody/tr[2]/td[1]")
print(t.text)