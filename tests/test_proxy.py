#  -*- coding: utf-8 -*-

from __future__ import unicode_literals

from collections import OrderedDict
import unittest
try:
    from unittest.mock import patch, PropertyMock
except ImportError:
    from mock import patch, PropertyMock

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
        locale = ['en-US', 'en_PH', 'ja_JP', 'de-DE']
        expected = ['en_US', 'en_PH', 'ja_JP', 'de_DE']
        for _ in range(10):
            self.faker = Faker(locale)
            assert self.faker.locales == expected
            assert len(self.faker.factories) == len(expected)

        locale = ['en-US', 'en_PH', 'ja_JP', 'de-DE', 'ja-JP', 'de_DE', 'en-US'] * 3
        expected = ['en_US', 'en_PH', 'ja_JP', 'de_DE']
        for _ in range(10):
            self.faker = Faker(locale)
            assert self.faker.locales == expected
            assert len(self.faker.factories) == len(expected)

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

        for l in locale:
            assert isinstance(self.faker[l], Generator)

        with self.assertRaises(KeyError):
            self.faker['en_GB']

    def test_seed_classmethod(self):
        self.faker = Faker()

        # Verify `seed()` is not callable from a class instance
        with self.assertRaises(TypeError):
            self.faker.seed(0)

        # Verify calls to `seed()` from a class object are proxied properly
        with patch('faker.generator.Generator.seed') as mock_seed:
            mock_seed.assert_not_called()
            Faker.seed(0)
            mock_seed.assert_called_once_with(0)

    def test_seed_instance(self):
        locale = ['de_DE', 'en-US', 'en-PH', 'ja_JP']
        self.faker = Faker(locale)

        with patch('faker.generator.Generator.seed_instance') as mock_seed_instance:
            mock_seed_instance.assert_not_called()
            self.faker.seed_instance(0)

            # Verify `seed_instance(0)` was called 4 times (one for each locale)
            calls = mock_seed_instance.call_args_list
            assert len(calls) == 4
            for call in calls:
                assert call.args == (0, )
                assert call.kwargs == {}

    def test_seed_locale(self):
        from faker.generator import random as shared_random_instance

        locale = ['de_DE', 'en-US', 'en-PH', 'ja_JP']
        self.faker = Faker(locale)

        # Get current state of each factory's random instance
        states = {}
        for locale, factory in self.faker.items():
            states[locale] = factory.random.getstate()

        # Create a new random instance for en_US factory with seed value
        self.faker.seed_locale('en_US', 0)

        for locale, factory in self.faker.items():
            # en_US factory should have changed
            if locale == 'en_US':
                assert factory.random != shared_random_instance
                assert factory.random.getstate() != states[locale]

            # There should be no changes for the rest
            else:
                assert factory.random == shared_random_instance
                assert factory.random.getstate() == states[locale]

    def test_single_locale_proxy_behavior(self):
        self.faker = Faker()
        internal_factory = self.faker.factories[0]

        # Test if `Generator` attributes are proxied properly
        for attr in self.faker.generator_attrs:
            assert getattr(self.faker, attr) == getattr(internal_factory, attr)

        # Test if `random` getter and setter are proxied properly
        tmp_random = self.faker.random
        assert internal_factory.random != 1
        self.faker.random = 1
        assert internal_factory.random == 1
        self.faker.random = tmp_random

        # Test if a valid provider method is proxied properly
        # Factory selection logic should not be triggered
        with patch('faker.proxy.Faker._select_factory') as mock_select_factory:
            mock_select_factory.assert_not_called()
            assert self.faker.name == internal_factory.name
            self.faker.name()
            mock_select_factory.assert_not_called()

    def test_multiple_locale_proxy_behavior(self):
        self.faker = Faker(['de-DE', 'en-US', 'en-PH', 'ja-JP'])

        # `Generator` attributes are not implemented
        for attr in self.faker.generator_attrs:
            with self.assertRaises(NotImplementedError):
                getattr(self.faker, attr)

        # The `random` getter is not implemented
        with self.assertRaises(NotImplementedError):
            random = self.faker.random
            random.seed(0)

        # The `random` setter is not implemented
        with self.assertRaises(NotImplementedError):
            self.faker.random = 1

    def test_multiple_locale_caching_behavior(self):
        self.faker = Faker(['de_DE', 'en-US', 'en-PH', 'ja_JP'])

        with patch('faker.proxy.Faker._map_provider_method',
                   wraps=self.faker._map_provider_method) as mock_map_method:
            mock_map_method.assert_not_called()
            assert not hasattr(self.faker, '_cached_name_mapping')

            # Test cache creation
            self.faker.name()
            assert hasattr(self.faker, '_cached_name_mapping')
            mock_map_method.assert_called_once_with('name')

            # Test subsequent cache access
            with patch.object(Faker, '_cached_name_mapping', create=True,
                              new_callable=PropertyMock) as mock_cached_map:
                # Keep test fast by patching the cached mapping to return something simpler
                mock_cached_map.return_value = [self.faker['en_US']], [1]
                for _ in range(100):
                    self.faker.name()

                # Python's hasattr() internally calls getattr()
                # So each call to name() accesses the cached mapping twice
                assert mock_cached_map.call_count == 200

    @patch('faker.proxy.random.choice')
    @patch('faker.proxy.choices_distribution')
    def test_multiple_locale_factory_selection_no_weights(self, mock_choices_fn, mock_random_choice):
        self.faker = Faker(['de_DE', 'en-US', 'en-PH', 'ja_JP'])

        # There are no distribution weights, so factory selection logic will use `random.choice`
        # if multiple factories have the specified provider method
        with patch('faker.proxy.Faker._select_factory',
                   wraps=self.faker._select_factory) as mock_select_factory:
            mock_select_factory.assert_not_called()
            mock_choices_fn.assert_not_called()
            mock_random_choice.assert_not_called()

            # All factories for the listed locales have the `name` provider method
            self.faker.name()
            mock_select_factory.assert_called_once_with('name')
            mock_choices_fn.assert_not_called()
            mock_random_choice.assert_called_once_with(self.faker.factories)
            mock_select_factory.reset_mock()
            mock_choices_fn.reset_mock()
            mock_random_choice.reset_mock()

            # Only `en_PH` factory has provider method `luzon_province`, so there is no
            # need for `random.choice` factory selection logic to run
            self.faker.luzon_province()
            mock_select_factory.assert_called_with('luzon_province')
            mock_choices_fn.assert_not_called()
            mock_random_choice.assert_not_called()
            mock_select_factory.reset_mock()
            mock_choices_fn.reset_mock()
            mock_random_choice.reset_mock()

            # Both `en_US` and `ja_JP` factories have provider method `zipcode`
            self.faker.zipcode()
            mock_select_factory.assert_called_once_with('zipcode')
            mock_choices_fn.assert_not_called()
            mock_random_choice.assert_called_once_with(
                [self.faker['en_US'], self.faker['ja_JP']],
            )
            mock_select_factory.reset_mock()
            mock_choices_fn.reset_mock()
            mock_random_choice.reset_mock()

    @patch('faker.proxy.random.choice')
    @patch('faker.proxy.choices_distribution')
    def test_multiple_locale_factory_selection_no_weights(self, mock_choices_fn, mock_random_choice):
        locale = OrderedDict([
            ('de_DE', 3),
            ('en-US', 2),
            ('en-PH', 1),
            ('ja_JP', 5),
        ])
        self.faker = Faker(locale)
        mock_choices_fn.assert_not_called()
        mock_random_choice.assert_not_called()

        # Distribution weights have been specified, so factory selection logic will use
        # `choices_distribution` if multiple factories have the specified provider method
        with patch('faker.proxy.Faker._select_factory',
                   wraps=self.faker._select_factory) as mock_select_factory:

            # All factories for the listed locales have the `name` provider method
            self.faker.name()
            mock_select_factory.assert_called_once_with('name')
            mock_choices_fn.assert_called_once_with(self.faker.factories, self.faker.weights, length=1)
            mock_random_choice.assert_not_called()
            mock_select_factory.reset_mock()
            mock_choices_fn.reset_mock()
            mock_random_choice.reset_mock()

            # Only `en_PH` factory has provider method `luzon_province`, so there is no
            # need for `choices_distribution` factory selection logic to run
            self.faker.luzon_province()
            mock_select_factory.assert_called_once_with('luzon_province')
            mock_choices_fn.assert_not_called()
            mock_random_choice.assert_not_called()
            mock_select_factory.reset_mock()
            mock_choices_fn.reset_mock()
            mock_random_choice.reset_mock()

            # Both `en_US` and `ja_JP` factories have provider method `zipcode`
            self.faker.zipcode()
            mock_select_factory.assert_called_once()
            mock_choices_fn.assert_called_once_with(
                [self.faker['en_US'], self.faker['ja_JP']], [2, 5], length=1,
            )
            mock_random_choice.assert_not_called()
            mock_select_factory.reset_mock()
            mock_choices_fn.reset_mock()
            mock_random_choice.reset_mock()
