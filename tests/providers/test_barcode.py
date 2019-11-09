# coding=utf-8

from __future__ import unicode_literals

import re
import unittest

from faker import Faker


class TestBarcodeProvider(unittest.TestCase):
    """ Tests barcode provider """

    num_sample_runs = 1000

    def setUp(self):
        self.ean8_pattern = re.compile(r'^\d{8}$')
        self.ean13_pattern = re.compile(r'^\d{13}$')
        self.factory = Faker()

    def test_ean(self):
        for _ in range(self.num_sample_runs):
            ean8 = self.factory.ean(8)
            ean13 = self.factory.ean(13)
            assert self.ean8_pattern.match(ean8)
            assert self.ean13_pattern.match(ean13)

            ean8_digits = [int(digit) for digit in ean8]
            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean8_digits) + 2 * sum(ean8_digits[::2])) % 10 == 0
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

    def test_ean8(self):
        for _ in range(self.num_sample_runs):
            ean8 = self.factory.ean8()
            assert self.ean8_pattern.match(ean8)

            # Included check digit must be correct
            ean8_digits = [int(digit) for digit in ean8]
            assert (sum(ean8_digits) + 2 * sum(ean8_digits[::2])) % 10 == 0

    def test_ean13(self):
        for _ in range(self.num_sample_runs):
            ean13 = self.factory.ean13()
            assert self.ean13_pattern.match(ean13)

            # Included check digit must be correct
            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

    def test_ean13_no_leading_zero(self):
        for _ in range(1000):
            ean13 = self.factory.ean13(no_leading_zero=True)
            assert self.ean13_pattern.match(ean13)
            assert ean13[0] != '0'

            # Included check digit must be correct
            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

    def test_ean13_force_leading_zero(self):
        for _ in range(1000):
            ean13 = self.factory.ean13(force_leading_zero=True)
            assert self.ean13_pattern.match(ean13)
            assert ean13[0] == '0'

            # Included check digit must be correct
            ean13_digits = [int(digit) for digit in ean13]
            assert (sum(ean13_digits) + 2 * sum(ean13_digits[1::2])) % 10 == 0

    def test_ean13_bad_arguments(self):
        with self.assertRaises(AssertionError):
            self.factory.ean13(no_leading_zero=True, force_leading_zero=True)
