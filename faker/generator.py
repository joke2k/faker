import re
import random


class Generator(object):

    def __init__(self):
        self.providers = []

    def add_provider(self, provider):

        self.providers.insert(0, provider)

        for method_name in dir(provider):
            # skip 'private' method
            if method_name.startswith('_'):
                continue

            faker_function = getattr(provider, method_name)

            if hasattr(faker_function, '__call__') or isinstance(faker_function, (classmethod, staticmethod)):
                # add all faker method to generator
                setattr(self, method_name, faker_function)

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
        try :
            return getattr(self, formatter)
        except AttributeError:
            raise AttributeError('Unknown formatter "{0}"'.format(formatter))

    def parse(self, text):
        """
        Replaces tokens ('{{ tokenName }}') with the result from the token method call
        """
        return re.sub( r'\{\{\s?(\w+)\s?\}\}', lambda matches: ( self.format( matches.group(1) ) ) , text )