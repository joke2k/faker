from __future__ import unicode_literals
import re
import random


class Generator(object):

    def __init__(self):
        self.providers = []

    def add_provider(self, provider):

        if type(provider) is type:
            provider = provider(self)

        self.providers.insert(0, provider)

        for method_name in dir(provider):
            # skip 'private' method
            if method_name.startswith('_'):
                continue

            faker_function = getattr(provider, method_name)

            if hasattr(faker_function, '__call__') or isinstance(faker_function, (classmethod, staticmethod)):
                # add all faker method to generator
                setattr(self, method_name, faker_function)

    def provider(self, name):
        try:
            return list(filter(lambda p: p.__provider__ == name.lower(), self.get_providers()))[0]
        except IndexError:
            return None

    def get_providers(self):
        """
        returns added providers
        """
        return self.providers

    def seed(self, seed=None):
        """
        calls random.seed
        """
        random.seed(seed)

    def format(self, formatter, *args, **kwargs):
        """
        this is a secure way to make a fake
        from other Provider
        TODO: data export?
        """
        return self.get_formatter(formatter)(*args, **kwargs)

    def get_formatter(self, formatter):
        try:
            return getattr(self, formatter)
        except AttributeError:
            raise AttributeError('Unknown formatter "{0}"'.format(formatter))

    def parse(self, text):
        """
        Replaces tokens ('{{ tokenName }}') with the result from the token method call
        """
        return re.sub(r'\{\{(\s?)(\w+)(\s?)\}\}', self.__format_token, text)
        #return re.sub( r'\{\{\s?(\w+)\s?\}\}', lambda matches: ( self.format( matches.group(1) ) ) , text )

    def __format_token(self, matches):
        formatter = list(matches.groups())
        #args = []
        #if ':' in formatter[1]:
        #    formatter[1], args = formatter[1].split(":")
        #    args = args.split(",")
        formatter[1] = self.format(formatter[1])

        return "".join(formatter)