# coding=utf-8

from __future__ import unicode_literals
from __future__ import absolute_import

from importlib import import_module
import locale as pylocale

from faker import Generator
from faker.config import DEFAULT_LOCALE, DEFAULT_PROVIDERS, AVAILABLE_LOCALES
from faker.utils.loading import list_module


class Factory(object):

    @classmethod
    def create(cls, locale=None, providers=None, generator=None, **config):

        # fix locale to package name
        locale = locale.replace('-', '_') if locale else DEFAULT_LOCALE
        locale = pylocale.normalize(locale).split('.')[0]
        if locale not in AVAILABLE_LOCALES:
            msg = 'Invalid configuration for faker locale "{0}"'.format(locale)
            raise AttributeError(msg)

        providers = providers or DEFAULT_PROVIDERS

        faker = generator or Generator(**config)

        for prov_name in providers:
            prov_cls, lang_found = cls._get_provider_class(prov_name, locale)
            provider = prov_cls(faker)
            provider.__provider__ = prov_name
            provider.__lang__ = lang_found
            faker.add_provider(provider)

        return faker

    @classmethod
    def _get_provider_class(cls, provider, locale=''):

        provider_class = cls._find_provider_class(provider, locale)

        if provider_class:
            return provider_class, locale

        if locale and locale != DEFAULT_LOCALE:
            # fallback to default locale
            provider_class = cls._find_provider_class(provider, DEFAULT_LOCALE)
            if provider_class:
                return provider_class, DEFAULT_LOCALE

        # fallback to no locale
        provider_class = cls._find_provider_class(provider)
        if provider_class:
            return provider_class, None

        msg = 'Unable to find provider "{0}" with locale "{1}"'.format(
            provider, locale)
        raise ValueError(msg)

    @classmethod
    def _find_provider_class(cls, provider_path, locale=None):
        provider_module = import_module(provider_path)

        if getattr(provider_module, 'localized', False):
            available_locales = list_module(provider_module)
            if not locale or locale not in available_locales:
                locale = getattr(provider_module, 'default_locale', DEFAULT_LOCALE)

            path = "{provider_path}.{locale}".format(
                provider_path=provider_path,
                locale=locale,
            )
            provider_module = import_module(path)
        else:
            if locale is not None:
                provider_module = import_module(provider_path)

        return provider_module.Provider
