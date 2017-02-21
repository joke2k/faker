# coding=utf-8

from __future__ import unicode_literals

import datetime
import json
import os
import re
import time
import unittest
import string
import six
import sys
import logging

try:
    from mock import patch
except ImportError:  # pragma: no cover
    from unittest.mock import patch

try:
    from StringIO import StringIO
except ImportError:  # pragma: no cover
    from io import StringIO

from faker import Generator, Factory
from faker.generator import random
from faker.utils import text, decorators

try:
    string_types = (basestring,)
except NameError:  # pragma: no cover
    string_types = (str,)


TEST_DIR = os.path.dirname(__file__)


class UTC(datetime.tzinfo):
    """
    UTC implementation taken from Python's docs.
    """
    def __repr__(self):
        return "<UTC>"

    def utcoffset(self, dt):
        return datetime.timedelta(0)

    def tzname(self, dt):
        return "UTC"

    def dst(self, dt):
        return datetime.timedelta(0)

utc = UTC()


class BarProvider(object):
    def foo_formatter(self):
        return 'barfoo'


class FooProvider(object):
    def foo_formatter(self):
        return 'foobar'

    def foo_formatter_with_arguments(self, param='', append=''):
        return 'baz' + param + append


class UtilsTestCase(unittest.TestCase):
    def test_choice_distribution(self):
        from faker.utils.distribution import choice_distribution

        a = ('a', 'b', 'c', 'd')
        p = (0.5, 0.2, 0.2, 0.1)

        sample = choice_distribution(a, p)
        self.assertTrue(sample in a)

        with open(os.path.join(TEST_DIR, 'random_state.json'), 'r') as fh:
            random_state = json.load(fh)
        random_state[1] = tuple(random_state[1])

        random.setstate(random_state)
        samples = [choice_distribution(a, p) for i in range(100)]
        a_pop = len([i for i in samples if i == 'a'])
        b_pop = len([i for i in samples if i == 'b'])
        c_pop = len([i for i in samples if i == 'c'])
        d_pop = len([i for i in samples if i == 'd'])

        boundaries = []
        tolerance = 5
        for probability in p:
            boundaries.append([100 * probability + tolerance,  100 * probability - tolerance])

        self.assertTrue(boundaries[0][0] > a_pop > boundaries[0][1])
        self.assertTrue(boundaries[1][0] > b_pop > boundaries[1][1])
        self.assertTrue(boundaries[2][0] > c_pop > boundaries[2][1])
        self.assertTrue(boundaries[3][0] > d_pop > boundaries[3][1])

    def test_add_dicts(self):
        from faker.utils.datasets import add_dicts

        t1 = {'a':1, 'b':2}
        t2 = {'b':1, 'c':3}
        t3 = {'d':4}

        result = add_dicts(t1, t2, t3)
        self.assertEqual(result, {'a': 1, 'c': 3, 'b': 3, 'd': 4})

    def test_find_available_locales(self):
        from faker.utils.loading import find_available_locales
        from faker.config import PROVIDERS

        result = find_available_locales(PROVIDERS)
        self.assertNotEqual(len(result), 0)

    def test_find_available_providers(self):
        from faker.utils.loading import find_available_providers
        from faker.config import META_PROVIDERS_MODULES
        from importlib import import_module

        modules = [import_module(path) for path in META_PROVIDERS_MODULES]
        providers = find_available_providers(modules)

        expected_providers = list(map(str, [
            'faker.providers.address',
            'faker.providers.barcode',
            'faker.providers.color',
            'faker.providers.company',
            'faker.providers.credit_card',
            'faker.providers.currency',
            'faker.providers.date_time',
            'faker.providers.file',
            'faker.providers.internet',
            'faker.providers.job',
            'faker.providers.lorem',
            'faker.providers.misc',
            'faker.providers.person',
            'faker.providers.phone_number',
            'faker.providers.profile',
            'faker.providers.python',
            'faker.providers.ssn',
            'faker.providers.user_agent',
        ]))
        self.assertEqual(providers, expected_providers)


class FactoryTestCase(unittest.TestCase):

    def setUp(self):
        self.generator = Generator()
        self.provider = FooProvider()
        self.generator.add_provider(self.provider)

    def test_add_provider_gives_priority_to_newly_added_provider(self):
        self.generator.add_provider(BarProvider())
        self.assertEqual('barfoo', self.generator.format('foo_formatter'))

    def test_get_formatter_returns_callable(self):
        formatter = self.generator.get_formatter('foo_formatter')
        self.assertTrue(hasattr(formatter, '__call__')
                        or isinstance(formatter, (classmethod, staticmethod)))

    def test_get_formatter_returns_correct_formatter(self):
        self.assertEqual(self.provider.foo_formatter,
                         self.generator.get_formatter('foo_formatter'))

    def test_get_formatter_throws_exception_on_incorrect_formatter(self):
        with self.assertRaises(AttributeError):
            self.generator.get_formatter('barFormatter')

    def test_format_calls_formatter_on_provider(self):
        self.assertEqual('foobar', self.generator.format('foo_formatter'))

    def test_format_transfers_arguments_to_formatter(self):
        result = self.generator.format('foo_formatter_with_arguments',
                                       'foo', append='!')
        self.assertEqual('bazfoo!', result)

    def test_parse_returns_same_string_when_it_contains_no_curly_braces(self):
        self.assertEqual('fooBar#?', self.generator.parse('fooBar#?'))

    def test_parse_returns_string_with_tokens_replaced_by_formatters(self):
        result = self.generator.parse(
            'This is {{foo_formatter}} a text with "{{ foo_formatter }}"')
        self.assertEqual('This is foobar a text with " foobar "', result)

#   def testParseReturnsStringWithTokensReplacedByFormatterWithArguments(self):
#       result = self.generator.parse(
#           'This is {{foo_formatter_with_arguments:bar}}')
#       self.assertEqual('This is foobar', result)

    def test_magic_call_calls_format(self):
        self.assertEqual('foobar', self.generator.foo_formatter())

    def test_magic_call_calls_format_with_arguments(self):
        self.assertEqual('bazfoo',
                         self.generator.foo_formatter_with_arguments('foo'))

    def test_documentor(self):
        from faker.cli import print_doc
        output = StringIO()
        print_doc(output=output)
        print_doc('address', output=output)
        print_doc('faker.providers.person.it_IT', output=output)
        assert output.getvalue()
        with self.assertRaises(AttributeError):
            self.generator.get_formatter('barFormatter')

    def test_command(self):
        from faker.cli import Command
        orig_stdout = sys.stdout
        try:
            sys.stdout = StringIO()
            command = Command(['faker', 'address'])
            command.execute()
            assert sys.stdout.getvalue()
        finally:
            sys.stdout = orig_stdout

    def test_command_custom_provider(self):
        from faker.cli import Command
        orig_stdout = sys.stdout
        try:
            sys.stdout = StringIO()
            command = Command(['faker', 'foo', '-i', 'tests.mymodule.en_US'])
            command.execute()
            assert sys.stdout.getvalue()
        finally:
            sys.stdout = orig_stdout

    def test_slugify(self):
        slug = text.slugify("a'b/c")
        self.assertEqual(slug, 'abc')

        slug = text.slugify("àeìöú")
        self.assertEqual(slug, 'aeiou')

        slug = text.slugify("àeì.öú")
        self.assertEqual(slug, 'aeiou')

        slug = text.slugify("àeì.öú", allow_dots=True)
        self.assertEqual(slug, 'aei.ou')

        slug = text.slugify("àeì.öú", allow_unicode=True)
        self.assertEqual(slug, 'àeìöú')

        slug = text.slugify("àeì.öú", allow_unicode=True, allow_dots=True)
        self.assertEqual(slug, 'àeì.öú')

        @decorators.slugify
        def fn(s):
            return s

        slug = fn("a'b/c")
        self.assertEqual(slug, 'abc')

        @decorators.slugify_domain
        def fn(s):
            return s

        slug = fn("a'b/.c")
        self.assertEqual(slug, 'ab.c')

        @decorators.slugify_unicode
        def fn(s):
            return s

        slug = fn("a'b/.cé")
        self.assertEqual(slug, 'abcé')

    def test_random_element(self):
        from faker.providers import BaseProvider
        provider = BaseProvider(None)

        choices = ('a', 'b', 'c', 'd')
        pick = provider.random_element(choices)
        self.assertTrue(pick in choices)

        choices = {'a': 5, 'b': 2, 'c': 2, 'd':1 }
        pick = provider.random_element(choices)
        self.assertTrue(pick in choices)


        choices = {'a': 0.5, 'b': 0.2, 'c': 0.2, 'd':0.1}
        pick = provider.random_element(choices)
        self.assertTrue(pick in choices)

    def test_timezone_conversion(self):
        from faker.providers.date_time import datetime_to_timestamp

        now = datetime.datetime.now(utc).replace(microsecond=0)
        timestamp = datetime_to_timestamp(now)
        now_back = datetime.datetime.fromtimestamp(timestamp, utc)
        self.assertEqual(now, now_back)

        today = datetime.date.today()
        timestamp = datetime_to_timestamp(today)
        today_as_dt = datetime.datetime.combine(today, datetime.time.min)
        today_back = datetime.datetime.fromtimestamp(timestamp)
        self.assertEqual(today_as_dt, today_back)

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

        self.assertIsInstance(provider.date_object(), datetime.date)

    def test_time_object(self):
        from faker.providers.date_time import Provider
        provider = Provider

        self.assertIsInstance(provider.time_object(), datetime.time)

    def test_date_time_between_dates(self):
        from faker.providers.date_time import Provider
        provider = Provider

        timestamp_start = random.randint(0,2000000000)
        timestamp_end = timestamp_start+1

        datetime_start = datetime.datetime.fromtimestamp(timestamp_start)
        datetime_end = datetime.datetime.fromtimestamp(timestamp_end)

        random_date = provider.date_time_between_dates(datetime_start, datetime_end)
        self.assertTrue(datetime_start <= random_date)
        self.assertTrue(datetime_end >= random_date)

    def test_date_time_between_dates_with_tzinfo(self):
        from faker.providers.date_time import Provider
        provider = Provider

        timestamp_start = random.randint(0, 2000000000)
        timestamp_end = timestamp_start+1

        datetime_start = datetime.datetime.fromtimestamp(timestamp_start, utc)
        datetime_end = datetime.datetime.fromtimestamp(timestamp_end, utc)

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
        self.assertTrue(self._datetime_to_time(provider.date_time_this_century(after_now=False)) <= self._datetime_to_time(datetime.datetime.now()))
        self.assertTrue(self._datetime_to_time(provider.date_time_this_century(before_now=False, after_now=True)) >= self._datetime_to_time(datetime.datetime.now()))
        # test decade
        self.assertTrue(self._datetime_to_time(provider.date_time_this_decade(after_now=False)) <= self._datetime_to_time(datetime.datetime.now()))
        self.assertTrue(self._datetime_to_time(provider.date_time_this_decade(before_now=False, after_now=True)) >= self._datetime_to_time(datetime.datetime.now()))
        self.assertEqual(
            self._datetime_to_time(provider.date_time_this_decade(before_now=False, after_now=False)),
            self._datetime_to_time(datetime.datetime.now())
        )
        # test year
        self.assertTrue(self._datetime_to_time(provider.date_time_this_year(after_now=False)) <= self._datetime_to_time(datetime.datetime.now()))
        self.assertTrue(self._datetime_to_time(provider.date_time_this_year(before_now=False, after_now=True)) >= self._datetime_to_time(datetime.datetime.now()))
        self.assertEqual(
            self._datetime_to_time(provider.date_time_this_year(before_now=False, after_now=False)),
            self._datetime_to_time(datetime.datetime.now())
        )
        # test month
        self.assertTrue(self._datetime_to_time(provider.date_time_this_month(after_now=False)) <= self._datetime_to_time(datetime.datetime.now()))
        self.assertTrue(self._datetime_to_time(provider.date_time_this_month(before_now=False, after_now=True)) >= self._datetime_to_time(datetime.datetime.now()))
        self.assertEqual(
            self._datetime_to_time(provider.date_time_this_month(before_now=False, after_now=False)),
            self._datetime_to_time(datetime.datetime.now())
        )

    def test_date_time_this_period_with_tzinfo(self):
        from faker.providers.date_time import Provider
        provider = Provider

        # ensure all methods provide timezone aware datetimes
        with self.assertRaises(TypeError):
            provider.date_time_this_century(before_now=False, after_now=True, tzinfo=utc) >= datetime.datetime.now()
        with self.assertRaises(TypeError):
            provider.date_time_this_decade(after_now=False, tzinfo=utc) <= datetime.datetime.now()
        with self.assertRaises(TypeError):
            provider.date_time_this_year(after_now=False, tzinfo=utc) <= datetime.datetime.now()
        with self.assertRaises(TypeError):
            provider.date_time_this_month(after_now=False, tzinfo=utc) <= datetime.datetime.now()

        # test century
        self.assertTrue(provider.date_time_this_century(after_now=False, tzinfo=utc) <= datetime.datetime.now(utc))
        self.assertTrue(provider.date_time_this_century(before_now=False, after_now=True, tzinfo=utc) >= datetime.datetime.now(utc))
        # test decade
        self.assertTrue(provider.date_time_this_decade(after_now=False, tzinfo=utc) <= datetime.datetime.now(utc))
        self.assertTrue(provider.date_time_this_decade(before_now=False, after_now=True, tzinfo=utc) >= datetime.datetime.now(utc))

        self.assertEqual(
            provider.date_time_this_decade(before_now=False, after_now=False, tzinfo=utc).replace(second=0, microsecond=0),
            datetime.datetime.now(utc).replace(second=0, microsecond=0)
        )
        # test year
        self.assertTrue(provider.date_time_this_year(after_now=False, tzinfo=utc) <= datetime.datetime.now(utc))
        self.assertTrue(provider.date_time_this_year(before_now=False, after_now=True, tzinfo=utc) >= datetime.datetime.now(utc))
        self.assertEqual(
            provider.date_time_this_year(before_now=False, after_now=False, tzinfo=utc).replace(second=0, microsecond=0),
            datetime.datetime.now(utc).replace(second=0, microsecond=0)
        )
        # test month
        self.assertTrue(provider.date_time_this_month(after_now=False, tzinfo=utc) <= datetime.datetime.now(utc))
        self.assertTrue(provider.date_time_this_month(before_now=False, after_now=True, tzinfo=utc) >= datetime.datetime.now(utc))
        self.assertEqual(
            provider.date_time_this_month(before_now=False, after_now=False, tzinfo=utc).replace(second=0, microsecond=0),
            datetime.datetime.now(utc).replace(second=0, microsecond=0)
        )

    def test_binary(self):
        from faker.providers.misc import Provider

        for _ in range(999):
            length = random.randint(0, 2 ** 10)
            binary = Provider.binary(length)

            self.assertTrue(isinstance(binary, six.binary_type))
            self.assertTrue(len(binary) == length)

    def test_language_code(self):
        from faker.providers.misc import Provider

        for _ in range(99):
            language_code = Provider.language_code()
            self.assertTrue(isinstance(language_code, string_types))
            self.assertTrue(re.match(r'^[a-z]{2,3}$', language_code))

    def test_locale(self):
        from faker.providers.misc import Provider

        for _ in range(99):
            locale = Provider.locale()
            self.assertTrue(re.match(r'^[a-z]{2,3}_[A-Z]{2}$', locale))

    def test_password(self):
        from faker.providers.misc import Provider

        def in_string(char, _str):
            return char in _str

        for _ in range(999):
            password = Provider.password()

            self.assertTrue(any([in_string(char, password) for char in "!@#$%^&*()_+"]))
            self.assertTrue(any([in_string(char, password) for char in string.digits]))
            self.assertTrue(any([in_string(char, password) for char in string.ascii_uppercase]))
            self.assertTrue(any([in_string(char, password) for char in string.ascii_lowercase]))

        with self.assertRaises(AssertionError):
            Provider.password(length=2)

    def test_prefix_suffix_always_string(self):
        # Locales known to contain `*_male` and `*_female`.
        for locale in ("bg_BG", "dk_DK", "en", "ru_RU", "tr_TR"):
            f = Factory.create(locale=locale)
            for x in range(20):  # Probabilistic testing.
                assert isinstance(f.prefix(), string_types)
                assert isinstance(f.suffix(), string_types)

    def test_no_words_sentence(self):
        from faker.providers.lorem import Provider

        provider = Provider(None)

        paragraph = provider.paragraph(0)
        self.assertEqual(paragraph, '')

    def test_no_words_paragraph(self):
        from faker.providers.lorem import Provider

        provider = Provider(None)

        sentence = provider.sentence(0)
        self.assertEqual(sentence, '')

    def test_random_pystr_characters(self):
        from faker.providers.python import Provider
        provider = Provider(None)

        characters = provider.pystr()
        self.assertEqual(len(characters), 20)
        characters = provider.pystr(max_chars=255)
        self.assertEqual(len(characters), 255)
        characters = provider.pystr(max_chars=0)
        self.assertEqual(characters, '')
        characters = provider.pystr(max_chars=-10)
        self.assertEqual(characters, '')
        characters = provider.pystr(min_chars=10, max_chars=255)
        self.assertTrue((len(characters) >= 10))

    def test_random_pyfloat(self):
        from faker.providers.python import Provider
        provider = Provider(None)

        self.assertTrue(0 <= abs(provider.pyfloat(left_digits=1)) < 10)
        self.assertTrue(0 <= abs(provider.pyfloat(left_digits=0)) < 1)
        x=abs(provider.pyfloat(right_digits=0))
        self.assertTrue(x-int(x) == 0)
        with self.assertRaises(ValueError,
                               msg='A float number cannot have 0 digits '
                               'in total'):
            provider.pyfloat(left_digits=0, right_digits=0)

    def test_us_ssn_valid(self):
        from faker.providers.ssn.en_US import Provider

        provider = Provider(None)
        for i in range(1000):
            ssn = provider.ssn()
            self.assertEqual(len(ssn), 11)
            self.assertNotEqual(ssn[0], '9')
            self.assertNotEqual(ssn[0:3], '666')
            self.assertNotEqual(ssn[0:3], '000')
            self.assertNotEqual(ssn[4:6], '00')
            self.assertNotEqual(ssn[7:11], '0000')

    def test_nl_BE_ssn_valid(self):
        from faker.providers.ssn.nl_BE import Provider

        provider = Provider(None)

        for i in range (1000):
            ssn = provider.ssn()
            self.assertEqual(len(ssn), 11)
            gen_ssn_base = ssn[0:6]
            gen_seq = ssn[6:9]
            gen_chksum = ssn[9:11]
            gen_ssn_base_as_int = int(gen_ssn_base)
            gen_seq_as_int = int(gen_seq)
            gen_chksum_as_int = int(gen_chksum)
            # Check that the sequence nr is between 1 inclusive and 998 inclusive
            self.assertGreater(gen_seq_as_int,0)
            self.assertLessEqual(gen_seq_as_int, 998)

            # validate checksum calculation
            # Since the century is not part of ssn, try both below and above year 2000
            ssn_below = int(ssn[0:9])
            chksum_below = 97 - (ssn_below % 97)
            ssn_above = ssn_below + 2000000000
            chksum_above = 97 - (ssn_above % 97)
            results = [ chksum_above, chksum_below ]
            self.assertIn(gen_chksum_as_int,results)

    def test_email(self):
        from faker import Factory

        factory = Factory.create()

        for _ in range(999):
            email = factory.email()
            self.assertTrue('@' in email)

    def test_ipv4(self):
        from faker.providers.internet import Provider

        provider = Provider(None)

        for _ in range(999):
            address = provider.ipv4()
            self.assertTrue(len(address) >= 7)
            self.assertTrue(len(address) <= 15)
            self.assertTrue(
                re.compile(r'^(\d{1,3}\.){3}\d{1,3}$').search(address))

        for _ in range(999):
            address = provider.ipv4(network=True)
            self.assertTrue(len(address) >= 9)
            self.assertTrue(len(address) <= 18)
            self.assertTrue(
                re.compile(r'^(\d{1,3}\.){3}\d{1,3}/\d{1,2}$').search(address))

    def test_ipv6(self):
        from faker.providers.internet import Provider

        provider = Provider(None)

        for _ in range(999):
            address = provider.ipv6()
            self.assertTrue(len(address) >= 3)  # ::1
            self.assertTrue(len(address) <= 39)
            self.assertTrue(
                re.compile(r'^([0-9a-f]{0,4}:){2,7}[0-9a-f]{1,4}$').search(address))

        for _ in range(999):
            address = provider.ipv6(network=True)
            self.assertTrue(len(address) >= 4)  # ::/8
            self.assertTrue(len(address) <= 39 + 4)
            self.assertTrue(
                re.compile(r'^([0-9a-f]{0,4}:){2,7}[0-9a-f]{0,4}/\d{1,3}$').search(
                    address))

    def test_random_sample_unique(self):
        from faker.providers import BaseProvider
        provider = BaseProvider(None)

        sample = provider.random_sample_unique('abcde', 3)
        self.assertEqual(len(sample), 3)
        self.assertTrue(sample.issubset(set('abcde')))

        # Same length
        sample = provider.random_sample_unique('abcde', 5)
        self.assertEqual(sample, set('abcde'))

        # Length = 1
        sample = provider.random_sample_unique('abcde', 1)
        self.assertEqual(len(sample), 1)
        self.assertTrue(sample.issubset(set('abcde')))

        # Length = 0
        sample = provider.random_sample_unique('abcde', 0)
        self.assertEqual(sample, set())

        # Length = 0
        with self.assertRaises(ValueError):
            provider.random_sample_unique('abcde', 6)

    def test_random_number(self):
        from faker.providers import BaseProvider
        provider = BaseProvider

        number = provider.random_number(10, True)
        self.assertEqual(len(str(number)), 10)


class GeneratorTestCase(unittest.TestCase):

    def setUp(self):
        self.generator = Generator()

    @patch('random.getstate')
    def test_get_random(self, mock_system_random):
        random_instance = self.generator.random
        random_instance.getstate()
        self.assertFalse(mock_system_random.called)

    @patch('random.seed')
    def test_random_seed_doesnt_seed_system_random(self, mock_system_random):
        self.generator.seed(0)
        self.assertFalse(mock_system_random.called)


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
