import unittest

from model.base_64 import Base64


class TestCase(unittest.TestCase):
    def test_convert(self):
        converter = Base64()
        self.assertEquals(1, len(converter.convert("asdsadas")))
        self.assertEquals("YXNkc2FkYXM=", converter.convert("asdsadas")[0].subtitle)

        result2 = converter.convert("YXNkc2FkYXM=")
        self.assertEquals(2, len(result2))
        self.assertTrue(result2[0].subtitle == "asdsadas" or result2[1].subtitle == "asdsadas")
