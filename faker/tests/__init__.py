# coding=utf-8

from __future__ import unicode_literals

import json
import os
import random
import unittest
import sys

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from faker import Generator, Factory
from faker.utils import text, decorators

try:
    string_types = (basestring,)
except NameError:
    string_types = (str,)


TEST_DIR = os.path.dirname(__file__)


class BarProvider(object):
    def foo_formatter(self):
        return 'barfoo'


class FooProvider(object):
    def foo_formatter(self):
        return 'foobar'

    def foo_formatter_with_arguments(self, param='', append=''):
        return 'baz' + param + append


class ShimsTestCase(unittest.TestCase):
    def test_counter(self):
        from faker.shims import Counter

        result = Counter('abbb') + Counter('bcc')
        self.assertEqual(result, Counter({'b': 4, 'c': 2, 'a': 1}))

        result = Counter('abbbc') - Counter('bccd')
        self.assertEqual(result, Counter({'b': 2, 'a': 1}))

        result = Counter('abbb') | Counter('bcc')
        self.assertEqual(result, Counter({'b': 3, 'c': 2, 'a': 1}))

        result = Counter('abbb') & Counter('bcc')
        self.assertEqual(result, Counter({'b': 1}))

        counter = Counter('which')
        counter.update('witch')
        d = Counter('watch')
        counter.update(d)
        self.assertEqual(counter['h'], 4)


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
        from faker.config import DEFAULT_PROVIDERS

        result = find_available_locales(DEFAULT_PROVIDERS)
        self.assertNotEqual(len(result), 0)

    def test_find_available_providers(self):
        from faker.utils.loading import find_available_providers
        from faker.config import DEFAULT_PROVIDERS_MODULES
        from importlib import import_module

        modules = [import_module(path) for path in DEFAULT_PROVIDERS_MODULES]
        providers = find_available_providers(modules)

        expected_providers = list(map(str, [
            'address',
            'barcode',
            'color',
            'company',
            'credit_card',
            'currency',
            'date_time',
            'file',
            'internet',
            'job',
            'lorem',
            'misc',
            'miscelleneous',
            'person',
            'phone_number',
            'profile',
            'python',
            'ssn',
            'user_agent',
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
        self.assertRaises(AttributeError,
                          self.generator.get_formatter, 'barFormatter')

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
        print_doc('faker.providers.it_IT.person', output=output)
        assert output.getvalue()
        self.assertRaises(AttributeError,
                          self.generator.get_formatter,
                          'barFormatter')

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

    def test_slugify(self):
        slug = text.slugify("a'b/c")
        self.assertEqual(slug, 'abc')

        slug = text.slugify("àeìöú")
        self.assertEqual(slug, 'aeiou')

        slug = text.slugify("àeì.öú")
        self.assertEqual(slug, 'aeiou')

        slug = text.slugify("àeì.öú", allow_dots=True)
        self.assertEqual(slug, 'aei.ou')

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

    def test_datetime_safe(self):
        from faker.utils import datetime_safe
        # test using example provided in module
        result = datetime_safe.date(1850, 8, 2).strftime('%Y/%m/%d was a %A')
        self.assertEqual(result, '1850/08/02 was a Friday')
        # test against certain formatting strings used on pre-1900 dates
        # NOTE: the lambda approach in assertRaises is needed for Python 2.6
        #       in 2.7 and 3.x we could also use:
        #           with self.assertRaises(TypeError):
        #               datetime_safe.date(1850, 8, 2).strftime('%s')
        self.assertRaises(
            TypeError,
            lambda: datetime_safe.date(1850, 8, 2).strftime('%s'))
        self.assertRaises(
            TypeError,
            lambda: datetime_safe.date(1850, 8, 2).strftime('%y'))
        # test using 29-Feb-2012 and escaped percentage sign
        result = datetime_safe.date(2012, 2, 29).strftime('%Y-%m-%d was a 100%% %A')
        self.assertEqual(result, r'2012-02-29 was a 100% Wednesday')
        # test that certain formatting strings are allowed on post-1900 dates
        result = datetime_safe.date(2008, 2, 29).strftime('%y')
        self.assertEqual(result, r'08')

    def test_prefix_suffix_always_string(self):
        # Locales known to contain `*_male` and `*_female`.
        for locale in ("bg_BG", "dk_DK", "en", "ru_RU", "tr_TR"):
            f = Factory.create(locale=locale)
            for x in range(20):  # Probabilistic testing.
                assert isinstance(f.prefix(), string_types)
                assert isinstance(f.suffix(), string_types)


if __name__ == '__main__':
    unittest.main()
