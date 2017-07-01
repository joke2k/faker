#  -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import re
from datetime import datetime

from faker import Factory
from faker.providers.ssn.et_EE import Provider as EtProvider, checksum as et_checksum
from faker.providers.ssn.hr_HR import Provider as HrProvider, checksum as hr_checksum
from faker.providers.ssn.pt_BR import Provider as PtProvider, checksum as pt_checksum
from faker.providers.ssn.pl_PL import (Provider as PlProvider, checksum as pl_checksum,
                                       calculate_month as pl_calculate_mouth)


class TestEtEE(unittest.TestCase):
    """ Tests SSN in the et_EE locale """

    def setUp(self):
        self.factory = Factory.create('et_EE')

    def test_ssn_checksum(self):
        self.assertEqual(et_checksum([4, 4, 1, 1, 1, 3, 0, 4, 9, 2]), 3)
        self.assertEqual(et_checksum([3, 6, 7, 0, 1, 1, 6, 6, 2, 7]), 8)
        self.assertEqual(et_checksum([4, 7, 0, 0, 4, 2, 1, 5, 0, 1]), 2)
        self.assertEqual(et_checksum([3, 9, 7, 0, 3, 0, 4, 3, 3, 6]), 0)

    def test_ssn(self):
        for _ in range(100):
            self.assertTrue(re.search(r'^\d{11}$', EtProvider.ssn()))


class TestHrHR(unittest.TestCase):
    """ Tests SSN in the hr_HR locale """

    def setUp(self):
        self.factory = Factory.create('hr_HR')

    def test_ssn_checksum(self):
        self.assertEqual(hr_checksum([0, 0, 2, 2, 8, 2, 6, 9, 2, 8]), 9)
        self.assertEqual(hr_checksum([5, 8, 9, 3, 6, 9, 5, 1, 2, 5]), 1)
        self.assertEqual(hr_checksum([5, 7, 8, 0, 2, 0, 3, 4, 2, 3]), 7)
        self.assertEqual(hr_checksum([4, 3, 3, 3, 1, 4, 6, 7, 6, 2]), 2)
        self.assertEqual(hr_checksum([0, 5, 9, 3, 7, 7, 5, 9, 1, 8]), 7)
        self.assertEqual(hr_checksum([7, 1, 1, 4, 9, 9, 1, 2, 4, 1]), 6)

    def test_ssn(self):
        for _ in range(100):
            self.assertTrue(re.search(r'^\d{11}$', HrProvider.ssn()))


class TestPtBR(unittest.TestCase):
    def setUp(self):
        self.factory = Factory.create('pt_BR')

    def test_pt_BR_ssn_checksum(self):
        self.assertEqual(pt_checksum([8, 8, 2, 8, 2, 1, 6, 5, 2]), 2)
        self.assertEqual(pt_checksum([8, 8, 2, 8, 2, 1, 6, 5, 2, 2]), 1)

    def test_pt_BR_ssn(self):
        for _ in range(100):
            self.assertTrue(re.search(r'^\d{11}$', PtProvider.ssn()))

    def test_pt_BR_cpf(self):
        for _ in range(100):
            self.assertTrue(re.search(r'\d{3}\.\d{3}\.\d{3}\-\d{2}', PtProvider.cpf()))


class TestPlPL(unittest.TestCase):
    """ Tests SSN in the pl_PL locale """

    def setUp(self):
        self.factory = Factory.create('pl_PL')

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
            self.assertTrue(re.search(r'^\d{11}$', PlProvider.ssn()))
