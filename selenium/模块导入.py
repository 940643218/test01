#coding:utf-8
from selenium import webdriver
import unittest
from login_pub import Login_Blog
login_url="https://passport.cnblogs.com/user/signin"
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get(login_url)
    def tearDown(self):
        self.driver.quit()
    def test_login(self):
        Login_Blog(self.driver).login("18617093687","1qw2!QW@")
if __name__=="__main__":
    unittest.main()