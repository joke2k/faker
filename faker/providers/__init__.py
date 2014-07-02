import re
import random
import string


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

    @classmethod
    def random_int(cls, min=0, max=9999):
        """
        Returns a random integer between two values.

        :param min: lower bound value (inclusive; default=0)
        :param max: upper bound value (inclusive; default=9999)
        :returns: random integer between min and max
        """
        return random.randint(min, max)

    @classmethod
    def random_digit(cls):
        """
        Returns a random digit/number
        between 0 and 9.
        """
        return random.randint(0, 9)

    @classmethod
    def random_digit_not_null(cls):
        """
        Returns a random non-zero digit/number
        between 1 and 9.
        """
        return random.randint(1, 9)

    @classmethod
    def random_digit_or_empty(cls):
        """
        Returns a random digit/number
        between 0 and 9 or an empty string.
        """
        if random.randint(0, 1):
            return random.randint(0, 9)
        else:
            return ''

    @classmethod
    def random_digit_not_null_or_empty(cls):
        """
        Returns a random non-zero digit/number
        between 1 and 9 or and empty string.
        """
        if random.randint(0, 1):
            return random.randint(1, 9)
        else:
            return ''

    @classmethod
    def random_number(cls, digits=None):
        """
        Returns a random number with 1 digit (default, when digits==None)
        or a random number with 0 to given number of digits.

        :param digits: maximum number of digits
        :returns: random number with 0 to given number of digits
        """
        if digits is None:
            digits = BaseProvider.random_digit()
        return random.randint(0, pow(10, digits) - 1)

    @classmethod
    def random_letter(cls):
        """Returns a random letter (between a-z and A-Z)."""
        return random.choice(getattr(string, 'letters', string.letters))

    @classmethod
    def random_element(cls, array=('a', 'b', 'b')):
        """
        Returns a random element from non-empty sequence.

        :param array: a non-empty sequence
        :returns: random element from a sequence
        """
        return random.choice(array)

    @classmethod
    def randomize_nb_elements(cls, number=10, le=False, ge=False):
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
        return int(number * random.randint(_min, _max) / 100) + 1

    @classmethod
    def numerify(cls, text='###'):
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
            lambda x: str(BaseProvider.random_digit()),
            text)
        text = _re_perc.sub(
            lambda x: str(BaseProvider.random_digit_not_null()),
            text)
        text = _re_excl.sub(
            lambda x: str(BaseProvider.random_digit_or_empty()),
            text)
        text = _re_at.sub(
            lambda x: str(BaseProvider.random_digit_not_null_or_empty()),
            text)
        return text

    @classmethod
    def lexify(cls, text='????'):
        """
        Replaces all question mark ('?') occurrences with a random letter.

        :param text: string to be parsed
        :returns: string with all letter placeholders filled in
        """
        return _re_qm.sub(lambda x: BaseProvider.random_letter(), text)

    @classmethod
    def bothify(cls, text='## ??'):
        """
        Replaces all placeholders with random numbers and letters.

        :param text: string to be parsed
        :returns: string with all numerical and letter placeholders filled in
        """
        return BaseProvider.lexify(BaseProvider.numerify(text))
