# coding=utf-8

from __future__ import unicode_literals

import unittest
import re

from faker import Factory
from ukpostcodeparser.parser import parse_uk_postcode


class TestEnGB(unittest.TestCase):
    """ Tests postcodes in the en_GB locale """

    def setUp(self):
        self.factory = Factory.create('en_GB')

    def test_en_gb_postcode(self):
        for i in range(100):
            assert isinstance(parse_uk_postcode(self.factory.postcode()), tuple)
