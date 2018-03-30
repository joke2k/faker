import unittest
import string

import six

from faker import Generator
from faker.providers import BaseProvider


class TestBaseProvider(unittest.TestCase):
    def setUp(self):
        generator = Generator()
        self.provider = BaseProvider(generator)

    def test_lexify_empty_text(self):
        text = ''

        lexified = self.provider.lexify(text)
        assert not lexified
        lexified = self.provider.lexify(text, letters='someletters')
        assert not lexified

    def test_lexify_only_letters(self):
        text = '???'
        letters = 'someletters'

        # all letters to choose from
        lexified = self.provider.lexify(text)
        self.assertIsInstance(lexified, six.string_types)
        assert len(lexified) == len(text)

        # A set of letters to choose from
        lexified = self.provider.lexify(text, letters=letters)
        self.assertIsInstance(lexified, six.string_types)
        assert len(lexified) == len(text)
        for letter in lexified:
            assert letter in letters

    def test_lexify_mixed_values(self):
        text = '?#? ?# ## ??'
        letters = 'someletters'

        # all letters to choose from
        lexified = self.provider.lexify(text)
        self.assertIsInstance(lexified, six.string_types)
        assert len(lexified) == len(text)

        # A set of letters to choose from
        lexified = self.provider.lexify(text, letters=letters)
        self.assertIsInstance(lexified, six.string_types)
        assert len(lexified) == len(text)
        for letter in lexified:
            assert letter in letters + '# '

    def test_bothify_only_letters(self):
        text = '???'
        letters = 'someletters'

        # all letters to choose from
        bothify = self.provider.bothify(text)
        self.assertIsInstance(bothify, six.string_types)
        assert len(bothify) == len(text)

        # A set of letters to choose from
        bothify = self.provider.bothify(text, letters=letters)
        self.assertIsInstance(bothify, six.string_types)
        assert len(bothify) == len(text)
        for letter in bothify:
            assert letter in letters

    def test_bothify_mixed_values(self):
        text = '?#? ?# ## ??'
        letters = 'someletters'

        # all letters to choose from
        bothify = self.provider.bothify(text)
        self.assertIsInstance(bothify, six.string_types)
        assert len(bothify) == len(text)

        # A set of letters to choose from
        bothify = self.provider.bothify(text, letters=letters)
        self.assertIsInstance(bothify, six.string_types)
        assert len(bothify) == len(text)
        for letter in bothify:
            assert letter in letters + '0123456789# '

    def test_bothify_empty_text(self):
        text = ''

        bothified = self.provider.lexify(text)
        assert not bothified
        bothified = self.provider.lexify(text, letters='someletters')
        assert not bothified

    def test_hexify(self):
        text = '^^^'

        for i in range(1000):
            hexified = self.provider.hexify(text)
            for c in hexified:
                assert c in string.hexdigits[:-6]
                assert c not in string.hexdigits[-6:]

        for i in range(1000):
            hexified = self.provider.hexify(text, upper=True)
            for c in hexified:
                assert c in string.hexdigits[:-6].upper()
                assert c not in string.hexdigits[-6:].lower()

    def test_random_letter(self):
        for i in range(100):
            letter = self.provider.random_letter()
            assert letter.isalpha()

    def test_random_lowercase_letter(self):
        for i in range(100):
            letter = self.provider.random_lowercase_letter()
            assert letter.isalpha()
            assert letter.lower() == letter

    def test_random_uppercase_letter(self):
        for i in range(100):
            letter = self.provider.random_uppercase_letter()
            assert letter.isalpha()
            assert letter.upper() == letter
