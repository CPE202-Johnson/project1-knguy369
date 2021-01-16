import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):
    #determines if BaseConvert returns correct strings for base 2
    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")
        self.assertEqual(convert(0,2),"0")

    #determines if BaseConvert returns correct strings for base 4
    def test_base4(self):
        self.assertEqual(convert(30,4),"132")
        self.assertEqual(convert(1,4),"1")

    #determines if BaseConvert returns correct strings for base 6
    def test_base6(self):
        self.assertEqual(convert(14,6),"22")

    #determines if BaseConvert returns correct strings for base 16
    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")
        self.assertEqual(convert(1488,16),"5D0")


if __name__ == "__main__":
        unittest.main()
