# coding=utf-8

from __future__ import unicode_literals

import re
import unittest
from decimal import Decimal

from faker import Faker


class TestEnUS(unittest.TestCase):
    """ Tests geographic locations in the en_US locale """

    def setUp(self):
        self.factory = Faker('en_US')

    def test_location_on_land(self):
        loc = self.factory.location_on_land()
        assert isinstance(loc, tuple)
        assert len(loc) == 5
        assert Decimal(loc[0])  # Should be able to cast first two elements of tuple to Decimal
        assert Decimal(loc[1])
        assert isinstance(loc[2], str)  # Place is a sting
        assert isinstance(loc[3], str)  # Country code is a string
        assert len(loc[3]) == 2  # Country code is two letters
        assert isinstance(loc[4], str)  # Timezone is a string

    def test_location_on_land_coords_only(self):
        loc = self.factory.location_on_land(coords_only=True)
        assert isinstance(loc, tuple)
        assert len(loc) == 2
        assert Decimal(loc[0])  # Should be able to cast first two elements of tuple to Decimal
        assert Decimal(loc[1])


class TestDeAT(unittest.TestCase):
    """ Tests in addresses in the de_AT locale """

    def setUp(self):
        self.factory = Faker('de_AT')

    def test_latitude(self):
        latitude = self.factory.latitude()
        assert re.match(r"4[6-8]\.\d+", str(latitude))

    def test_longitude(self):
        longitude = self.factory.longitude()
        assert re.match(r"1[1-5]\.\d+", str(longitude))
