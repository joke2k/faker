import unittest
from re import search
from faker import Faker

from faker.providers.color.hy_AM import Provider as HyAmProvider
from six import string_types


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


class TestHyAM(unittest.TestCase):
    """ Tests colors in the hy_AM locale """

    def setUp(self):
        self.factory = Faker('hy_AM')

    def test_color_name(self):
        color_name = self.factory.color_name()
        assert isinstance(color_name, string_types)
        assert color_name in HyAmProvider.all_colors.keys()

    def test_safe_color_name(self):
        safe_color_name = self.factory.safe_color_name()
        assert isinstance(safe_color_name, string_types)
        assert safe_color_name in HyAmProvider.safe_colors
