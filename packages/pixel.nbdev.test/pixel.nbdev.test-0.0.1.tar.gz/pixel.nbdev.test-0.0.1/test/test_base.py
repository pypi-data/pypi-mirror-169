import unittest
from nbdev_1 import foo


class TestQueryHelper(unittest.TestCase):
    def test_1(self):
        self.assertEqual(foo.foo("foo"), "foo bar")
