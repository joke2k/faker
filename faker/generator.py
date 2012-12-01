import re
import random


class Generator(object):

    def __init__(self):
        self.providers = []


    def addProvider(self, provider):

        self.providers.insert(0, provider)

        for method_name in dir(provider):
            # skip 'private' method
            if method_name.startswith('_'): continue

            faker_function = getattr(provider,method_name)

            if hasattr(faker_function, '__call__') or isinstance(faker_function,(classmethod,staticmethod)) :
                # add all faker method to generator
                setattr(self, method_name, faker_function )

    def getProviders(self):

        return self.providers

    def seed(self, seed=None ):

        random.seed(seed)

    def format(self, formatter, *args, **kwargs):
        """
        this is a secure way to make a fake
        from other Provider
        TODO: data export?
        """
        return self.getFormatter( formatter )( *args, **kwargs )

    def getFormatter(self, formatter):
        try :
            return getattr(self, formatter)
        except AttributeError:
            raise AttributeError('Unknown formatter "%s"' % formatter)

    def parse(self, text):
        """
        Replaces tokens ('{{ tokenName }}') with the result from the token method call
        """
        return re.sub( r'\{\{\s?(\w+)\s?\}\}', lambda matches: ( self.format( matches.group(1) ) ) , text )


#    def help(self, provider_or_field=None, *args):
#        """
#        Useful for shell
#        """
#        already_faked = []
#        def get_example(provider, fake):
#            """
#            TODO: read example in __doc__ string of getattr(provider,faker)
#            """
#            fake_method = getattr(self, fake)
#            #            if fake_method.__doc__:
#            #                return fake_method.__doc__
#            try:
#                already_faked.append(fake)
#                return fake_method()
#            except TypeError:
#                return 'TypeError'
#            except ValueError:
#                return 'ValueError'
#
#        def get_help(provider):
#
#            return "\n".join([
#            u"fake.{fake:<30}# {example}".format(fake=fake, example=get_example(provider,fake))
#            for fake in get_provider_methods(provider)
#            ])
#
#        def get_provider_name(provider_class):
#            name = provider_class.__module__.split('.')[-1]
#            if name == 'providers':
#                return 'BaseProvider'
#            return name
#
#        def get_provider_methods(provider_class):
#            return [fake for fake in dir(provider_class)
#                    if not fake.startswith('_') and fake not in already_faked and is_faker_method(getattr(provider_class,fake))
#                    #                        and ( hasattr(fake, '__call__') or isinstance(fake,(classmethod,staticmethod)) )
#                    #                if not fake.startswith('_') and fake not in already_faked
#                    #                and isinstance(getattr(provider_class,fake), (types.MethodType,types.FunctionType))
#            ]
#
#        providers = self.providers
#        with_base_provider = True
#        if provider_or_field:
#            try:
#                print getattr(self,provider_or_field)(*args)
#                return
#            except AttributeError:
#                providers = [p for p in providers if get_provider_name(p) == provider_or_field]
#                if not providers:
#                    return 'No faker found for "%s"' % provider_or_field
#                with_base_provider = False
#
#        from faker.providers import BaseProvider
#        if with_base_provider:
#            providers.append(BaseProvider)
#        else:
#            already_faked = [fake for fake in get_provider_methods(BaseProvider)]
#
#        print u"\n{:*^60}".format(' START HELP ')
#        print u"\n".join([u"\n# {faker}:\n{examples}".format(faker=get_provider_name(p),examples=get_help(p))  for p in providers[::-1]])
#        print u"\n{:*^60}".format(' END HELP ')