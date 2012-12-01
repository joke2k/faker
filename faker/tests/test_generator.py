import unittest
from faker import Generator

class BarProvider(object):

    def fooFormatter(self):
        return 'barfoo'


class FooProvider(object):

    def fooFormatter(self):
        return 'foobar'

    def fooFormatterWithArguments(self, param='', append=''):
        return 'baz' + param + append


class FactoryTestCase(unittest.TestCase):
    def setUp(self):
        self.generator = Generator()
        self.provider = FooProvider()
        self.generator.addProvider(self.provider)


    def testAddProviderGivesPriorityToNewlyAddedProvider(self):
        self.generator.addProvider(BarProvider())
        self.assertEqual('barfoo', self.generator.format('fooFormatter'))


    def testGetFormatterReturnsCallable(self):
        formatter = self.generator.getFormatter('fooFormatter')
        self.assertTrue( hasattr(formatter, '__call__') or isinstance(formatter,(classmethod,staticmethod)) )


    def testGetFormatterReturnsCorrectFormatter(self):
        self.assertEqual(self.provider.fooFormatter, self.generator.getFormatter('fooFormatter') )


    def testGetFormatterThrowsExceptionOnIncorrectFormatter(self):
        with self.assertRaises(AttributeError):
            self.generator.getFormatter('barFormatter')


    def testFormatCallsFormatterOnProvider(self):
        self.assertEqual('foobar', self.generator.format('fooFormatter'))


    def testFormatTransfersArgumentsToFormatter(self):
        self.assertEqual('bazfoo!', self.generator.format('fooFormatterWithArguments', 'foo', append='!'))


    def testParseReturnsSameStringWhenItContainsNoCurlyBraces(self):
        self.assertEqual('fooBar#?', self.generator.parse('fooBar#?'))


    def testParseReturnsStringWithTokensReplacedByFormatters(self):
        self.assertEqual('This is foobar a text with foobar',
            self.generator.parse('This is {{fooFormatter}} a text with {{ fooFormatter }}'))


    def testMagicCallCallsFormat(self):
        self.assertEqual('foobar', self.generator.fooFormatter())


    def testMagicCallCallsFormatWithArguments(self):
        self.assertEqual('bazfoo', self.generator.fooFormatterWithArguments('foo'))



if __name__ == '__main__':
    unittest.main()