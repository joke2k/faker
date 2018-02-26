# coding=utf-8

from __future__ import unicode_literals

import re
import unittest
import string
import sys
from ipaddress import ip_address, ip_network

try:
    from StringIO import StringIO
except ImportError:  # pragma: no cover
    from io import StringIO

from faker import Generator, Faker
from faker.generator import random
from faker.utils import text, decorators
from tests import string_types


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
        with self.assertRaises(AttributeError) as exc:
            self.generator.get_formatter('barFormatter')
            self.assertEqual(exc.args[0], 'Unknown formatter "barFormatter"')

        faker = Faker('it_IT')
        with self.assertRaises(AttributeError) as exc:
            faker.get_formatter('barFormatter')
            self.assertEqual(exc.args[0], 'Unknown formatter "barFormatter" with locale "it_IT"')

    def test_invalid_locale(self):
        with self.assertRaises(AttributeError):
            Faker('foo_Bar')

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
        provider = BaseProvider(self.generator)

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
        provider = Provider(self.generator)

        for _ in range(999):
            length = random.randint(0, 2 ** 10)
            binary = provider.binary(length)

            self.assertTrue(isinstance(binary, (bytes, bytearray)))
            self.assertTrue(len(binary) == length)

        for _ in range(999):
            self.generator.seed(_)
            binary1 = provider.binary(_)
            self.generator.seed(_)
            binary2 = provider.binary(_)

            self.assertTrue(binary1 == binary2)

    def test_language_code(self):
        from faker.providers.misc import Provider
        provider = Provider(self.generator)

        for _ in range(99):
            language_code = provider.language_code()
            self.assertTrue(isinstance(language_code, string_types))
            self.assertTrue(re.match(r'^[a-z]{2,3}$', language_code))

    def test_locale(self):
        from faker.providers.misc import Provider
        provider = Provider(self.generator)

        for _ in range(99):
            locale = provider.locale()
            self.assertTrue(re.match(r'^[a-z]{2,3}_[A-Z]{2}$', locale))

    def test_password(self):
        from faker.providers.misc import Provider
        provider = Provider(self.generator)

        def in_string(char, _str):
            return char in _str

        for _ in range(999):
            password = provider.password()

            self.assertTrue(any([in_string(char, password) for char in "!@#$%^&*()_+"]))
            self.assertTrue(any([in_string(char, password) for char in string.digits]))
            self.assertTrue(any([in_string(char, password) for char in string.ascii_uppercase]))
            self.assertTrue(any([in_string(char, password) for char in string.ascii_lowercase]))

        with self.assertRaises(AssertionError):
            provider.password(length=2)

    def test_prefix_suffix_always_string(self):
        # Locales known to contain `*_male` and `*_female`.
        for locale in ("bg_BG", "dk_DK", "en", "ru_RU", "tr_TR"):
            f = Faker(locale=locale)
            for x in range(20):  # Probabilistic testing.
                self.assertIsInstance(f.prefix(), string_types)
                self.assertIsInstance(f.suffix(), string_types)

    def test_no_words_sentence(self):
        from faker.providers.lorem import Provider

        provider = Provider(self.generator)

        paragraph = provider.paragraph(0)
        self.assertEqual(paragraph, '')

    def test_words_valueerror(self):
        f = Faker()
        self.assertRaises(ValueError, f.text, max_nb_chars=4)

    def test_no_words_paragraph(self):
        from faker.providers.lorem import Provider

        provider = Provider(self.generator)

        sentence = provider.sentence(0)
        self.assertEqual(sentence, '')

    def test_ext_word_list(self):
        fake = Faker()

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
        provider = Provider(self.generator)

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
        provider = Provider(self.generator)

        self.assertTrue(0 <= abs(provider.pyfloat(left_digits=1)) < 10)
        self.assertTrue(0 <= abs(provider.pyfloat(left_digits=0)) < 1)
        x = abs(provider.pyfloat(right_digits=0))
        self.assertTrue(x - int(x) == 0)
        with self.assertRaises(ValueError,
                               msg='A float number cannot have 0 digits '
                               'in total'):
            provider.pyfloat(left_digits=0, right_digits=0)

    def test_us_ssn_valid(self):
        from faker.providers.ssn.en_US import Provider

        provider = Provider(self.generator)
        for i in range(1000):
            ssn = provider.ssn()
            self.assertEqual(len(ssn), 11)
            self.assertNotEqual(ssn[0], '9')
            self.assertNotEqual(ssn[0:3], '666')
            self.assertNotEqual(ssn[0:3], '000')
            self.assertNotEqual(ssn[4:6], '00')
            self.assertNotEqual(ssn[7:11], '0000')

    def test_nl_BE_ssn_valid(self):
        provider = Faker('nl_BE').provider('faker.providers.ssn')

        for i in range(1000):
            ssn = provider.ssn()
            self.assertEqual(len(ssn), 11)
            gen_seq = ssn[6:9]
            gen_chksum = ssn[9:11]
            gen_seq_as_int = int(gen_seq)
            gen_chksum_as_int = int(gen_chksum)
            # Check that the sequence nr is between 1 inclusive and 998 inclusive
            self.assertGreater(gen_seq_as_int, 0)
            self.assertLessEqual(gen_seq_as_int, 998)

            # validate checksum calculation
            # Since the century is not part of ssn, try both below and above year 2000
            ssn_below = int(ssn[0:9])
            chksum_below = 97 - (ssn_below % 97)
            ssn_above = ssn_below + 2000000000
            chksum_above = 97 - (ssn_above % 97)
            results = [chksum_above, chksum_below]
            self.assertIn(gen_chksum_as_int, results)

    def test_email(self):
        factory = Faker()

        for _ in range(999):
            email = factory.email()
            self.assertTrue('@' in email)

    def test_ipv4(self):
        from faker.providers.internet import Provider

        provider = Provider(self.generator)

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

        address = provider.ipv4(private=True)
        self.assertTrue(len(address) >= 7)
        self.assertTrue(len(address) <= 15)
        self.assertTrue(
            re.compile(r'^(\d{1,3}\.){3}\d{1,3}$').search(address))

        address = provider.ipv4(private=False)
        self.assertTrue(len(address) >= 7)
        self.assertTrue(len(address) <= 15)
        self.assertTrue(
            re.compile(r'^(\d{1,3}\.){3}\d{1,3}$').search(address))

    def test_ipv4_network_class(self):
        from faker.providers.internet import Provider
        provider = Provider(self.generator)

        for _ in range(999):
            klass = provider.ipv4_network_class()
            self.assertIn(klass, 'abc')

    def test_ipv4_private(self):
        from faker.providers.internet import Provider
        provider = Provider(self.generator)

        for _ in range(999):
            address = provider.ipv4_private()
            address = text.force_text(address)
            self.assertTrue(len(address) >= 7)
            self.assertTrue(len(address) <= 15)
            self.assertTrue(ip_address(address).is_private)
            self.assertTrue(
                re.compile(r'^(\d{1,3}\.){3}\d{1,3}$').search(address))

        for _ in range(999):
            address = provider.ipv4_private(network=True)
            address = text.force_text(address)
            self.assertTrue(len(address) >= 9)
            self.assertTrue(len(address) <= 18)
            self.assertTrue(ip_network(address)[0].is_private)
            self.assertTrue(
                re.compile(r'^(\d{1,3}\.){3}\d{1,3}/\d{1,2}$').search(address))

    def test_ipv4_private_class_a(self):
        from faker.providers.internet import Provider
        provider = Provider(self.generator)

        for _ in range(999):
            address = provider.ipv4_private(address_class='a')
            address = text.force_text(address)
            self.assertTrue(len(address) >= 7)
            self.assertTrue(len(address) <= 15)
            self.assertTrue(ip_address(address).is_private)
            self.assertTrue(
                re.compile(r'^10\.(\d{1,3}\.){2}\d{1,3}$').search(address))

    def test_ipv4_private_class_b(self):
        from faker.providers.internet import Provider
        provider = Provider(self.generator)

        for _ in range(999):
            address = provider.ipv4_private(address_class='b')
            address = text.force_text(address)
            self.assertTrue(len(address) >= 7)
            self.assertTrue(len(address) <= 15)
            self.assertTrue(ip_address(address).is_private)
            self.assertTrue(
                re.compile(r'^172\.(\d{1,3}\.){2}\d{1,3}$').search(address))

    def test_ipv4_private_class_c(self):
        from faker.providers.internet import Provider
        provider = Provider(self.generator)

        for _ in range(999):
            address = provider.ipv4_private(address_class='c')
            address = text.force_text(address)
            self.assertTrue(len(address) >= 7)
            self.assertTrue(len(address) <= 15)
            self.assertTrue(ip_address(address).is_private)
            self.assertTrue(
                re.compile(r'^192\.168\.\d{1,3}\.\d{1,3}$').search(address))

    def test_ipv4_public(self):
        from faker.providers.internet import Provider
        provider = Provider(self.generator)

        for _ in range(999):
            address = provider.ipv4_public()
            address = text.force_text(address)
            self.assertTrue(len(address) >= 7)
            self.assertTrue(len(address) <= 15)
            self.assertFalse(ip_address(address).is_private, address)
            self.assertTrue(
                re.compile(r'^(\d{1,3}\.){3}\d{1,3}$').search(address))

        for _ in range(999):
            address = provider.ipv4_public(network=True)
            address = text.force_text(address)
            self.assertTrue(len(address) >= 9)
            self.assertTrue(len(address) <= 18)
            # Hack around ipaddress module
            # As 192.0.0.0 is net addr of many 192.0.0.0/* nets
            # ipaddress considers them as private
            if ip_network(address).network_address != ip_address('192.0.0.0'):
                self.assertFalse(ip_network(address)[0].is_private, address)
            self.assertTrue(
                re.compile(r'^(\d{1,3}\.){3}\d{1,3}/\d{1,2}$').search(address))

    def test_ipv4_public_class_a(self):
        from faker.providers.internet import Provider
        provider = Provider(self.generator)

        for _ in range(999):
            address = provider.ipv4_public(address_class='a')
            address = text.force_text(address)
            self.assertTrue(len(address) >= 7)
            self.assertTrue(len(address) <= 15)
            self.assertFalse(ip_address(address).is_private, address)

    def test_ipv4_public_class_b(self):
        from faker.providers.internet import Provider
        provider = Provider(self.generator)

        for _ in range(999):
            address = provider.ipv4_public(address_class='b')
            address = text.force_text(address)
            self.assertTrue(len(address) >= 7)
            self.assertTrue(len(address) <= 15)
            self.assertFalse(ip_address(address).is_private, address)

    def test_ipv4_public_class_c(self):
        from faker.providers.internet import Provider
        provider = Provider(self.generator)

        for _ in range(999):
            address = provider.ipv4_public(address_class='c')
            address = text.force_text(address)
            self.assertTrue(len(address) >= 7)
            self.assertTrue(len(address) <= 15)
            self.assertFalse(ip_address(address).is_private, address)

    def test_ipv6(self):
        from faker.providers.internet import Provider

        provider = Provider(self.generator)

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
        provider = BaseProvider(self.generator)

        # Too many items requested
        with self.assertRaises(ValueError):
            provider.random_sample_unique('abcde', 6)

        # Duplicate inputs reduced to unique set
        with self.assertRaises(ValueError):
            provider.random_sample_unique('aabcd', 5)

        # Same length
        sample = provider.random_sample_unique('aabcd', 4)
        self.assertEqual(sample, set('abcd'))

        sample = provider.random_sample_unique('abcde', 5)
        self.assertEqual(sample, set('abcde'))

        # Length = 3
        sample = provider.random_sample_unique('abcde', 3)
        self.assertEqual(len(sample), 3)
        self.assertTrue(sample.issubset(set('abcde')))

        # Length = 1
        sample = provider.random_sample_unique('abcde', 1)
        self.assertEqual(len(sample), 1)
        self.assertTrue(sample.issubset(set('abcde')))

        # Length = 0
        sample = provider.random_sample_unique('abcde', 0)
        self.assertEqual(sample, set())

    def test_random_number(self):
        from faker.providers import BaseProvider
        provider = BaseProvider(self.generator)

        number = provider.random_number(10, True)
        self.assertEqual(len(str(number)), 10)

    def test_instance_seed_chain(self):
        factory = Faker()

        names = ['Real Name0', 'Real Name1', 'Real Name2', 'Real Name0', 'Real Name2']
        anonymized = [factory.seed_instance(name).name() for name in names]
        self.assertEqual(anonymized[0], anonymized[3])
        self.assertEqual(anonymized[2], anonymized[4])


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
