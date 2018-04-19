#coding:utf-8
from selenium import webdriver
driver=webdriver.Firefox()
driver.get("https://www.baidu.com")
print(driver.name)
"回到顶部"
def scroll_top():
    if driver.name=="chrome":
        js="var q=document.body.scrollTop=0"
    else:
        js="var q=document.documentElement.scrollTop=0"
    return driver.execute_script(js)
"拉到底部"
def scroll_foot():
    if driver.name=="chome":
        js="var q=document.body.scrollTop=10000"
    else:
        js="var q=document.documentElement.scrollTop=10000"
        return driver.execute_script(js)
"滚动到底部"
js="window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js)
"滚动到顶部"
js="window.scrollTo(0,0)"
driver.execute_script(js)
"聚焦元素"
target=driver.find_element_by_id("kw")
driver.execute_script("arguments[0].scrollIntoView();",target)

        