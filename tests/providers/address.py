# coding=utf-8

from __future__ import unicode_literals

import unittest

from faker import Factory
from ukpostcodeparser.parser import parse_uk_postcode
from faker.providers.address.hu_HU import Provider as HuProvider


class TestEnGB(unittest.TestCase):
    """ Tests addresses in the en_GB locale """

    def setUp(self):
        self.factory = Factory.create('en_GB')

    def test_postcode(self):
        for i in range(100):
            assert isinstance(parse_uk_postcode(self.factory.postcode()), tuple)


class TestHuHU(unittest.TestCase):
    """ Tests addresses in the hu_HU locale """

    def test_postcode_first_digit(self):
        # Hungarian postcodes begin with 'H-' followed by 4 digits.
        # The first digit may not begin with a zero.
        for i in range(100):
            pcd = HuProvider.postcode()
            assert pcd[2] > "0"
