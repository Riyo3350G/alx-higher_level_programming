#!/usr/bin/python3

import unittest

max_integer = __import__("6-max_integer").max_integer

class TestMaxInt(unittest.TestCase):
    def test_list(self):
        l = [1, 3, 6, 12, 5]
        self.assertEqual(max_integer(l), 12)
    def empty_list(self):
        l = []
        self.assertEqual(max_integer(l), None)
    def string_list(self):
        l = ["ab", "ac", "ad"]
        self.assertEqual(max_integer(l), "ad")
    def float_list(self):
        l = [1.5, 6.1, 10.1]
        self.assertEqual(max_integer(l), 10.1)
    def one_element(self):
        l = [10]
        self.assertEqual(max_integer(l), 10)
if __name__ == "__main__":
    unittest.main()
