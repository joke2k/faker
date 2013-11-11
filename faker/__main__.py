from __future__ import unicode_literals
from __future__ import print_function
import sys

if sys.version < '3':
    text_type = unicode
    binary_type = str
else:
    text_type = str
    binary_type = bytes


def print_provider(doc, provider, formatters, excludes=None):
    if excludes is None:
        excludes = []

    print()
    print("### faker.providers.{0}".format(doc.get_provider_name(provider)))
    print()

    for signature, example in formatters.items():
        if signature in excludes:
            continue
        try:
            lines = text_type(example).expandtabs().splitlines()
        except UnicodeEncodeError:
            raise Exception('error on "{0}" with value "{1}"'.format(signature, example))
        margin = max(30, doc.max_name_len+1)
        remains = 150 - margin
        separator = '#'
        for line in lines:
            for i in range(0, (len(line) // remains) + 1):
                print("\t{fake:<{margin}}{separator} {example}".format(
                    fake=signature,
                    separator=separator,
                    example=line[i*remains:(i+1)*remains],
                    margin=margin
                ))
                signature = separator = ' '


def main(provider_or_field=None, *args):
    from faker import Faker, Factory, documentor, DEFAULT_LOCALE, AVAILABLE_LOCALES
    fake = Faker(locale=DEFAULT_LOCALE)

    from faker.providers import BaseProvider
    base_provider_formatters = [f for f in dir(BaseProvider)]

    if provider_or_field:
        if '.' in provider_or_field:
            parts = provider_or_field.split('.')
            locale = parts[-2] if parts[-2] in AVAILABLE_LOCALES else DEFAULT_LOCALE
            fake = Factory.create(locale, providers=[parts[-1]])
            doc = documentor.Documentor(fake)
            doc.already_generated = base_provider_formatters
            print_provider(doc, fake.get_providers()[0], doc.get_provider_formatters(fake.get_providers()[0]))
        else:
            try:
                print(fake.format(provider_or_field, *args))
            except AttributeError:
                print('No faker found for "{0}({1})"'.format(provider_or_field, args))

    else:
        doc = documentor.Documentor(fake)

        formatters = doc.get_formatters(with_args=True, with_defaults=True)

        for provider, fakers in formatters:

            print_provider(doc, provider, fakers)

        for lang in AVAILABLE_LOCALES:
            if lang == DEFAULT_LOCALE:
                continue
            print()
            print('## LANGUAGE {0}'.format(lang))
            fake = Faker(locale=lang)
            d = documentor.Documentor(fake)

            for p, fs in d.get_formatters(with_args=True, with_defaults=True, locale=lang,
                                          excludes=base_provider_formatters):
                print_provider(d, p, fs)


if __name__ == "__main__":
    if sys.stdout.encoding is None:
        print("please set python env PYTHONIOENCODING=UTF-8, example: "
              "export PYTHONIOENCODING=UTF-8, when write to stdout", file=sys.stderr)
        exit(1)
    main(*sys.argv[1:])