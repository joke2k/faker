import inspect
from faker.providers import BaseProvider


class Documentor(object):

    def __init__(self, generator):
        """
        :param generator: a Generator localized and with providers already filled,
                          that we want write documentation
        :type generator: faker.Generator()
        """
        self.generator = generator
        self.max_name_len = 0
        self.already_generated = []

    def get_formatters(self, **kwargs):

        self.max_name_len = 0
        self.already_generated = []
        formatters = []
        providers = self.generator.get_providers()
        providers.append(BaseProvider)
        for provider in providers[::-1]:  # reverse
            formatters.append(
                (provider, self.get_provider_formatters(provider, **kwargs))
            )
        return formatters

    def get_provider_formatters(self, provider, prefix='fake.', with_args=True, with_defaults=True):

        formatters = {}

        for name, method in inspect.getmembers(provider, inspect.ismethod):

            # skip 'private' method and inherited methods
            if name.startswith('_') or name in self.already_generated: continue

            arguments = []

            if with_args:
                # retrieve all parameter
                argspec = inspect.getargspec(method)

                for i, arg in enumerate([x for x in argspec.args if x not in ['self', 'cls']]):

                    if argspec.defaults and with_defaults:

                        try:
                            default = argspec.defaults[-1 * (i+1)]
                            if isinstance(default, basestring):
                                default = ('"{}"' if '"' not in default else '"{}"').format(default)
                            else:
                                # TODO check default type
                                default = "{}".format(default)

                            arg = "{}={}".format(arg, default)

                        except IndexError:
                            pass

                    arguments.append(arg)
                    if with_args == 'first':
                        break

                if with_args != 'first':
                    if argspec.varargs:
                        arguments.append(u'*' + argspec.varargs)
                    if argspec.keywords:
                        arguments.append(u'**' + argspec.keywords)

            # build fake method signature
            signature = u"{}{}({})".format(prefix, name, u", ".join(arguments))

            # make a fake example
            example = self.generator.format(name)

            formatters[signature] = example

            self.max_name_len = max(self.max_name_len, len(signature))
            self.already_generated.append(name)

        return formatters

    @staticmethod
    def get_provider_name(provider_class):
        name = provider_class.__module__.split('.')[-1]
        if name == 'providers':
            return 'BaseProvider'
        return name

