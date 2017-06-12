# coding=utf-8

from __future__ import unicode_literals

import re
import unittest
import string
import six
import sys

try:
    from StringIO import StringIO
except ImportError:  # pragma: no cover
    from io import StringIO

from faker import Generator, Factory
from faker.generator import random
from faker.utils import text, decorators
from . import string_types


class BarProvider(object):

    def foo_formatter(self):
        return 'barfoo'


class FooProvider(object):

    def foo_formatter(self):
        return 'foobar'

    def foo_formatter_with_arguments(self, param='', append=''):
        return 'baz' + param + append


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

        choices = {'a': 5, 'b': 2, 'c': 2, 'd': 1}
        pick = provider.random_element(choices)
        self.assertTrue(pick in choices)

        choices = {'a': 0.5, 'b': 0.2, 'c': 0.2, 'd': 0.1}
        pick = provider.random_element(choices)
        self.assertTrue(pick in choices)

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

    def test_words_valueerror(self):
        f = Factory.create()
        self.assertRaises(ValueError, f.text, max_nb_chars=4)

    def test_no_words_paragraph(self):
        from faker.providers.lorem import Provider

        provider = Provider(None)

        sentence = provider.sentence(0)
        self.assertEqual(sentence, '')

    def test_ext_word_list(self):
        from faker import Factory
        fake = Factory.create()

        my_word_list = [
        'danish',
        'cheesecake',
        'sugar',
        'Lollipop',
        'wafer',
        'Gummies',
        'Jelly',
        'pie',
        ]
        word = fake.word(ext_word_list=my_word_list)
        self.assertIn(word, my_word_list)

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


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
