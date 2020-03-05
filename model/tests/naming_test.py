import unittest

from model.naming import Naming


class TestCase(unittest.TestCase):
    def test_split_words(self):
        converter = Naming()
        self.assertEquals(["hello", "world"], converter.split_words("hello_world"))
        self.assertEquals(["hello", "world"], converter.split_words("hello-world"))
        self.assertEquals(["hello", "world"], converter.split_words("helloWorld"))
        self.assertEquals(["hello", "world"], converter.split_words("HelloWorld"))
        self.assertEquals(["xml", "converter"], converter.split_words("XMLConverter"))
        self.assertEquals(["converter", "xml"], converter.split_words("ConverterXML"))
        self.assertEquals(["x", "converter"], converter.split_words("XConverter"))

    def test_convert(self):
        converter = Naming()
        self.assertEquals(3, len(converter.convert("hello_world")))
