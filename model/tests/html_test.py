import unittest

from model.html import Html


class TestCase(unittest.TestCase):
    def test_convert(self):
        converter = Html()

        result1 = converter.convert("&lt;")
        self.assertEquals(2, len(result1))
        self.assertTrue(result1[0].subtitle == "<" or result1[1].subtitle == "<")

        result2 = converter.convert("<")
        self.assertEquals(2, len(result2))
        self.assertTrue(result2[0].subtitle == "&lt;" or result2[1].subtitle == "&lt;")
