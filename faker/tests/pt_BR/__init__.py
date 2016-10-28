#  -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import re

from faker import Factory
from faker.providers.company.pt_BR import Provider as CompanyProvider, company_id_checksum
from faker.providers.ssn.pt_BR import Provider, checksum


class pt_BR_FactoryTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = Factory.create('pt_BR')

    def test_pt_BR_ssn_checksum(self):
        self.assertEqual(checksum([8, 8, 2, 8, 2, 1, 6, 5, 2]), 2)
        self.assertEqual(checksum([8, 8, 2, 8, 2, 1, 6, 5, 2, 2]), 1)

    def test_pt_BR_ssn(self):
        for _ in range(100):
            self.assertTrue(re.search(r'^\d{11}$', Provider.ssn()))

    def test_pt_BR_cpf(self):
        for _ in range(100):
            self.assertTrue(re.search(r'\d{3}\.\d{3}\.\d{3}\-\d{2}', Provider.cpf()))

    def test_pt_BR_company_id_checksum(self):
        self.assertEqual(company_id_checksum([9, 4, 9, 5, 3, 4, 4, 1, 0, 0, 0, 1]), [5, 1])
        self.assertEqual(company_id_checksum([1, 6, 0, 0, 4, 6, 3, 9, 0, 0, 0, 1]), [8, 5])

    def test_pt_BR_company_id(self):
        for _ in range(100):
            self.assertTrue(re.search(r'^\d{14}$', CompanyProvider.company_id()))

    def test_pt_BR_cnpj(self):
        for _ in range(100):
            cnpj = CompanyProvider.cnpj()
            self.assertTrue(re.search(r'\d{2}\.\d{3}\.\d{3}/0001-\d{2}', cnpj))
