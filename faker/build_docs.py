from __future__ import print_function
import os
import sys

if sys.version < '3':
    text_type = unicode
    binary_type = str
else:
    text_type = str
    binary_type = bytes


def print_provider(doc, provider, formatters, excludes=None, fh=None):

    if excludes is None:
        excludes = []

    if fh:
        write = fh.write
    else:
        import ipdb; ipdb.set_trace()
        write = print

    write('\n')
    title = "``faker.providers.{0}``".format(doc.get_provider_name(provider))
    write('%s\n' % title)
    write("-" * len(title))
    write('\n\n::\n')

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
        write('\n')
        for line in lines:
            for i in range(0, (len(line) // remains) + 1):
                write("\t{fake:<{margin}}{separator} {example}".format(
                    fake=signature,
                    separator=separator,
                    example=line[i*remains:(i+1)*remains].encode('utf-8'),
                    margin=margin
                ))
                signature = separator = ' '
    write('\n')


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
            provider_name = doc.get_provider_name(provider)
            with open(os.path.join('providers', '%s.rst' % provider_name), 'wb') as fh:
                print_provider(doc, provider, fakers, fh=fh)

        with open('providers.rst', 'wb') as fh:
            fh.write('Providers\n')
            fh.write('=========\n')
            fh.write('.. toctree::\n')
            fh.write('   :maxdepth: 2\n\n')
            [fh.write('   providers/%s\n' % doc.get_provider_name(provider)) for provider, fakers in formatters]

        for lang in AVAILABLE_LOCALES:
            with open(os.path.join('locales', '%s.rst' % lang), 'wb') as fh:
                fh.write('\n')
                title = 'Language {0}\n'.format(lang).encode('utf-8')
                fh.write(title)
                fh.write('=' * len(title))
                fh.write('\n')
                fake = Faker(locale=lang)
                d = documentor.Documentor(fake)

                for p, fs in d.get_formatters(with_args=True, with_defaults=True, locale=lang,
                                              excludes=base_provider_formatters):
                    print_provider(d, p, fs, fh=fh)
        with open('locales.rst', 'wb') as fh:
            fh.write('Locales\n')
            fh.write('=======\n')
            fh.write('.. toctree::\n')
            fh.write('   :maxdepth: 2\n\n')
            [fh.write('   locales/%s\n' % lang) for lang in AVAILABLE_LOCALES]


# wrappers for sphinx
def _main(app, *args, **kwargs):
    return main(*args, **kwargs)

def setup(app):
    app.connect('builder-inited', _main)


if __name__ == "__main__":
    if sys.stdout.encoding is None:
        print("please set python env PYTHONIOENCODING=UTF-8, example: "
              "export PYTHONIOENCODING=UTF-8, when write to stdout", file=sys.stderr)
        exit(1)
    main(*sys.argv[1:])
