
# import testclass
# class Foo(unittest.TestCase):
#     # ִ��ÿ��������������֮ǰ����ִ��setUp,��ʼ��ִ�л���
#     def setUp(self):
#         # print "setUp..."
#         self.m = testclass.Maths()
# 
#     def test_add(self):
#         m = self.m
#         ret = m.add(3, 5)
#         self.assertEqual(ret, 8, "3 + 5 != 8")
# 
#     def test_sub(self):
#         m = self.m
#         ret = m.sub(3, 5)
#         self.assertEqual(ret, -2, "3 - 5 != -2")

#     def test_mul(self):
#         m = self.m
#         ret = m.mul(3, 5)
#         self.assertEqual(ret, 15, "3 * 5 != 15")
# 
#     # ִ����ÿ����������������,��ִ��tearDown����,����ִ�л���
#     def tearDown(self):
#         del self.m
# 
# if __name__ == '__main__':
#     # unittest.main()
#     # ���������׼�
#     ts = unittest.TestSuite()
# 
#     # �Ѳ���������ӵ������׼�
#     ts.addTest(Foo('test_add'))
#     ts.addTest(Foo('test_mul'))
# 
#     # ��������ִ�в����׼��Ķ���
#     runner = unittest.TextTestRunner()
#     # ִ�в����׼�
#     # runner.run(ts)
#     runner.run(Foo("test_add"))
