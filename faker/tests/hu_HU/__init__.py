# coding=utf-8

from __future__ import unicode_literals

import unittest
import re

from faker import Factory


class hu_HU_FactoryTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = Factory.create('hu_HU')

