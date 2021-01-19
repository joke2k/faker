import os
import platform
import random
import re
import sys
import time
import unittest

from datetime import date, datetime
from datetime import time as datetime_time
from datetime import timedelta, tzinfo

import freezegun
import pytest

from faker import Faker
from faker.providers.date_time import Provider as DatetimeProvider
from faker.providers.date_time import change_year
from faker.providers.date_time.ar_AA import Provider as ArProvider
from faker.providers.date_time.ar_EG import Provider as EgProvider
from faker.providers.date_time.cs_CZ import Provider as CsCzProvider
from faker.providers.date_time.de_AT import Provider as DeAtProvider
from faker.providers.date_time.de_DE import Provider as DeDeProvider
from faker.providers.date_time.es_ES import Provider as EsEsProvider
from faker.providers.date_time.hy_AM import Provider as HyAmProvider
from faker.providers.date_time.it_IT import Provider as ItItProvider
from faker.providers.date_time.pl_PL import Provider as PlProvider
from faker.providers.date_time.pt_PT import Provider as PtPtProvider
from faker.providers.date_time.ru_RU import Provider as RuProvider
from faker.providers.date_time.sk_SK import Provider as SkSkProvider
from faker.providers.date_time.ta_IN import Provider as TaInProvider
from faker.providers.date_time.tr_TR import Provider as TrTrProvider


def is64bit():
    return sys.maxsize > 2**32


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
        self.fake = Faker('ko_KR')
        Faker.seed(0)

    def test_day(self):
        day = self.fake.day_of_week()
        assert isinstance(day, str)

    def test_month(self):
        month = self.fake.month()
        assert isinstance(month, str)


class TestDateTime(unittest.TestCase):

    def setUp(self):
        self.fake = Faker()
        Faker.seed(0)

    def assertBetween(self, date, start_date, end_date):
        assert date <= end_date
        assert date >= start_date

    def test_day(self):
        day = self.fake.day_of_week()
        assert isinstance(day, str)

    def test_month(self):
        month = self.fake.month()
        assert isinstance(month, str)

    def test_past_datetime(self):
        past_datetime = self.fake.past_datetime()
        assert past_datetime < datetime.now()

    def test_past_date(self):
        past_date = self.fake.past_date()
        assert past_date < date.today()

    def test_future_datetime(self):
        future_datetime, now = self.fake.future_datetime(), datetime.now()
        assert future_datetime > now

    def test_future_date(self):
        future_date = self.fake.future_date()
        assert future_date > date.today()

    def test_parse_date_time(self):
        timestamp = DatetimeProvider._parse_date_time('+30d')
        now = DatetimeProvider._parse_date_time('now')
        assert timestamp > now
        delta = timedelta(days=30)
        from_delta = DatetimeProvider._parse_date_time(delta)
        from_int = DatetimeProvider._parse_date_time(30)

        assert datetime.fromtimestamp(from_delta).date() == (
                         datetime.fromtimestamp(timestamp).date())

        assert datetime.fromtimestamp(from_int).date() == (
                         datetime.fromtimestamp(timestamp).date())

    def test_parse_date(self):
        parsed = DatetimeProvider._parse_date('+30d')
        now = DatetimeProvider._parse_date('now')
        today = DatetimeProvider._parse_date('today')
        assert isinstance(parsed, date)
        assert isinstance(now, date)
        assert isinstance(today, date)
        assert today == date.today()
        assert now == today
        assert parsed == today + timedelta(days=30)
        assert DatetimeProvider._parse_date(datetime.now()) == today
        assert DatetimeProvider._parse_date(parsed) == parsed
        assert DatetimeProvider._parse_date(30) == parsed
        assert DatetimeProvider._parse_date(timedelta(days=30)) == parsed

    def test_timezone_conversion(self):
        from faker.providers.date_time import datetime_to_timestamp

        now = datetime.now(utc).replace(microsecond=0)
        timestamp = datetime_to_timestamp(now)
        now_back = datetime.fromtimestamp(timestamp, utc)
        assert now == now_back

        today = date.today()
        timestamp = datetime_to_timestamp(today)
        today_back = datetime.fromtimestamp(timestamp, utc).date()
        assert today == today_back

    def test_pytimezone(self):
        import dateutil
        pytz = self.fake.pytimezone()
        assert isinstance(pytz, dateutil.tz.tz.tzfile)

    def test_pytimezone_usable(self):
        pytz = self.fake.pytimezone()
        date = datetime(2000, 1, 1, tzinfo=pytz)
        assert date.tzinfo == pytz

    def test_datetimes_with_and_without_tzinfo(self):
        assert self.fake.date_time().tzinfo is None
        assert self.fake.date_time(utc).tzinfo == utc

        assert self.fake.date_time_ad().tzinfo is None
        assert self.fake.date_time_ad(utc).tzinfo == utc

        assert not self.fake.iso8601().endswith('+00:00')
        assert self.fake.iso8601(utc).endswith('+00:00')

    def test_date_object(self):
        assert isinstance(self.fake.date_object(), date)

    def test_time_object(self):
        assert isinstance(self.fake.time_object(), datetime_time)

    def test_timedelta(self):
        delta = self.fake.time_delta(end_datetime=timedelta(seconds=60))
        assert delta.seconds <= 60

        delta = self.fake.time_delta(end_datetime=timedelta(seconds=-60))
        assert delta.seconds >= -60

        delta = self.fake.time_delta(end_datetime='+60s')
        assert delta.seconds <= 60

        delta = self.fake.time_delta(end_datetime='-60s')
        assert delta.seconds >= 60

        delta = self.fake.time_delta(end_datetime='now')
        assert delta.seconds <= 0

    def test_date_time_between_dates(self):
        timestamp_start = random.randint(0, 2000000000)
        timestamp_end = timestamp_start + 1

        datetime_start = datetime.fromtimestamp(timestamp_start)
        datetime_end = datetime.fromtimestamp(timestamp_end)

        random_date = self.fake.date_time_between_dates(datetime_start, datetime_end)
        assert datetime_start <= random_date
        assert datetime_end >= random_date

    def test_date_time_between_dates_with_tzinfo(self):
        timestamp_start = random.randint(0, 2000000000)
        timestamp_end = timestamp_start + 1

        datetime_start = datetime.fromtimestamp(timestamp_start, utc)
        datetime_end = datetime.fromtimestamp(timestamp_end, utc)

        random_date_naive = self.fake.date_time_between_dates(datetime_start, datetime_end)
        with pytest.raises(TypeError):
            datetime_start <= random_date_naive

        random_date = self.fake.date_time_between_dates(datetime_start, datetime_end, utc)
        assert datetime_start <= random_date
        assert datetime_end >= random_date

    def test_past_datetime_within_second(self):
        # Should not raise a ``ValueError``
        self.fake.past_datetime(start_date='+1s')

    def test_date_between_dates(self):
        date_end = date.today()
        date_start = date_end - timedelta(days=10)

        random_date = self.fake.date_between_dates(date_start, date_end)
        assert date_start <= random_date
        assert date_end >= random_date

    def _datetime_to_time(self, value):
        return int(time.mktime(value.timetuple()))

    @unittest.skipUnless(is64bit(), "requires 64bit")
    def test_date_time_this_period(self):
        # test century
        this_century_start = self._datetime_to_time(
            datetime(datetime.now().year - (datetime.now().year % 100), 1, 1),
        )

        assert (
            self._datetime_to_time(self.fake.date_time_this_century(after_now=False)) <=
            self._datetime_to_time(datetime.now())
        )
        assert (
            self._datetime_to_time(self.fake.date_time_this_century(before_now=False, after_now=True)) >=
            self._datetime_to_time(datetime.now())
        )
        assert (
            self._datetime_to_time(self.fake.date_time_this_century(before_now=True, after_now=True)) >=
            this_century_start
        )

        # test decade
        this_decade_start = self._datetime_to_time(
            datetime(datetime.now().year - (datetime.now().year % 10), 1, 1),
        )

        assert (
            self._datetime_to_time(self.fake.date_time_this_decade(after_now=False)) <=
            self._datetime_to_time(datetime.now())
        )
        assert (
            self._datetime_to_time(self.fake.date_time_this_decade(before_now=False, after_now=True)) >=
            self._datetime_to_time(datetime.now())
        )
        assert (
            self._datetime_to_time(self.fake.date_time_this_decade(before_now=False, after_now=False)) ==
            self._datetime_to_time(datetime.now())
        )
        assert (
            self._datetime_to_time(self.fake.date_time_this_decade(before_now=True, after_now=True)) >=
            this_decade_start
        )
        # test year
        assert (
            self._datetime_to_time(self.fake.date_time_this_year(after_now=False)) <=
            self._datetime_to_time(datetime.now())
        )
        assert (
            self._datetime_to_time(self.fake.date_time_this_year(before_now=False, after_now=True)) >=
            self._datetime_to_time(datetime.now())
        )
        assert (
            self._datetime_to_time(self.fake.date_time_this_year(before_now=False, after_now=False)) ==
            self._datetime_to_time(datetime.now())
        )
        # test month
        assert (
            self._datetime_to_time(self.fake.date_time_this_month(after_now=False)) <=
            self._datetime_to_time(datetime.now())
        )
        assert (
            self._datetime_to_time(self.fake.date_time_this_month(before_now=False, after_now=True)) >=
            self._datetime_to_time(datetime.now())
        )
        assert (
            self._datetime_to_time(self.fake.date_time_this_month(before_now=False, after_now=False)) ==
            self._datetime_to_time(datetime.now())
        )

    @unittest.skipUnless(is64bit(), "requires 64bit")
    def test_date_time_this_period_with_tzinfo(self):
        # ensure all methods provide timezone aware datetimes
        with pytest.raises(TypeError):
            self.fake.date_time_this_century(before_now=False, after_now=True, tzinfo=utc) >= datetime.now()
        with pytest.raises(TypeError):
            self.fake.date_time_this_decade(after_now=False, tzinfo=utc) <= datetime.now()
        with pytest.raises(TypeError):
            self.fake.date_time_this_year(after_now=False, tzinfo=utc) <= datetime.now()
        with pytest.raises(TypeError):
            self.fake.date_time_this_month(after_now=False, tzinfo=utc) <= datetime.now()

        # test century
        assert self.fake.date_time_this_century(after_now=False, tzinfo=utc) <= datetime.now(utc)
        assert self.fake.date_time_this_century(before_now=False, after_now=True, tzinfo=utc) >= datetime.now(utc)
        assert (
            self.fake.date_time_this_century(before_now=False, after_now=False, tzinfo=utc).
            replace(second=0, microsecond=0) == datetime.now(utc).replace(second=0, microsecond=0)
        )
        # test decade
        assert self.fake.date_time_this_decade(after_now=False, tzinfo=utc) <= datetime.now(utc)
        assert self.fake.date_time_this_decade(before_now=False, after_now=True, tzinfo=utc) >= datetime.now(utc)

        assert (
            self.fake.date_time_this_decade(before_now=False, after_now=False, tzinfo=utc).
            replace(second=0, microsecond=0) == datetime.now(utc).replace(second=0, microsecond=0)
        )
        # test year
        assert self.fake.date_time_this_year(after_now=False, tzinfo=utc) <= datetime.now(utc)
        assert self.fake.date_time_this_year(before_now=False, after_now=True, tzinfo=utc) >= datetime.now(utc)
        assert (
            self.fake.date_time_this_year(before_now=False, after_now=False, tzinfo=utc).
            replace(second=0, microsecond=0) == datetime.now(utc).replace(second=0, microsecond=0)
        )
        assert (
            self.fake.date_time_this_year(before_now=True, after_now=True, tzinfo=utc).
            year == datetime.now(utc).year
        )
        # test month
        assert self.fake.date_time_this_month(after_now=False, tzinfo=utc) <= datetime.now(utc)
        assert self.fake.date_time_this_month(before_now=False, after_now=True, tzinfo=utc) >= datetime.now(utc)
        assert (
            self.fake.date_time_this_month(before_now=False, after_now=False, tzinfo=utc).
            replace(second=0, microsecond=0) == datetime.now(utc).replace(second=0, microsecond=0)
        )
        assert (
            self.fake.date_time_this_month(before_now=True, after_now=True, tzinfo=utc).
            month == datetime.now(utc).month
        ) and (
            self.fake.date_time_this_month(before_now=True, after_now=True, tzinfo=utc).
            year == datetime.now(utc).year
        )

    @unittest.skipUnless(is64bit(), "requires 64bit")
    def test_date_this_period(self):
        # test century
        assert (
            self.fake.date_this_century(before_today=True, after_today=True).
            strftime("%G")[:2] == datetime.now().strftime("%G")[:2]
        )
        assert self.fake.date_this_century(after_today=False) <= date.today()
        assert self.fake.date_this_century(before_today=False, after_today=True) >= date.today()
        assert self.fake.date_this_century(before_today=False, after_today=False) == date.today()
        # test decade
        assert (
            self.fake.date_this_decade(before_today=True, after_today=True).
            strftime("%G")[:3] == datetime.now().strftime("%G")[:3]
        )
        assert self.fake.date_this_decade(after_today=False) <= date.today()
        assert self.fake.date_this_decade(before_today=False, after_today=True) >= date.today()
        assert (
            self.fake.date_this_decade(before_today=False, after_today=False) == date.today()
        )
        # test year
        assert (
            self.fake.date_this_year(before_today=True, after_today=True).
            year == datetime.now().year
        )
        assert self.fake.date_this_year(after_today=False) <= date.today()
        assert self.fake.date_this_year(before_today=False, after_today=True) >= date.today()
        assert (
            self.fake.date_this_year(before_today=False, after_today=False) == date.today()
        )
        # test month
        assert (
            self.fake.date_this_month(before_today=True, after_today=True).
            month == datetime.now().month
        ) and (
            self.fake.date_this_month(before_today=True, after_today=True).
            year == datetime.now().year
        )
        assert self.fake.date_this_month(after_today=False) <= date.today()
        assert self.fake.date_this_month(before_today=False, after_today=True) >= date.today()
        assert (
            self.fake.date_this_month(before_today=False, after_today=False) == date.today()
        )

    def test_date_time_between(self):
        now = datetime.now()
        _30_years_ago = change_year(now, -30)
        _20_years_ago = change_year(now, -20)

        random_datetime = self.fake.date_time_between(start_date='-30y', end_date='-20y')
        assert isinstance(random_datetime, datetime)
        self.assertBetween(random_datetime, _30_years_ago, _20_years_ago)

        now = datetime.now(tz=utc)
        _30_years_ago = change_year(now, -30)
        _20_years_ago = change_year(now, -20)

        random_datetime = self.fake.date_time_between(start_date='-30y', end_date='-20y', tzinfo=utc)
        assert isinstance(random_datetime, datetime)
        self.assertBetween(random_datetime, _30_years_ago, _20_years_ago)

    def test_date_between(self):
        today = date.today()
        _30_years_ago = change_year(today, -30)
        _20_years_ago = change_year(today, -20)

        random_date = self.fake.date_between(start_date='-30y', end_date='-20y')

        assert isinstance(random_date, date)
        self.assertBetween(random_date, _30_years_ago, _20_years_ago)

    def test_date_between_months(self):
        today = date.today()
        _2_months_ago = today - timedelta(days=2 * (365.24/12))
        _9_months_ago = today - timedelta(days=9 * (365.24/12))

        random_date = self.fake.date_between(start_date='-9M', end_date='-2M')

        assert isinstance(random_date, date)
        self.assertBetween(random_date, _9_months_ago, _2_months_ago)

    def test_parse_timedelta(self):
        from faker.providers.date_time import Provider

        td = timedelta(days=7)
        seconds = Provider._parse_timedelta(td)
        assert seconds == 604800

        seconds = Provider._parse_timedelta('+1w')
        assert seconds == 604800

        seconds = Provider._parse_timedelta('+1y')
        assert seconds == 31556736

        with pytest.raises(ValueError):
            Provider._parse_timedelta('foobar')

    def test_time_series(self):
        series = list(self.fake.time_series())
        assert len(series), 30
        assert series[1][0] - series[0][0], timedelta(days=1)

        uniform = lambda dt: random.uniform(0, 5)  # noqa
        series = list(self.fake.time_series('now', '+1w', '+1d', uniform))
        assert len(series), 7
        assert series[1][0] - series[0][0], timedelta(days=1)

        end = datetime.now() + timedelta(days=7)
        series = list(self.fake.time_series('now', end, '+1d', uniform))
        assert len(series), 7
        assert series[1][0] - series[0][0], timedelta(days=1)

        assert series[-1][0] <= end

        with pytest.raises(ValueError):
            list(self.fake.time_series('+1w', 'now', '+1d', uniform))

        with pytest.raises(ValueError):
            list(self.fake.time_series('now', '+1w', '+1d', 'uniform'))

        series = list(self.fake.time_series('now', end, '+1d', uniform, tzinfo=utc))
        assert len(series), 7
        assert series[1][0] - series[0][0], timedelta(days=1)

        # avoid microseconds as provider's internal parsing uses POSIX timestamps which only have second granularity
        end = datetime.now(utc).replace(microsecond=0)
        start = end - timedelta(days=15)

        series = list(self.fake.time_series(start_date=start, end_date=end, tzinfo=start.tzinfo))
        assert series[0][0] == start

    def test_unix_time(self):
        from faker.providers.date_time import datetime_to_timestamp

        for _ in range(100):
            now = datetime.now().replace(microsecond=0)
            epoch_start = datetime(1970, 1, 1, tzinfo=utc)

            # Ensure doubly-constrained unix_times are generated correctly
            start_datetime = datetime(2001, 1, 1, tzinfo=utc)
            end_datetime = datetime(2001, 1, 2, tzinfo=utc)

            constrained_unix_time = self.fake.unix_time(end_datetime=end_datetime, start_datetime=start_datetime)

            self.assertIsInstance(constrained_unix_time, int)
            self.assertBetween(
                constrained_unix_time,
                datetime_to_timestamp(start_datetime),
                datetime_to_timestamp(end_datetime),
            )

            # Ensure relative unix_times partially-constrained by a start time are generated correctly
            one_day_ago = datetime.today()-timedelta(days=1)

            recent_unix_time = self.fake.unix_time(start_datetime=one_day_ago)

            self.assertIsInstance(recent_unix_time, int)
            self.assertBetween(recent_unix_time, datetime_to_timestamp(one_day_ago), datetime_to_timestamp(now))

            # Ensure relative unix_times partially-constrained by an end time are generated correctly
            one_day_after_epoch_start = datetime(1970, 1, 2, tzinfo=utc)

            distant_unix_time = self.fake.unix_time(end_datetime=one_day_after_epoch_start)

            self.assertIsInstance(distant_unix_time, int)
            self.assertBetween(
                distant_unix_time,
                datetime_to_timestamp(epoch_start),
                datetime_to_timestamp(one_day_after_epoch_start),
            )

            # Ensure wide-open unix_times are generated correctly
            self.fake.unix_time()

            self.assertIsInstance(constrained_unix_time, int)
            self.assertBetween(constrained_unix_time, 0, datetime_to_timestamp(now))

            # Ensure it does not throw error with startdate='now' for machines with negative offset
            if platform.system() != 'Windows':
                os.environ['TZ'] = 'Europe/Paris'
                time.tzset()
            self.fake.unix_time(start_datetime='now')
            if platform.system() != 'Windows':
                del os.environ['TZ']

    def test_change_year(self):
        _2020_06_01 = datetime.strptime("2020-06-01", "%Y-%m-%d")
        _20_years_ago = change_year(_2020_06_01, -20)
        self.assertEqual(_20_years_ago.strftime("%Y-%m-%d"), "2000-06-01")
        # Verify a leap day
        today = datetime.strptime("2020-02-29", "%Y-%m-%d")
        with self.assertRaises(ValueError):
            _11_years_ago = today.replace(year=11)
        _11_years_ago = change_year(today, -11)
        self.assertEqual(_11_years_ago.strftime("%Y-%m-%d"), "2009-03-01")
        # 0 is an invalid year, so it should still raise a ValueError
        with self.assertRaises(ValueError):
            change_year(today, -today.year)


class TestDeDe(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('de_DE')
        Faker.seed(0)

    def test_day(self):
        day = self.fake.day_of_week()
        assert day in DeDeProvider.DAY_NAMES.values()

    def test_month(self):
        month = self.fake.month_name()
        assert month in DeDeProvider.MONTH_NAMES.values()


class TestPlPL(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('pl_PL')
        Faker.seed(0)

    def test_day(self):
        day = self.fake.day_of_week()
        assert day in PlProvider.DAY_NAMES.values()

    def test_month(self):
        month = self.fake.month_name()
        assert month in PlProvider.MONTH_NAMES.values()


class TestHyAm(unittest.TestCase):
    """ Tests date_time in the hy_AM locale """

    def setUp(self):
        self.fake = Faker('hy_AM')
        Faker.seed(0)

    def test_day(self):
        day = self.fake.day_of_week()
        assert isinstance(day, str)
        assert day in HyAmProvider.DAY_NAMES.values()

    def test_month(self):
        month = self.fake.month_name()
        assert isinstance(month, str)
        assert month in HyAmProvider.MONTH_NAMES.values()


class TestAr(unittest.TestCase):
    def test_ar_aa(self):
        fake = Faker('ar')
        Faker.seed(0)

        # AM/PM
        assert fake.am_pm() in ArProvider.AM_PM.values()
        # Day of week
        assert fake.century() in ArProvider.centuries
        # Month name
        assert (
            fake.month_name()) in (
            ArProvider.MONTH_NAMES.values()
        )
        # Day of week
        assert (
            fake.day_of_week()) in (
            ArProvider.DAY_NAMES.values()
        )

    def test_ar_eg(self):
        fake = Faker('ar_EG')
        Faker.seed(0)

        # AM/PM
        assert fake.am_pm() in ArProvider.AM_PM.values()
        # Day of week
        assert fake.century() in ArProvider.centuries
        # Day of week
        assert (
            fake.day_of_week()) in (
            ArProvider.DAY_NAMES.values()
        )
        # Month name
        assert (
            fake.month_name()) in (
            EgProvider.MONTH_NAMES.values()
        )
        # Month name
        assert (
            fake.month_name()) not in (
            ArProvider.MONTH_NAMES.values()
        )


class DatesOfBirth(unittest.TestCase):
    """
    Test Dates of Birth
    """

    def setUp(self):
        self.fake = Faker()
        Faker.seed(0)

    def test_date_of_birth(self):
        dob = self.fake.date_of_birth()
        assert isinstance(dob, date)

    @freezegun.freeze_time('2020-02-29')
    def test_date_of_birth_on_leap_day(self):
        """
        Freeze the date to a leap day to verify that the date_of_birth method  does not
        raise an error
        """
        dob = self.fake.date_of_birth()
        assert isinstance(dob, date)

    def test_value_errors(self):
        with self.assertRaises(ValueError):
            self.fake.date_of_birth(minimum_age=-1)

        with self.assertRaises(ValueError):
            self.fake.date_of_birth(maximum_age=-1)

        with self.assertRaises(ValueError):
            self.fake.date_of_birth(minimum_age=-2, maximum_age=-1)

        with self.assertRaises(ValueError):
            self.fake.date_of_birth(minimum_age=5, maximum_age=4)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            self.fake.date_of_birth(minimum_age=0.5)

        with self.assertRaises(TypeError):
            self.fake.date_of_birth(maximum_age='hello')

    def test_bad_age_range(self):
        with self.assertRaises(ValueError):
            self.fake.date_of_birth(minimum_age=5, maximum_age=0)

    def test_acceptable_age_range_five_years(self):
        for _ in range(100):
            now = datetime.now(utc).date()

            days_since_now = now - now
            days_since_six_years_ago = now - change_year(now, -6)

            dob = self.fake.date_of_birth(tzinfo=utc, minimum_age=0, maximum_age=5)
            days_since_dob = now - dob

            assert isinstance(dob, date)
            assert days_since_six_years_ago > days_since_dob >= days_since_now

    def test_acceptable_age_range_eighteen_years(self):
        for _ in range(100):
            now = datetime.now(utc).date()

            days_since_now = now - now
            days_since_nineteen_years_ago = now - change_year(now, -19)

            dob = self.fake.date_of_birth(tzinfo=utc, minimum_age=0, maximum_age=18)
            days_since_dob = now - dob

            assert isinstance(dob, date)
            assert days_since_nineteen_years_ago > days_since_dob >= days_since_now

    def test_identical_age_range(self):
        for _ in range(100):
            now = datetime.now(utc).date()

            days_since_five_years_ago = now - change_year(now, -5)
            days_since_six_years_ago = now - change_year(now, -6)

            dob = self.fake.date_of_birth(tzinfo=utc, minimum_age=5, maximum_age=5)
            days_since_dob = now - dob

            assert isinstance(dob, date)
            assert days_since_six_years_ago > days_since_dob >= days_since_five_years_ago

    def test_distant_age_range(self):
        for _ in range(100):
            now = datetime.now(utc).date()

            days_since_one_hundred_years_ago = now - change_year(now, -100)
            days_since_one_hundred_eleven_years_ago = now - change_year(now, -111)

            dob = self.fake.date_of_birth(minimum_age=100, maximum_age=110)
            days_since_dob = now - dob

            assert isinstance(dob, date)
            assert days_since_one_hundred_eleven_years_ago > days_since_dob >= days_since_one_hundred_years_ago


class TestFilPh(unittest.TestCase):
    num_sample_runs = 50

    def setUp(self):
        self.setup_constants()
        self.setup_faker()

    def setup_faker(self):
        self.fake = Faker('fil_PH')
        Faker.seed(0)

    def setup_constants(self):
        from faker.providers.date_time.fil_PH import Provider
        self.day_names = Provider.DAY_NAMES.values()
        self.month_names = Provider.MONTH_NAMES.values()

    def test_PH_of_week(self):
        for _ in range(self.num_sample_runs):
            assert self.fake.day_of_week() in self.day_names

    def test_PH_month_name(self):
        for _ in range(self.num_sample_runs):
            assert self.fake.month_name() in self.month_names


class TestTlPh(TestFilPh):

    def setup_faker(self):
        self.fake = Faker('tl_PH')
        Faker.seed(0)


class TestTaIN(unittest.TestCase):
    """ Tests date_time in the ta_IN locale """

    def setUp(self):
        self.fake = Faker('ta_IN')
        Faker.seed(0)

    def test_day(self):
        day = self.fake.day_of_week()
        assert isinstance(day, str)
        assert day in TaInProvider.DAY_NAMES.values()

    def test_month(self):
        month = self.fake.month_name()
        assert isinstance(month, str)
        assert month in TaInProvider.MONTH_NAMES.values()


class TestRuRu(unittest.TestCase):
    """ Tests date_time in the ru_RU locale """

    def setUp(self):
        self.fake = Faker('ru_RU')
        Faker.seed(0)

    def test_day(self):
        for _ in range(50):
            day = self.fake.day_of_week()
            assert isinstance(day, str)
            assert day in RuProvider.DAY_NAMES.values()

    def test_month(self):
        for _ in range(50):
            month = self.fake.month_name()
            assert isinstance(month, str)
            assert month in RuProvider.MONTH_NAMES.values()

    def test_timezone(self):
        for _ in range(100):
            timezone = self.fake.timezone()
            assert isinstance(timezone, str)
            assert re.match(r'[А-Яа-я]', timezone)


class TestCsCz(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('cs_CZ')
        Faker.seed(0)

    def test_day(self):
        day = self.fake.day_of_week()
        assert day in CsCzProvider.DAY_NAMES.values()

    def test_month(self):
        month = self.fake.month_name()
        assert month in CsCzProvider.MONTH_NAMES.values()


class TestDeAt(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('de_AT')
        Faker.seed(0)

    def test_day(self):
        day = self.fake.day_of_week()
        assert day in DeAtProvider.DAY_NAMES.values()

    def test_month(self):
        month = self.fake.month_name()
        assert month in DeAtProvider.MONTH_NAMES.values()


class TestEsEs(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('es_ES')
        Faker.seed(0)

    def test_day(self):
        day = self.fake.day_of_week()
        assert day in EsEsProvider.DAY_NAMES.values()

    def test_month(self):
        month = self.fake.month_name()
        assert month in EsEsProvider.MONTH_NAMES.values()


class TestItIt(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('it_IT')
        Faker.seed(0)

    def test_day(self):
        day = self.fake.day_of_week()
        assert day in ItItProvider.DAY_NAMES.values()

    def test_month(self):
        month = self.fake.month_name()
        assert month in ItItProvider.MONTH_NAMES.values()


class TestSkSk(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('sk_SK')
        Faker.seed(0)

    def test_day(self):
        day = self.fake.day_of_week()
        assert day in SkSkProvider.DAY_NAMES.values()

    def test_month(self):
        month = self.fake.month_name()
        assert month in SkSkProvider.MONTH_NAMES.values()


class TestThTh(unittest.TestCase):
    num_sample_runs = 50

    def setUp(self):
        self.fake = Faker('th_TH')
        Faker.seed(0)

    def test_day(self):
        day = self.fake.day_of_week()
        assert isinstance(day, str)
        assert day.startswith("วัน")

    def test_month(self):
        month = self.fake.month_name()
        assert isinstance(month, str)

    def test_date(self):
        # default format is "%-d %b %Y"
        # (date with no padding, abbreviated month, full year [4 digits])
        date = self.fake.date(thai_digit=True)
        for _ in range(self.num_sample_runs):
            assert re.fullmatch(
                    r'[๐-๙]{1,2} '
                    r'(ม\.ค\.|ก\.พ\.|มี\.ค\.|เม\.ย\.|พ\.ค\.|มิ\.ย\.|ก\.ค\.|ส\.ค\.|ก\.ย\.|ต\.ค\.|พ\.ย\.|ธ\.ค\.) '
                    r'[๐-๙]{4}',
                    date,
                )

    def test_time(self):
        time = self.fake.time(thai_digit=True)
        for _ in range(self.num_sample_runs):
            assert re.fullmatch(r'[๐-๙]{2}:[๐-๙]{2}:[๐-๙]{2}', time)

    def test_century(self):
        century = self.fake.century()
        assert isinstance(century, str)
        assert len(century) <= 2
        century = self.fake.century(thai_digit=True)
        for _ in range(self.num_sample_runs):
            assert re.fullmatch(r'[๑-๒]?[๐-๙]', century)

    def test_date_pattern(self):
        # unsupported or incomplete directive
        date = self.fake.date("%Q")
        assert date == "Q"
        date = self.fake.date("%%")
        assert date == "%"
        date = self.fake.date("%-")
        assert date == "-"
        date = self.fake.date("% ")
        assert date == " "
        date = self.fake.date("%0")
        assert date == "0"
        date = self.fake.date("%")
        assert date == "%"

        # may be not supported on Windows, try for coverage
        date = self.fake.date("%s")
        date = self.fake.date("%f")

        # National representation of the full weekday name
        date = self.fake.date("%A")
        assert isinstance(date, str)

        # National representation of the abbreviated weekday
        date = self.fake.date("%a")
        assert isinstance(date, str)
        assert len(date) <= 2

        # National representation of the full month name
        date = self.fake.date("%B")
        assert isinstance(date, str)
        assert "." not in date

        # National representation of the abbreviated month name
        date = self.fake.date("%b")
        assert isinstance(date, str)
        assert "." in date

        # Century as decimal number
        date = self.fake.date("%C")
        assert isinstance(date, str)

        # Locale’s appropriate date and time representation
        # พ   6 ต.ค. 01:40:00 2519  <-- left-aligned weekday, right-aligned day
        date = self.fake.date("%c")
        assert isinstance(date, str)

        # Equivalent to ``%m/%d/%y''
        date = self.fake.date("%D")
        assert isinstance(date, str)

        # Equivalent to ``%Y-%m-%d''
        date = self.fake.date("%F")
        assert isinstance(date, str)

        # ISO 8601 year with century representing the year that contains
        # the greater part of the ISO week (%V). Monday as the first day
        # of the week.
        date = self.fake.date("%G")
        assert isinstance(date, str)

        # Same year as in ``%G'',
        # but as a decimal number without century (00-99).
        date = self.fake.date("%g")
        assert isinstance(date, str)
        assert len(date) <= 2

        # BSD extension, ' 6-ต.ค.-2519'
        date = self.fake.date("%v")
        assert isinstance(date, str)

        # Locale’s appropriate time representation.
        date = self.fake.date("%X")
        assert isinstance(date, str)

        # Locale’s appropriate date representation.
        date = self.fake.date("%x")
        assert isinstance(date, str)

        # Year with century
        date = self.fake.date("%Y")
        assert isinstance(date, str)

        # Year without century
        date = self.fake.date("%y")
        assert isinstance(date, str)
        assert len(date) <= 2

        # National representation of the date and time
        # (the format is similar to that produced by date(1))
        # Wed  6 Oct 1976 01:40:00
        date = self.fake.date("%+")
        assert isinstance(date, str)

        # GNU libc extension,
        # no padding
        for _ in range(self.num_sample_runs):
            date = self.fake.date("%-d")
            assert isinstance(date, str)
            assert date[0] != "0"

        # GNU libc extension,
        # explicitly specify space (" ") for padding
        for _ in range(self.num_sample_runs):
            date = self.fake.date("%_d")
            assert isinstance(date, str)
            assert date[0] != "0"

        # GNU libc extension,
        # explicitly specify zero ("0") for padding
        for _ in range(self.num_sample_runs):
            date = self.fake.date("%0v")
            assert isinstance(date, str)
            assert date[0] != " "

        # GNU libc extension,
        # convert to upper case
        date = self.fake.date("%^p")
        assert isinstance(date, str)
        assert date.isupper()

        # GNU libc extension,
        # swap case - useful for %Z
        date = self.fake.date("%#p")
        assert isinstance(date, str)
        assert date.islower()

        # POSIX extension,
        # uses the locale's alternative representation
        # Not implemented yet
        # swap case - useful for %Z
        date = self.fake.date("%Ed")
        assert isinstance(date, str)

        # POSIX extension,
        # uses the locale's alternative numeric symbols
        date = self.fake.date("%Od")
        assert isinstance(date, str)
        assert date[0] not in "0123456789"


class TestTrTr(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('tr_TR')
        Faker.seed(0)

    def test_day(self):
        day = self.fake.day_of_week()
        assert day in TrTrProvider.DAY_NAMES.values()

    def test_month(self):
        month = self.fake.month_name()
        assert month in TrTrProvider.MONTH_NAMES.values()


class TestPtPt(unittest.TestCase):

    def setUp(self):
        self.fake = Faker('pt_PT')
        Faker.seed(0)

    def test_day(self):
        day = self.fake.day_of_week()
        assert day in PtPtProvider.DAY_NAMES.values()

    def test_month(self):
        month = self.fake.month_name()
        assert month in PtPtProvider.MONTH_NAMES.values()
