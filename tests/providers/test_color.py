import copy
import random
import re

import pytest

from faker.providers.color import RandomColor
from faker.providers.color.es_ES import Provider as EsEsColorProvider
from faker.providers.color.fa_IR import Provider as FaIrColorProvider
from faker.providers.color.he_IL import Provider as HeILColorProvider
from faker.providers.color.hy_AM import Provider as HyAmColorProvider
from faker.providers.color.sk_SK import Provider as SkSkColorProvider


class TestColorProvider:
    """Test color provider methods"""
    num_samples = 10000

    def test_safe_hex_color(self, faker, num_samples):
        assert all(
            re.fullmatch(r'#(?:([0-9a-f])\1){3}', faker.safe_hex_color())
            for _ in range(num_samples)
        )

    def test_hex_color(self, faker, num_samples):
        assert all(
            re.fullmatch(r'#[0-9a-f]{6}', faker.hex_color())
            for _ in range(num_samples)
        )

    def test_rgb_color(self, faker, num_samples):
        for _ in range(num_samples):
            r, g, b = list(map(int, faker.rgb_color().split(',')))
            assert 0 <= r <= 255
            assert 0 <= g <= 255
            assert 0 <= b <= 255

    def test_rgb_css_color(self, faker, num_samples):
        pattern = re.compile(r'rgb\((?P<rgb>\d{1,3},\d{1,3},\d{1,3})\)')
        for _ in range(num_samples):
            match = pattern.fullmatch(faker.rgb_css_color())
            rgb = match.group('rgb')
            r, g, b = list(map(int, rgb.split(',')))
            assert 0 <= r <= 255
            assert 0 <= g <= 255
            assert 0 <= b <= 255

    def test_color(self, faker, num_samples):
        baseline_random_color = RandomColor(seed=4761)
        expected = [baseline_random_color.generate() for _ in range(num_samples)]

        # The `color` provider method should behave like the `generate`
        # method of a standalone RandomColor instance for a given seed
        faker.seed_instance(4761)
        colors = [faker.color() for _ in range(num_samples)]
        assert colors == expected


class TestRandomColor:
    """Test RandomColor class"""
    num_samples = 1000
    seed = 4761
    hsv_color_pattern = re.compile(
        r'hsv\('
        r'(?P<h>\d|[1-9]\d|[1-3]\d{2}), '
        r'(?P<s>\d|[1-9]\d|100), '
        r'(?P<v>\d|[1-9]\d|100)\)',
    )
    hsl_color_pattern = re.compile(
        r'hsl\('
        r'(?P<h>\d|[1-9]\d|[1-3]\d{2}), '
        r'(?P<s>\d|[1-9]\d|[1-3]\d{2}), '
        r'(?P<l>\d|[1-9]\d|[1-3]\d{2})\)',
    )
    rgb_color_pattern = re.compile(
        r'rgb\('
        r'(?P<r>\d|[1-9]\d|[1-3]\d{2}), '
        r'(?P<g>\d|[1-9]\d|[1-3]\d{2}), '
        r'(?P<b>\d|[1-9]\d|[1-3]\d{2})\)',
    )
    hex_color_pattern = re.compile(r'#[0-9a-f]{6}')

    def setup_method(self):
        self.random_color = RandomColor(seed=self.seed)

    def test_color_format_hsv(self, num_samples):
        for _ in range(num_samples):
            hsv_color = self.random_color.generate(color_format='hsv')
            match = self.hsv_color_pattern.fullmatch(hsv_color)
            assert match
            groupdict = match.groupdict()
            assert 0 <= int(groupdict['h']) <= 360
            assert 0 <= int(groupdict['s']) <= 100
            assert 0 <= int(groupdict['v']) <= 100

    def test_color_format_hsl(self, num_samples):
        for _ in range(num_samples):
            hsl_color = self.random_color.generate(color_format='hsl')
            match = self.hsl_color_pattern.fullmatch(hsl_color)
            assert match
            groupdict = match.groupdict()
            assert 0 <= int(groupdict['h']) <= 360
            assert 0 <= int(groupdict['s']) <= 100
            assert 0 <= int(groupdict['l']) <= 100

    def test_color_format_rgb(self, num_samples):
        for _ in range(num_samples):
            rgb_color = self.random_color.generate(color_format='rgb')
            match = self.rgb_color_pattern.fullmatch(rgb_color)
            assert match
            groupdict = match.groupdict()
            assert 0 <= int(groupdict['r']) <= 255
            assert 0 <= int(groupdict['g']) <= 255
            assert 0 <= int(groupdict['b']) <= 255

    def test_color_format_hex(self, num_samples):
        for _ in range(num_samples):
            hex_color = self.random_color.generate(color_format='hex')
            assert self.hex_color_pattern.fullmatch(hex_color)

    def test_color_format_unspecified(self, num_samples):
        for _ in range(num_samples):
            color = self.random_color.generate()
            assert self.hex_color_pattern.fullmatch(color)

    def test_hue_integer(self):
        # HSV format is used, because whatever hue value supplied must be present in the output
        for hue in range(360):
            colors = [self.random_color.generate(hue=hue, color_format='hsv') for _ in range(10)]
            for color in colors:
                match = self.hsv_color_pattern.fullmatch(color)
                assert match
                groupdict = match.groupdict()
                assert int(groupdict['h']) == hue

    def test_hue_float(self, num_samples):
        baseline_random_color = RandomColor(seed=self.seed)
        for _ in range(num_samples):
            hue_float = random.uniform(0, 360)
            hue_int = int(hue_float)
            expected = [baseline_random_color.generate(hue=hue_int) for _ in range(10)]

            # Using a float value between 0 and 360 should yield the same results
            # as using an integer rounded down from that float value for a given seed
            colors = [self.random_color.generate(hue=hue_float) for _ in range(10)]
            assert colors == expected

    def test_hue_word(self):
        expected = ['#cecece', '#ededed', '#efefef', '#bcbcbc', '#777777']
        colors = [self.random_color.generate(hue='monochrome') for _ in range(5)]
        assert colors == expected

        expected = ['#ef0b31', '#f2b7ab', '#f74c55', '#a53822', '#8e3712']
        colors = [self.random_color.generate(hue='red') for _ in range(5)]
        assert colors == expected

        expected = ['#f98313', '#ddb77e', '#f9c413', '#f4ce81', '#ddae71']
        colors = [self.random_color.generate(hue='orange') for _ in range(5)]
        assert colors == expected

        expected = ['#dbe04e', '#efc621', '#fff65b', '#ceaf27', '#fcf9ae']
        colors = [self.random_color.generate(hue='yellow') for _ in range(5)]
        assert colors == expected

        expected = ['#05876f', '#57e095', '#50ceaa', '#e4f7a0', '#698909']
        colors = [self.random_color.generate(hue='green') for _ in range(5)]
        assert colors == expected

        expected = ['#2b839b', '#a4d3e8', '#3d2caa', '#3859a0', '#52349e']
        colors = [self.random_color.generate(hue='blue') for _ in range(5)]
        assert colors == expected

        expected = ['#a074e8', '#6122bf', '#9f76cc', '#250570', '#3c1599']
        colors = [self.random_color.generate(hue='purple') for _ in range(5)]
        assert colors == expected

        expected = ['#c605c6', '#fcc4ec', '#d979f7', '#ce108c', '#d3289d']
        colors = [self.random_color.generate(hue='pink') for _ in range(5)]
        assert colors == expected

    def test_hue_tuple_beyond_limits(self, num_samples):
        baseline_random_color = RandomColor(seed=self.seed)
        expected = [baseline_random_color.generate(hue=[0, 360]) for _ in range(num_samples)]

        # Using a tuple with values not between 0 and 360 should yield the same results
        # as using a tuple with clamped values for a given seed
        colors = [self.random_color.generate(hue=[-100, 4500]) for _ in range(num_samples)]
        assert colors == expected

    def test_hue_tuple_inverted_values(self, num_samples):
        baseline_random_color = RandomColor(seed=self.seed)
        expected = [baseline_random_color.generate(hue=[45, 75]) for _ in range(num_samples)]

        # Using a tuple with inverted values should yield the same results
        # as using the correctly ordered tuple for a given seed
        colors = [self.random_color.generate(hue=[75, 45]) for _ in range(num_samples)]
        assert colors == expected

    def test_hue_invalid(self):
        invalid_values = [
            -0.000000001,       # Very slightly under the min numerical value of 0
            360.000000001,      # Very slightly over the max numerical value of 360
            'invalid value',    # Unsupported string
            [1, 2, 3],          # List with incorrect number of elements of valid data types
            ['ab', 1],          # List with correct number of elements with invalid data types
            self,               # Any other garbage
        ]

        for invalid_value in invalid_values:
            with pytest.raises(TypeError):
                self.random_color.generate(hue=invalid_value)

    def test_luminosity_word(self):
        expected = ['#2b7700', '#073c8c', '#d813aa', '#01961a', '#ce840e']
        colors = [self.random_color.generate(luminosity='dark') for _ in range(5)]
        assert colors == expected

        expected = ['#16b5ff', '#6266ef', '#fc4e3f', '#b2ff70', '#a30424']
        colors = [self.random_color.generate(luminosity='bright') for _ in range(5)]
        assert colors == expected

        expected = ['#f276a1', '#fcec94', '#aaffe5', '#ffbd7f', '#98f9dc']
        colors = [self.random_color.generate(luminosity='light') for _ in range(5)]
        assert colors == expected

        expected = ['#070603', '#99a2a3', '#10a85c', '#3f4f0c', '#004f1c']
        colors = [self.random_color.generate(luminosity='random') for _ in range(5)]
        assert colors == expected

    def test_luminosity_invalid(self, num_samples):
        baseline_random_color = RandomColor(seed=self.seed)
        expected = [baseline_random_color.generate() for _ in range(num_samples)]

        colors = [self.random_color.generate(luminosity='invalid_value') for _ in range(num_samples)]
        assert colors == expected

    def test_bad_color_map(self):
        # Initial baseline using 62 as hue value
        self.random_color.generate(hue=62)

        # If we remove 62 from the yellow range, calling the previous function should fail
        colormap = copy.deepcopy(self.random_color.colormap)
        colormap['yellow']['hue_range'] = [47, 61]
        self.random_color.colormap = colormap
        with pytest.raises(ValueError):
            self.random_color.generate(hue=62)


class TestHyAm:
    """Test hy_AM color provider methods"""

    def test_color_name(self, faker, num_samples):
        for _ in range(num_samples):
            color_name = faker.color_name()
            assert isinstance(color_name, str)
            assert color_name in HyAmColorProvider.all_colors.keys()

    def test_safe_color_name(self, faker, num_samples):
        for _ in range(num_samples):
            safe_color_name = faker.safe_color_name()
            assert isinstance(safe_color_name, str)
            assert safe_color_name in HyAmColorProvider.safe_colors


class TestFaIr:
    """Test fa_IR color provider methods"""

    def test_color_name(self, faker, num_samples):
        for _ in range(num_samples):
            color_name = faker.color_name()
            assert isinstance(color_name, str)
            assert color_name in FaIrColorProvider.all_colors.keys()

    def test_safe_color_name(self, faker, num_samples):
        for _ in range(num_samples):
            safe_color_name = faker.safe_color_name()
            assert isinstance(safe_color_name, str)
            assert safe_color_name in FaIrColorProvider.safe_colors


class TestEsEs:
    """Test es_ES color provider methods"""

    def test_color_name(self, faker, num_samples):
        for _ in range(num_samples):
            color_name = faker.color_name()
            assert isinstance(color_name, str)
            assert color_name in EsEsColorProvider.all_colors.keys()

    def test_safe_color_name(self, faker, num_samples):
        for _ in range(num_samples):
            safe_color_name = faker.safe_color_name()
            assert isinstance(safe_color_name, str)
            assert safe_color_name in EsEsColorProvider.safe_colors


class TestSkSk:
    """Test sk_SK color provider methods"""

    def test_safe_color_name(self, faker, num_samples):
        for _ in range(num_samples):
            safe_color_name = faker.safe_color_name()
            assert isinstance(safe_color_name, str)
            assert safe_color_name in SkSkColorProvider.safe_colors


class TestHeIl:
    """Test he_IL color provider methods"""

    def test_color_name(self, faker, num_samples):
        for _ in range(num_samples):
            color_name = faker.color_name()
            assert isinstance(color_name, str)
            assert color_name in HeILColorProvider.all_colors.keys()

    def test_safe_color_name(self, faker, num_samples):
        for _ in range(num_samples):
            safe_color_name = faker.safe_color_name()
            assert isinstance(safe_color_name, str)
            assert safe_color_name in HeILColorProvider.safe_colors
