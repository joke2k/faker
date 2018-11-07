# coding=utf-8

from __future__ import unicode_literals

import re
import unittest

from faker import Faker


class TestDeAT(unittest.TestCase):
    """ Tests in addresses in the de_AT locale """

    def setUp(self):
        self.factory = Faker('de_AT')

    def test_latitude(self):
        latitude = self.factory.latitude()
        assert re.match(r"4[5-8]\.\d+", str(latitude))

    def test_longitude(self):
        longitude = self.factory.longitude()
        assert re.match(r"-1[5-8][0-9].\d+", str(longitude))
