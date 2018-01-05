# coding: utf-8
from __future__ import unicode_literals

from datetime import date, datetime, timedelta, tzinfo
from datetime import time as datetime_time
import time
import unittest
import random

from faker import Faker
from faker.providers.date_time import Provider as DatetimeProvider
from faker.providers.date_time.pl_PL import Provider as PlProvider
from faker.providers.date_time.ar_AA import Provider as ArProvider
from faker.providers.date_time.ar_EG import Provider as EgProvider

from tests import string_types


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


class TestKoKR(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('ko_KR')

    def test_day(self):
        day = self.factory.day_of_week()
        assert isinstance(day, string_types)

    def test_month(self):
        month = self.factory.month()
        assert isinstance(month, string_types)


class TestDateTime(unittest.TestCase):

    def setUp(self):
        self.factory = Faker()

    def assertBetween(self, date, start_date, end_date):
        self.assertTrue(date <= end_date)
        self.assertTrue(date >= start_date)

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
        delta = timedelta(days=-30)
        from_delta = DatetimeProvider._parse_date_time(delta)
        from_int = DatetimeProvider._parse_date_time(30)

        self.assertEqual(datetime.fromtimestamp(from_delta).date(),
                         datetime.fromtimestamp(timestamp).date())

        self.assertEqual(datetime.fromtimestamp(from_int).date(),
                         datetime.fromtimestamp(timestamp).date())

    def test_parse_date(self):
        parsed = DatetimeProvider._parse_date('+30d')
        now = DatetimeProvider._parse_date('now')
        today = DatetimeProvider._parse_date('today')
        self.assertIsInstance(parsed, date)
        self.assertIsInstance(now, date)
        self.assertIsInstance(today, date)
        self.assertEqual(today, date.today())
        self.assertEqual(now, today)
        self.assertEqual(parsed, today + timedelta(days=30))
        self.assertEqual(DatetimeProvider._parse_date(datetime.now()), today)
        self.assertEqual(DatetimeProvider._parse_date(parsed), parsed)
        self.assertEqual(DatetimeProvider._parse_date(30), parsed)
        self.assertEqual(DatetimeProvider._parse_date(timedelta(days=-30)), parsed)

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
        self.assertEqual(self.factory.date_time().tzinfo, None)
        self.assertEqual(self.factory.date_time(utc).tzinfo, utc)

        self.assertEqual(self.factory.date_time_ad().tzinfo, None)
        self.assertEqual(self.factory.date_time_ad(utc).tzinfo, utc)

        self.assertFalse(self.factory.iso8601().endswith('+00:00'))
        self.assertTrue(self.factory.iso8601(utc).endswith('+00:00'))

    def test_date_object(self):
        self.assertIsInstance(self.factory.date_object(), date)

    def test_time_object(self):
        self.assertIsInstance(self.factory.time_object(), datetime_time)

    def test_date_time_between_dates(self):
        timestamp_start = random.randint(0, 2000000000)
        timestamp_end = timestamp_start + 1

        datetime_start = datetime.fromtimestamp(timestamp_start)
        datetime_end = datetime.fromtimestamp(timestamp_end)

        random_date = self.factory.date_time_between_dates(datetime_start, datetime_end)
        self.assertTrue(datetime_start <= random_date)
        self.assertTrue(datetime_end >= random_date)

    def test_date_time_between_dates_with_tzinfo(self):
        timestamp_start = random.randint(0, 2000000000)
        timestamp_end = timestamp_start + 1

        datetime_start = datetime.fromtimestamp(timestamp_start, utc)
        datetime_end = datetime.fromtimestamp(timestamp_end, utc)

        random_date_naive = self.factory.date_time_between_dates(datetime_start, datetime_end)
        with self.assertRaises(TypeError):
            datetime_start <= random_date_naive

        random_date = self.factory.date_time_between_dates(datetime_start, datetime_end, utc)
        self.assertTrue(datetime_start <= random_date)
        self.assertTrue(datetime_end >= random_date)

    def test_past_datetime_within_second(self):
        # Should not raise a ``ValueError``
        self.factory.past_datetime(start_date='+1s')

    def test_date_between_dates(self):
        date_end = date.today()
        date_start = date_end - timedelta(days=10)

        random_date = self.factory.date_between_dates(date_start, date_end)
        self.assertTrue(date_start <= random_date)
        self.assertTrue(date_end >= random_date)

    def _datetime_to_time(self, value):
        return int(time.mktime(value.timetuple()))

    def test_date_time_this_period(self):
        # test century
        self.assertTrue(self._datetime_to_time(self.factory.date_time_this_century(after_now=False)) <= self._datetime_to_time(datetime.now()))
        self.assertTrue(self._datetime_to_time(self.factory.date_time_this_century(before_now=False, after_now=True)) >= self._datetime_to_time(datetime.now()))
        # test decade
        self.assertTrue(self._datetime_to_time(self.factory.date_time_this_decade(after_now=False)) <= self._datetime_to_time(datetime.now()))
        self.assertTrue(self._datetime_to_time(self.factory.date_time_this_decade(before_now=False, after_now=True)) >= self._datetime_to_time(datetime.now()))
        self.assertEqual(
            self._datetime_to_time(self.factory.date_time_this_decade(before_now=False, after_now=False)),
            self._datetime_to_time(datetime.now())
        )
        # test year
        self.assertTrue(self._datetime_to_time(self.factory.date_time_this_year(after_now=False)) <= self._datetime_to_time(datetime.now()))
        self.assertTrue(self._datetime_to_time(self.factory.date_time_this_year(before_now=False, after_now=True)) >= self._datetime_to_time(datetime.now()))
        self.assertEqual(
            self._datetime_to_time(self.factory.date_time_this_year(before_now=False, after_now=False)),
            self._datetime_to_time(datetime.now())
        )
        # test month
        self.assertTrue(self._datetime_to_time(self.factory.date_time_this_month(after_now=False)) <= self._datetime_to_time(datetime.now()))
        self.assertTrue(self._datetime_to_time(self.factory.date_time_this_month(before_now=False, after_now=True)) >= self._datetime_to_time(datetime.now()))
        self.assertEqual(
            self._datetime_to_time(self.factory.date_time_this_month(before_now=False, after_now=False)),
            self._datetime_to_time(datetime.now())
        )

    def test_date_time_this_period_with_tzinfo(self):
        # ensure all methods provide timezone aware datetimes
        with self.assertRaises(TypeError):
            self.factory.date_time_this_century(before_now=False, after_now=True, tzinfo=utc) >= datetime.now()
        with self.assertRaises(TypeError):
            self.factory.date_time_this_decade(after_now=False, tzinfo=utc) <= datetime.now()
        with self.assertRaises(TypeError):
            self.factory.date_time_this_year(after_now=False, tzinfo=utc) <= datetime.now()
        with self.assertRaises(TypeError):
            self.factory.date_time_this_month(after_now=False, tzinfo=utc) <= datetime.now()

        # test century
        self.assertTrue(self.factory.date_time_this_century(after_now=False, tzinfo=utc) <= datetime.now(utc))
        self.assertTrue(self.factory.date_time_this_century(before_now=False, after_now=True, tzinfo=utc) >= datetime.now(utc))
        # test decade
        self.assertTrue(self.factory.date_time_this_decade(after_now=False, tzinfo=utc) <= datetime.now(utc))
        self.assertTrue(self.factory.date_time_this_decade(before_now=False, after_now=True, tzinfo=utc) >= datetime.now(utc))

        self.assertEqual(
            self.factory.date_time_this_decade(before_now=False, after_now=False, tzinfo=utc).replace(second=0, microsecond=0),
            datetime.now(utc).replace(second=0, microsecond=0)
        )
        # test year
        self.assertTrue(self.factory.date_time_this_year(after_now=False, tzinfo=utc) <= datetime.now(utc))
        self.assertTrue(self.factory.date_time_this_year(before_now=False, after_now=True, tzinfo=utc) >= datetime.now(utc))
        self.assertEqual(
            self.factory.date_time_this_year(before_now=False, after_now=False, tzinfo=utc).replace(second=0, microsecond=0),
            datetime.now(utc).replace(second=0, microsecond=0)
        )
        # test month
        self.assertTrue(self.factory.date_time_this_month(after_now=False, tzinfo=utc) <= datetime.now(utc))
        self.assertTrue(self.factory.date_time_this_month(before_now=False, after_now=True, tzinfo=utc) >= datetime.now(utc))
        self.assertEqual(
            self.factory.date_time_this_month(before_now=False, after_now=False, tzinfo=utc).replace(second=0, microsecond=0),
            datetime.now(utc).replace(second=0, microsecond=0)
        )

    def test_date_this_period(self):
        # test century
        self.assertTrue(self.factory.date_this_century(after_today=False) <= date.today())
        self.assertTrue(self.factory.date_this_century(before_today=False, after_today=True) >= date.today())
        # test decade
        self.assertTrue(self.factory.date_this_decade(after_today=False) <= date.today())
        self.assertTrue(self.factory.date_this_decade(before_today=False, after_today=True) >= date.today())
        self.assertEqual(
            self.factory.date_this_decade(before_today=False, after_today=False),
            date.today()
        )
        # test year
        self.assertTrue(self.factory.date_this_year(after_today=False) <= date.today())
        self.assertTrue(self.factory.date_this_year(before_today=False, after_today=True) >= date.today())
        self.assertEqual(
            self.factory.date_this_year(before_today=False, after_today=False),
            date.today()
        )
        # test month
        self.assertTrue(self.factory.date_this_month(after_today=False) <= date.today())
        self.assertTrue(self.factory.date_this_month(before_today=False, after_today=True) >= date.today())
        self.assertEqual(
            self.factory.date_this_month(before_today=False, after_today=False),
            datetime.now()
        )

    def test_date_time_between(self):
        now = datetime.now()
        _30_years_ago = now.replace(year=now.year - 30)
        _20_years_ago = now.replace(year=now.year - 20)

        random_datetime = self.factory.date_time_between(start_date='-30y', end_date='-20y')

        self.assertIsInstance(random_datetime, datetime)
        self.assertBetween(random_datetime, _30_years_ago, _20_years_ago)

    def test_date_between(self):
        today = date.today()
        _30_years_ago = today.replace(year=today.year - 30)
        _20_years_ago = today.replace(year=today.year - 20)

        random_date = self.factory.date_between(start_date='-30y', end_date='-20y')

        self.assertIsInstance(random_date, date)
        self.assertBetween(random_date, _30_years_ago, _20_years_ago)

    def test_parse_timedelta(self):
        from faker.providers.date_time import Provider

        td = timedelta(days=7)
        seconds = Provider._parse_timedelta(td)
        self.assertEqual(seconds, 604800.0)

        seconds = Provider._parse_timedelta('+1w')
        self.assertEqual(seconds, 604800.0)

        seconds = Provider._parse_timedelta('+1y')
        self.assertEqual(seconds, 31556736.0)

        with self.assertRaises(ValueError):
            Provider._parse_timedelta('foobar')

    def test_time_series(self):
        series = [i for i in self.factory.time_series()]
        self.assertTrue(len(series), 30)
        self.assertTrue(series[1][0] - series[0][0], timedelta(days=1))

        uniform = lambda dt: random.uniform(0, 5)  # noqa
        series = [i for i in self.factory.time_series('now', '+1w', '+1d', uniform)]
        self.assertTrue(len(series), 7)
        self.assertTrue(series[1][0] - series[0][0], timedelta(days=1))

        end = datetime.now() + timedelta(days=7)
        series = [i for i in self.factory.time_series('now', end, '+1d', uniform)]
        self.assertTrue(len(series), 7)
        self.assertTrue(series[1][0] - series[0][0], timedelta(days=1))

        self.assertTrue(series[-1][0] <= end)

        with self.assertRaises(ValueError):
            [i for i in self.factory.time_series('+1w', 'now', '+1d', uniform)]

        with self.assertRaises(ValueError):
            [i for i in self.factory.time_series('now', '+1w', '+1d', 'uniform')]

        series = [i for i in self.factory.time_series('now', end, '+1d', uniform, tzinfo=utc)]
        self.assertTrue(len(series), 7)
        self.assertTrue(series[1][0] - series[0][0], timedelta(days=1))

        # avoid microseconds as provider's internal parsing uses POSIX timestamps which only have second granularity
        end = datetime.now(utc).replace(microsecond=0)
        start = end - timedelta(days=15)

        series = [i for i in self.factory.time_series(start_date=start, end_date=end, tzinfo=start.tzinfo)]
        self.assertEqual(series[0][0], start)


class TestPlPL(unittest.TestCase):

    def setUp(self):
        self.factory = Faker('pl_PL')
        self.provider = self.factory.provider('faker.providers.date_time')

    def test_day(self):
        day = self.factory.day_of_week()
        assert day in PlProvider.DAY_NAMES.values()

    def test_month(self):
        month = self.factory.month_name()
        assert month in PlProvider.MONTH_NAMES.values()


class TestAr(unittest.TestCase):
    def test_ar_aa(self):
        factory = Faker('ar')

        # AM/PM
        self.assertIn(factory.am_pm(), ArProvider.AM_PM.values())
        # Day of week
        self.assertIn(factory.century(), ArProvider.centuries)
        # Month name
        self.assertIn(
            factory.month_name(),
            ArProvider.MONTH_NAMES.values()
        )
        # Day of week
        self.assertIn(
            factory.day_of_week(),
            ArProvider.DAY_NAMES.values()
        )

    def test_ar_eg(self):
        factory = Faker('ar_EG')

        # AM/PM
        self.assertIn(factory.am_pm(), ArProvider.AM_PM.values())
        # Day of week
        self.assertIn(factory.century(), ArProvider.centuries)
        # Day of week
        self.assertIn(
            factory.day_of_week(),
            ArProvider.DAY_NAMES.values()
        )
        # Month name
        self.assertIn(
            factory.month_name(),
            EgProvider.MONTH_NAMES.values()
        )
        # Month name
        self.assertNotIn(
            factory.month_name(),
            ArProvider.MONTH_NAMES.values()
        )
