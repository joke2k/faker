# coding=utf-8

from __future__ import unicode_literals

import re
import random


_re_token = re.compile(r'\{\{(\s?)(\w+)(\s?)\}\}')
random = random.Random()


class Generator(object):

    __config = {}

    def __init__(self, **config):
        self.providers = []
        self.__config = dict(
            list(self.__config.items()) + list(config.items()))

    def add_provider(self, provider):

        if type(provider) is type:
            provider = provider(self)

        self.providers.insert(0, provider)

        for method_name in dir(provider):
            # skip 'private' method
            if method_name.startswith('_'):
                continue

            faker_function = getattr(provider, method_name)

            if hasattr(faker_function, '__call__') or \
                    isinstance(faker_function, (classmethod, staticmethod)):
                # add all faker method to generator
                self.set_formatter(method_name, faker_function)

    def provider(self, name):
        try:
            lst = [p for p in self.get_providers()
                   if p.__provider__ == name.lower()]
            return lst[0]
        except IndexError:
            return None

    def get_providers(self):
        """Returns added providers."""
        return self.providers

    @property
    def random(self):
        return random

    def seed(self, seed=None):
        """Calls random.seed"""
        random.seed(seed)

    def format(self, formatter, *args, **kwargs):
        """
        This is a secure way to make a fake from another Provider.
        """
        # TODO: data export?
        return self.get_formatter(formatter)(*args, **kwargs)

    def get_formatter(self, formatter):
        try:
            return getattr(self, formatter)
        except AttributeError:
            raise AttributeError('Unknown formatter "{0}"'.format(formatter))

    def set_formatter(self, name, method):
        """
        This method adds a provider method to generator.
        Override this method to add some decoration or logging stuff.
        """
        setattr(self, name, method)

    def parse(self, text):
        """
        Replaces tokens (like '{{ tokenName }}' or '{{tokenName}}')
        with the result from the token method call.
        """
        return _re_token.sub(self.__format_token, text)

    def __format_token(self, matches):
        formatter = list(matches.groups())
        formatter[1] = self.format(formatter[1])
        return ''.join(formatter)
