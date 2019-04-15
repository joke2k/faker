#  -*- coding: utf-8 -*-

import unittest

from faker import Faker


class TestPyint(unittest.TestCase):
    def setUp(self):
        self.factory = Faker()

    def test_pyint(self):
        self.assertIsInstance(self.factory.pyint(), int)

    def test_pyint_bounds(self):
        self.assertTrue(0 <= self.factory.pyint() <= 9999)

    def test_pyint_step(self):
        random_int = self.factory.pyint(step=2)
        self.assertEqual(0, random_int % 2)

    def test_pyint_bound_0(self):
        self.assertEqual(0, self.factory.pyint(min=0, max=0))

    def test_pyint_bound_positive(self):
        self.assertEqual(5, self.factory.pyint(min=5, max=5))

    def test_pyint_bound_negative(self):
        self.assertEqual(-5, self.factory.pyint(min=-5, max=-5))

    def test_pyint_range(self):
        self.assertTrue(0 <= self.factory.pyint(min=0, max=2) <= 2)


class TestPyfloat(unittest.TestCase):
    def setUp(self):
        self.factory = Faker()

    def test_pyfloat(self):
        result = self.factory.pyfloat()

        self.assertIsInstance(result, float)

    def test_left_digits(self):
        expected_left_digits = 10

        result = self.factory.pyfloat(left_digits=expected_left_digits)

        left_digits = len(str(abs(int(result))))
        self.assertGreaterEqual(expected_left_digits, left_digits)

    def test_right_digits(self):
        expected_right_digits = 10

        result = self.factory.pyfloat(right_digits=expected_right_digits)

        right_digits = len(str(result).split('.')[1])
        self.assertGreaterEqual(expected_right_digits, right_digits)

    def test_positive(self):
        result = self.factory.pyfloat(positive=True)

        self.assertGreaterEqual(result, 0)
        self.assertEqual(result, abs(result))

    def test_min_value(self):
        min_values = (0, 10, -1000, 1000, 999999)

        for min_value in min_values:
            result = self.factory.pyfloat(min_value=min_value)
            self.assertGreaterEqual(result, min_value)

    def test_max_value(self):
        max_values = (0, 10, -1000, 1000, 999999)

        for max_value in max_values:
            result = self.factory.pyfloat(max_value=max_value)
            self.assertLessEqual(result, max_value)

    def test_max_value_should_be_greater_than_min_value(self):
        """
        An exception should be raised if min_value is greater than max_value
        """
        expected_message = 'Min value cannot be greater than max value'
        with self.assertRaises(ValueError) as raises:
            self.factory.pyfloat(min_value=100, max_value=0)

        message = str(raises.exception)
        self.assertEqual(message, expected_message)
