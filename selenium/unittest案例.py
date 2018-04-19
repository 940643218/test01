#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class Blog(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("https://home.cnblogs.com/u/lifeng315021/")
    
    def test_blog(self):
        time.sleep(3)
        result=EC.title_is(u"18617093687的主页-博客园")(self.driver)
        print(result)
        self.assertTrue(result)
    
    def tearDown(self):
        self.driver.quit()
        
if __name__=="__main__":
    unittest.main()