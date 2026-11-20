import re

import pytest

from faker import Factory
from faker.config import AVAILABLE_LOCALES, DEFAULT_LOCALE, PROVIDERS

locales = AVAILABLE_LOCALES

# searches {{group}} and capture the _group_
find_group = re.compile(r"\{\{(\w+)\}\}")


@pytest.mark.parametrize("locale", locales)
def test_no_invalid_formats(locale):
    """
    For each locale, for each provider, search all the definitions of "formats"
    and make sure that all the providers in there (e.g. {{group}}) are valid
    and do not emit empty strings. Empty strings are allowed only if the group
    is not surrounded by spaces. This is a quick way to make sure that no
    string is generated with "double spaces", starting spaces or ending spaces.
    """
    faker = Factory.create(locale)
    errors = []

    for provider in PROVIDERS:
        if provider == "faker.providers":
            continue
        prov_cls, lang, default_lang = Factory._find_provider_class(provider, locale)
        if default_lang is None:
            # for non-localized providers, the discovered language will be None
            assert lang is None
        else:
            # for localized providers, the discovered language will either be
            # the requested one
            # or the default language of the provider
            # or the fallback locale
            assert lang in (locale, default_lang or DEFAULT_LOCALE)

        attributes = set(dir(prov_cls))

        for attribute in attributes:
            # consider only the format attributes
            if not attribute.endswith("formats"):
                continue
            formats = getattr(prov_cls, attribute)
            # may be a function or some other bizarre types
            if not isinstance(formats, (list, tuple)):
                continue
            for format in formats:
                # search all the {{groups}} in the format
                for match in find_group.finditer(format):
                    group = match.group(1)
                    try:
                        attr = faker.format(group)
                    except AttributeError as e:
                        errors.append(str(e))
                        continue
                    # touching = True if the group is touching sometime on at
                    # least one side, i.e. it's not surrounded by spaces
                    touching = False
                    if match.start() != 0 and format[match.start() - 1] != " ":
                        touching = True
                    if match.end() != len(format) and format[match.end()] != " ":
                        touching = True

                    if not attr and not touching:
                        errors.append(
                            "Attribute {{%s}} provided an invalid value in format '%s' from %s.%s.%s"
                            % (group, format, provider, locale, attribute),
                        )
    # group errors reporting all the ones from the same locale
    assert not errors, "Errors:\n - " + "\n - ".join(errors)


# a run of letters (no digits, no underscore)
find_word = re.compile(r"[^\W\d_]+")
latin_letter = re.compile(r"[A-Za-z]")
cyrillic_letter = re.compile(r"[Ѐ-ӿ]")


def _strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for key, item in value.items():
            yield from _strings(key)
            yield from _strings(item)
    elif isinstance(value, (list, tuple, set, frozenset)):
        for item in value:
            yield from _strings(item)


@pytest.mark.parametrize("locale", locales)
def test_no_mixed_latin_and_cyrillic_words(locale):
    """
    Latin and Cyrillic have letters that look the same (a/а, e/е, o/о, c/с, i/і, ...).
    A word that mixes both scripts looks right but compares, sorts and searches wrong,
    so no word in the provider data may contain letters from both scripts.
    """
    errors = []
    for provider in PROVIDERS:
        if provider == "faker.providers":
            continue
        prov_cls, _, _ = Factory._find_provider_class(provider, locale)
        for attribute, value in vars(prov_cls).items():
            if attribute.startswith("__"):
                continue
            for string in _strings(value):
                for word in find_word.findall(string):
                    if latin_letter.search(word) and cyrillic_letter.search(word):
                        errors.append(f"{prov_cls.__module__}.{attribute}: {word!r}")
    assert not errors, "Words mixing Latin and Cyrillic letters:\n - " + "\n - ".join(sorted(set(errors)))
