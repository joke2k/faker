# coding: utf-8
from __future__ import unicode_literals

from datetime import date, datetime, timedelta, tzinfo
from datetime import time as datetime_time
import time
import unittest

from faker import Factory
from faker.generator import random
from faker.providers.date_time import Provider as DatetimeProvider
from .. import string_types


class UTC(tzinfo):
    """
    UTC implementation taken from Python's docs.
    """

    def __repr__(self):
        return "<UTC>"

    def utcoffset(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return timedelta(0)


utc = UTC()


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

    def test_timezone_conversion(self):
        from faker.providers.date_time import datetime_to_timestamp

        now = datetime.now(utc).replace(microsecond=0)
        timestamp = datetime_to_timestamp(now)
        now_back = datetime.fromtimestamp(timestamp, utc)
        self.assertEqual(now, now_back)

        today = date.today()
        timestamp = datetime_to_timestamp(today)
        today_back = datetime.fromtimestamp(timestamp, utc).date()
        self.assertEqual(today, today_back)

    def test_datetime_safe(self):
        from faker.utils import datetime_safe
        # test using example provided in module
        result = datetime_safe.date(1850, 8, 2).strftime('%Y/%m/%d was a %A')
        self.assertEqual(result, '1850/08/02 was a Friday')
        # test against certain formatting strings used on pre-1900 dates
        with self.assertRaises(TypeError):
            datetime_safe.date(1850, 8, 2).strftime('%s')
        with self.assertRaises(TypeError):
            datetime_safe.date(1850, 8, 2).strftime('%y')
        # test using 29-Feb-2012 and escaped percentage sign
        result = datetime_safe.date(2012, 2, 29).strftime('%Y-%m-%d was a 100%% %A')
        self.assertEqual(result, r'2012-02-29 was a 100% Wednesday')
        # test that certain formatting strings are allowed on post-1900 dates
        result = datetime_safe.date(2008, 2, 29).strftime('%y')
        self.assertEqual(result, r'08')

    def test_datetime_safe_new_date(self):
        from faker.utils import datetime_safe
        d = datetime_safe.date(1850, 8, 2)
        result = datetime_safe.new_date(d)
        self.assertEqual(result, date(1850, 8, 2))

    def test_datetimes_with_and_without_tzinfo(self):
        from faker.providers.date_time import Provider
        provider = Provider

        self.assertEqual(provider.date_time().tzinfo, None)
        self.assertEqual(provider.date_time(utc).tzinfo, utc)

        self.assertEqual(provider.date_time_ad().tzinfo, None)
        self.assertEqual(provider.date_time_ad(utc).tzinfo, utc)

        self.assertFalse(provider.iso8601().endswith('+00:00'))
        self.assertTrue(provider.iso8601(utc).endswith('+00:00'))

    def test_date_object(self):
        from faker.providers.date_time import Provider
        provider = Provider

        self.assertIsInstance(provider.date_object(), date)

    def test_time_object(self):
        from faker.providers.date_time import Provider
        provider = Provider

        self.assertIsInstance(provider.time_object(), datetime_time)

    def test_date_time_between_dates(self):
        from faker.providers.date_time import Provider
        provider = Provider

        timestamp_start = random.randint(0, 2000000000)
        timestamp_end = timestamp_start + 1

        datetime_start = datetime.fromtimestamp(timestamp_start)
        datetime_end = datetime.fromtimestamp(timestamp_end)

        random_date = provider.date_time_between_dates(datetime_start, datetime_end)
        self.assertTrue(datetime_start <= random_date)
        self.assertTrue(datetime_end >= random_date)

    def test_date_time_between_dates_with_tzinfo(self):
        from faker.providers.date_time import Provider
        provider = Provider

        timestamp_start = random.randint(0, 2000000000)
        timestamp_end = timestamp_start + 1

        datetime_start = datetime.fromtimestamp(timestamp_start, utc)
        datetime_end = datetime.fromtimestamp(timestamp_end, utc)

        random_date_naive = provider.date_time_between_dates(datetime_start, datetime_end)
        with self.assertRaises(TypeError):
            datetime_start <= random_date_naive

        random_date = provider.date_time_between_dates(datetime_start, datetime_end, utc)
        self.assertTrue(datetime_start <= random_date)
        self.assertTrue(datetime_end >= random_date)

    def _datetime_to_time(self, value):
        return int(time.mktime(value.timetuple()))

    def test_date_time_this_period(self):
        from faker.providers.date_time import Provider
        provider = Provider
        # test century
        self.assertTrue(self._datetime_to_time(provider.date_time_this_century(after_now=False)) <= self._datetime_to_time(datetime.now()))
        self.assertTrue(self._datetime_to_time(provider.date_time_this_century(before_now=False, after_now=True)) >= self._datetime_to_time(datetime.now()))
        # test decade
        self.assertTrue(self._datetime_to_time(provider.date_time_this_decade(after_now=False)) <= self._datetime_to_time(datetime.now()))
        self.assertTrue(self._datetime_to_time(provider.date_time_this_decade(before_now=False, after_now=True)) >= self._datetime_to_time(datetime.now()))
        self.assertEqual(
            self._datetime_to_time(provider.date_time_this_decade(before_now=False, after_now=False)),
            self._datetime_to_time(datetime.now())
        )
        # test year
        self.assertTrue(self._datetime_to_time(provider.date_time_this_year(after_now=False)) <= self._datetime_to_time(datetime.now()))
        self.assertTrue(self._datetime_to_time(provider.date_time_this_year(before_now=False, after_now=True)) >= self._datetime_to_time(datetime.now()))
        self.assertEqual(
            self._datetime_to_time(provider.date_time_this_year(before_now=False, after_now=False)),
            self._datetime_to_time(datetime.now())
        )
        # test month
        self.assertTrue(self._datetime_to_time(provider.date_time_this_month(after_now=False)) <= self._datetime_to_time(datetime.now()))
        self.assertTrue(self._datetime_to_time(provider.date_time_this_month(before_now=False, after_now=True)) >= self._datetime_to_time(datetime.now()))
        self.assertEqual(
            self._datetime_to_time(provider.date_time_this_month(before_now=False, after_now=False)),
            self._datetime_to_time(datetime.now())
        )

    def test_date_time_this_period_with_tzinfo(self):
        from faker.providers.date_time import Provider
        provider = Provider

        # ensure all methods provide timezone aware datetimes
        with self.assertRaises(TypeError):
            provider.date_time_this_century(before_now=False, after_now=True, tzinfo=utc) >= datetime.now()
        with self.assertRaises(TypeError):
            provider.date_time_this_decade(after_now=False, tzinfo=utc) <= datetime.now()
        with self.assertRaises(TypeError):
            provider.date_time_this_year(after_now=False, tzinfo=utc) <= datetime.now()
        with self.assertRaises(TypeError):
            provider.date_time_this_month(after_now=False, tzinfo=utc) <= datetime.now()

        # test century
        self.assertTrue(provider.date_time_this_century(after_now=False, tzinfo=utc) <= datetime.now(utc))
        self.assertTrue(provider.date_time_this_century(before_now=False, after_now=True, tzinfo=utc) >= datetime.now(utc))
        # test decade
        self.assertTrue(provider.date_time_this_decade(after_now=False, tzinfo=utc) <= datetime.now(utc))
        self.assertTrue(provider.date_time_this_decade(before_now=False, after_now=True, tzinfo=utc) >= datetime.now(utc))

        self.assertEqual(
            provider.date_time_this_decade(before_now=False, after_now=False, tzinfo=utc).replace(second=0, microsecond=0),
            datetime.now(utc).replace(second=0, microsecond=0)
        )
        # test year
        self.assertTrue(provider.date_time_this_year(after_now=False, tzinfo=utc) <= datetime.now(utc))
        self.assertTrue(provider.date_time_this_year(before_now=False, after_now=True, tzinfo=utc) >= datetime.now(utc))
        self.assertEqual(
            provider.date_time_this_year(before_now=False, after_now=False, tzinfo=utc).replace(second=0, microsecond=0),
            datetime.now(utc).replace(second=0, microsecond=0)
        )
        # test month
        self.assertTrue(provider.date_time_this_month(after_now=False, tzinfo=utc) <= datetime.now(utc))
        self.assertTrue(provider.date_time_this_month(before_now=False, after_now=True, tzinfo=utc) >= datetime.now(utc))
        self.assertEqual(
            provider.date_time_this_month(before_now=False, after_now=False, tzinfo=utc).replace(second=0, microsecond=0),
            datetime.now(utc).replace(second=0, microsecond=0)
        )


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
