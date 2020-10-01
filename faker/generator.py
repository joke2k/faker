import random as random_module
import re

_re_token = re.compile(r'\{\{\s*(\w+)(:\s*\w+?)?\s*\}\}')
random = random_module.Random()
mod_random = random  # compat with name released in 0.8


class Generator:

    __config = {
        'arguments': {},
    }

    def __init__(self, **config):
        self.providers = []
        self.__config = dict(
            list(self.__config.items()) + list(config.items()))
        self.__random = random

    def add_provider(self, provider):

        if isinstance(provider, type):
            provider = provider(self)

        self.providers.insert(0, provider)

        for method_name in dir(provider):
            # skip 'private' method
            if method_name.startswith('_'):
                continue

            faker_function = getattr(provider, method_name)

            if callable(faker_function):
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
        return self.__random

    @random.setter
    def random(self, value):
        self.__random = value

    def seed_instance(self, seed=None):
        """Calls random.seed"""
        if self.__random == random:
            # create per-instance random obj when first time seed_instance() is
            # called
            self.__random = random_module.Random()
        self.__random.seed(seed)
        return self

    @classmethod
    def seed(cls, seed=None):
        random.seed(seed)

    def format(self, formatter, *args, **kwargs):
        """
        This is a secure way to make a fake from another Provider.
        """
        return self.get_formatter(formatter)(*args, **kwargs)

    def get_formatter(self, formatter):
        try:
            return getattr(self, formatter)
        except AttributeError:
            if 'locale' in self.__config:
                msg = 'Unknown formatter "{}" with locale "{}"'.format(
                    formatter, self.__config['locale'],
                )
            else:
                raise AttributeError('Unknown formatter "{}"'.format(
                    formatter,
                ))
            raise AttributeError(msg)

    def set_formatter(self, name, method):
        """
        This method adds a provider method to generator.
        Override this method to add some decoration or logging stuff.
        """
        setattr(self, name, method)

    def set_arguments(self, group, argument, value=None):
        """
        Creates an argument group, with an individual argument or a dictionary
        of arguments. The argument groups is used to apply arguments to tokens,
        when using the generator.parse() method. To further manage argument
        groups, use get_arguments() and del_arguments() methods.

        generator.set_arguments('small', 'max_value', 10)
        generator.set_arguments('small', {'min_value': 5, 'max_value': 10})
        """
        if group not in self.__config['arguments']:
            self.__config['arguments'][group] = {}

        if isinstance(argument, dict):
            self.__config['arguments'][group] = argument
        elif not isinstance(argument, str):
            raise ValueError("Arguments must be either a string or dictionary")
        else:
            self.__config['arguments'][group][argument] = value

    def get_arguments(self, group, argument=None):
        """
        Get the value of an argument configured within a argument group, or
        the entire group as a dictionary. Used in conjunction with the
        set_arguments() method.

        generator.get_arguments('small', 'max_value')
        generator.get_arguments('small')
        """
        if group in self.__config['arguments'] and argument:
            result = self.__config['arguments'][group].get(argument)
        else:
            result = self.__config['arguments'].get(group)

        return result

    def del_arguments(self, group, argument=None):
        """
        Delete an argument from an argument group or the entire argument group.
        Used in conjunction with the set_arguments() method.

        generator.del_arguments('small')
        generator.del_arguments('small', 'max_value')
        """
        if group in self.__config['arguments']:
            if argument:
                result = self.__config['arguments'][group].pop(argument)
            else:
                result = self.__config['arguments'].pop(group)
        else:
            result = None

        return result

    def parse(self, text):
        """
        Replaces tokens like '{{ tokenName }}' or '{{tokenName}}' in a string with
        the result from the token method call. Arguments can be parsed by using an
        argument group. For more information on the use of argument groups, please
        refer to the set_arguments() method.

        Example:

        generator.set_arguments('red_rgb', {'hue': 'red', 'color_format': 'rgb'})
        generator.set_arguments('small', 'max_value', 10)

        generator.parse('{{ color:red_rgb }} - {{ pyint:small }}')
        """
        return _re_token.sub(self.__format_token, text)

    def __format_token(self, matches):
        formatter, argument_group = list(matches.groups())
        argument_group = argument_group.lstrip(":").strip() if argument_group else ''

        if argument_group:
            try:
                arguments = self.__config['arguments'][argument_group]
            except KeyError:
                raise AttributeError('Unknown argument group "{}"'.format(argument_group))

            formatted = str(self.format(formatter, **arguments))
        else:
            formatted = str(self.format(formatter))

        return ''.join(formatted)
