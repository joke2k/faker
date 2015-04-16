# coding=utf-8
from importlib import import_module
from faker.utils.loading import find_available_locales, find_available_providers

DEFAULT_LOCALE = 'en_US'

DEFAULT_PROVIDERS_MODULES = (
    'faker.providers',
)

DEFAULT_PROVIDERS = find_available_providers([import_module(path) for path in DEFAULT_PROVIDERS_MODULES])

AVAILABLE_LOCALES = find_available_locales(DEFAULT_PROVIDERS)
