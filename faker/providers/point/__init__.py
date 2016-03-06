localized = False

import random
from .. import BaseProvider


class Provider(BaseProvider):
    """Random coordinate pairs (or triples) within a specified range."""

    @classmethod
    def point_xy(cls, min=0, max=100, step=1,
            min_x=None, max_x=None, step_x=None,
            min_y=None, max_y=None, step_y=None,
        ):
        """
        Get a pair of numbers that represents a point on the XY plane.

        :param min Minimum value for both X and Y. Defaults to 0.
        :param max Maximum value for both X and Y. Defaults to 100.
        :param step Interval between possible values for both X and Y.
            Defaults to 1.
        :param min_x Minimum value for X. Defauls to the `min` value.
        :param max_x Maximum value for X. Defaults to the `max` value.
        :param step_x Step value for X. Defaults to the `step` value.
        :param min_y Minimum value for Y. Defauls to the `min` value.
        :param max_y Maximum value for Y. Defaults to the `max` value.
        :param step_y Step value for Y. Defaults to the `step` value.
        :example (3, 7)
        :return tuple
        """
        if min_x is None:
            min_x = min
        if max_x is None:
            max_x = max
        if step_x is None:
            step_x = step
        if min_y is None:
            min_y = min
        if max_y is None:
            max_y = max
        if step_y is None:
            step_y = step

        x = cls.random_int(min_x, max_x, step_x)
        y = cls.random_int(min_y, max_y, step_y)
        return (x, y)

    @classmethod
    def point_xyz(cls, min=0, max=100, step=1,
            min_x=None, max_x=None, step_x=None,
            min_y=None, max_y=None, step_y=None,
            min_z=None, max_z=None, step_z=None,
        ):
        """
        Get a pair of numbers that represents a point in 3-space.

        :param min Minimum value for X, Y, and Z. Defaults to 0.
        :param max Maximum value for X, Y, and Z. Defaults to 100
        :param step Interval between possible values for X, Y, and Z.
            Defaults to 1.
        :param min_x Minimum value for X. Defauls to the `min` value.
        :param max_x Maximum value for X. Defaults to the `max` value.
        :param step_x Step value for X. Defaults to the `step` value.
        :param min_y Minimum value for Y. Defauls to the `min` value.
        :param max_y Maximum value for Y. Defaults to the `max` value.
        :param step_y Step value for Y. Defaults to the `step` value.
        :param min_z Minimum value for Z. Defauls to the `min` value.
        :param max_z Maximum value for Z. Defaults to the `max` value.
        :param step_z Step value for Z. Defaults to the `step` value.
        :example (3, 7, 10)
        :return tuple
        """
        if min_x is None:
            min_x = min
        if max_x is None:
            max_x = max
        if step_x is None:
            step_x = step
        if min_y is None:
            min_y = min
        if max_y is None:
            max_y = max
        if step_y is None:
            step_y = step
        if min_z is None:
            min_z = min
        if max_z is None:
            max_z = max
        if step_z is None:
            step_z = step

        x = cls.random_int(min_x, max_x, step_x)
        y = cls.random_int(min_y, max_y, step_y)
        z = cls.random_int(min_z, max_z, step_z)
        return (x, y, z)
