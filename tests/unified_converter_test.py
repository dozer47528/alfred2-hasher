import unittest

from unified_converter import UnifiedConverter


class TestCase(unittest.TestCase):
    converter = UnifiedConverter()
    converter.convert("ascii 1")

