import string
import sys
import warnings

from decimal import Decimal

from .. import BaseProvider


class Provider(BaseProvider):
    default_value_types = (
        'str', 'str', 'str', 'str', 'float', 'int', 'int', 'decimal',
        'date_time', 'uri', 'email',
    )

    def _check_signature(self, value_types, allowed_types):
        if value_types is not None and not isinstance(value_types, (list, tuple)):
            value_types = [value_types]
            warnings.warn(
                'Passing value types as positional arguments is going to be '
                'deprecated.  Pass them as a list or tuple instead.',
                PendingDeprecationWarning,
            )
        if value_types is None:
            value_types = ()
        return tuple(value_types) + allowed_types

    def pybool(self):
        return self.random_int(0, 1) == 1

    def pystr(self, min_chars=None, max_chars=20):
        """
        Generates a random string of upper and lowercase letters.
        :type min_chars: int
        :type max_chars: int
        :return: String. Random of random length between min and max characters.
        """
        if min_chars is None:
            return "".join(self.random_letters(length=max_chars))
        else:
            assert (
                max_chars >= min_chars), "Maximum length must be greater than or equal to minium length"
            return "".join(
                self.random_letters(
                    length=self.generator.random.randint(min_chars, max_chars),
                ),
            )

    def pystr_format(self, string_format='?#-###{{random_int}}{{random_letter}}', letters=string.ascii_letters):
        return self.bothify(self.generator.parse(string_format), letters=letters)

    def pyfloat(self, left_digits=None, right_digits=None, positive=False,
                min_value=None, max_value=None):
        if left_digits is not None and left_digits < 0:
            raise ValueError(
                'A float number cannot have less than 0 digits in its '
                'integer part')
        if right_digits is not None and right_digits < 0:
            raise ValueError(
                'A float number cannot have less than 0 digits in its '
                'fractional part')
        if left_digits == 0 and right_digits == 0:
            raise ValueError(
                'A float number cannot have less than 0 digits in total')
        if None not in (min_value, max_value) and min_value > max_value:
            raise ValueError('Min value cannot be greater than max value')
        if None not in (min_value, max_value) and min_value == max_value:
            raise ValueError('Min and max value cannot be the same')
        if positive and min_value is not None and min_value < 0:
            raise ValueError(
                'Cannot combine positive=True and negative min_value')

        left_digits = left_digits if left_digits is not None else (
            self.random_int(1, sys.float_info.dig))
        right_digits = right_digits if right_digits is not None else (
            self.random_int(0, sys.float_info.dig - left_digits))
        sign = ''
        if (min_value is not None) or (max_value is not None):
            if max_value is not None and max_value < 0:
                max_value += 1  # as the random_int will be generated up to max_value - 1
            if min_value is not None and min_value < 0:
                min_value += 1  # as we then append digits after the left_number
            left_number = self._safe_random_int(
                min_value, max_value, positive,
            )
        else:
            sign = '+' if positive else self.random_element(('+', '-'))
            left_number = self.random_number(left_digits)

        return float("{}{}.{}".format(
            sign,
            left_number,
            self.random_number(right_digits),
        ))

    def _safe_random_int(self, min_value, max_value, positive):
        orig_min_value = min_value
        orig_max_value = max_value

        if min_value is None:
            min_value = max_value - self.random_int()
        if max_value is None:
            max_value = min_value + self.random_int()
        if positive:
            min_value = max(min_value, 0)

        if min_value == max_value:
            return self._safe_random_int(orig_min_value, orig_max_value, positive)
        else:
            return self.random_int(min_value, max_value - 1)

    def pyint(self, min_value=0, max_value=9999, step=1):
        return self.generator.random_int(min_value, max_value, step=step)

    def pydecimal(self, left_digits=None, right_digits=None, positive=False,
                  min_value=None, max_value=None):

        float_ = self.pyfloat(
            left_digits, right_digits, positive, min_value, max_value)
        return Decimal(str(float_))

    def pytuple(self, nb_elements=10, variable_nb_elements=True, value_types=None, *allowed_types):
        return tuple(
            self.pyset(
                nb_elements,
                variable_nb_elements,
                value_types,
                *allowed_types))

    def pyset(self, nb_elements=10, variable_nb_elements=True, value_types=None, *allowed_types):
        return set(
            self._pyiterable(
                nb_elements,
                variable_nb_elements,
                value_types,
                *allowed_types))

    def pylist(self, nb_elements=10, variable_nb_elements=True, value_types=None, *allowed_types):
        return list(
            self._pyiterable(
                nb_elements,
                variable_nb_elements,
                value_types,
                *allowed_types))

    def pyiterable(
            self,
            nb_elements=10,
            variable_nb_elements=True,
            value_types=None,
            *allowed_types):
        value_types = self._check_signature(value_types, allowed_types)
        return self.random_element([self.pylist, self.pytuple, self.pyset])(
            nb_elements, variable_nb_elements, value_types, *allowed_types)

    def _random_type(self, type_list):
        value_type = self.random_element(type_list)

        method_name = "py{}".format(value_type)
        if hasattr(self, method_name):
            value_type = method_name

        return self.generator.format(value_type)

    def _pyiterable(
            self,
            nb_elements=10,
            variable_nb_elements=True,
            value_types=None,
            *allowed_types):

        value_types = self._check_signature(value_types, allowed_types)

        value_types = [t if isinstance(t, str) else getattr(t, '__name__', type(t).__name__).lower()
                       for t in value_types
                       # avoid recursion
                       if t not in ['iterable', 'list', 'tuple', 'dict', 'set']]
        if not value_types:
            value_types = self.default_value_types

        if variable_nb_elements:
            nb_elements = self.randomize_nb_elements(nb_elements, min=1)

        for _ in range(nb_elements):
            yield self._random_type(value_types)

    def pydict(self, nb_elements=10, variable_nb_elements=True, value_types=None, *allowed_types):
        """
        Returns a dictionary.

        :nb_elements: number of elements for dictionary
        :variable_nb_elements: is use variable number of elements for dictionary
        :value_types: type of dictionary values
        """
        if variable_nb_elements:
            nb_elements = self.randomize_nb_elements(nb_elements, min=1)

        return dict(zip(
            self.generator.words(nb_elements, unique=True),
            self._pyiterable(nb_elements, False, value_types, *allowed_types),
        ))

    def pystruct(self, count=10, value_types=None, *allowed_types):
        value_types = self._check_signature(value_types, allowed_types)

        value_types = [t if isinstance(t, str) else getattr(t, '__name__', type(t).__name__).lower()
                       for t in value_types
                       # avoid recursion
                       if t != 'struct']
        if not value_types:
            value_types = self.default_value_types

        types = []
        d = {}
        nd = {}
        for i in range(count):
            d[self.generator.word()] = self._random_type(value_types)
            types.append(self._random_type(value_types))
            nd[self.generator.word()] = {i: self._random_type(value_types),
                                         i + 1: [self._random_type(value_types),
                                                 self._random_type(value_types),
                                                 self._random_type(value_types)],
                                         i + 2: {i: self._random_type(value_types),
                                                 i + 1: self._random_type(value_types),
                                                 i + 2: [self._random_type(value_types),
                                                         self._random_type(value_types)]}}
        return types, d, nd
