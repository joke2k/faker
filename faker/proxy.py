# coding=utf-8

from __future__ import absolute_import, unicode_literals

from collections import OrderedDict
import random
import re
import six

from faker.config import DEFAULT_LOCALE
from faker.factory import Factory
from faker.generator import Generator
from faker.utils.distribution import choices_distribution


class Faker(object):
    """Proxy class capable of supporting multiple locales"""

    cache_pattern = re.compile(r'^_cached_\w*_mapping$')
    generator_attrs = [attr for attr in dir(Generator) if not attr.startswith('__')]

    def __init__(self, locale=None, providers=None,
                 generator=None, includes=None, **config):
        self._factory_map = OrderedDict()
        self._weights = None

        if isinstance(locale, six.string_types):
            locales = [locale]

        # This guarantees a FIFO ordering of elements in `locales` based on the final
        # locale string while discarding duplicates after processing
        elif isinstance(locale, (list, set)):
            assert all(isinstance(l, six.string_types) for l in locale)
            locales = []
            for l in locale:
                final_locale = l.replace('-', '_')
                if final_locale not in locales:
                    locales.append(final_locale)

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
        """
        Handles the "attribute resolution" behavior of this proxy class

        This method checks the specified `attr` in this order:
        1.  Regardless of how many locales were specified, first try to return
            the attribute `attr` if it is present in this proxy class
        2a. In single locale mode, proxy all __getattr__ calls to the only
            internal `Generator` object that will be created
        2b. In multiple locale mode,

        This, however, does not proxy calls to setters, so getters and setters
        should be defined separately.

        :param attr: attribute name
        :return: the appropriate attribute
        """

        try:
            return object.__getattribute__(self, attr)
        except AttributeError:
            if len(self._factories) == 1:
                return getattr(self._factories[0], attr)
            elif attr in self.generator_attrs:
                msg = 'Proxying calls to `%s` is not implemented in multiple locale mode.' % attr
                raise NotImplementedError(msg)
            elif self.cache_pattern.match(attr):
                msg = 'Cached attribute `%s` does not exist' % attr
                raise AttributeError(msg)
            else:
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
    def random(self):
        """
        Proxies `random` getter calls

        In single locale mode, this will be proxied to the `random` getter
        of the only internal `Generator` object. Subclasses will have to
        implement desired behavior in multiple locale mode.
        """

        if len(self._factories) == 1:
            return self._factories[0].random
        else:
            msg = 'Proxying `random` getter calls is not implemented in multiple locale mode.'
            raise NotImplementedError(msg)

    @random.setter
    def random(self, value):
        """
        Proxies `random` setter calls

        In single locale mode, this will be proxied to the `random` setter
        of the only internal `Generator` object. Subclasses will have to
        implement desired behavior in multiple locale mode.
        """

        if len(self._factories) == 1:
            self._factories[0].random = value
        else:
            msg = 'Proxying `random` setter calls is not implemented in multiple locale mode.'
            raise NotImplementedError(msg)

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
