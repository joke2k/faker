# coding=utf-8

from __future__ import absolute_import, unicode_literals

from collections import OrderedDict
import random
import six

from faker.config import DEFAULT_LOCALE
from faker.factory import Factory
from faker.utils.distribution import choices_distribution


class Faker(object):
    """Proxy class capable of supporting multiple locales"""

    def __init__(self, locale=None, providers=None,
                 generator=None, includes=None, **config):
        self._factory_map = OrderedDict()
        self._weights = None
        if isinstance(locale, six.string_types):
            locales = [locale]
        elif isinstance(locale, (list, set)):
            assert all(isinstance(l, six.string_types) for l in locale)
            locales = list({l.replace('-', '_') for l in locale})
        elif isinstance(locale, OrderedDict):
            assert all(isinstance(v, (int, float)) for v in locale.values())
            odict = OrderedDict()
            for k, v in locale.items():
                key = k.replace('-', '_')
                odict[key] = v
            locales = list(odict.keys())
            self._weights = list(odict.values())
        else:
            locales = [DEFAULT_LOCALE]

        for locale in locales:
            self._factory_map[locale] = Factory.create(locale, providers, generator, includes, **config)

        self._locales = locales
        self._factories = list(self._factory_map.values())

    def __getitem__(self, locale):
        return self._factory_map[locale]

    def __getattr__(self, attr):
        try:
            return object.__getattribute__(self, attr)
        except AttributeError:
            if attr.startswith('_cached') and attr.endswith('_mapping'):
                raise AttributeError()
            factory = self._select_factory(attr)
            return getattr(factory, attr)

    def _select_factory(self, method_name):
        """
        Returns a random factory that supports the provider method

        :param method_name: Name of provider method
        :return: A factory that supports the provider method
        """

        if len(self._factories) == 1:
            return self._factories[0]

        factories, weights = self._map_provider_method(method_name)
        if len(factories) == 0:
            msg = "No generator object has attribute '{}'".format(method_name)
            raise AttributeError(msg)
        elif len(factories) == 1:
            return factories[0]

        if weights:
            factory = choices_distribution(factories, weights, length=1)[0]
        else:
            factory = random.choice(factories)
        return factory

    def _map_provider_method(self, method_name):
        """
        Creates a 2-tuple of factories and weights for the given provider method name

        The first element of the tuple contains a list of compatible factories.
        The second element of the tuple contains a list of distribution weights.

        :param method_name: Name of provider method
        :return: 2-tuple (factories, weights)
        """

        # Return cached mapping if it exists for given method
        attr = '_cached_{}_mapping'.format(method_name)
        if hasattr(self, attr):
            return getattr(self, attr)

        # Create mapping if it does not exist
        if self._weights:
            value = [
                (factory, weight)
                for factory, weight in zip(self.factories, self._weights)
                if hasattr(factory, method_name)
            ]
            factories, weights = zip(*value)
            mapping = list(factories), list(weights)
        else:
            value = [
                factory
                for factory in self.factories
                if hasattr(factory, method_name)
            ]
            mapping = value, None

        # Then cache and return results
        setattr(self, attr, mapping)
        return mapping

    @property
    def locales(self):
        return list(self._locales)

    @property
    def weights(self):
        return self._weights

    @property
    def factories(self):
        return self._factories

    def items(self):
        return self._factory_map.items()
