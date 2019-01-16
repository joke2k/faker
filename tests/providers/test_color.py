import unittest
from re import search
from faker import Faker


class TestColor(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('en_US')

    def test_safe_hex_color(self):
        assert all((search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', self.factory.safe_hex_color()) for _ in range(1000)))

    def test_hex_color(self):
        assert all((search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', self.factory.hex_color()) for _ in range(1000)))

    def test_rgb_color(self):
        maxval = 0
        minval = 0

        for _ in range(1000):
            current = list(map(int, self.factory.rgb_color().split(',')))
            if max(current) > maxval:
                maxval = max(current)
            if min(current) > minval:
                minval = min(current)

        assert maxval <= 255
        assert minval >= 0

    def test_rgb_css_color(self):
        maxval = 0
        minval = 0

        for _ in range(1000):
            current = list(map(int, self.factory.rgb_css_color()[4:-1].split(',')))
            if max(current) > maxval:
                maxval = max(current)
            if min(current) > minval:
                minval = min(current)

        assert maxval <= 255
        assert minval >= 0
