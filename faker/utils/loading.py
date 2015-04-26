import os
from importlib import import_module
import pkgutil


def list_module(module):
    path = os.path.dirname(module.__file__)
    modules = [name for finder, name, is_pkg in pkgutil.iter_modules([path]) if is_pkg]
    if len(modules) > 0:
        return modules
    return [i for i in os.listdir(path) if os.path.isdir(os.path.join(path, i)) and not i.startswith('_')]


def find_available_locales(providers):
    available_locales = set()

    for provider_path in providers:

        provider_module = import_module(provider_path)
        if getattr(provider_module, 'localized', False):
            langs = list_module(provider_module)
            available_locales.update(langs)
    return available_locales


def find_available_providers(modules):
    available_providers = set()
    for providers_mod in modules:
        providers = ['.'.join([providers_mod.__package__, mod]) for mod in list_module(providers_mod)]
        available_providers.update(providers)
    return sorted(available_providers)
