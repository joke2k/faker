#  -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import re

from faker import Factory
from faker.providers.ssn.pt_BR import Provider, checksum


class pt_BR_FactoryTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = Factory.create('pt_BR')

    def test_pt_BR_ssn_checksum(self):
        self.assertEqual(checksum([8, 8, 2, 8, 2, 1, 6, 5, 2]), 2)
        self.assertEqual(checksum([8, 8, 2, 8, 2, 1, 6, 5, 2, 2]), 1)

    def test_pt_BR_ssn(self):
        for i in range(100):
            self.assertTrue(re.search(r'^\d{11}$', Provider.ssn()))

    def test_pt_BR_cpf(self):
        for i in range(100):
            self.assertTrue(re.search(r'\d{3}\.\d{3}\.\d{3}\-\d{2}', Provider.cpf()))
