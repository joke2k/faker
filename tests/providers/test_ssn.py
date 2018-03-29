#  -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import re
from datetime import datetime

from faker import Faker
from faker.providers.ssn.et_EE import checksum as et_checksum
from faker.providers.ssn.fi_FI import Provider as fi_Provider
from faker.providers.ssn.hr_HR import checksum as hr_checksum
from faker.providers.ssn.pt_BR import checksum as pt_checksum
from faker.providers.ssn.pl_PL import checksum as pl_checksum, calculate_month as pl_calculate_mouth
from faker.providers.ssn.no_NO import checksum as no_checksum, Provider


class TestEtEE(unittest.TestCase):
    """ Tests SSN in the et_EE locale """

    def setUp(self):
        self.factory = Faker('et_EE')

    def test_ssn_checksum(self):
        self.assertEqual(et_checksum([4, 4, 1, 1, 1, 3, 0, 4, 9, 2]), 3)
        self.assertEqual(et_checksum([3, 6, 7, 0, 1, 1, 6, 6, 2, 7]), 8)
        self.assertEqual(et_checksum([4, 7, 0, 0, 4, 2, 1, 5, 0, 1]), 2)
        self.assertEqual(et_checksum([3, 9, 7, 0, 3, 0, 4, 3, 3, 6]), 0)

    def test_ssn(self):
        for _ in range(100):
            self.assertTrue(re.search(r'^\d{11}$', self.factory.ssn()))


class TestFiFI(unittest.TestCase):
    """ Tests SSN in the fi_FI locale """

    def setUp(self):
        self.factory = Faker('fi_FI')
        self.provider = fi_Provider

    def test_century_code(self):
        self.assertEqual(self.provider._get_century_code(1900), '-')
        self.assertEqual(self.provider._get_century_code(1999), '-')
        self.assertEqual(self.provider._get_century_code(2000), 'A')
        self.assertEqual(self.provider._get_century_code(2999), 'A')
        self.assertEqual(self.provider._get_century_code(1800), '+')
        self.assertEqual(self.provider._get_century_code(1899), '+')
        with self.assertRaises(ValueError):
            self.provider._get_century_code(1799)
        with self.assertRaises(ValueError):
            self.provider._get_century_code(3000)

    def test_ssn_sanity(self):
        for age in range(100):
            self.factory.ssn(min_age=age, max_age=age+1)


class TestHrHR(unittest.TestCase):
    """ Tests SSN in the hr_HR locale """

    def setUp(self):
        self.factory = Faker('hr_HR')

    def test_ssn_checksum(self):
        self.assertEqual(hr_checksum([0, 0, 2, 2, 8, 2, 6, 9, 2, 8]), 9)
        self.assertEqual(hr_checksum([5, 8, 9, 3, 6, 9, 5, 1, 2, 5]), 1)
        self.assertEqual(hr_checksum([5, 7, 8, 0, 2, 0, 3, 4, 2, 3]), 7)
        self.assertEqual(hr_checksum([4, 3, 3, 3, 1, 4, 6, 7, 6, 2]), 2)
        self.assertEqual(hr_checksum([0, 5, 9, 3, 7, 7, 5, 9, 1, 8]), 7)
        self.assertEqual(hr_checksum([7, 1, 1, 4, 9, 9, 1, 2, 4, 1]), 6)

    def test_ssn(self):
        for _ in range(100):
            self.assertTrue(re.search(r'^\d{11}$', self.factory.ssn()))


class TestHuHU(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('hu_HU')
        self.factory.seed(0)

    def test_ssn(self):
        for _ in range(100):
            ssn = self.factory.ssn()
            assert ssn.isdigit()
            assert len(ssn) >= 10
            assert len(ssn) <= 12

        for _ in range(100):
            dob_val = '{:02d}{:02d}{:02d}'.format(
                self.factory.random_int(0, 99),
                self.factory.random_int(1, 12),
                self.factory.random_int(1, 31))
            dob = self.factory.random.choice([None, dob_val])
            gender = self.factory.random.choice([None, 'F', 'M', 'z'])
            try:
                ssn = self.factory.ssn(dob=dob, gender=gender)
                assert ssn.isdigit()
                assert len(ssn) >= 10
                assert len(ssn) <= 12
            except ValueError:
                pass


class TestPtBR(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('pt_BR')

    def test_pt_BR_ssn_checksum(self):
        self.assertEqual(pt_checksum([8, 8, 2, 8, 2, 1, 6, 5, 2]), 2)
        self.assertEqual(pt_checksum([8, 8, 2, 8, 2, 1, 6, 5, 2, 2]), 1)

    def test_pt_BR_ssn(self):
        for _ in range(100):
            self.assertTrue(re.search(r'^\d{11}$', self.factory.ssn()))

    def test_pt_BR_cpf(self):
        for _ in range(100):
            self.assertTrue(re.search(r'\d{3}\.\d{3}\.\d{3}\-\d{2}', self.factory.cpf()))


class TestPlPL(unittest.TestCase):
    """ Tests SSN in the pl_PL locale """

    def setUp(self):
        self.factory = Faker('pl_PL')

    def test_ssn_checksum(self):
        self.assertEqual(pl_checksum([0, 5, 2, 6, 2, 8, 1, 2, 3, 6]), 5)
        self.assertEqual(pl_checksum([8, 5, 0, 5, 0, 8, 1, 5, 5, 8]), 7)
        self.assertEqual(pl_checksum([4, 5, 1, 1, 1, 0, 0, 2, 4, 3]), 3)
        self.assertEqual(pl_checksum([9, 1, 0, 7, 2, 6, 1, 4, 8, 7]), 3)
        self.assertEqual(pl_checksum([8, 1, 1, 2, 1, 4, 1, 1, 8, 7]), 6)

    def test_calculate_month(self):
        self.assertEqual(pl_calculate_mouth(datetime.strptime('1 1 1900', '%m %d %Y')), 1)
        self.assertEqual(pl_calculate_mouth(datetime.strptime('12 1 1900', '%m %d %Y')), 12)
        self.assertEqual(pl_calculate_mouth(datetime.strptime('1 1 1999', '%m %d %Y')), 1)

        self.assertEqual(pl_calculate_mouth(datetime.strptime('1 1 2000', '%m %d %Y')), 21)
        self.assertEqual(pl_calculate_mouth(datetime.strptime('12 1 2000', '%m %d %Y')), 32)
        self.assertEqual(pl_calculate_mouth(datetime.strptime('1 1 2099', '%m %d %Y')), 21)

        self.assertEqual(pl_calculate_mouth(datetime.strptime('1 1 2100', '%m %d %Y')), 41)
        self.assertEqual(pl_calculate_mouth(datetime.strptime('12 1 2100', '%m %d %Y')), 52)
        self.assertEqual(pl_calculate_mouth(datetime.strptime('1 1 2199', '%m %d %Y')), 41)

        self.assertEqual(pl_calculate_mouth(datetime.strptime('1 1 2200', '%m %d %Y')), 61)
        self.assertEqual(pl_calculate_mouth(datetime.strptime('12 1 2200', '%m %d %Y')), 72)
        self.assertEqual(pl_calculate_mouth(datetime.strptime('1 1 2299', '%m %d %Y')), 61)

    def test_ssn(self):
        for _ in range(100):
            self.assertTrue(re.search(r'^\d{11}$', self.factory.ssn()))


class TestNoNO(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('no_NO')

    def test_no_NO_ssn_checksum(self):
        self.assertEqual(no_checksum([0, 1, 0, 2, 0, 3, 9, 8, 7], Provider.scale1), 6)
        self.assertEqual(no_checksum([0, 1, 0, 2, 0, 3, 9, 8, 7, 6], Provider.scale2), 7)

    def test_no_NO_ssn(self):
        for _ in range(100):
            ssn = self.factory.ssn()
            self.assertTrue(ssn.isdigit())
            self.assertEqual(len(ssn), 11)

    def test_no_NO_ssn_dob_passed(self):
        date_of_birth = '20010203'
        ssn = self.factory.ssn(dob=date_of_birth)
        self.assertEqual(ssn[:6], date_of_birth[2:])

    def test_no_NO_ssn_invalid_dob_passed(self):
        with self.assertRaises(ValueError):
            self.factory.ssn(dob='010401')
        with self.assertRaises(ValueError):
            self.factory.ssn(dob='hello_world')
        with self.assertRaises(ValueError):
            self.factory.ssn(dob='001301')

    def test_no_NO_ssn_gender_passed(self):
        # Females have even number at index 8
        ssn = self.factory.ssn(gender='F')
        self.assertTrue(int(ssn[8]) % 2 == 0)
        # Males have odd number at index 8
        ssn = self.factory.ssn(gender='M')
        self.assertTrue(int(ssn[8]) % 2 == 1)

    def test_no_NO_ssn_invalid_gender_passed(self):
        with self.assertRaises(ValueError):
            self.factory.ssn(gender='A')
