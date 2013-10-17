from __future__ import unicode_literals
import sys


def print_provider(doc, provider, formatters, excludes=None):
    if excludes is None:
        excludes = []

    print
    print "### faker.providers.%s" % doc.get_provider_name(provider)
    print

    for signature, example in formatters.items():
        if signature in excludes:
            continue
        print "{fake:<{margin}}# {example}".format(
            fake=signature,
            example=example,
            margin=max(30, doc.max_name_len+1)
        )


def main(provider_or_field=None, *args):
    from faker import Faker, documentor, DEFAULT_LOCALE, AVAILABLE_LOCALES
    fake = Faker(locale=DEFAULT_LOCALE)

    doc = documentor.Documentor(fake)

    if provider_or_field:
        try:

            print fake.format(provider_or_field, *args)
            return
        except AttributeError:
            providers = [p for p in fake.providers if doc.get_provider_name(p) == provider_or_field]
            if not providers:
                return 'No faker found for "%s"' % provider_or_field
            from faker.providers import BaseProvider
            doc.already_generated = [f for f in dir(BaseProvider)]
            print_provider(doc, providers[0], doc.get_provider_formatters(providers[0]))
    else:
        formatters = doc.get_formatters(with_args='first', with_defaults=True)

        for provider, fakers in formatters:

            print_provider(doc, provider, fakers)

        for lang in AVAILABLE_LOCALES:
            if lang == DEFAULT_LOCALE:
                continue
            print
            print '############### LANGUAGE {0}'.format(lang)
            fake = Faker(locale=lang)
            d = documentor.Documentor(fake)

            for p, fs in d.get_formatters(with_args='first', with_defaults=True, locale=lang):
                print_provider(d, p, fs)


if __name__ == "__main__":
    if sys.stdout.encoding is None:
        print >> sys.stderr, \
            "please set python env PYTHONIOENCODING=UTF-8, example: export PYTHONIOENCODING=UTF-8, when write to stdout"
        exit(1)
    main(*sys.argv[1:])