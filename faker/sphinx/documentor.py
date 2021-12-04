# coding=utf-8
import importlib
import inspect
import os

from pathlib import Path

from faker.config import AVAILABLE_LOCALES
from faker.config import PROVIDERS as STANDARD_PROVIDER_NAMES
from faker.providers import BaseProvider

if os.environ.get("READTHEDOCS", False):
    version = os.environ["READTHEDOCS_VERSION"]
    HOME = Path("/home/docs/checkouts/readthedocs.org/user_builds/faker/checkouts") / version
    DOCS_ROOT = HOME / "docs"
else:
    DOCS_ROOT = Path(__file__).resolve().parents[2] / "docs"

SECTION_ADORNMENTS = "#*=-~"

PROVIDER_AUTODOC_TEMPLATE = """
.. autoclass:: {provider_class}
   :members: {provider_methods}
   :undoc-members:
   :show-inheritance:

"""

BASE_PROVIDER_METHOD_NAMES = [
    name for name, method in inspect.getmembers(BaseProvider, inspect.isfunction) if not name.startswith("_")
]


def _get_provider_methods(provider_class):
    try:
        provider_module_name, obj_name = provider_class.rsplit(".", 1)
        provider_module = importlib.import_module(provider_module_name)
        provider = getattr(provider_module, obj_name, None)
    except (ModuleNotFoundError, AttributeError):
        return ""
    else:
        return ", ".join(
            [
                name
                for name, method in inspect.getmembers(provider, inspect.isfunction)
                if not name.startswith("_") and name not in BASE_PROVIDER_METHOD_NAMES
            ]
        )


def _get_localized_provider_info(locale):
    info = []
    for provider_name in STANDARD_PROVIDER_NAMES:
        try:
            locale_module_path = f"{provider_name}.{locale}"
            locale_module = importlib.import_module(locale_module_path)
            provider = getattr(locale_module, "Provider")
        except (ModuleNotFoundError, AttributeError):
            continue
        else:
            provider_class = f"{provider.__module__}.Provider"
            info.append((provider_class, provider_name))
    return info


def _write(fh, s):
    return fh.write(s.encode("utf-8"))


def _hide_edit_on_github(fh):
    _write(fh, ":github_url: hide\n\n")


def _write_title(fh, title, level=1):
    if not isinstance(level, int) or level < 1 or level > 5:
        raise ValueError("`level` must be an integer from 1 to 5")
    if level <= 2:
        _write(fh, SECTION_ADORNMENTS[level - 1] * len(title))
        _write(fh, "\n")
    _write(fh, f"{title}\n")
    _write(fh, SECTION_ADORNMENTS[level - 1] * len(title))
    _write(fh, "\n\n")


def _write_includes(fh):
    _write(fh, ".. include:: ../includes/substitutions.rst")
    _write(fh, "\n\n")


def _write_standard_provider_index():
    with (DOCS_ROOT / "providers.rst").open("wb") as fh:
        _hide_edit_on_github(fh)
        _write_title(fh, "Standard Providers")
        _write(fh, ".. toctree::\n")
        _write(fh, "   :maxdepth: 2\n\n")
        _write(fh, "   providers/baseprovider\n")
        for provider_name in STANDARD_PROVIDER_NAMES:
            _write(fh, f"   providers/{provider_name}\n")


def _write_base_provider_docs():
    (DOCS_ROOT / "providers").mkdir(parents=True, exist_ok=True)
    with (DOCS_ROOT / "providers" / "baseprovider.rst").open("wb") as fh:
        _hide_edit_on_github(fh)
        _write_title(fh, "``faker.providers``")
        _write_includes(fh)
        _write(
            fh,
            PROVIDER_AUTODOC_TEMPLATE.format(
                provider_class="faker.providers.BaseProvider",
                provider_methods=",".join(BASE_PROVIDER_METHOD_NAMES),
            ),
        )


def _write_standard_provider_docs():
    (DOCS_ROOT / "providers").mkdir(parents=True, exist_ok=True)
    for provider_name in STANDARD_PROVIDER_NAMES:
        with (DOCS_ROOT / "providers" / f"{provider_name}.rst").open("wb") as fh:
            provider_class = f"{provider_name}.Provider"
            provider_methods = _get_provider_methods(provider_class)
            _hide_edit_on_github(fh)
            _write_title(fh, f"``{provider_name}``")
            _write_includes(fh)
            _write(
                fh,
                PROVIDER_AUTODOC_TEMPLATE.format(
                    provider_class=provider_class,
                    provider_methods=provider_methods,
                ),
            )


def _write_localized_provider_index():
    with (DOCS_ROOT / "locales.rst").open("wb") as fh:
        _hide_edit_on_github(fh)
        _write_title(fh, "Localized Providers")
        _write(fh, ".. toctree::\n")
        _write(fh, "   :maxdepth: 2\n\n")
        for locale in AVAILABLE_LOCALES:
            _write(fh, f"   locales/{locale}\n")


def _write_localized_provider_docs():
    (DOCS_ROOT / "locales").mkdir(parents=True, exist_ok=True)
    for locale in AVAILABLE_LOCALES:
        info = _get_localized_provider_info(locale)
        with (DOCS_ROOT / "locales" / "{}.rst".format(locale)).open("wb") as fh:
            _hide_edit_on_github(fh)
            _write_title(fh, f"Locale {locale}")
            _write_includes(fh)
            for provider_class, standard_provider_name in info:
                provider_methods = _get_provider_methods(provider_class)
                _write_title(fh, f"``{standard_provider_name}``", level=2)
                _write(
                    fh,
                    PROVIDER_AUTODOC_TEMPLATE.format(
                        provider_class=provider_class,
                        provider_methods=provider_methods,
                    ),
                )


def write_provider_docs():
    DOCS_ROOT.mkdir(parents=True, exist_ok=True)
    _write_standard_provider_index()
    _write_base_provider_docs()
    _write_standard_provider_docs()
    _write_localized_provider_index()
    _write_localized_provider_docs()
