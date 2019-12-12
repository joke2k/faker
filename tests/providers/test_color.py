import unittest
import re
from re import search
from faker import Faker

from faker.providers.color import RandomColor
from faker.providers.color.hy_AM import Provider as HyAmProvider
import six
from six import string_types


class TestColor(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('en_US')
        Faker.seed(0)

    def test_safe_hex_color(self):
        assert all((search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', self.fake.safe_hex_color()) for _ in range(1000)))

    def test_hex_color(self):
        assert all((search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', self.fake.hex_color()) for _ in range(1000)))

    def test_rgb_color(self):
        maxval = 0
        minval = 0

        for _ in range(1000):
            current = list(map(int, self.fake.rgb_color().split(',')))
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
            current = list(map(int, self.fake.rgb_css_color()[4:-1].split(',')))
            if max(current) > maxval:
                maxval = max(current)
            if min(current) > minval:
                minval = min(current)

        assert maxval <= 255
        assert minval >= 0

    def test_color(self):
        baseline_random_color = RandomColor(seed=4761)
        expected = [baseline_random_color.generate() for _ in range(10000)]

        # The `color` provider method should behave like the `generate`
        # method of a standalone RandomColor instance for a given seed
        Faker.seed(4761)
        colors = [self.fake.color() for _ in range(10000)]
        assert colors == expected


class TestRandomColor(unittest.TestCase):

    seed = 4761
    hsv_color_pattern = re.compile(
        r'^hsv\('
        r'(?P<h>\d|[1-9]\d|[1-3]\d{2}), '
        r'(?P<s>\d|[1-9]\d|100), '
        r'(?P<v>\d|[1-9]\d|100)\)$',
    )
    hsl_color_pattern = re.compile(
        r'^hsl\('
        r'(?P<h>\d|[1-9]\d|[1-3]\d{2}), '
        r'(?P<s>\d|[1-9]\d|[1-3]\d{2}), '
        r'(?P<l>\d|[1-9]\d|[1-3]\d{2})\)$',
    )
    rgb_color_pattern = re.compile(
        r'^rgb\('
        r'(?P<r>\d|[1-9]\d|[1-3]\d{2}), '
        r'(?P<g>\d|[1-9]\d|[1-3]\d{2}), '
        r'(?P<b>\d|[1-9]\d|[1-3]\d{2})\)$',
    )
    hex_color_pattern = re.compile(r'^#[0-9a-f]{6}$')

    def setUp(self):
        self.random_color = RandomColor(seed=self.seed)

    def test_color_format_hsv(self):
        for _ in range(10000):
            hsv_color = self.random_color.generate(color_format='hsv')
            match = self.hsv_color_pattern.match(hsv_color)
            assert match
            groupdict = match.groupdict()
            assert 0 <= int(groupdict['h']) <= 360
            assert 0 <= int(groupdict['s']) <= 100
            assert 0 <= int(groupdict['v']) <= 100

    def test_color_format_hsl(self):
        for _ in range(10000):
            hsl_color = self.random_color.generate(color_format='hsl')
            match = self.hsl_color_pattern.match(hsl_color)
            assert match
            groupdict = match.groupdict()
            assert 0 <= int(groupdict['h']) <= 360
            assert 0 <= int(groupdict['s']) <= 100
            assert 0 <= int(groupdict['l']) <= 100

    def test_color_format_rgb(self):
        for _ in range(10000):
            rgb_color = self.random_color.generate(color_format='rgb')
            match = self.rgb_color_pattern.match(rgb_color)
            assert match
            groupdict = match.groupdict()
            assert 0 <= int(groupdict['r']) <= 255
            assert 0 <= int(groupdict['g']) <= 255
            assert 0 <= int(groupdict['b']) <= 255

    def test_color_format_hex(self):
        for _ in range(10000):
            hex_color = self.random_color.generate(color_format='hex')
            assert self.hex_color_pattern.match(hex_color)

    def test_color_format_unspecified(self):
        for _ in range(10000):
            color = self.random_color.generate()
            assert self.hex_color_pattern.match(color)

    def test_hue_word(self):
        if six.PY2:
            expected = ['#f2f2f2', '#6b6b6b', '#939393', '#5e5e5e', '#aaaaaa']
        else:
            expected = ['#cecece', '#ededed', '#efefef', '#bcbcbc', '#777777']
        colors = [self.random_color.generate(hue='monochrome') for _ in range(5)]
        assert colors == expected

        if six.PY2:
            expected = ['#c46542', '#d8495f', '#c42c09', '#dd4b68', '#c6135e']
        else:
            expected = ['#ef0b31', '#f2b7ab', '#f74c55', '#a53822', '#8e3712']
        colors = [self.random_color.generate(hue='red') for _ in range(5)]
        assert colors == expected

        if six.PY2:
            expected = ['#fcda9f', '#ffa566', '#b55609', '#c9761e', '#fcd9c7']
        else:
            expected = ['#f98313', '#ddb77e', '#f9c413', '#f4ce81', '#ddae71']
        colors = [self.random_color.generate(hue='orange') for _ in range(5)]
        assert colors == expected

        if six.PY2:
            expected = ['#f2f75b', '#d8cb38', '#efe3a5', '#dbc053', '#eae096']
        else:
            expected = ['#dbe04e', '#efc621', '#fff65b', '#ceaf27', '#fcf9ae']
        colors = [self.random_color.generate(hue='yellow') for _ in range(5)]
        assert colors == expected

        if six.PY2:
            expected = ['#54d387', '#b1d15c', '#c0f78a', '#27b278', '#1bc43a']
        else:
            expected = ['#05876f', '#57e095', '#50ceaa', '#e4f7a0', '#698909']
        colors = [self.random_color.generate(hue='green') for _ in range(5)]
        assert colors == expected

        if six.PY2:
            expected = ['#0b577c', '#7ad3d3', '#4884ce', '#bae8f2', '#79cafc']
        else:
            expected = ['#2b839b', '#a4d3e8', '#3d2caa', '#3859a0', '#52349e']
        colors = [self.random_color.generate(hue='blue') for _ in range(5)]
        assert colors == expected

        if six.PY2:
            expected = ['#d2a7e5', '#a519fc', '#8b0ece', '#b17fe2', '#a949dd']
        else:
            expected = ['#a074e8', '#6122bf', '#9f76cc', '#250570', '#3c1599']
        colors = [self.random_color.generate(hue='purple') for _ in range(5)]
        assert colors == expected

        if six.PY2:
            expected = ['#f453c4', '#db81ac', '#f99fc9', '#e23fff', '#bb68cc']
        else:
            expected = ['#c605c6', '#fcc4ec', '#d979f7', '#ce108c', '#d3289d']
        colors = [self.random_color.generate(hue='pink') for _ in range(5)]
        assert colors == expected

    def test_hue_tuple_beyond_limits(self):
        baseline_random_color = RandomColor(seed=self.seed)
        expected = [baseline_random_color.generate(hue=[0, 360]) for _ in range(1000)]

        # Using a tuple with values not between 0 and 360 should yield the same results
        # as using a tuple with clamped values for a given seed
        colors = [self.random_color.generate(hue=[-100, 4500]) for _ in range(1000)]
        assert colors == expected

    def test_hue_tuple_inverted_values(self):
        baseline_random_color = RandomColor(seed=self.seed)
        expected = [baseline_random_color.generate(hue=[45, 75]) for _ in range(1000)]

        # Using a tuple with inverted values should yield the same results
        # as using the correctly ordered tuple for a given seed
        colors = [self.random_color.generate(hue=[75, 45]) for _ in range(1000)]
        assert colors == expected

    def test_hue_invalid(self):
        invalid_values = [
            'invalid value',    # Unsupported string
            [1, 2, 3],          # List with incorrect number of elements of valid data types
            ['ab', 1],          # List with correct number of elements with invalid data types
            self,               # Any other garbage
        ]

        for invalid_value in invalid_values:
            with self.assertRaises(TypeError):
                self.random_color.generate(hue=invalid_value)

    def test_luminosity_word(self):
        if six.PY2:
            expected = ['#7c000a', '#018748', '#dd8a0d', '#000068', '#7c9308']
        else:
            expected = ['#2b7700', '#073c8c', '#d813aa', '#01961a', '#ce840e']
        colors = [self.random_color.generate(luminosity='dark') for _ in range(5)]
        assert colors == expected

        if six.PY2:
            expected = ['#11f7c9', '#3eafc9', '#6ad4f2', '#125582', '#e55098']
        else:
            expected = ['#16b5ff', '#6266ef', '#fc4e3f', '#b2ff70', '#a30424']
        colors = [self.random_color.generate(luminosity='bright') for _ in range(5)]
        assert colors == expected

        if six.PY2:
            expected = ['#ffafb5', '#fcc1a1', '#b7fcab', '#6df280', '#f599f7']
        else:
            expected = ['#f276a1', '#fcec94', '#aaffe5', '#ffbd7f', '#98f9dc']
        colors = [self.random_color.generate(luminosity='light') for _ in range(5)]
        assert colors == expected

        if six.PY2:
            expected = ['#11140f', '#7f7674', '#262116', '#376d20', '#535e53']
        else:
            expected = ['#070603', '#99a2a3', '#10a85c', '#3f4f0c', '#004f1c']
        colors = [self.random_color.generate(luminosity='random') for _ in range(5)]
        assert colors == expected

    def test_luminosity_invalid(self):
        baseline_random_color = RandomColor(seed=self.seed)
        expected = [baseline_random_color.generate() for _ in range(1000)]

        colors = [self.random_color.generate(luminosity='invalid_value') for _ in range(1000)]
        assert colors == expected


class TestHyAM(unittest.TestCase):
    """ Tests colors in the hy_AM locale """

    def setUp(self):
        self.fake = Faker('hy_AM')
        Faker.seed(0)

    def test_color_name(self):
        color_name = self.fake.color_name()
        assert isinstance(color_name, string_types)
        assert color_name in HyAmProvider.all_colors.keys()

    def test_safe_color_name(self):
        safe_color_name = self.fake.safe_color_name()
        assert isinstance(safe_color_name, string_types)
        assert safe_color_name in HyAmProvider.safe_colors
