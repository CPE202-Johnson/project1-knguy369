import unittest
from bears import *

class TestAssign1(unittest.TestCase):
    #determnes is bear function correctly returns True/False
    def test_bear_01(self):
        self.assertTrue(bears(250))

    def test_bear_02(self):
        self.assertTrue(bears(42))
        self.assertTrue(bears(52))
        self.assertTrue(bears(7190))

    def test_bear_03(self):
        self.assertFalse(bears(53))
        self.assertFalse(bears(5208))

    def test_bear_04(self):
        self.assertFalse(bears(41))
        self.assertFalse(bears(708))

    def test_bear_05(self):
        self.assertFalse(bears(99))

    def test_bear_06(self):
        self.assertFalse(bears(-10))

    def test_bear_07(self):
        self.assertFalse(bears(77))





if __name__ == "__main__":
    unittest.main()
