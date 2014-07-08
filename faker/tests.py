# coding=utf-8

from __future__ import unicode_literals

import unittest

from faker import Generator
from faker.utils import text, decorators


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
        print_doc()
        print_doc('address')
        print_doc('faker.providers.it_IT.person')
        self.assertRaises(AttributeError,
                          self.generator.get_formatter,
                          'barFormatter')

    def test_command(self):
        from faker.cli import execute_from_command_line
        execute_from_command_line(['faker', 'address'])

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


if __name__ == '__main__':
    unittest.main()
