# coding=utf-8

from __future__ import unicode_literals
from __future__ import absolute_import

import locale as pylocale
import sys

from faker import DEFAULT_LOCALE, DEFAULT_PROVIDERS, AVAILABLE_LOCALES
from faker import Generator
from faker import providers as providers_mod


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
        faker.add_provider(providers_mod.BaseProvider)

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
    def _find_provider_class(cls, provider, locale=''):

        path = "{providers}{lang}.{provider}".format(
            providers=providers_mod.__package__ or providers_mod.__name__,
            lang='.' + locale if locale else '',
            provider=provider
        )

        try:
            __import__(path)
        except ImportError:
            return None

        return sys.modules[path].Provider
