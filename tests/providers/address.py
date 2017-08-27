# coding=utf-8

from __future__ import unicode_literals

import re
import unittest

from ukpostcodeparser.parser import parse_uk_postcode

from faker import Factory
from faker.providers.address.de_DE import Provider as DeProvider
from faker.providers.address.hu_HU import Provider as HuProvider
from faker.providers.address.ja_JP import Provider as JaProvider
from faker.providers.address.ne_NP import Provider as NeProvider
from six import string_types


class TestDeDE(unittest.TestCase):
    """ Tests in addresses in the de_DE locale """

    def setUp(self):
        self.factory = Factory.create('de_DE')

    def test_city(self):
        city = self.factory.city()
        assert isinstance(city, string_types)
        assert city in DeProvider.cities

    def test_state(self):
        state = self.factory.state()
        assert isinstance(state, string_types)
        assert state in DeProvider.states

    def test_street_suffix_short(self):
        street_suffix_short = self.factory.street_suffix_short()
        assert isinstance(street_suffix_short, string_types)
        assert street_suffix_short in DeProvider.street_suffixes_short

    def test_street_suffix_long(self):
        street_suffix_long = self.factory.street_suffix_long()
        assert isinstance(street_suffix_long, string_types)
        assert street_suffix_long in DeProvider.street_suffixes_long

    def test_country(self):
        country = self.factory.country()
        assert isinstance(country, string_types)
        assert country in DeProvider.countries


class TestEnGB(unittest.TestCase):
    """ Tests addresses in the en_GB locale """

    def setUp(self):
        self.factory = Factory.create('en_GB')

    def test_postcode(self):
        for _ in range(100):
            assert isinstance(parse_uk_postcode(self.factory.postcode()), tuple)


class TestHuHU(unittest.TestCase):
    """ Tests addresses in the hu_HU locale """

    def setUp(self):
        self.factory = Factory.create('hu_HU')

    def test_postcode_first_digit(self):
        # Hungarian postcodes begin with 'H-' followed by 4 digits.
        # The first digit may not begin with a zero.
        for _ in range(100):
            pcd = self.factory.postcode()
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
    """ Tests addresses in the ne_NP locale """

    def setUp(self):
        self.factory = Factory.create('ne_NP')

    def test_address(self):
        """ Tests the street address in ne_NP locale """
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
    """ Tests the street address in no_NO locale """

    def setUp(self):
        self.factory = Factory.create('no_NO')

    def test_postcode(self):
        for _ in range(100):
            self.assertTrue(re.match(r'^[0-9]{4}$', self.factory.postcode()))

    def test_city_suffix(self):
        suffix = self.factory.city_suffix()
        assert isinstance(suffix, string_types)

    def test_street_suffix(self):
        suffix = self.factory.street_suffix()
        assert isinstance(suffix, string_types)

    def test_address(self):
        address = self.factory.address()
        assert isinstance(address, string_types)


class TestZhTW(unittest.TestCase):
    """ Tests addresses in the zh_tw locale """

    def setUp(self):
        self.factory = Factory.create('zh_TW')

    def test_address(self):
        country = self.factory.country()
        assert isinstance(country, string_types)

        street = self.factory.street_name()
        assert isinstance(street, string_types)

        city = self.factory.city()
        assert isinstance(city, string_types)

        address = self.factory.address()
        assert isinstance(address, string_types)

class TestZhCN(unittest.TestCase):
    """ Tests addresses in the zh_cn locale """

    def setUp(self):
        self.factory = Factory.create('zh_CN')

    def test_address(self):
        country = self.factory.country()
        assert isinstance(country, string_types)

        street = self.factory.street_name()
        assert isinstance(street, string_types)

        city = self.factory.street_address()
        assert isinstance(city, string_types)

        province = self.factory.province()
        assert isinstance(province, string_types)

        district = self.factory.district()
        assert isinstance(district, string_types)

        address = self.factory.address()
        assert isinstance(address, string_types)

        for _ in range(100):
            self.assertTrue(re.match(r'\d{5}', self.factory.postcode()))
