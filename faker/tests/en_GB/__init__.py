# coding=utf-8

from __future__ import unicode_literals

import unittest
import re

from faker import Factory
from ukpostcodeparser.parser import parse_uk_postcode


class en_GB_FactoryTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = Factory.create('en_GB')

    def test_en_GB_postcode(self):
        from faker.providers.address.en_GB import Provider
        for i in range(100):
            assert isinstance(parse_uk_postcode(self.factory.postcode()), tuple)
