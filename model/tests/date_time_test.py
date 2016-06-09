import unittest

from model.base_64 import Base64
from model.date_time import DateTime


class TestCase(unittest.TestCase):
    def test_convert(self):
        converter = DateTime()
        self.assertEquals("1478865600", converter.convert("2016-11-11 12:00")[0].subtitle)
