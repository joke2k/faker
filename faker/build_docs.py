import os
import pprint
import sys

DOCS_ROOT = os.path.abspath(os.path.join('..', 'docs'))


def write(fh, s):
    return fh.write(s.encode())


def write_base_provider(fh, doc, base_provider):
    formatters = doc.get_provider_formatters(base_provider)
    write(fh, ':github_url: hide\n\n')
    write_provider(fh, doc, base_provider, formatters)


def write_provider(fh, doc, provider, formatters, excludes=None):

    if excludes is None:
        excludes = []

    write(fh, '\n')
    title = "``{}``".format(doc.get_provider_name(provider))
    write(fh, '%s\n' % title)
    write(fh, "-" * len(title))
    write(fh, '\n\n::\n')

    for signature, example in formatters.items():
        if signature in excludes:
            continue
        try:
            # `pprint` can't format sets of heterogenous types.
            if not isinstance(example, set):
                example = pprint.pformat(example, indent=4)
            lines = str(example).expandtabs().splitlines()
        except UnicodeEncodeError:
            msg = 'error on "{}" with value "{}"'.format(signature, example)
            raise Exception(msg)
        write(fh, '\n')
        write(fh, "\t{fake}\n{example}\n".format(
            fake=signature,
            example='\n'.join(['\t# ' + line for line in lines]),
        ))


def write_docs(*args, **kwargs):
    from faker import Faker, documentor
    from faker.config import DEFAULT_LOCALE, AVAILABLE_LOCALES
    from faker.providers import BaseProvider

    fake = Faker(locale=DEFAULT_LOCALE)
    doc = documentor.Documentor(fake)

    # Write docs for fakers.providers.BaseProvider
    base_provider = BaseProvider(fake)
    fname = os.path.join(DOCS_ROOT, 'providers', 'BaseProvider.rst')
    with open(fname, 'wb') as fh:
        write_base_provider(fh, doc, base_provider)

    # Write docs for default locale providers
    base_provider_formatters = list(dir(BaseProvider))
    formatters = doc.get_formatters(with_args=True, with_defaults=True,
                                    excludes=base_provider_formatters)
    for provider, fakers in formatters:
        provider_name = doc.get_provider_name(provider)
        fname = os.path.join(DOCS_ROOT, 'providers', '%s.rst' % provider_name)
        with open(fname, 'wb') as fh:
            write(fh, ':github_url: hide\n\n')
            write_provider(fh, doc, provider, fakers)

    # Write providers index page
    with open(os.path.join(DOCS_ROOT, 'providers.rst'), 'wb') as fh:
        write(fh, ':github_url: hide\n\n')
        write(fh, 'Providers\n')
        write(fh, '=========\n')
        write(fh, '.. toctree::\n')
        write(fh, '   :maxdepth: 2\n\n')
        write(fh, '   providers/BaseProvider\n')
        [write(fh, '   providers/%s\n' % doc.get_provider_name(provider))
         for provider, fakers in formatters]

    # Write docs for locale-specific providers
    AVAILABLE_LOCALES = sorted(AVAILABLE_LOCALES)
    for lang in AVAILABLE_LOCALES:
        fname = os.path.join(DOCS_ROOT, 'locales', '%s.rst' % lang)
        with open(fname, 'wb') as fh:
            write(fh, ':github_url: hide\n\n')
            title = 'Language {}\n'.format(lang)
            write(fh, title)
            write(fh, '=' * len(title))
            write(fh, '\n')
            fake = Faker(locale=lang)
            d = documentor.Documentor(fake)

            for p, fs in d.get_formatters(with_args=True, with_defaults=True,
                                          locale=lang,
                                          excludes=base_provider_formatters):
                write_provider(fh, d, p, fs)

    # Write locales index page
    with open(os.path.join(DOCS_ROOT, 'locales.rst'), 'wb') as fh:
        write(fh, ':github_url: hide\n\n')
        write(fh, 'Locales\n')
        write(fh, '=======\n')
        write(fh, '.. toctree::\n')
        write(fh, '   :maxdepth: 2\n\n')
        [write(fh, '   locales/%s\n' % lang) for lang in AVAILABLE_LOCALES]


# wrappers for sphinx
def _main(app, *args, **kwargs):
    return write_docs(*args, **kwargs)


def setup(app):
    app.connect('builder-inited', _main)


if __name__ == "__main__":
    write_docs(*sys.argv[1:])
