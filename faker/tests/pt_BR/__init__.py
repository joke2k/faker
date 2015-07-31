#  -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import re

from faker import Factory


class pt_BR_FactoryTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = Factory.create('pt_BR')

    def test_pt_BR_ssn(self):
        from faker.providers.ssn.pt_BR import Provider
        for i in range(100):
            self.assertRegexpMatches(Provider.ssn(),r'^\d{11}$')

    def test_pt_BR_cpf(self):
        from faker.providers.ssn.pt_BR import Provider
        for i in range(100):
            self.assertTrue(re.search(r'\d{3}\.\d{3}\.\d{3}\-\d{2}', Provider.cpf()))
