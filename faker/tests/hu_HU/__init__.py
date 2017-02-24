# coding=utf-8

from __future__ import unicode_literals

import unittest
import re

from faker import Factory


class hu_HU_FactoryTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = Factory.create('hu_HU')

    def test_hungarian_postcodes_for_consistency(self):
        # Hungarian postcodes may not begin with a zero. This test case tests for consistency with that rule.

        from faker.providers.address.hu_HU import Provider

        for i in range(100):
            pcd = Provider.postcode()
            assert pcd[2] > "0"
