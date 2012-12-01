import re
import random
import string

class BaseProvider(object):

    def __init__(self, generator ):

        self.generator = generator

    @classmethod
    def randomInt(cls,min=0,max=9999):
        return random.randint(min,max)

    @classmethod
    def randomDigit(cls):
        """ Returns a random number between 0 and 9 """
        return random.randint(0,9)

    @classmethod
    def randomDigitNotNull(cls):
        """ Returns a random number between 1 and 9 """
        return random.randint(1,9)

    @classmethod
    def randomNumber( cls, nbDigits=None ):
        """ Returns a random number with 0 to $nbDigits digits """
        if nbDigits is None:
            nbDigits = BaseProvider.randomDigit()
        return random.randint(0, pow(10, nbDigits)-1 )

    @classmethod
    def randomLetter(cls):
        """ Returns a random letter from a to z """
        return random.choice( string.letters )

    @classmethod
    def randomElement( cls,array=('a','b','b') ):
        """ Returns a random element from a passed array """
        return array[ random.randint(0, len(array)-1) ]

    @classmethod
    def randomizeNbElements(cls, nbElements=10, le=False, gt=False ):
        """
        Returns a random value near to nbElements
        :param le: lower or equals to nbElements
        :param gt: greater or equals to nbElements
        :returns: a random int near to nbElements
        """
        if le and gt: return nbElements
        return int( nbElements * random.randint(100 if gt else 60,100 if le else 140) / 100 ) + 1

    @classmethod
    def numerify( cls,text = '###' ):
        """
        Replaces all hash sign ('#') occurrences with a random number
        Replaces all percentage sign ('%') occurrences with a not null number

        :param string text that needs to bet parsed
        """
        text = re.sub( r'#',lambda x: str(BaseProvider.randomDigit()), text )
        text = re.sub( r'%',lambda x: str(BaseProvider.randomDigitNotNull()), text )

        return text

    @classmethod
    def lexify( cls,text = '????' ):
        """
        Replaces all question mark ('?') occurrences with a random letter
        :param string text that needs to bet parsed
        """
        return re.sub( r'\?', lambda x: BaseProvider.randomLetter(), text )


    @classmethod
    def bothify( cls,text='## ??' ):
        """
        Replaces hash signs and question marks with random numbers and letters
        :param string text that needs to bet parsed
        """

        return BaseProvider.lexify( BaseProvider.numerify( text ) )

