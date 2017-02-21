#  -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import re

from faker import Factory
from faker.providers.ssn.hr_HR import Provider, checksum


class hr_HR_FactoryTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = Factory.create('hr_HR')

    def test_hr_HR_ssn_checksum(self):
        self.assertEqual(checksum([0, 0, 2, 2, 8, 2, 6, 9, 2, 8]), 9)
        self.assertEqual(checksum([5, 8, 9, 3, 6, 9, 5, 1, 2, 5]), 1)
        self.assertEqual(checksum([5, 7, 8, 0, 2, 0, 3, 4, 2, 3]), 7)
        self.assertEqual(checksum([4, 3, 3, 3, 1, 4, 6, 7, 6, 2]), 2)
        self.assertEqual(checksum([0, 5, 9, 3, 7, 7, 5, 9, 1, 8]), 7)
        self.assertEqual(checksum([7, 1, 1, 4, 9, 9, 1, 2, 4, 1]), 6)

    def test_hr_HR_ssn(self):
        for i in range(100):
            self.assertTrue(re.search(r'^\d{11}$', Provider.ssn()))
