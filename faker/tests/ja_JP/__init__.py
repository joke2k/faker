# coding=utf-8

from __future__ import unicode_literals

import unittest
import re

from faker import Factory
from .. import string_types


class ja_JP_FactoryTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = Factory.create('ja')

    def test_ja_JP_address(self):
        from faker.providers.address.ja_JP import Provider
        countries = Provider.countries
        country   = self.factory.country()
        assert country
        assert isinstance(country, string_types)
        assert country in countries

        prefectures = Provider.prefectures
        prefecture  = self.factory.prefecture()
        assert prefecture
        assert isinstance(prefecture, string_types)
        assert prefecture in prefectures

        cities = Provider.cities
        city   = self.factory.city()
        assert city
        assert isinstance(city, string_types)
        assert city in cities

        towns = Provider.towns
        town  = self.factory.town()
        assert town
        assert isinstance(town, string_types)
        assert town in towns

        chome = self.factory.chome()
        assert chome
        assert isinstance(chome, string_types)
        assert re.match("\d{1,2}丁目", chome)

        ban = self.factory.ban()
        assert ban
        assert isinstance(ban, string_types)
        assert re.match("\d{1,2}番", ban)

        gou = self.factory.gou()
        assert gou
        assert isinstance(gou, string_types)
        assert re.match("\d{1,2}号", gou)

        building_names = Provider.building_names
        building_name  = self.factory.building_name()
        assert building_name
        assert isinstance(building_name, string_types)
        assert building_name in building_names

        zipcode = self.factory.zipcode()
        assert zipcode
        assert isinstance(zipcode, string_types)
        assert re.match("\d{3}-\d{4}", zipcode)

        address = self.factory.address()
        assert address
        assert isinstance(address, string_types)

    def test_ja_JP_company(self):
        from faker.providers.company.ja_JP import Provider
        prefixes = Provider.company_prefixes

        prefix = self.factory.company_prefix()
        assert prefix
        assert isinstance(prefix, string_types)
        assert prefix in prefixes

        company = self.factory.company()
        assert company
        assert isinstance(company, string_types)
        assert any(prefix in company for prefix in prefixes)
        assert any(company.startswith(prefix) for prefix in prefixes)

    def test_ja_JP_person(self):
        name = self.factory.name()
        assert name
        assert isinstance(name, string_types)

        first_name = self.factory.first_name()
        assert first_name
        assert isinstance(first_name, string_types)

        last_name = self.factory.last_name()
        assert last_name
        assert isinstance(last_name, string_types)

        kana_name = self.factory.kana_name()
        assert kana_name
        assert isinstance(kana_name, string_types)

        first_kana_name = self.factory.first_kana_name()
        assert first_kana_name
        assert isinstance(first_kana_name, string_types)

        first_kana_name_male = self.factory.first_kana_name_male()
        assert first_kana_name_male
        assert isinstance(first_kana_name_male, string_types)

        first_kana_name_female = self.factory.first_kana_name_female()
        assert first_kana_name_female
        assert isinstance(first_kana_name_female, string_types)

        last_kana_name = self.factory.last_kana_name()
        assert last_kana_name
        assert isinstance(last_kana_name, string_types)

    def test_ja_JP_phone_number(self):
        pn = self.factory.phone_number()
        formats = (
            '070',
            '080',
            '090',
        )

        assert pn
        assert isinstance(pn, string_types)
        first, second, third = pn.split('-')
        assert first
        assert first.isdigit()
        assert second
        assert second.isdigit()
        assert third
        assert third.isdigit()
        if len(first) == 2:
            assert len(second) == 4
            assert len(third) == 4
        else:
            assert len(first) == 3
            assert len(second) == 4
            assert len(third) == 4
            assert first in formats
