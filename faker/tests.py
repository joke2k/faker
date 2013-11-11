from __future__ import unicode_literals
import unittest
from faker import Generator


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
        self.assertTrue(hasattr(formatter, '__call__') or isinstance(formatter, (classmethod, staticmethod)))

    def test_get_formatter_returns_correct_formatter(self):
        self.assertEqual(self.provider.foo_formatter, self.generator.get_formatter('foo_formatter'))

    def test_get_formatter_throws_exception_on_incorrect_formatter(self):
        self.assertRaises(AttributeError, self.generator.get_formatter, 'barFormatter')

    def test_format_calls_formatter_on_provider(self):
        self.assertEqual('foobar', self.generator.format('foo_formatter'))

    def test_format_transfers_arguments_to_formatter(self):
        self.assertEqual('bazfoo!', self.generator.format('foo_formatter_with_arguments', 'foo', append='!'))

    def test_parse_returns_same_string_when_it_contains_no_curly_braces(self):
        self.assertEqual('fooBar#?', self.generator.parse('fooBar#?'))

    def test_parse_returns_string_with_tokens_replaced_by_formatters(self):
        self.assertEqual('This is foobar a text with " foobar "',
                         self.generator.parse('This is {{foo_formatter}} a text with "{{ foo_formatter }}"'))

    #def testParseReturnsStringWithTokensReplacedByFormattersWithArguments(self):
    #    self.assertEqual('This is foobar',
    #                     self.generator.parse('This is {{foo_formatter_with_arguments:bar}}'))

    def test_magic_call_calls_format(self):
        self.assertEqual('foobar', self.generator.foo_formatter())

    def test_magic_call_calls_format_with_arguments(self):
        self.assertEqual('bazfoo', self.generator.foo_formatter_with_arguments('foo'))

    def test_documentor(self):
        from faker.__main__ import main
        main()
        main('address')
        main('faker.providers.it_IT.person')
        self.assertRaises(AttributeError, self.generator.get_formatter, 'barFormatter')


if __name__ == '__main__':
    unittest.main()
