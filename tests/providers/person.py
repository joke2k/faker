# coding=utf-8

from __future__ import unicode_literals

import unittest

from faker import Factory
from faker.providers.person.ne_NP import Provider as NeProvider
from .. import string_types


class TestJaJP(unittest.TestCase):
    """ Tests person in the ja_JP locale """

    def setUp(self):
        self.factory = Factory.create('ja')

    def test_person(self):
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


class TestNeNP(unittest.TestCase):

    def setUp(self):
        self.factory = Factory.create('ne_NP')

    def test_names(self):
        name = self.factory.name().split()
        assert all(isinstance(n, string_types) for n in name)
        # name should always be 2-3 words. If 3, first word
        # should be a prefix.
        assert name[-2] in NeProvider.first_names
        assert name[-1] in NeProvider.last_names
        prefixes = NeProvider.prefixes_male + NeProvider.prefixes_female
        if len(name) == 3:
            assert name[0] in prefixes
