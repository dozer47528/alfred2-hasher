import unittest

from model.ascii import ASCII


class TestCase(unittest.TestCase):
    def test_number_range(self):
        converter = ASCII()
        self.assertEquals(0, len(converter.convert("31")))
        self.assertEquals(1, len(converter.convert("32")))
        self.assertEquals(1, len(converter.convert("126")))
        self.assertEquals(0, len(converter.convert("127")))

    def test_char_to_number(self):
        converter = ASCII()
        self.assertEquals('97', converter.convert("a")[0].subtitle)

    def test_number_to_char(self):
        converter = ASCII()
        self.assertEquals('a', converter.convert("97")[0].subtitle)
