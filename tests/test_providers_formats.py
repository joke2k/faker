import re

import pytest

from faker import Factory
from faker.config import AVAILABLE_LOCALES, PROVIDERS

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
        prov_cls, lang = Factory._get_provider_class(provider, locale)
        assert lang == locale

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
