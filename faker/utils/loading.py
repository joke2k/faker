import os
from importlib import import_module

try:
    import pkgutil

    iter_modules = pkgutil.iter_modules

    def list_module(module):
        path = os.path.dirname(module.__file__)
        return [name for finder, name, is_pkg in iter_modules([path]) if is_pkg]

except (ImportError, NameError):

    def list_module(module):
        path = os.path.dirname(module.__file__)
        return [i for i in os.listdir(path) if os.path.isdir(os.path.join(path, i)) and not i.startswith('_')]


def find_available_locales(providers):
    available_locales = set()
    from faker import providers as providers_mod

    for provider in providers:
        providers_mod_name = providers_mod.__package__ or providers_mod.__name__
 
        path = "{providers}.{provider}".format(
            providers=providers_mod_name,
            provider=provider
        )

        provider_module = import_module(path)
        if getattr(provider_module, 'localized', False):
            langs = list_module(provider_module)
            available_locales.update(langs)
    return available_locales
