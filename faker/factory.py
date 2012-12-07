import sys
from faker import DEFAULT_LOCALE, DEFAULT_PROVIDERS, AVAILABLE_LOCALES
from faker import Generator
from faker import providers

class Factory(object):

    @classmethod
    def create(cls, locale=None, providers=None ):

        # fix locale to package name
        locale = locale.replace('-','_') if locale else DEFAULT_LOCALE
        if '_' in locale:
            locale = locale[:2] + locale[2:].upper()
        if locale not in AVAILABLE_LOCALES:
            raise AttributeError('Invalid configuration for faker locale "%s"' % locale)

        providers = providers or DEFAULT_PROVIDERS

        generator = Generator()
        for provider in providers:

            providerClass = cls._getProviderClass( provider, locale )
            generator.addProvider( providerClass(generator) )

        return generator

    @classmethod
    def _getProviderClass(cls, provider, locale=''):

        providerClass = cls._findProviderClass( provider, locale )

        if providerClass:
            return providerClass

        if locale and locale != DEFAULT_LOCALE:
            # fallback to default locale
            providerClass = cls._findProviderClass( provider, DEFAULT_LOCALE )
            if providerClass:
                return providerClass

        # fallback to no locale
        providerClass = cls._findProviderClass( provider )
        if providerClass:
            return providerClass

        raise ValueError('Unable to find provider "%s" with locale "%s"' % (provider, locale))

    @classmethod
    def _findProviderClass(cls, provider, locale=''):

        path = "{providers}{lang}.{provider}".format(
            providers=providers.__package__,
            lang='.' + locale if locale else '',
            provider=provider
        )

        try:
            __import__(path)
        except ImportError:
            return None

        return sys.modules[path].Provider
