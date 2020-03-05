import unittest

from model.base_64 import Base64
from model.date_time import DateTime


class TestCase(unittest.TestCase):
    def test_convert(self):
        converter = DateTime()
        self.assertEquals("1478865600", converter.convert("2016-11-11 12:00")[0].subtitle)
        result = converter.convert("1478865600")
        self.assertTrue("2016-11-11 12:00:00" == result[0].subtitle or "2016-11-11 12:00:00" == result[1].subtitle)
        result = converter.convert("1478865600000")
        self.assertTrue("2016-11-11 12:00:00" == result[0].subtitle or "2016-11-11 12:00:00" == result[1].subtitle)
