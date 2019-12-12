# coding=utf-8

from __future__ import unicode_literals

import re
import unittest
import datetime
import six

try:
    from unittest import mock
except ImportError:
    import mock

from faker import Faker
from faker.providers.person.ar_AA import Provider as ArProvider
from faker.providers.person.fi_FI import Provider as FiProvider
from faker.providers.person.hy_AM import Provider as HyAmProvider
from faker.providers.person.ne_NP import Provider as NeProvider
from faker.providers.person.sv_SE import Provider as SvSEProvider
from faker.providers.person.cs_CZ import Provider as CsCZProvider
from faker.providers.person.pl_PL import Provider as PlPLProvider
from faker.providers.person.pl_PL import (
    checksum_identity_card_number as pl_checksum_identity_card_number,
)
from faker.providers.person.zh_CN import Provider as ZhCNProvider
from faker.providers.person.zh_TW import Provider as ZhTWProvider
from faker.providers.person.ta_IN import Provider as TaINProvider


class TestAr(unittest.TestCase):
    """ Tests person in the ar locale """

    def setUp(self):
        self.fake = Faker('ar')
        Faker.seed(0)

    def test_first_name(self):
        # General first name
        name = self.fake.first_name()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ArProvider.first_names

        # Females first name
        name = self.fake.first_name_female()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ArProvider.first_names
        assert name in ArProvider.first_names_female

        # Male first name
        name = self.fake.first_name_male()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ArProvider.first_names
        assert name in ArProvider.first_names_male

    def test_last_name(self):
        # There's no gender-specific last name in Arabic.
        assert not hasattr(ArProvider, 'last_names_male')
        assert not hasattr(ArProvider, 'last_names_female')
        # All last names apply for all genders.
        assert hasattr(ArProvider, 'last_names')

        # General last name.
        name = self.fake.last_name()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ArProvider.last_names

        # Females last name.
        name = self.fake.last_name_female()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ArProvider.last_names
        assert name in ArProvider.last_names

        # Male last name.
        name = self.fake.last_name_male()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ArProvider.last_names
        assert name in ArProvider.last_names


class TestJaJP(unittest.TestCase):
    """ Tests person in the ja_JP locale """

    def setUp(self):
        self.fake = Faker('ja')
        Faker.seed(0)

    def test_person(self):
        name = self.fake.name()
        assert name
        assert isinstance(name, six.string_types)

        first_name = self.fake.first_name()
        assert first_name
        assert isinstance(first_name, six.string_types)

        last_name = self.fake.last_name()
        assert last_name
        assert isinstance(last_name, six.string_types)

        kana_name = self.fake.kana_name()
        assert kana_name
        assert isinstance(kana_name, six.string_types)

        first_kana_name = self.fake.first_kana_name()
        assert first_kana_name
        assert isinstance(first_kana_name, six.string_types)

        first_kana_name_male = self.fake.first_kana_name_male()
        assert first_kana_name_male
        assert isinstance(first_kana_name_male, six.string_types)

        first_kana_name_female = self.fake.first_kana_name_female()
        assert first_kana_name_female
        assert isinstance(first_kana_name_female, six.string_types)

        last_kana_name = self.fake.last_kana_name()
        assert last_kana_name
        assert isinstance(last_kana_name, six.string_types)

        romanized_name = self.fake.romanized_name()
        assert romanized_name
        assert isinstance(romanized_name, six.string_types)

        first_romanized_name = self.fake.first_romanized_name()
        assert first_romanized_name
        assert isinstance(first_romanized_name, six.string_types)

        first_romanized_name_male = self.fake.first_romanized_name_male()
        assert first_romanized_name_male
        assert isinstance(first_romanized_name_male, six.string_types)

        first_romanized_name_female = self.fake.first_romanized_name_female()
        assert first_romanized_name_female
        assert isinstance(first_romanized_name_female, six.string_types)

        last_romanized_name = self.fake.last_romanized_name()
        assert last_romanized_name
        assert isinstance(last_romanized_name, six.string_types)


class TestNeNP(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('ne_NP')
        Faker.seed(0)

    def test_names(self):
        name = self.fake.name().split()
        assert all(isinstance(n, six.string_types) for n in name)
        # name should always be 2-3 words. If 3, first word
        # should be a prefix.
        assert name[-2] in NeProvider.first_names
        assert name[-1] in NeProvider.last_names
        prefixes = NeProvider.prefixes_male + NeProvider.prefixes_female
        if len(name) == 3:
            assert name[0] in prefixes


class TestFiFI(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('fi_FI')
        Faker.seed(0)

    def test_gender_first_names(self):
        female_name = self.fake.first_name_female()
        self.assertIsInstance(female_name, six.string_types)
        assert female_name in FiProvider.first_names_female
        male_name = self.fake.first_name_male()
        self.assertIsInstance(male_name, six.string_types)
        assert male_name in FiProvider.first_names_male
        first_name = self.fake.first_name()
        self.assertIsInstance(first_name, six.string_types)
        assert first_name in FiProvider.first_names

    def test_last_names(self):
        last_name = self.fake.last_name()
        self.assertIsInstance(last_name, six.string_types)
        assert last_name in FiProvider.last_names


class TestSvSE(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('sv_SE')
        Faker.seed(0)

    def test_gender_first_names(self):
        """simple test to verify that we are pulling gender specific names"""
        name = self.fake.first_name_female()
        assert name in SvSEProvider.first_names_female
        name = self.fake.first_name_male()
        assert name in SvSEProvider.first_names_male
        name = self.fake.first_name()
        assert name in SvSEProvider.first_names


class TestPlPL(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('pl_PL')
        Faker.seed(0)

    def test_identity_card_number_checksum(self):
        assert pl_checksum_identity_card_number(['A', 'I', 'S', 8, 5, 0, 2, 1, 4]) == 8
        assert pl_checksum_identity_card_number(['A', 'U', 'L', 9, 2, 7, 2, 8, 5]) == 9
        assert pl_checksum_identity_card_number(['A', 'E', 'I', 2, 5, 1, 8, 2, 4]) == 2
        assert pl_checksum_identity_card_number(['A', 'H', 'F', 2, 2, 0, 6, 8, 0]) == 2
        assert pl_checksum_identity_card_number(['A', 'X', 'E', 8, 2, 0, 3, 4, 0]) == 8

    def test_identity_card_number(self):
        for _ in range(100):
            assert re.search(r'^[A-Z]{3}\d{6}$', self.fake.identity_card_number())

    @mock.patch.object(PlPLProvider, 'random_digit')
    def test_pesel_birth_date(self, mock_random_digit):
        mock_random_digit.side_effect = [3, 5, 8, 8, 7, 9, 9, 3]
        assert self.fake.pesel(datetime.date(1999, 12, 31)) == '99123135885'
        assert self.fake.pesel(datetime.date(2000,  1,  1)) == '00210179936'

    @mock.patch.object(PlPLProvider, 'random_digit')
    def test_pesel_sex_male(self, mock_random_digit):
        mock_random_digit.side_effect = [1, 3, 4, 5, 6, 1, 7, 0]
        assert self.fake.pesel(datetime.date(1909, 3, 3), 'M') == '09030313454'
        assert self.fake.pesel(datetime.date(1913, 8, 16), 'M') == '13081661718'

    @mock.patch.object(PlPLProvider, 'random_digit')
    def test_pesel_sex_female(self, mock_random_digit):
        mock_random_digit.side_effect = [4, 9, 1, 6, 6, 1, 7, 3]
        assert self.fake.pesel(datetime.date(2007, 4, 13), 'F') == '07241349161'
        assert self.fake.pesel(datetime.date(1933, 12, 16), 'F') == '33121661744'

    @mock.patch.object(PlPLProvider, 'random_digit')
    def test_pwz_doctor(self, mock_random_digit):
        mock_random_digit.side_effect = [6, 9, 1, 9, 6, 5, 2, 7, 9, 9, 1, 5]
        assert self.fake.pwz_doctor() == '2691965'
        assert self.fake.pwz_doctor() == '4279915'

    @mock.patch.object(PlPLProvider, 'random_digit')
    def test_pwz_doctor_check_digit_zero(self, mock_random_digit):
        mock_random_digit.side_effect = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 9, 9]
        assert self.fake.pwz_doctor() == '6000012'
        assert self.fake.pwz_doctor() == '1000090'

    @mock.patch.object(PlPLProvider, 'random_int')
    @mock.patch.object(PlPLProvider, 'random_digit')
    def test_pwz_nurse(self, mock_random_digit, mock_random_int):
        mock_random_digit.side_effect = [3, 4, 5, 6, 7, 1, 7, 5, 1, 2]
        mock_random_int.side_effect = [45, 3]
        assert self.fake.pwz_nurse(kind='nurse') == '4534567P'
        assert self.fake.pwz_nurse(kind='midwife') == '0317512A'


class TestCsCZ(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('cs_CZ')
        Faker.seed(0)

    def test_name_male(self):
        male_name = self.fake.name_male()
        name_parts = male_name.split(" ")
        first_name, last_name = "", ""
        if len(name_parts) == 2:
            first_name = name_parts[0]
            last_name = name_parts[1]
        elif len(name_parts) == 4:
            first_name = name_parts[1]
            last_name = name_parts[2]
        elif len(name_parts) == 3:
            if name_parts[-1] in CsCZProvider.suffixes:
                first_name = name_parts[0]
                last_name = name_parts[1]
            else:
                first_name = name_parts[1]
                last_name = name_parts[2]
        assert first_name in CsCZProvider.first_names_male
        assert last_name in CsCZProvider.last_names_male

    def test_name_female(self):
        female_name = self.fake.name_female()
        name_parts = female_name.split(" ")
        first_name, last_name = "", ""
        if len(name_parts) == 2:
            first_name = name_parts[0]
            last_name = name_parts[1]
        elif len(name_parts) == 4:
            first_name = name_parts[1]
            last_name = name_parts[2]
        elif len(name_parts) == 3:
            if name_parts[-1] in CsCZProvider.suffixes:
                first_name = name_parts[0]
                last_name = name_parts[1]
            else:
                first_name = name_parts[1]
                last_name = name_parts[2]
        assert first_name in CsCZProvider.first_names_female
        assert last_name in CsCZProvider.last_names_female


class TestZhCN(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('zh_CN')
        Faker.seed(0)

    def test_last_name(self):
        # There's no gender-specific last name in Chinese.
        assert not hasattr(ZhCNProvider, 'last_names_male')
        assert not hasattr(ZhCNProvider, 'last_names_female')
        assert not hasattr(ZhCNProvider, 'last_romanized_names_male')
        assert not hasattr(ZhCNProvider, 'last_romanized_names_female')
        # All last names apply for all genders.
        assert hasattr(ZhCNProvider, 'last_names')

        # General last name.
        name = self.fake.last_name()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ZhCNProvider.last_names

        # Females last name.
        name = self.fake.last_name_female()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ZhCNProvider.last_names

        # Male last name.
        name = self.fake.last_name_male()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ZhCNProvider.last_names

        # General last romanized name
        name = self.fake.last_romanized_name()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ZhCNProvider.last_romanized_names

    def test_first_name(self):
        # General first name
        name = self.fake.first_name()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ZhCNProvider.first_names

        # Females first name
        name = self.fake.first_name_female()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ZhCNProvider.first_names
        assert name in ZhCNProvider.first_names_female

        # Male first name
        name = self.fake.first_name_male()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ZhCNProvider.first_names
        assert name in ZhCNProvider.first_names_male

        # General first romanized name
        name = self.fake.first_romanized_name()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ZhCNProvider.first_romanized_names

    def test_name(self):
        # Full name
        name = self.fake.name()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name[0] in ZhCNProvider.last_names or name[:2] in ZhCNProvider.last_names
        assert name[1:] in ZhCNProvider.first_names or name[2:] in ZhCNProvider.first_names

        # Full romanized name
        name = self.fake.romanized_name()
        assert name
        self.assertIsInstance(name, six.string_types)
        first_romanized_name, last_romanized_name = name.split(' ')
        assert first_romanized_name in ZhCNProvider.first_romanized_names
        assert last_romanized_name in ZhCNProvider.last_romanized_names


class TestZhTW(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('zh_TW')
        Faker.seed(0)

    def test_last_name(self):
        # There's no gender-specific last name in Chinese.
        assert not hasattr(ZhTWProvider, 'last_names_male')
        assert not hasattr(ZhTWProvider, 'last_names_female')
        assert not hasattr(ZhTWProvider, 'last_romanized_names_male')
        assert not hasattr(ZhTWProvider, 'last_romanized_names_female')
        # All last names apply for all genders.
        assert hasattr(ZhTWProvider, 'last_names')

        # General last name.
        name = self.fake.last_name()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ZhTWProvider.last_names

        # Females last name.
        name = self.fake.last_name_female()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ZhTWProvider.last_names

        # Male last name.
        name = self.fake.last_name_male()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ZhTWProvider.last_names

        # General last romanized name
        name = self.fake.last_romanized_name()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ZhTWProvider.last_romanized_names

    def test_first_name(self):
        # General first name
        name = self.fake.first_name()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ZhTWProvider.first_names

        # Females first name
        name = self.fake.first_name_female()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ZhTWProvider.first_names
        assert name in ZhTWProvider.first_names_female

        # Male first name
        name = self.fake.first_name_male()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ZhTWProvider.first_names
        assert name in ZhTWProvider.first_names_male

        # General first romanized name
        name = self.fake.first_romanized_name()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name in ZhTWProvider.first_romanized_names

    def test_name(self):
        # Full name
        name = self.fake.name()
        assert name
        self.assertIsInstance(name, six.string_types)
        assert name[0] in ZhTWProvider.last_names or name[:2] in ZhTWProvider.last_names
        assert name[1:] in ZhTWProvider.first_names or name[2:] in ZhTWProvider.first_names

        # Full romanized name
        name = self.fake.romanized_name()
        assert name
        self.assertIsInstance(name, six.string_types)
        first_romanized_name, last_romanized_name = name.split(' ')
        assert first_romanized_name in ZhTWProvider.first_romanized_names
        assert last_romanized_name in ZhTWProvider.last_romanized_names


class TestHyAM(unittest.TestCase):
    """ Tests person in the hy_AM locale """

    def setUp(self):
        self.fake = Faker('hy_AM')
        Faker.seed(0)

    def test_name(self):
        # General name
        name = self.fake.name()
        self.assertIsInstance(name, six.string_types)

        # Female name
        name = self.fake.name_female()
        self.assertIsInstance(name, six.string_types)

        # Male name
        name = self.fake.name_male()
        self.assertIsInstance(name, six.string_types)

    def test_first_name(self):
        # General first name
        name = self.fake.first_name()
        self.assertIsInstance(name, six.string_types)
        assert name in HyAmProvider.first_names

        # Female first name
        name = self.fake.first_name_female()
        self.assertIsInstance(name, six.string_types)
        assert name in HyAmProvider.first_names
        assert name in HyAmProvider.first_names_female

        # Male first name
        name = self.fake.first_name_male()
        self.assertIsInstance(name, six.string_types)
        assert name in HyAmProvider.first_names
        assert name in HyAmProvider.first_names_male

    def test_last_name(self):
        # There's no gender-specific last name in Armenian.
        assert not hasattr(HyAmProvider, 'last_names_male')
        assert not hasattr(HyAmProvider, 'last_names_female')
        # All last names apply for all genders.
        assert hasattr(HyAmProvider, 'last_names')

        # General last name.
        name = self.fake.last_name()
        self.assertIsInstance(name, six.string_types)
        assert name in HyAmProvider.last_names

        # Females last name.
        name = self.fake.last_name_female()
        self.assertIsInstance(name, six.string_types)
        assert name in HyAmProvider.last_names

        # Male last name.
        name = self.fake.last_name_male()
        self.assertIsInstance(name, six.string_types)
        assert name in HyAmProvider.last_names


class TestTaIN(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('ta_IN')
        Faker.seed(0)

    def test_gender_first_names(self):
        """simple test to verify that we are pulling gender specific names"""
        name = self.fake.first_name_female()
        assert name in TaINProvider.first_names_female
        name = self.fake.first_name_male()
        assert name in TaINProvider.first_names_male
        name = self.fake.first_name()
        assert name in TaINProvider.first_names
