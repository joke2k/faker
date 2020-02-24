"""
Code adapted from:
- https://github.com/davidmerfield/randomColor  (CC0)
- https://github.com/kevinwuhoo/randomcolor-py  (MIT License)

Additional reference from:
- https://en.wikipedia.org/wiki/HSL_and_HSV
"""

import colorsys
import math
import random
import sys

COLOR_MAP = {
    'monochrome': {
        'hue_range': [0, 0],
        'lower_bounds': [
            [0, 0], [100, 0],
        ],
    },
    'red': {
        'hue_range': [-26, 18],
        'lower_bounds': [
            [20, 100], [30, 92], [40, 89],
            [50, 85], [60, 78], [70, 70],
            [80, 60], [90, 55], [100, 50],
        ],
    },
    'orange': {
        'hue_range': [19, 46],
        'lower_bounds': [
            [20, 100], [30, 93], [40, 88], [50, 86],
            [60, 85], [70, 70], [100, 70],
        ],
    },
    'yellow': {
        'hue_range': [47, 62],
        'lower_bounds': [
            [25, 100], [40, 94], [50, 89], [60, 86],
            [70, 84], [80, 82], [90, 80], [100, 75],
        ],
    },
    'green': {
        'hue_range': [63, 178],
        'lower_bounds': [
            [30, 100], [40, 90], [50, 85], [60, 81],
            [70, 74], [80, 64], [90, 50], [100, 40],
        ],
    },
    'blue': {
        'hue_range': [179, 257],
        'lower_bounds': [
            [20, 100], [30, 86], [40, 80],
            [50, 74], [60, 60], [70, 52],
            [80, 44], [90, 39], [100, 35],
        ],
    },
    'purple': {
        'hue_range': [258, 282],
        'lower_bounds': [
            [20, 100], [30, 87], [40, 79],
            [50, 70], [60, 65], [70, 59],
            [80, 52], [90, 45], [100, 42],
        ],
    },
    'pink': {
        'hue_range': [283, 334],
        'lower_bounds': [
            [20, 100], [30, 90], [40, 86], [60, 84],
            [80, 80], [90, 75], [100, 73],
        ],
    },
}


class RandomColor:

    def __init__(self, generator=None, seed=None):
        self.colormap = COLOR_MAP

        # Option to specify a seed was not removed so this class
        # can still be tested independently w/o generators
        if generator:
            self.random = generator.random
        else:
            self.seed = seed if seed else random.randint(0, sys.maxsize)
            self.random = random.Random(self.seed)

        for color_name, color_attrs in self.colormap.items():
            lower_bounds = color_attrs['lower_bounds']
            s_min = lower_bounds[0][0]
            s_max = lower_bounds[-1][0]

            b_min = lower_bounds[-1][1]
            b_max = lower_bounds[0][1]

            self.colormap[color_name]['saturation_range'] = [s_min, s_max]
            self.colormap[color_name]['brightness_range'] = [b_min, b_max]

    def generate(self, hue=None, luminosity=None, color_format='hex'):
        # First we pick a hue (H)
        h = self.pick_hue(hue)

        # Then use H to determine saturation (S)
        s = self.pick_saturation(h, hue, luminosity)

        # Then use S and H to determine brightness (B).
        b = self.pick_brightness(h, s, luminosity)

        # Then we return the HSB color in the desired format
        return self.set_format([h, s, b], color_format)

    def pick_hue(self, hue):
        hue_range = self.get_hue_range(hue)
        hue = self.random_within(hue_range)

        # Instead of storing red as two separate ranges,
        # we group them, using negative numbers
        if hue < 0:
            hue += 360

        return hue

    def pick_saturation(self, hue, hue_name, luminosity):
        if luminosity == 'random':
            return self.random_within([0, 100])

        if hue_name == 'monochrome':
            return 0

        saturation_range = self.get_saturation_range(hue)

        s_min = saturation_range[0]
        s_max = saturation_range[1]

        if luminosity == 'bright':
            s_min = 55
        elif luminosity == 'dark':
            s_min = s_max - 10
        elif luminosity == 'light':
            s_max = 55

        return self.random_within([s_min, s_max])

    def pick_brightness(self, h, s, luminosity):
        b_min = self.get_minimum_brightness(h, s)
        b_max = 100

        if luminosity == 'dark':
            b_max = b_min + 20
        elif luminosity == 'light':
            b_min = (b_max + b_min) / 2
        elif luminosity == 'random':
            b_min = 0
            b_max = 100

        return self.random_within([b_min, b_max])

    def set_format(self, hsv, color_format):
        if color_format == 'hsv':
            color = 'hsv({}, {}, {})'.format(*hsv)

        elif color_format == 'hsl':
            hsl = self.hsv_to_hsl(hsv)
            color = 'hsl({}, {}, {})'.format(*hsl)

        elif color_format == 'rgb':
            rgb = self.hsv_to_rgb(hsv)
            color = 'rgb({}, {}, {})'.format(*rgb)

        else:
            rgb = self.hsv_to_rgb(hsv)
            color = '#{:02x}{:02x}{:02x}'.format(*rgb)

        return color

    def get_minimum_brightness(self, h, s):
        lower_bounds = self.get_color_info(h)['lower_bounds']

        for i in range(len(lower_bounds) - 1):
            s1 = lower_bounds[i][0]
            v1 = lower_bounds[i][1]

            s2 = lower_bounds[i + 1][0]
            v2 = lower_bounds[i + 1][1]

            if s1 <= s <= s2:
                m = (v2 - v1) / (s2 - s1)
                b = v1 - m * s1

                return m * s + b

        return 0

    def get_hue_range(self, color_input):
        if isinstance(color_input, (int, float)) and 0 <= color_input <= 360:
            color_input = int(color_input)
            return [color_input, color_input]

        elif isinstance(color_input, str) and color_input in self.colormap:
            return self.colormap[color_input]['hue_range']

        elif color_input is None:
            return [0, 360]

        try:
            v1, v2 = color_input
            v1 = int(v1)
            v2 = int(v2)
        except (ValueError, TypeError):
            msg = 'Hue must be a valid string, numeric type, or a tuple/list of 2 numeric types.'
            raise TypeError(msg)
        else:
            if v2 < v1:
                v1, v2 = v2, v1
            if v1 < 0:
                v1 = 0
            if v2 > 360:
                v2 = 360
            return [v1, v2]

    def get_saturation_range(self, hue):
        return self.get_color_info(hue)['saturation_range']

    def get_color_info(self, hue):
        # Maps red colors to make picking hue easier
        if 334 <= hue <= 360:
            hue -= 360

        for color_name, color in self.colormap.items():
            if color['hue_range'][0] <= hue <= color['hue_range'][1]:
                return self.colormap[color_name]
        else:
            raise ValueError('Value of hue `%s` is invalid.' % hue)

    def random_within(self, r):
        return self.random.randint(int(r[0]), int(r[1]))

    @classmethod
    def hsv_to_rgb(cls, hsv):
        """
        Converts HSV to RGB

        :param hsv: 3-tuple of h, s, and v values
        :return: 3-tuple of r, g, and b values
        """
        h, s, v = hsv
        h = 1 if h == 0 else h
        h = 359 if h == 360 else h

        h = float(h)/360
        s = float(s)/100
        v = float(v)/100

        rgb = colorsys.hsv_to_rgb(h, s, v)
        return (int(c * 255) for c in rgb)

    @classmethod
    def hsv_to_hsl(cls, hsv):
        """
        Converts HSV to HSL

        :param hsv: 3-tuple of h, s, and v values
        :return: 3-tuple of h, s, and l values
        """
        h, s, v = hsv

        s = float(s)/100
        v = float(v)/100
        l = 0.5 * v * (2 - s)   # noqa: E741

        if l in [0, 1]:
            s = 0
        else:
            s = v * s / (1 - math.fabs(2 * l - 1))
        return (int(c) for c in [h, s * 100, l * 100])
