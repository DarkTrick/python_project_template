import unittest

from my_package.myclass import MyMainClass

class MyTests(unittest.TestCase):
  def test_nothing(self):
    print (MyMainClass().run())
    pass