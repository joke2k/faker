import importlib
from faker import DEFAULT_LOCALE, DEFAULT_PROVIDERS, PROVIDERS_PACKAGE, Generator

class Factory(object):

    @classmethod
    def create(cls, locale=DEFAULT_LOCALE ):

        generator = Generator()
        for provider in DEFAULT_PROVIDERS:

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

        providerModulename = '.'
        if locale :
            providerModulename += '%s.%s' % (locale, provider)
        else:
            providerModulename += provider

        try:
            module = importlib.import_module( providerModulename, package= PROVIDERS_PACKAGE )
        except ImportError as e:
            return None

        return getattr(module, 'Provider', None)
