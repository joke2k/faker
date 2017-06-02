# coding: utf-8
from __future__ import unicode_literals

from datetime import date, datetime
import unittest

from faker import Factory
from faker.providers.date_time import Provider as DatetimeProvider
from .. import string_types


class TestDateTime(unittest.TestCase):

    def setUp(self):
        self.factory = Factory.create()

    def test_day(self):
        day = self.factory.day_of_week()
        assert isinstance(day, string_types)

    def test_month(self):
        month = self.factory.month()
        assert isinstance(month, string_types)

    def test_past_datetime(self):
        past_datetime = self.factory.past_datetime()
        self.assertTrue(past_datetime < datetime.now())

    def test_past_date(self):
        past_date = self.factory.past_date()
        self.assertTrue(past_date < date.today())

    def test_future_datetime(self):
        future_datetime, now = self.factory.future_datetime(), datetime.now()
        self.assertTrue(future_datetime > now)

    def test_future_date(self):
        future_date = self.factory.future_date()
        self.assertTrue(future_date > date.today())

    def test_parse_date_time(self):
        timestamp = DatetimeProvider._parse_date_time('+30d')
        now = DatetimeProvider._parse_date_time('now')
        self.assertTrue(timestamp > now)


class TestPlPL(unittest.TestCase):

    def setUp(self):
        self.factory = Factory.create('pl_PL')
        self.provider = self.factory.provider('faker.providers.date_time')

    def test_day(self):
        day = self.factory.day_of_week()
        assert day in self.provider.DAY_NAMES.values()

    def test_month(self):
        month = self.factory.month_name()
        assert month in self.provider.MONTH_NAMES.values()
