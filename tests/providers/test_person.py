# coding=utf-8

from __future__ import unicode_literals

import re
import unittest

from faker import Faker
from faker.providers.person.ar_AA import Provider as ArProvider
from faker.providers.person.fi_FI import Provider as FiProvider
from faker.providers.person.ne_NP import Provider as NeProvider
from faker.providers.person.sv_SE import Provider as SvSEProvider
from faker.providers.person.pl_PL import (
    checksum_identity_card_number as pl_checksum_identity_card_number,
)
from tests import string_types


class TestAr(unittest.TestCase):
    """ Tests person in the ar locale """

    def setUp(self):
        self.factory = Faker('ar')

    def test_first_name(self):
        # General first name
        name = self.factory.first_name()
        self.assertTrue(name)
        self.assertIsInstance(name, string_types)
        self.assertIn(name, ArProvider.first_names)

        # Females first name
        name = self.factory.first_name_female()
        self.assertTrue(name)
        self.assertIsInstance(name, string_types)
        self.assertIn(name, ArProvider.first_names)
        self.assertIn(name, ArProvider.first_names_female)

        # Male first name
        name = self.factory.first_name_male()
        self.assertTrue(name)
        self.assertIsInstance(name, string_types)
        self.assertIn(name, ArProvider.first_names)
        self.assertIn(name, ArProvider.first_names_male)

    def test_last_name(self):
        # There's no gender-specific last name in Arabic.
        self.assertFalse(hasattr(ArProvider, 'last_names_male'))
        self.assertFalse(hasattr(ArProvider, 'last_names_female'))
        # All last names apply for all genders.
        self.assertTrue(hasattr(ArProvider, 'last_names'))

        # General first name.
        name = self.factory.last_name()
        self.assertTrue(name)
        self.assertIsInstance(name, string_types)
        self.assertIn(name, ArProvider.last_names)

        # Females last name.
        name = self.factory.last_name_female()
        self.assertTrue(name)
        self.assertIsInstance(name, string_types)
        self.assertIn(name, ArProvider.last_names)
        self.assertIn(name, ArProvider.last_names)

        # Male last name.
        name = self.factory.last_name_male()
        self.assertTrue(name)
        self.assertIsInstance(name, string_types)
        self.assertIn(name, ArProvider.last_names)
        self.assertIn(name, ArProvider.last_names)


class TestJaJP(unittest.TestCase):
    """ Tests person in the ja_JP locale """

    def setUp(self):
        self.factory = Faker('ja')

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
        self.factory = Faker('ne_NP')

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


class TestFiFI(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('fi_FI')

    def test_gender_first_names(self):
        female_name = self.factory.first_name_female()
        self.assertIsInstance(female_name, string_types)
        self.assertIn(female_name, FiProvider.first_names_female)
        male_name = self.factory.first_name_male()
        self.assertIsInstance(male_name, string_types)
        self.assertIn(male_name, FiProvider.first_names_male)
        first_name = self.factory.first_name()
        self.assertIsInstance(first_name, string_types)
        self.assertIn(first_name, FiProvider.first_names)

    def test_last_names(self):
        last_name = self.factory.last_name()
        self.assertIsInstance(last_name, string_types)
        self.assertIn(last_name, FiProvider.last_names)


class TestSvSE(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('sv_SE')

    def test_gender_first_names(self):
        """simple test to verify that we are pulling gender specific names"""
        name = self.factory.first_name_female()
        self.assertIn(name, SvSEProvider.first_names_female)
        name = self.factory.first_name_male()
        self.assertIn(name, SvSEProvider.first_names_male)
        name = self.factory.first_name()
        self.assertIn(name, SvSEProvider.first_names)


class TestPlPL(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('pl_PL')

    def test_identity_card_number_checksum(self):
        self.assertEqual(pl_checksum_identity_card_number(['A', 'I', 'S', 8, 5, 0, 2, 1, 4]), 8)
        self.assertEqual(pl_checksum_identity_card_number(['A', 'U', 'L', 9, 2, 7, 2, 8, 5]), 9)
        self.assertEqual(pl_checksum_identity_card_number(['A', 'E', 'I', 2, 5, 1, 8, 2, 4]), 2)
        self.assertEqual(pl_checksum_identity_card_number(['A', 'H', 'F', 2, 2, 0, 6, 8, 0]), 2)
        self.assertEqual(pl_checksum_identity_card_number(['A', 'X', 'E', 8, 2, 0, 3, 4, 0]), 8)

    def test_identity_card_number(self):
        for _ in range(100):
            self.assertTrue(re.search(r'^[A-Z]{3}\d{6}$', self.factory.identity_card_number()))
