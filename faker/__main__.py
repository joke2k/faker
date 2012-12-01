import sys


def main(provider_or_field=None, *args):
    from faker import Faker, documentor
    fake = Faker()

    doc = documentor.Documentor(fake)

    if provider_or_field:
        try:

            print fake.format(provider_or_field, *args)
            return
        except AttributeError:
            providers = [p for p in fake.providers if documentor.Documentor.getProviderName(p) == provider_or_field]
            if not providers:
                return 'No faker found for "%s"' % provider_or_field
            from faker.providers import BaseProvider
            doc.already_generated = [fake for fake in dir(BaseProvider)]
            formatters = [(providers[0],doc.getProviderFormatters(providers[0]))]
    else:
        formatters = doc.getFormatters(with_args='first', with_defaults=True)


    for provider, fakers in formatters:

        print
        print "### %s" % documentor.Documentor.getProviderName(provider)
        print

        for signature, example in fakers.items():

            print u"{fake:<{margin}}# {example}".format(fake=signature, example=example, margin=max(30,doc.max_name_len+1))


if __name__ == "__main__":
    main(*sys.argv[1:])