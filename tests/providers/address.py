# coding=utf-8

from __future__ import unicode_literals

import re
import unittest

from ukpostcodeparser.parser import parse_uk_postcode

from faker import Factory
from faker.providers.address.hu_HU import Provider as HuProvider
from faker.providers.address.ja_JP import Provider as JaProvider
from faker.providers.address.ne_NP import Provider as NeProvider
from .. import string_types


class TestEnGB(unittest.TestCase):
    """ Tests addresses in the en_GB locale """

    def setUp(self):
        self.factory = Factory.create('en_GB')

    def test_postcode(self):
        for i in range(100):
            assert isinstance(parse_uk_postcode(self.factory.postcode()), tuple)


class TestHuHU(unittest.TestCase):
    """ Tests addresses in the hu_HU locale """

    def setUp(self):
        self.factory = Factory.create('hu_HU')

    def test_postcode_first_digit(self):
        # Hungarian postcodes begin with 'H-' followed by 4 digits.
        # The first digit may not begin with a zero.
        for i in range(100):
            pcd = HuProvider.postcode()
            assert pcd[2] > "0"

    def test_street_address(self):
        """ Tests the street address in the hu_HU locale """
        address = self.factory.address()
        assert isinstance(address, string_types)
        address_with_county = self.factory.street_address_with_county()
        assert isinstance(address_with_county, string_types)


class TestJaJP(unittest.TestCase):
    """ Tests addresses in the ja_JP locale """

    def setUp(self):
        self.factory = Factory.create('ja')

    def test_address(self):
        """ Test"""
        country = self.factory.country()
        assert isinstance(country, string_types)
        assert country in JaProvider.countries

        prefecture = self.factory.prefecture()
        assert isinstance(prefecture, string_types)
        assert prefecture in JaProvider.prefectures

        city = self.factory.city()
        assert isinstance(city, string_types)
        assert city in JaProvider.cities

        town = self.factory.town()
        assert isinstance(town, string_types)
        assert town in JaProvider.towns

        chome = self.factory.chome()
        assert isinstance(chome, string_types)
        assert re.match("\d{1,2}丁目", chome)

        ban = self.factory.ban()
        assert isinstance(ban, string_types)
        assert re.match("\d{1,2}番", ban)

        gou = self.factory.gou()
        assert isinstance(gou, string_types)
        assert re.match("\d{1,2}号", gou)

        building_name = self.factory.building_name()
        assert isinstance(building_name, string_types)
        assert building_name in JaProvider.building_names

        zipcode = self.factory.zipcode()
        assert isinstance(zipcode, string_types)
        assert re.match("\d{3}-\d{4}", zipcode)

        address = self.factory.address()
        assert isinstance(address, string_types)


class TestNeNP(unittest.TestCase):

    def setUp(self):
        self.factory = Factory.create('ne_NP')

    def test_address(self):
        country = self.factory.country()
        assert isinstance(country, string_types)
        assert country in NeProvider.countries

        district = self.factory.district()
        assert isinstance(district, string_types)
        assert district in NeProvider.districts

        city = self.factory.city()
        assert isinstance(city, string_types)
        assert city in NeProvider.cities


class TestNoNO(unittest.TestCase):

    def setUp(self):
        self.factory = Factory.create('no_NO')

    def test_postcode(self):
        for i in range(100):
            self.assertTrue(re.match(r'^[0-9]{4}$', self.factory.postcode()))
