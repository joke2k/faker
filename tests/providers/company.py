# coding=utf-8

from __future__ import unicode_literals

import unittest
import re

from faker import Factory
from faker.providers.company.hu_HU import Provider as HuProvider
from faker.providers.company.ja_JP import Provider as JaProvider
from faker.providers.company.pt_BR import Provider as PtProvider, company_id_checksum
from faker.providers.company.pl_PL import (Provider as PlProvider, regon_checksum, local_regon_checksum,
                                           company_vat_checksum)
from .. import string_types


class TestJaJP(unittest.TestCase):
    """ Tests companies in the ja_JP locale """

    def setUp(self):
        self.factory = Factory.create('ja')

    def test_company(self):
        prefixes = JaProvider.company_prefixes

        prefix = self.factory.company_prefix()
        assert isinstance(prefix, string_types)
        assert prefix in prefixes

        company = self.factory.company()
        assert isinstance(company, string_types)
        assert any(prefix in company for prefix in prefixes)
        assert any(company.startswith(prefix) for prefix in prefixes)


class TestPtBR(unittest.TestCase):
    """ Tests company in the pt_BR locale """

    def setUp(self):
        self.factory = Factory.create('pt_BR')

    def test_pt_BR_company_id_checksum(self):
        self.assertEqual(company_id_checksum([9, 4, 9, 5, 3, 4, 4, 1, 0, 0, 0, 1]), [5, 1])
        self.assertEqual(company_id_checksum([1, 6, 0, 0, 4, 6, 3, 9, 0, 0, 0, 1]), [8, 5])

    def test_pt_BR_company_id(self):
        for _ in range(100):
            self.assertTrue(re.search(r'^\d{14}$', PtProvider.company_id()))

    def test_pt_BR_cnpj(self):
        for _ in range(100):
            cnpj = PtProvider.cnpj()
            self.assertTrue(re.search(r'\d{2}\.\d{3}\.\d{3}/0001-\d{2}', cnpj))


class TestHuHU(unittest.TestCase):
    """ Tests company in the hu_HU locale """

    def setUp(self):
        self.factory = Factory.create('hu_HU')

    def test_company_suffix(self):
        suffixes = HuProvider.company_suffixes
        suffix = self.factory.company_suffix()
        assert isinstance(suffix, string_types)
        assert suffix in suffixes

    def test_company(self):
        company = self.factory.company()
        assert isinstance(company, string_types)


class TestPlPL(unittest.TestCase):
    """ Tests company in the pl_PL locale """

    def setUp(self):
        self.factory = Factory.create('pl_PL')

    def test_regon_checksum(self):
        self.assertEqual(regon_checksum([1, 2, 3, 4, 5, 6, 7, 8]), 5)
        self.assertEqual(regon_checksum([8, 9, 1, 9, 5, 7, 8, 8]), 3)
        self.assertEqual(regon_checksum([2, 1, 7, 1, 5, 4, 8, 3]), 8)
        self.assertEqual(regon_checksum([7, 9, 3, 5, 4, 7, 9, 3]), 9)
        self.assertEqual(regon_checksum([9, 1, 5, 9, 6, 9, 4, 7]), 7)

    def test_regon(self):
        for _ in range(100):
            self.assertTrue(re.search(r'^\d{9}$', PlProvider.regon()))

    def test_local_regon_checksum(self):
        self.assertEqual(local_regon_checksum([1, 2, 3, 4, 5, 6, 7, 8, 5, 1, 2, 3, 4]), 7)
        self.assertEqual(local_regon_checksum([6, 1, 1, 9, 4, 8, 8, 3, 2, 7, 5, 8, 0]), 3)
        self.assertEqual(local_regon_checksum([8, 9, 2, 0, 0, 3, 6, 6, 0, 7, 0, 3, 2]), 3)
        self.assertEqual(local_regon_checksum([3, 5, 7, 7, 1, 0, 2, 2, 2, 5, 4, 3, 3]), 0)
        self.assertEqual(local_regon_checksum([9, 3, 5, 3, 1, 1, 0, 1, 2, 4, 8, 8, 2]), 1)

    def test_local_regon(self):
        for _ in range(100):
            self.assertTrue(re.search(r'^\d{14}$', PlProvider.local_regon()))

    def test_company_vat_checksum(self):
        self.assertEqual(company_vat_checksum([7, 7, 5, 7, 7, 7, 6, 0, 5]), 9)
        self.assertEqual(company_vat_checksum([1, 8, 6, 5, 4, 9, 9, 6, 4]), 2)
        self.assertEqual(company_vat_checksum([7, 1, 2, 8, 9, 2, 4, 9, 9]), 7)
        self.assertEqual(company_vat_checksum([3, 5, 4, 6, 1, 0, 6, 5, 8]), 4)
        self.assertEqual(company_vat_checksum([3, 1, 9, 5, 5, 7, 0, 4, 5]), 0)

    def test_company_vat(self):
        for _ in range(100):
            self.assertTrue(re.search(r'^\d{10}$', PlProvider.company_vat()))
