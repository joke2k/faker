# coding=utf-8

from __future__ import unicode_literals

import unittest
import re

from faker import Factory


class no_NO_FactoryTestCase(unittest.TestCase):

    def setUp(self):
        self.factory = Factory.create('no_NO')

    def test_en_GB_postcode(self):
        for i in range(100):
            self.assertTrue(re.match(r'^[0-9]{4}$', self.factory.postcode()))
