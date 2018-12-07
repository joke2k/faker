# coding=utf-8

from __future__ import unicode_literals

import unittest
import re

import six

from faker import Faker
from faker.providers.company.ja_JP import Provider as JaProvider
from faker.providers.company.pt_BR import company_id_checksum
from faker.providers.company.pl_PL import (
    company_vat_checksum, regon_checksum, local_regon_checksum, Provider as PlProvider,
)


class TestFiFI(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('fi_FI')

    def test_company_business_id(self):
        self.factory.random.seed(6)
        company_id = self.factory.company_business_id()
        assert company_id.endswith('0')
        for seed in range(0, 11):
            self.factory.random.seed(seed)
            self.factory.company_business_id()


class TestJaJP(unittest.TestCase):
    """ Tests companies in the ja_JP locale """

    def setUp(self):
        self.factory = Faker('ja')

    def test_company(self):
        prefixes = JaProvider.company_prefixes
        prefix = self.factory.company_prefix()
        assert isinstance(prefix, six.string_types)
        assert prefix in prefixes

        categories = JaProvider.company_categories
        category = self.factory.company_category()
        assert isinstance(category, six.string_types)
        assert category in categories

        company = self.factory.company()
        assert isinstance(company, six.string_types)
        assert any(company.startswith(prefix) or company.endswith(prefix) for prefix in prefixes)
        assert any(category in company for category in categories)


class TestPtBR(unittest.TestCase):
    """ Tests company in the pt_BR locale """

    def setUp(self):
        self.factory = Faker('pt_BR')

    def test_pt_BR_company_id_checksum(self):
        assert company_id_checksum([9, 4, 9, 5, 3, 4, 4, 1, 0, 0, 0, 1]) == [5, 1]
        assert company_id_checksum([1, 6, 0, 0, 4, 6, 3, 9, 0, 0, 0, 1]) == [8, 5]

    def test_pt_BR_company_id(self):
        for _ in range(100):
            assert re.search(r'^\d{14}$', self.factory.company_id())

    def test_pt_BR_cnpj(self):
        for _ in range(100):
            cnpj = self.factory.cnpj()
            assert re.search(r'\d{2}\.\d{3}\.\d{3}/0001-\d{2}', cnpj)


class TestHuHU(unittest.TestCase):
    """ Tests company in the hu_HU locale """

    def setUp(self):
        self.factory = Faker('hu_HU')
        self.valid_suffixes = ('Kft.', 'Kht.', 'Zrt.', 'Bt.', 'Nyrt.', 'Kkt.')

    def test_company_suffix(self):
        suffix = self.factory.company_suffix()
        assert isinstance(suffix, six.string_types)
        assert suffix in self.valid_suffixes

    def test_company(self):
        company = self.factory.company()
        assert isinstance(company, six.string_types)
        assert company.split(" ")[-1] in self.valid_suffixes


class TestPlPL(unittest.TestCase):
    """ Tests company in the pl_PL locale """

    def setUp(self):
        self.factory = Faker('pl_PL')

    def test_regon_checksum(self):
        assert regon_checksum([1, 2, 3, 4, 5, 6, 7, 8]) == 5
        assert regon_checksum([8, 9, 1, 9, 5, 7, 8, 8]) == 3
        assert regon_checksum([2, 1, 7, 1, 5, 4, 8, 3]) == 8
        assert regon_checksum([7, 9, 3, 5, 4, 7, 9, 3]) == 9
        assert regon_checksum([9, 1, 5, 9, 6, 9, 4, 7]) == 7

    def test_regon(self):
        for _ in range(100):
            assert re.search(r'^\d{9}$', self.factory.regon())

    def test_local_regon_checksum(self):
        assert local_regon_checksum([1, 2, 3, 4, 5, 6, 7, 8, 5, 1, 2, 3, 4]) == 7
        assert local_regon_checksum([6, 1, 1, 9, 4, 8, 8, 3, 2, 7, 5, 8, 0]) == 3
        assert local_regon_checksum([8, 9, 2, 0, 0, 3, 6, 6, 0, 7, 0, 3, 2]) == 3
        assert local_regon_checksum([3, 5, 7, 7, 1, 0, 2, 2, 2, 5, 4, 3, 3]) == 0
        assert local_regon_checksum([9, 3, 5, 3, 1, 1, 0, 1, 2, 4, 8, 8, 2]) == 1

    def test_local_regon(self):
        for _ in range(100):
            assert re.search(r'^\d{14}$', self.factory.local_regon())

    def test_company_vat_checksum(self):
        assert company_vat_checksum([7, 7, 5, 7, 7, 7, 6, 0, 5]) == 9
        assert company_vat_checksum([1, 8, 6, 5, 4, 9, 9, 6, 4]) == 2
        assert company_vat_checksum([7, 1, 2, 8, 9, 2, 4, 9, 9]) == 7
        assert company_vat_checksum([3, 5, 4, 6, 1, 0, 6, 5, 8]) == 4
        assert company_vat_checksum([3, 1, 9, 5, 5, 7, 0, 4, 5]) == 0

    def test_company_vat(self):
        for _ in range(100):
            assert re.search(r'^\d{10}$', self.factory.company_vat())

    def test_company_prefix(self):
        prefixes = PlProvider.company_prefixes
        prefix = self.factory.company_prefix()
        assert isinstance(prefix, six.string_types)
        assert prefix in prefixes

    def test_company_suffix(self):
        suffixes = PlProvider.company_suffixes
        suffix = self.factory.company_suffix()
        assert isinstance(suffix, six.string_types)
        assert suffix in suffixes
