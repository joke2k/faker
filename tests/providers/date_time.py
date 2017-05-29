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


class TestPlPL(unittest.TestCase):

    DAY_NAMES = (
        'poniedziałek',
        'wtorek',
        'środa',
        'czwartek',
        'piątek',
        'sobota',
        'niedziela',
    )

    MONTH_NAMES = (
        'styczeń',
        'luty',
        'marzec',
        'kwiecień',
        'maj',
        'czerwiec',
        'lipiec',
        'sierpień',
        'wrzesień',
        'październik',
        'listopad',
        'grudzień'
    )

    def setUp(self):
        self.factory = Factory.create('pl_PL')

    def test_day(self):
        day = self.factory.day_of_week()
        assert day in self.DAY_NAMES

    def test_month(self):
        month = self.factory.month_name()
        assert month in self.MONTH_NAMES
