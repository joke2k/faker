# coding=utf-8

from __future__ import unicode_literals

import re
import unittest
from decimal import Decimal

from faker import Faker


class TestGlobal(unittest.TestCase):
    """ Tests geographic locations regardless of locale"""

    def setUp(self):
        self.factory = Faker()  # No locale specified, gets global for this provider

    def test_local_latlng(self):
        loc = self.factory.local_latlng(country_code='US')
        assert isinstance(loc, tuple)
        assert len(loc) == 5
        assert Decimal(loc[0])
        assert Decimal(loc[1])

        loc_short = self.factory.local_latlng(country_code='US', coords_only=True)
        assert len(loc_short) == 2
        assert Decimal(loc_short[0])
        assert Decimal(loc_short[1])


class TestEnUS(unittest.TestCase):
    """ Tests geographic locations in the en_US locale """

    def setUp(self):
        self.factory = Faker('en_US')

    def test_latitude(self):
        lat = self.factory.latitude()
        assert isinstance(lat, Decimal)

    def test_longitude(self):
        long = self.factory.longitude()
        assert isinstance(long, Decimal)

    def test_latlng(self):
        loc = self.factory.latlng()
        assert isinstance(loc, tuple)
        assert len(loc) == 2
        assert isinstance(loc[0], Decimal)
        assert isinstance(loc[1], Decimal)

    def test_coordinate(self):
        loc = self.factory.coordinate()
        assert isinstance(loc, Decimal)

    def test_coordinate_centered(self):
        loc = self.factory.coordinate(center=23)
        assert round(loc) == 23

    def test_coordinate_rounded(self):
        loc = self.factory.coordinate(center=23, radius=3)
        assert round(loc) >= 20 <= 26

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

    def test_local_latitude(self):
        local_latitude = self.factory.local_latitude()
        assert re.match(r"4[6-8]\.\d+", str(local_latitude))

    def test_local_longitude(self):
        local_longitude = self.factory.local_longitude()
        assert re.match(r"1[1-5]\.\d+", str(local_longitude))
