import random
import re

from collections import OrderedDict

from faker.config import DEFAULT_LOCALE
from faker.factory import Factory
from faker.generator import Generator
from faker.utils.distribution import choices_distribution


class Faker:
    """Proxy class capable of supporting multiple locales"""

    cache_pattern = re.compile(r'^_cached_\w*_mapping$')
    generator_attrs = [
        attr for attr in dir(Generator)
        if not attr.startswith('__')
        and attr not in ['seed', 'seed_instance', 'random']
    ]

    def __init__(self, locale=None, providers=None,
                 generator=None, includes=None, **config):
        self._factory_map = OrderedDict()
        self._weights = None

        if isinstance(locale, str):
            locales = [locale.replace('-', '_')]

        # This guarantees a FIFO ordering of elements in `locales` based on the final
        # locale string while discarding duplicates after processing
        elif isinstance(locale, (list, tuple, set)):
            assert all(isinstance(local_code, str) for local_code in locale)
            locales = []
            for code in locale:
                final_locale = code.replace('-', '_')
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

    def __dir__(self):
        attributes = set(super(Faker, self).__dir__())
        for factory in self.factories:
            attributes |= {
                attr for attr in dir(factory) if not attr.startswith('_')
            }
        return sorted(attributes)

    def __getitem__(self, locale):
        return self._factory_map[locale.replace('-', '_')]

    def __getattribute__(self, attr):
        """
        Handles the "attribute resolution" behavior for declared members of this proxy class

        The class method `seed` cannot be called from an instance.

        :param attr: attribute name
        :return: the appropriate attribute
        """
        if attr == 'seed':
            msg = (
                'Calling `.seed()` on instances is deprecated. '
                'Use the class method `Faker.seed()` instead.'
            )
            raise TypeError(msg)
        else:
            return super().__getattribute__(attr)

    def __getattr__(self, attr):
        """
        Handles cache access and proxying behavior

        :param attr: attribute name
        :return: the appropriate attribute
        """

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

    @classmethod
    def seed(cls, seed=None):
        """
        Seeds the shared `random.Random` object across all factories

        :param seed: seed value
        """
        Generator.seed(seed)

    def seed_instance(self, seed=None):
        """
        Creates and seeds a new `random.Random` object for each factory

        :param seed: seed value
        """
        for factory in self._factories:
            factory.seed_instance(seed)

    def seed_locale(self, locale, seed=None):
        """
        Creates and seeds a new `random.Random` object for the factory of the specified locale

        :param locale: locale string
        :param seed: seed value
        """
        self._factory_map[locale.replace('-', '_')].seed_instance(seed)

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
