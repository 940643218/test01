#encoding=utf-8
from selenium import webdriver
profile_directory=r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\zf4klf5g.default'
profile=webdriver.FirefoxProfile(profile_directory)
driver=webdriver.Firefox(profile)