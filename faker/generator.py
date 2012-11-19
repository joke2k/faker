import re
import random
import types

class Generator(object):

    def __init__(self):
        self.providers = []
        self.formatters = {}


    def addProvider(self, provider):

        self.providers.insert(0, provider)

    def getProviders(self):

        return self.providers

    def seed(self, seed=None ):

        random.seed(seed)

    def format(self, formatter):
        return self.getFormatter(formatter)

    def getFormatter(self, formatter):
        if formatter in self.formatters:
            return self.formatters[formatter]
        for provider in self.providers:
            if hasattr(provider, formatter):
                self.formatters[formatter] = getattr(provider, formatter)
                return self.formatters[formatter]

        raise ValueError('Unknown formatter "%s"' % formatter)

    def parse(self, text):
        """
        Replaces tokens ('{{ tokenName }}') with the result from the token method call
        """
        return re.sub( r'\{\{\s?(\w+)\s?\}\}', self.callFormatWithMatches , text )

    def callFormatWithMatches(self, matches):
        return self.format( matches.group(1) )()

    def __getattr__(self, item):
        return self.format( item )

    def help(self, provider_or_field=None, *args):
        """
        Useful for shell
        """
        already_faked = []
        def get_example(provider, fake):
            """
            TODO: read example in __doc__ string of getattr(provider,faker)
            """
            fake_method = self.__getattr__(fake)
#            if fake_method.__doc__:
#                return fake_method.__doc__
            try:
                already_faked.append(fake)
                return fake_method()
            except TypeError:
                return 'TypeError'
            except ValueError:
                return 'ValueError'

        def get_help(provider):

            return "\n".join([
                u"faker.{fake:<30}# {example}".format(fake=fake, example=get_example(provider,fake))
                for fake in get_provider_methods(provider)
            ])

        def get_provider_name(provider_class):
            name = provider_class.__module__.split('.')[-1]
            if name == 'providers':
                return 'BaseProvider'
            return name

        def get_provider_methods(provider_class):
            return [fake for fake in dir(provider_class)
                if not fake.startswith('_') and fake not in already_faked
                and isinstance(getattr(provider_class,fake), (types.MethodType,types.FunctionType))
            ]

        providers = self.providers
        with_base_provider = True
        if provider_or_field:
            try:
                print self.__getattr__(provider_or_field)(*args)
                return
            except ValueError:
                providers = [p for p in providers if get_provider_name(p) == provider_or_field]
                if not providers:
                    return 'No faker found for "%s"' % provider_or_field
                with_base_provider = False

        from faker.providers import BaseProvider
        if with_base_provider:
            providers.insert(0,BaseProvider)
        else:
            already_faked = [fake for fake in get_provider_methods(BaseProvider)]

        print u"\n{:*^60}".format(' START HELP ')
        print u"\n".join([u"\n# {faker}:\n{examples}".format(faker=get_provider_name(p),examples=get_help(p))  for p in providers])
        print u"\n{:*^60}".format(' END HELP ')