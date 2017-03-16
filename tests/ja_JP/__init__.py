# coding=utf-8

from __future__ import unicode_literals

import unittest
import re

from faker import Factory
from faker.utils import text
from .. import string_types


class ja_JP_FactoryTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = Factory.create('ja')

    def test_ja_JP_internet(self):
        from faker.providers.person.ja_JP import Provider
        last_romanized_names = Provider.last_romanized_names

        domain_word = self.factory.domain_word()
        assert domain_word
        assert isinstance(domain_word, string_types)
        assert any(domain_word == text.slugify(last_romanized_name) for last_romanized_name in last_romanized_names)

        user_name = self.factory.user_name()
        assert user_name
        assert isinstance(user_name, string_types)

        tld = self.factory.tld()
        assert tld
        assert isinstance(tld, string_types)

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

        romanized_name = self.factory.romanized_name()
        assert romanized_name
        assert isinstance(romanized_name, string_types)

        first_romanized_name = self.factory.first_romanized_name()
        assert first_romanized_name
        assert isinstance(first_romanized_name, string_types)

        first_romanized_name_male = self.factory.first_romanized_name_male()
        assert first_romanized_name_male
        assert isinstance(first_romanized_name_male, string_types)

        first_romanized_name_female = self.factory.first_romanized_name_female()
        assert first_romanized_name_female
        assert isinstance(first_romanized_name_female, string_types)

        last_romanized_name = self.factory.last_romanized_name()
        assert last_romanized_name
        assert isinstance(last_romanized_name, string_types)

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
