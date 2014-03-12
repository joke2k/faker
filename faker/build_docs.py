from __future__ import print_function
from __future__ import unicode_literals
import os
import sys

if sys.version < '3':
    text_type = unicode
    binary_type = str
else:
    text_type = str
    binary_type = bytes


DOCS_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'docs')

def write(fh, s):
    if fh:
        return fh.write(s.encode('utf-8'))
    else:
        return print(s)

def print_provider(fh, doc, provider, formatters, excludes=None):

    if excludes is None:
        excludes = []


    write(fh, '\n')
    title = "``faker.providers.{0}``".format(doc.get_provider_name(provider))
    write(fh, '%s\n' % title)
    write(fh, "-" * len(title))
    write(fh, '\n\n::\n')

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
        write(fh, '\n')
        for line in lines:
            for i in range(0, (len(line) // remains) + 1):
                write(fh, "\t{fake:<{margin}}{separator} {example}".format(
                    fake=signature,
                    separator=separator,
                    example=line[i*remains:(i+1)*remains],
                    margin=margin
                ))
                signature = separator = ' '
    write(fh, '\n')


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
            print_provider(None, doc, fake.get_providers()[0], doc.get_provider_formatters(fake.get_providers()[0]))
        else:
            try:
                print(fake.format(provider_or_field, *args))
            except AttributeError:
                print('No faker found for "{0}({1})"'.format(provider_or_field, args))

    else:
        doc = documentor.Documentor(fake)

        formatters = doc.get_formatters(with_args=True, with_defaults=True)

        for provider, fakers in formatters:
            provider_name = doc.get_provider_name(provider)
            with open(os.path.join(DOCS_ROOT, 'providers', '%s.rst' % provider_name), 'wb') as fh:
                print_provider(fh, doc, provider, fakers)

        with open(os.path.join(DOCS_ROOT, 'providers.rst'), 'wb') as fh:
            write(fh, 'Providers\n')
            write(fh, '=========\n')
            write(fh, '.. toctree::\n')
            write(fh, '   :maxdepth: 2\n\n')
            [write(fh, '   providers/%s\n' % doc.get_provider_name(provider)) for provider, fakers in formatters]

        for lang in AVAILABLE_LOCALES:
            with open(os.path.join(DOCS_ROOT, 'locales', '%s.rst' % lang), 'wb') as fh:
                write(fh, '\n')
                title = 'Language {0}\n'.format(lang)
                write(fh, title)
                write(fh, '=' * len(title))
                write(fh, '\n')
                fake = Faker(locale=lang)
                d = documentor.Documentor(fake)

                for p, fs in d.get_formatters(with_args=True, with_defaults=True, locale=lang,
                                              excludes=base_provider_formatters):
                    print_provider(fh, d, p, fs)
        with open(os.path.join(DOCS_ROOT, 'locales.rst'), 'wb') as fh:
            write(fh, 'Locales\n')
            write(fh, '=======\n')
            write(fh, '.. toctree::\n')
            write(fh, '   :maxdepth: 2\n\n')
            [write(fh, '   locales/%s\n' % lang) for lang in AVAILABLE_LOCALES]


# wrappers for sphinx
def _main(app, *args, **kwargs):
    return main(*args, **kwargs)

def setup(app):
    app.connect(str('builder-inited'), _main)


if __name__ == "__main__":
    if sys.stdout.encoding is None:
        print("please set python env PYTHONIOENCODING=UTF-8, example: "
              "export PYTHONIOENCODING=UTF-8, when write to stdout", file=sys.stderr)
        exit(1)
    main(*sys.argv[1:])
