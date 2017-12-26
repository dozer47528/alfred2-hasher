import unittest

from model.the_uuid import TheUUID


class TestCase(unittest.TestCase):
    def test_convert(self):
        converter = TheUUID()

        result1 = converter.convert("6f125fd5-f338-4d2f-95e5-1fb61260e9cb")
        self.assertEquals(2, len(result1))
        self.assertTrue(result1[0].subtitle == "6f125fd5f3384d2f95e51fb61260e9cb" or result1[1].subtitle == "6f125fd5f3384d2f95e51fb61260e9cb")
        self.assertTrue(result1[0].subtitle == "0x6f125fd5f3384d2f95e51fb61260e9cb" or result1[1].subtitle == "0x6f125fd5f3384d2f95e51fb61260e9cb")

        result2 = converter.convert("6f125fd5f3384d2f95e51fb61260e9cb")
        self.assertEquals(2, len(result2))
        self.assertTrue(result2[0].subtitle == "6f125fd5-f338-4d2f-95e5-1fb61260e9cb" or result2[1].subtitle == "6f125fd5-f338-4d2f-95e5-1fb61260e9cb")
        self.assertTrue(result2[0].subtitle == "0x6f125fd5f3384d2f95e51fb61260e9cb" or result2[1].subtitle == "0x6f125fd5f3384d2f95e51fb61260e9cb")

        result3 = converter.convert("0x6f125fd5f3384d2f95e51fb61260e9cb")
        self.assertEquals(2, len(result3))
        self.assertTrue(result3[0].subtitle == "6f125fd5-f338-4d2f-95e5-1fb61260e9cb" or result3[1].subtitle == "6f125fd5-f338-4d2f-95e5-1fb61260e9cb")
        self.assertTrue(result3[0].subtitle == "6f125fd5f3384d2f95e51fb61260e9cb" or result3[1].subtitle == "6f125fd5f3384d2f95e51fb61260e9cb")
