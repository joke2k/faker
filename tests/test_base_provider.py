import unittest

from faker import Generator
from faker.providers import BaseProvider
from tests import string_types


class TestBaseProvider(unittest.TestCase):
    def setUp(self):
        generator = Generator()
        self.provider = BaseProvider(generator)

    def test_lexify_empty_text(self):
        text = ''

        lexified = self.provider.lexify(text)
        self.assertFalse(lexified)
        lexified = self.provider.lexify(text, letters='someletters')
        self.assertFalse(lexified)

    def test_lexify_only_letters(self):
        text = '???'
        letters = 'someletters'

        # all letters to choose from
        lexified = self.provider.lexify(text)
        self.assertIsInstance(lexified, string_types)
        self.assertEqual(len(lexified), len(text))

        # A set of letters to choose from
        lexified = self.provider.lexify(text, letters=letters)
        self.assertIsInstance(lexified, string_types)
        self.assertEqual(len(lexified), len(text))
        for letter in lexified:
            self.assertIn(letter, letters)

    def test_lexify_mixed_values(self):
        text = '?#? ?# ## ??'
        letters = 'someletters'

        # all letters to choose from
        lexified = self.provider.lexify(text)
        self.assertIsInstance(lexified, string_types)
        self.assertEqual(len(lexified), len(text))

        # A set of letters to choose from
        lexified = self.provider.lexify(text, letters=letters)
        self.assertIsInstance(lexified, string_types)
        self.assertEqual(len(lexified), len(text))
        for letter in lexified:
            self.assertIn(letter, letters + '# ')

    def test_bothify_only_letters(self):
        text = '???'
        letters = 'someletters'

        # all letters to choose from
        bothify = self.provider.bothify(text)
        self.assertIsInstance(bothify, string_types)
        self.assertEqual(len(bothify), len(text))

        # A set of letters to choose from
        bothify = self.provider.bothify(text, letters=letters)
        self.assertIsInstance(bothify, string_types)
        self.assertEqual(len(bothify), len(text))
        for letter in bothify:
            self.assertIn(letter, letters)

    def test_bothify_mixed_values(self):
        text = '?#? ?# ## ??'
        letters = 'someletters'

        # all letters to choose from
        bothify = self.provider.bothify(text)
        self.assertIsInstance(bothify, string_types)
        self.assertEqual(len(bothify), len(text))

        # A set of letters to choose from
        bothify = self.provider.bothify(text, letters=letters)
        self.assertIsInstance(bothify, string_types)
        self.assertEqual(len(bothify), len(text))
        for letter in bothify:
            self.assertIn(letter, letters + '0123456789# ')

    def test_bothify_empty_text(self):
        text = ''

        bothified = self.provider.lexify(text)
        self.assertFalse(bothified)
        bothified = self.provider.lexify(text, letters='someletters')
        self.assertFalse(bothified)
