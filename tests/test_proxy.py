#  -*- coding: utf-8 -*-

from __future__ import unicode_literals

from collections import OrderedDict
import unittest
try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from faker import Faker
from faker.config import DEFAULT_LOCALE
from faker.generator import Generator


class TestFakerProxyClass(unittest.TestCase):

    def setUp(self):
        self.faker = None

    def test_unspecified_locale(self):
        self.faker = Faker()
        assert len(self.faker.locales) == 1
        assert len(self.faker.factories) == 1
        assert self.faker.locales[0] == DEFAULT_LOCALE

    def test_locale_as_string(self):
        locale = 'en_US'
        self.faker = Faker()
        assert len(self.faker.locales) == 1
        assert len(self.faker.factories) == 1
        assert self.faker.locales[0] == locale

    def test_locale_as_list(self):
        locale = ['en_US', 'en_PH', 'ja_JP', 'de_DE']
        self.faker = Faker(locale)
        assert set(self.faker.locales) == set(locale)
        assert len(self.faker.factories) == len(set(locale))

        locale = locale * 3
        self.faker = Faker(locale)
        assert set(self.faker.locales) == set(locale)
        assert len(self.faker.factories) == len(set(locale))

    def test_locale_as_ordereddict(self):
        locale = OrderedDict([
            ('de_DE', 3),
            ('en-US', 2),
            ('en-PH', 1),
            ('ja_JP', 5),
        ])

        self.faker = Faker(locale)
        assert len(self.faker.locales) == 4
        assert self.faker.locales == ['de_DE', 'en_US', 'en_PH', 'ja_JP']
        assert self.faker.weights == [3, 2, 1, 5]

        locale = OrderedDict([
            ('de_DE', 3),
            ('en-US', 2),
            ('en-PH', 1),
            ('ja_JP', 5),
            ('de-DE', 4),
            ('ja-JP', 2),
            ('en-US', 1),
        ])
        self.faker = Faker(locale)
        assert self.faker.locales == ['de_DE', 'en_US', 'en_PH', 'ja_JP']
        assert self.faker.weights == [4, 1, 1, 2]

    def test_items(self):
        locale = ['de_DE', 'en-US', 'en-PH', 'ja_JP', 'de-DE', 'ja-JP', 'en-US']
        processed_locale = list({l.replace('-', '_') for l in locale})
        self.faker = Faker(locale)
        for locale_name, factory in self.faker.items():
            assert locale_name in processed_locale
            assert isinstance(factory, Generator)

    def test_dunder_getitem(self):
        locale = ['de_DE', 'en-US', 'en-PH', 'ja_JP']
        self.faker = Faker(locale)
        assert isinstance(self.faker['en_US'], Generator)
        with self.assertRaises(KeyError):
            self.faker['en-US']

    @patch('faker.proxy.Faker._map_provider_method')
    def test_dunder_getattr_single_locale(self, mock_map_method):
        locales = [None, 'en-US']

        for locale in locales:
            self.faker = Faker(locale)
            mock_map_method.assert_not_called()

            # Multi-locale factory selection logic should not be triggered
            # since there is only one factory (which is immediately returned)
            self.faker.name()
            mock_map_method.assert_not_called()

            # Reset mock object
            mock_map_method.reset_mock()

    @patch('faker.proxy.random.choice')
    @patch('faker.proxy.choices_distribution')
    def test_dunder_getattr_multi_locale_no_weights(self, mock_choices_fn, mock_random_choice):
        locale = ['de_DE', 'en-US', 'en-PH', 'ja_JP']
        self.faker = Faker(locale)
        mock_choices_fn.assert_not_called()
        mock_random_choice.assert_not_called()

        # There are multiple locales, so provider mapping logic is guaranteed to run, and since there
        # are no distribution weights, factory selection logic (if necessary) will use `random.choice`
        with patch('faker.proxy.Faker._map_provider_method',
                   wraps=self.faker._map_provider_method) as mock_map_method:

            # All factories for the listed locales have the `name` provider method
            self.faker.name()
            mock_map_method.assert_called_once()
            mock_choices_fn.assert_not_called()
            mock_random_choice.assert_called_once_with(self.faker.factories)

            # Only `en_PH` factory has provider method `luzon_province`, so there is no
            # need for `random.choice` factory selection logic to run
            mock_map_method.reset_mock()
            mock_choices_fn.reset_mock()
            mock_random_choice.reset_mock()
            self.faker.luzon_province()
            mock_map_method.assert_called_once()
            mock_choices_fn.assert_not_called()
            mock_random_choice.assert_not_called()

            # Both `en_US` and `ja_JP` factories have provider method `zipcode`
            mock_map_method.reset_mock()
            mock_choices_fn.reset_mock()
            mock_random_choice.reset_mock()
            self.faker.zipcode()
            mock_map_method.assert_called_once()
            mock_choices_fn.assert_not_called()
            mock_random_choice.assert_called_once_with(
                [self.faker['en_US'], self.faker['ja_JP']],
            )

    @patch('faker.proxy.random.choice')
    @patch('faker.proxy.choices_distribution')
    def test_dunder_getattr_with_weights(self, mock_choices_fn, mock_random_choice):
        locale = OrderedDict([
            ('de_DE', 3),
            ('en-US', 2),
            ('en-PH', 1),
            ('ja_JP', 5),
        ])
        self.faker = Faker(locale)
        mock_choices_fn.assert_not_called()
        mock_random_choice.assert_not_called()

        # There are multiple locales, so provider mapping logic is guaranteed to run, and since there are
        # distribution weights, factory selection logic (if necessary) will use `choices_distribution`
        with patch('faker.proxy.Faker._map_provider_method',
                   wraps=self.faker._map_provider_method) as mock_map_method:

            # All factories for the listed locales have the `name` provider method
            self.faker.name()
            mock_map_method.assert_called_once()
            mock_choices_fn.assert_called_once_with(self.faker.factories, self.faker.weights, length=1)
            mock_random_choice.assert_not_called()

            # Only `en_PH` factory has provider method `luzon_province`, so there is no
            # need for `choices_distribution` factory selection logic to run
            mock_map_method.reset_mock()
            mock_choices_fn.reset_mock()
            mock_random_choice.reset_mock()
            self.faker.luzon_province()
            mock_map_method.assert_called_once()
            mock_choices_fn.assert_not_called()
            mock_random_choice.assert_not_called()

            # Both `en_US` and `ja_JP` factories have provider method `zipcode`
            mock_map_method.reset_mock()
            mock_choices_fn.reset_mock()
            mock_random_choice.reset_mock()
            self.faker.zipcode()
            mock_map_method.assert_called_once()
            mock_choices_fn.assert_called_once_with(
                [self.faker['en_US'], self.faker['ja_JP']], [2, 5], length=1,
            )
            mock_random_choice.assert_not_called()
