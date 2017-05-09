# coding: utf-8

from __future__ import unicode_literals

import unittest
from faker import Factory
from .. import string_types

class TestHuHU(unittest.TestCase):
    """ Tests date_time in hu_HU locale. """

    def setUp(self):
        self.factory = Factory.create('hu_HU')

    def test_day(self):
        day = self.factory.day_of_week()
        assert isinstance(day, string_types)

    def test_month(self):
        month = self.factory.month()
        assert isinstance(month, string_types)

