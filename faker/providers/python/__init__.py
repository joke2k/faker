# coding=utf-8

from __future__ import unicode_literals

from decimal import Decimal
import sys

from faker.providers.lorem.la import Provider as Lorem
from faker.generator import random

from .. import BaseProvider


if sys.version_info[0] == 2:
    string_types = (basestring,)
elif sys.version_info[0] == 3:
    string_types = (str, bytes)
else:
    raise SystemError("Unrecognized python version: {}".format(sys.version_info[0]))


class Provider(BaseProvider):
    @classmethod
    def pybool(cls):
        return cls.random_int(0, 1) == 1

    @classmethod
    def pystr(cls, min_chars=None, max_chars=20):
        """
        Generates a random string of upper and lowercase letters.
        :type min_chars: int
        :type max_chars: int
        :return: String. Random of random length between min and max characters.
        """
        if min_chars is None:
            return "".join(cls.random_letter() for i in range(max_chars))
        else:
            assert (max_chars >= min_chars), "Maximum length must be greater than or equal to minium length"
            return "".join(cls.random_letter() for i in range(0, random.randint(min_chars, max_chars)))

    @classmethod
    def pyfloat(cls, left_digits=None, right_digits=None, positive=False):
        if left_digits is not None and left_digits < 0:
            raise ValueError('A float number cannot have less than 0 digits in its '
                             'integer part')
        if right_digits is not None and right_digits < 0:
            raise ValueError('A float number cannot have less than 0 digits in its '
                             'fractional part')
        if left_digits == 0 and right_digits == 0:
            raise ValueError('A float number cannot have less than 0 digits in total')

        left_digits = left_digits if left_digits is not None else (
            cls.random_int(1, sys.float_info.dig))
        right_digits = right_digits if right_digits is not None else (
            cls.random_int(0, sys.float_info.dig-left_digits))
        sign = 1 if positive else cls.random_element((-1, 1))

        return float("{0}.{1}".format(
            sign * cls.random_number(left_digits),
            cls.random_number(right_digits)
        ))

    @classmethod
    def pyint(cls):
        return cls.random_int()

    @classmethod
    def pydecimal(cls, left_digits=None, right_digits=None, positive=False):
        return Decimal(str(cls.pyfloat(left_digits, right_digits, positive)))

    def pytuple(self, nb_elements=10, variable_nb_elements=True, *value_types):
        return tuple(self.pyset(nb_elements, variable_nb_elements, *value_types))

    def pyset(self, nb_elements=10, variable_nb_elements=True, *value_types):
        return set(self._pyiterable(nb_elements, variable_nb_elements, *value_types))

    def pylist(self, nb_elements=10, variable_nb_elements=True, *value_types):
        return list(self._pyiterable(nb_elements, variable_nb_elements, *value_types))

    def pyiterable(self, nb_elements=10, variable_nb_elements=True, *value_types):
        return self.random_element([self.pylist, self.pytuple, self.pyset])(nb_elements, variable_nb_elements, *value_types)

    def _random_type(self, type_list):
        value_type = self.random_element(type_list)

        method_name = "py{0}".format(value_type)
        if hasattr(self, method_name):
            value_type = method_name

        return self.generator.format(value_type)

    def _pyiterable(self, nb_elements=10, variable_nb_elements=True, *value_types):

        value_types = [t if isinstance(t, string_types) else getattr(t, '__name__', type(t).__name__).lower()
                      for t in value_types
                      # avoid recursion
                      if t not in ['iterable', 'list', 'tuple', 'dict', 'set']]
        if not value_types:
            value_types = ['str', 'str', 'str', 'str', 'float', 'int', 'int', 'decimal', 'date_time', 'uri', 'email']

        if variable_nb_elements:
            nb_elements = self.randomize_nb_elements(nb_elements)

        for f in range(nb_elements):
            yield self._random_type(value_types)

    def pydict(self, nb_elements=10, variable_nb_elements=True, *value_types):
        """
        Returns a dictionary.

        :nb_elements: number of elements for dictionary
        :variable_nb_elements: is use variable number of elements for dictionary
        :value_types: type of dictionary values
        """
        if variable_nb_elements:
            nb_elements = self.randomize_nb_elements(nb_elements)

        return dict(zip(
            Lorem.words(nb_elements),
            self._pyiterable(nb_elements, False, *value_types)
        ))

    def pystruct(self, count=10, *value_types):

        value_types = [t if isinstance(t, string_types) else getattr(t, '__name__', type(t).__name__).lower()
                      for t in value_types
                      # avoid recursion
                      if t != 'struct']
        if not value_types:
            value_types = ['str', 'str', 'str', 'str', 'float', 'int', 'int', 'decimal', 'date_time', 'uri', 'email']

        l = []
        d = {}
        nd = {}
        for i in range(count):
            d[Lorem.word()] = self._random_type(value_types)
            l.append(self._random_type(value_types))
            nd[Lorem.word()] = {
                i: self._random_type(value_types),
                i + 1: [self._random_type(value_types), self._random_type(value_types), self._random_type(value_types)],
                i + 2: {
                    i: self._random_type(value_types),
                    i + 1: self._random_type(value_types),
                    i + 2: [
                        self._random_type(value_types),
                        self._random_type(value_types)
                    ]
                }
            }
        return l, d, nd
