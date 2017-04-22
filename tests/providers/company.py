# coding=utf-8

from __future__ import unicode_literals

import unittest
import re

from faker import Factory
from faker.providers.company.hu_HU import Provider as HuProvider
from faker.providers.company.ja_JP import Provider as JaProvider
from faker.providers.company.pt_BR import Provider as PtProvider, company_id_checksum
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
