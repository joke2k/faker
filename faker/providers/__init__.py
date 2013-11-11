import re
import random
import string


class BaseProvider(object):

    __provider__ = 'base'
    __lang__ = None

    def __init__(self, generator):

        self.generator = generator

    @classmethod
    def random_int(cls, min=0, max=9999):
        return random.randint(min, max)

    @classmethod
    def random_digit(cls):
        """ Returns a random number between 0 and 9 """
        return random.randint(0, 9)

    @classmethod
    def random_digit_not_null(cls):
        """ Returns a random number between 1 and 9 """
        return random.randint(1, 9)

    @classmethod
    def random_number(cls, digits=None):
        """ Returns a random number with 0 to $digits digits """
        if digits is None:
            digits = BaseProvider.random_digit()
        return random.randint(0, pow(10, digits) - 1)

    @classmethod
    def random_letter(cls):
        """ Returns a random letter from a to z """
        return random.choice(string.letters if hasattr(string, 'letters') else string.ascii_lowercase)

    @classmethod
    def random_element(cls, array=('a', 'b', 'b')):
        """ Returns a random element from a passed array """
        array = list(array)
        return array[random.randint(0, len(array) - 1)]

    @classmethod
    def randomize_nb_elements(cls, number=10, le=False, ge=False):
        """
        Returns a random value near to number
        :param le: lower or equals to number
        :param ge: greater or equals to number
        :returns: a random int near to number
        """
        if le and ge: return number
        return int(number * random.randint(100 if ge else 60, 100 if le else 140) / 100) + 1

    @classmethod
    def numerify(cls, text='###'):
        """
        Replaces all hash sign ('#') occurrences with a random number
        Replaces all percentage sign ('%') occurrences with a not null number

        :param text that needs to bet parsed
        """
        text = re.sub(r'#', lambda x: str(BaseProvider.random_digit()), text)
        text = re.sub(r'%', lambda x: str(BaseProvider.random_digit_not_null()), text)

        return text

    @classmethod
    def lexify(cls, text='????'):
        """
        Replaces all question mark ('?') occurrences with a random letter
        :param text that needs to bet parsed
        """
        return re.sub(r'\?', lambda x: BaseProvider.random_letter(), text)

    @classmethod
    def bothify(cls, text='## ??'):
        """
        Replaces hash signs and question marks with random numbers and letters
        :param text that needs to bet parsed
        """

        return BaseProvider.lexify(BaseProvider.numerify(text))

