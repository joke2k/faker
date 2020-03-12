# coding=utf-8
import importlib
import inspect
import os

from faker.config import AVAILABLE_LOCALES
from faker.config import PROVIDERS as STANDARD_PROVIDER_NAMES
from faker.providers import BaseProvider

DOCS_ROOT = os.path.abspath(os.path.join('..', 'docs'))

SECTION_ADORNMENTS = '#*=-~'

PROVIDER_AUTODOC_TEMPLATE = """
.. autoclass:: {provider_class}
   :members: {provider_methods}
   :undoc-members:
   :show-inheritance:

"""

BASE_PROVIDER_METHOD_NAMES = [
    name for name, method in inspect.getmembers(BaseProvider, inspect.isfunction)
    if not name.startswith('_')
]


def _get_provider_methods(provider_class):
    try:
        provider_module_name, obj_name = provider_class.rsplit('.', 1)
        provider_module = importlib.import_module(provider_module_name)
        provider = getattr(provider_module, obj_name, None)
    except (ModuleNotFoundError, AttributeError):
        return ''
    else:
        return ', '.join([
            name for name, method in inspect.getmembers(provider, inspect.isfunction)
            if not name.startswith('_') and name not in BASE_PROVIDER_METHOD_NAMES
        ])


def _get_localized_provider_info(locale):
    info = []
    for provider_name in STANDARD_PROVIDER_NAMES:
        try:
            locale_module_path = '{}.{}'.format(provider_name, locale)
            locale_module = importlib.import_module(locale_module_path)
            provider = getattr(locale_module, 'Provider')
        except (ModuleNotFoundError, AttributeError):
            continue
        else:
            provider_class = '{}.Provider'.format(provider.__module__)
            info.append((provider_class, provider_name))
    return info


def _write(fh, s):
    return fh.write(s.encode('utf-8'))


def _hide_edit_on_github(fh):
    _write(fh, ':github_url: hide\n\n')


def _write_title(fh, title, level=1):
    if not isinstance(level, int) or level < 1 or level > 5:
        raise ValueError('`level` must be an integer from 1 to 5')
    if level <= 2:
        _write(fh, SECTION_ADORNMENTS[level - 1] * len(title))
        _write(fh, '\n')
    _write(fh, '{}\n'.format(title))
    _write(fh, SECTION_ADORNMENTS[level - 1] * len(title))
    _write(fh, '\n\n')


def _write_standard_provider_index():
    fname = os.path.join(DOCS_ROOT, 'providers.rst')
    with open(fname, 'wb') as fh:
        _hide_edit_on_github(fh)
        _write_title(fh, 'Standard Providers')
        _write(fh, '.. toctree::\n')
        _write(fh, '   :maxdepth: 2\n\n')
        _write(fh, '   providers/baseprovider\n')
        for provider_name in STANDARD_PROVIDER_NAMES:
            _write(fh, '   providers/{}\n'.format(provider_name))


def _write_base_provider_docs():
    fname = os.path.join(DOCS_ROOT, 'providers', 'baseprovider.rst')
    with open(fname, 'wb') as fh:
        _hide_edit_on_github(fh)
        _write_title(fh, '``faker.providers``')
        _write(fh, PROVIDER_AUTODOC_TEMPLATE.format(
            provider_class='faker.providers.BaseProvider',
            provider_methods=','.join(BASE_PROVIDER_METHOD_NAMES),
        ))


def _write_standard_provider_docs():
    for provider_name in STANDARD_PROVIDER_NAMES:
        fname = os.path.join(DOCS_ROOT, 'providers', '%s.rst' % provider_name)
        with open(fname, 'wb') as fh:
            provider_class = '{}.Provider'.format(provider_name)
            provider_methods = _get_provider_methods(provider_class)
            _hide_edit_on_github(fh)
            _write_title(fh, '``{}``'.format(provider_name))
            _write(fh, PROVIDER_AUTODOC_TEMPLATE.format(
                provider_class=provider_class,
                provider_methods=provider_methods,
            ))


def _write_localized_provider_index():
    fname = os.path.join(DOCS_ROOT, 'locales.rst')
    with open(fname, 'wb') as fh:
        _hide_edit_on_github(fh)
        _write_title(fh, 'Localized Providers')
        _write(fh, '.. toctree::\n')
        _write(fh, '   :maxdepth: 2\n\n')
        for locale in AVAILABLE_LOCALES:
            _write(fh, '   locales/{}\n'.format(locale))


def _write_localized_provider_docs():
    for locale in AVAILABLE_LOCALES:
        info = _get_localized_provider_info(locale)
        fname = os.path.join(DOCS_ROOT, 'locales', '{}.rst'.format(locale))
        with open(fname, 'wb') as fh:
            _hide_edit_on_github(fh)
            _write_title(fh, 'Locale {}'.format(locale))
            for provider_class, standard_provider_name in info:
                provider_methods = _get_provider_methods(provider_class)
                _write_title(fh, '``{}``'.format(standard_provider_name), level=2)
                _write(fh, PROVIDER_AUTODOC_TEMPLATE.format(
                    provider_class=provider_class,
                    provider_methods=provider_methods,
                ))


def write_provider_docs():
    _write_standard_provider_index()
    _write_base_provider_docs()
    _write_standard_provider_docs()
    _write_localized_provider_index()
    _write_localized_provider_docs()
