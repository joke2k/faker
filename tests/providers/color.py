import unittest
from re import search
from faker.providers.color.en_US import Provider as en_provider


class TestColor(unittest.TestCase):
    def test_safe_hex_color(self):
        assert all((search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', en_provider.safe_hex_color())
            for _ in range(1000)))


    def test_hex_color(self):
        assert all((search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', en_provider.hex_color())
            for _ in range(1000)))


    def test_rgb_color(self):
        maxval = 0
        minval = 0

        for _ in range(1000):
            current = list(map(int, en_provider.rgb_color().split(',')))
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
            current = list(map(int, en_provider.rgb_css_color()[4:-1].split(',')))
            if max(current) > maxval:
                maxval = max(current)
            if min(current) > minval:
                minval = min(current) 

        assert maxval <= 255
        assert minval >= 0
