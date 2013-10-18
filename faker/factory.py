from __future__ import unicode_literals
from __future__ import absolute_import
import sys
from faker import DEFAULT_LOCALE, DEFAULT_PROVIDERS, AVAILABLE_LOCALES
from faker import Generator
from faker import providers as providers_mod


class Factory(object):

    @classmethod
    def create(cls, locale=None, providers=None):

        # fix locale to package name
        locale = locale.replace('-', '_') if locale else DEFAULT_LOCALE
        if '_' in locale:
            locale = locale[:2] + locale[2:].upper()
        if locale not in AVAILABLE_LOCALES:
            raise AttributeError('Invalid configuration for faker locale "{0}"'.format(locale))

        providers = providers or DEFAULT_PROVIDERS

        generator = Generator()
        generator.add_provider(providers_mod.BaseProvider)
        for provider_name in providers:

            provider_class, lang_found = cls._get_provider_class(provider_name, locale)
            provider = provider_class(generator)
            provider.__provider__ = provider_name
            provider.__lang__ = lang_found
            generator.add_provider(provider)

        return generator

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

        raise ValueError('Unable to find provider "{0}" with locale "{1}"'.format(provider, locale))

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
