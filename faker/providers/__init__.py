# coding=utf-8

import re
import string

from faker.utils.distribution import choice_distribution


_re_hash = re.compile(r'#')
_re_perc = re.compile(r'%')
_re_excl = re.compile(r'!')
_re_at = re.compile(r'@')
_re_qm = re.compile(r'\?')


class BaseProvider(object):

    __provider__ = 'base'
    __lang__ = None

    def __init__(self, generator):
        self.generator = generator

    def random_int(self, min=0, max=9999):
        """
        Returns a random integer between two values.

        :param min: lower bound value (inclusive; default=0)
        :param max: upper bound value (inclusive; default=9999)
        :returns: random integer between min and max
        """
        return self.generator.random.randint(min, max)

    def random_digit(self):
        """
        Returns a random digit/number
        between 0 and 9.
        """
        return self.generator.random.randint(0, 9)

    def random_digit_not_null(self):
        """
        Returns a random non-zero digit/number
        between 1 and 9.
        """
        return self.generator.random.randint(1, 9)

    def random_digit_or_empty(self):
        """
        Returns a random digit/number
        between 0 and 9 or an empty string.
        """
        if self.generator.random.randint(0, 1):
            return self.generator.random.randint(0, 9)
        else:
            return ''

    def random_digit_not_null_or_empty(self):
        """
        Returns a random non-zero digit/number
        between 1 and 9 or and empty string.
        """
        if self.generator.random.randint(0, 1):
            return self.generator.random.randint(1, 9)
        else:
            return ''

    def random_number(self, digits=None, fix_len=False):
        """
        Returns a random number with 1 digit (default, when digits==None),
        a random number with 0 to given number of digits, or a random number
        with given number to given number of digits (when ``fix_len==True``).

        :param digits: maximum number of digits
        :param fix_len:  should the number have fixed length?
        :returns: random number with 0 to given number of digits or
            fixed length number
        """
        if digits is None:
            digits = self.random_digit()
        if fix_len:
            return self.generator.random.randint(pow(10, digits - 1), pow(10, digits) - 1)
        else:
            return self.generator.random.randint(0, pow(10, digits) - 1)

    def random_letter(self):
        """Returns a random letter (between a-z and A-Z)."""
        return self.generator.random.choice(getattr(string, 'letters', string.ascii_letters))

    def random_element(self, elements=('a', 'b', 'c')):
        """
        Returns a random element from a passed object.

        If `elements` is a dictionary, the value will be used as
        a weighting element. For example::

            random_element({"{{variable_1}}": 0.5, "{{variable_2}}": 0.2, "{{variable_3}}": 0.2, "{{variable_4}}": 0.1})

        will have the following distribution:
            * `variable_1`: 50% probability
            * `variable_2`: 20% probability
            * `variable_3`: 20% probability
            * `variable_4`: 10% probability

        """

        if isinstance(elements, dict):
            choices = elements.keys()
            probabilities = elements.values()
            return choice_distribution(list(choices), list(probabilities), self.generator.random)
        else:
            return self.generator.random.choice(list(elements))

    def random_sample(self, elements=('a', 'b', 'c'), length=None):
        if length is None:
            length = self.generator.random.randint(1, len(elements))

        return [self.random_element(elements) for _ in range(length)]

    def random_sample_unique(self, elements=('a', 'b', 'c'), length=None):
        """
        Returns a `set` of random unique elements for the specified length.
        """
        if length is None:
            length = self.generator.random.randint(1, len(elements))

        if length > len(elements):
            raise ValueError("Sample length cannot be longer than the number of elements to pick from.")
        sample = set()
        while len(sample) < length:
            sample.add(self.random_element(elements))
        return sample

    def randomize_nb_elements(self, number=10, le=False, ge=False):
        """
        Returns a random value near number.

        :param number: value to which the result must be near
        :param le: result must be lower or equal to number
        :param ge: result must be greater or equal to number
        :returns: a random int near number
        """
        if le and ge:
            return number
        _min = 100 if ge else 60
        _max = 100 if le else 140
        return int(number * self.generator.random.randint(_min, _max) / 100) + 1

    def numerify(self, text='###'):
        """
        Replaces all placeholders in given text with randomized values,
        replacing: all hash sign ('#') occurrences with a random digit
        (from 0 to 9); all percentage sign ('%') occurrences with a
        random non-zero digit (from 1 to 9); all exclamation mark ('!')
        occurrences with a random digit (from 0 to 9) or an empty string;
        and all at symbol ('@') occurrences with a random non-zero digit
        (from 1 to 9) or an empty string.

        :param text: string to be parsed
        :returns: string with all numerical placeholders filled in
        """
        text = _re_hash.sub(
            lambda x: str(self.random_digit()),
            text)
        text = _re_perc.sub(
            lambda x: str(self.random_digit_not_null()),
            text)
        text = _re_excl.sub(
            lambda x: str(self.random_digit_or_empty()),
            text)
        text = _re_at.sub(
            lambda x: str(self.random_digit_not_null_or_empty()),
            text)
        return text

    def lexify(self, text='????'):
        """
        Replaces all question mark ('?') occurrences with a random letter.

        :param text: string to be parsed
        :returns: string with all letter placeholders filled in
        """
        return _re_qm.sub(lambda x: self.random_letter(), text)

    def bothify(self, text='## ??'):
        """
        Replaces all placeholders with random numbers and letters.

        :param text: string to be parsed
        :returns: string with all numerical and letter placeholders filled in
        """
        return self.lexify(self.numerify(text))
