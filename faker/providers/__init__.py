# coding=utf-8

from collections import Counter
import re
import string

from faker.utils.distribution import choices_distribution, choices_distribution_unique


_re_hash = re.compile(r'#')
_re_perc = re.compile(r'%')
_re_excl = re.compile(r'!')
_re_at = re.compile(r'@')
_re_qm = re.compile(r'\?')
_re_cir = re.compile(r'\^')


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
            return self.generator.random.randint(
                pow(10, digits - 1), pow(10, digits) - 1)
        else:
            return self.generator.random.randint(0, pow(10, digits) - 1)

    def random_letter(self):
        """Returns a random letter (between a-z and A-Z)."""
        return self.generator.random.choice(
            getattr(string, 'letters', string.ascii_letters))

    def random_letters(self, length=16):
        """Returns a random letter (between a-z and A-Z)."""
        return self.random_choices(
            getattr(string, 'letters', string.ascii_letters),
            length=length,
        )

    def random_lowercase_letter(self):
        """Returns a random lowercase letter (between a-z)."""
        return self.generator.random.choice(string.ascii_lowercase)

    def random_uppercase_letter(self):
        """Returns a random letter (between A-Z)."""
        return self.generator.random.choice(string.ascii_uppercase)

    def random_elements(self, elements=('a', 'b', 'c'), length=None, unique=False):
        fn = choices_distribution_unique if unique else choices_distribution

        if length is None:
            length = self.generator.random.randint(1, len(elements))

        if unique and length > len(elements):
            raise ValueError(
                "Sample length cannot be longer than the number of unique elements to pick from.")

        if isinstance(elements, dict):
            choices = elements.keys()
            probabilities = elements.values()
        else:
            if unique:
                # shortcut
                return self.generator.random.sample(elements, length)
            choices = elements
            probabilities = [1.0 for _ in range(len(choices))]

        return fn(
            list(choices),
            list(probabilities),
            self.generator.random,
            length=length,
        )

    def random_choices(self, elements=('a', 'b', 'c'), length=None):
        """
        Returns a list of random, non-unique elements from a passed object.

        If `elements` is a dictionary, the value will be used as
        a weighting element. For example::

            random_element({"{{variable_1}}": 0.5, "{{variable_2}}": 0.2, "{{variable_3}}": 0.2, "{{variable_4}}": 0.1})

        will have the following distribution:
            * `variable_1`: 50% probability
            * `variable_2`: 20% probability
            * `variable_3`: 20% probability
            * `variable_4`: 10% probability

        """
        return self.random_elements(elements, length, unique=False)

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
        return self.random_elements(elements, length=1)[0]

    def random_sample(self, elements=('a', 'b', 'c'), length=None):
        """
        Returns a list of random unique elements for the specified length.
        Multiple occurrences of the same value increase its probability to be in the output.
        """
        return self.random_elements(elements, length, unique=True)

    def randomize_nb_elements(
            self,
            number=10,
            le=False,
            ge=False,
            min=None,
            max=None):
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
        nb = int(number * self.generator.random.randint(_min, _max) / 100)
        if min is not None and nb < min:
            nb = min
        if max is not None and nb > min:
            nb = max
        return nb

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

    def lexify(self, text='????', letters=string.ascii_letters):
        """
        Replaces all question mark ('?') occurrences with a random letter.

        :param text: string to be parsed
        :param letters: a set of letters to choose from.
        :returns: string with all letter placeholders filled in
        """
        return _re_qm.sub(lambda x: self.random_element(letters), text)

    def bothify(self, text='## ??', letters=string.ascii_letters):
        """
        Replaces all placeholders with random numbers and letters.

        :param text: string to be parsed
        :returns: string with all numerical and letter placeholders filled in
        """
        return self.lexify(self.numerify(text), letters=letters)

    def hexify(self, text='^^^^', upper=False):
        """
        Replaces all circumflex ('^') occurrences with a random
        hexadecimal character.

        :param text: string to be parsed
        :param upper: Format as uppercase hexadecimal
        :returns: string with all letter placeholders filled in
        """
        letters = string.hexdigits[:-6]
        if upper:
            letters = letters.upper()
        return _re_cir.sub(lambda x: self.random_element(letters), text)
