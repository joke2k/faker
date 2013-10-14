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


    def testAddProviderGivesPriorityToNewlyAddedProvider(self):
        self.generator.add_provider(BarProvider())
        self.assertEqual('barfoo', self.generator.format('foo_formatter'))


    def testGetFormatterReturnsCallable(self):
        formatter = self.generator.get_formatter('foo_formatter')
        self.assertTrue(hasattr(formatter, '__call__') or isinstance(formatter, (classmethod, staticmethod)))


    def testGetFormatterReturnsCorrectFormatter(self):
        self.assertEqual(self.provider.foo_formatter, self.generator.get_formatter('foo_formatter'))


    def testGetFormatterThrowsExceptionOnIncorrectFormatter(self):
        with self.assertRaises(AttributeError):
            self.generator.get_formatter('barFormatter')


    def testFormatCallsFormatterOnProvider(self):
        self.assertEqual('foobar', self.generator.format('foo_formatter'))


    def testFormatTransfersArgumentsToFormatter(self):
        self.assertEqual('bazfoo!', self.generator.format('foo_formatter_with_arguments', 'foo', append='!'))


    def testParseReturnsSameStringWhenItContainsNoCurlyBraces(self):
        self.assertEqual('fooBar#?', self.generator.parse('fooBar#?'))

    def testParseReturnsStringWithTokensReplacedByFormatters(self):
        self.assertEqual('This is foobar a text with " foobar "',
                         self.generator.parse('This is {{foo_formatter}} a text with "{{ foo_formatter }}"'))

    #def testParseReturnsStringWithTokensReplacedByFormattersWithArguments(self):
    #    self.assertEqual('This is foobar',
    #                     self.generator.parse('This is {{foo_formatter_with_arguments:bar}}'))

    def testMagicCallCallsFormat(self):
        self.assertEqual('foobar', self.generator.foo_formatter())

    def testMagicCallCallsFormatWithArguments(self):
        self.assertEqual('bazfoo', self.generator.foo_formatter_with_arguments('foo'))



if __name__ == '__main__':
    unittest.main()