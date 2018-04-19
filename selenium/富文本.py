#encoding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
profiledir=r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\zf4klf5g.default'
profile= webdriver.FirefoxProfile(profiledir)
driver=webdriver.Firefox(profile)