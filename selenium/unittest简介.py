#coding:utf-8
import unittest
class Test(unittest.TestCase):
    def testMinus(self):
        u'''这里是测试减法'''
        result=6-5
        hope=1
        self.assertEqual(result,hope)
    
    def testDivide(self):
        u'''这里是测试除法'''
        result = 7/ 2
        hope=3.5
        self.assertEqual(result, hope)

if __name__=='__main__':
    unittest.main()
    