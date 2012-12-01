# coding=utf-8

from ..Company import  Provider as CompanyProvider

class Provider(CompanyProvider):

    formats = (
        '{{lastName}} {{companySuffix}}',
        '{{lastName}} {{lastName}} {{companySuffix}}',
        '{{lastName}}',
        '{{lastName}}',
    )

    catchPhraseFormats = (
        '{{catchPhraseNoun}} {{catchPhraseVerb}} {{catchPhraseAttribute}}',
    )

    nouns = (
        'la sécurité', 'le plaisir', 'le confort', 'la simplicité', "l'assurance", "l'art", 'le pouvoir', 'le droit',
        'la possibilité', "l'avantage", 'la liberté'
    )

    verbs = (
        'de rouler', "d'avancer", "d'évoluer", 'de changer', "d'innover", 'de louer', "d'atteindre vos buts",
        'de concrétiser vos projets'
    )

    attributes = (
        'de manière efficace', 'plus rapidement', 'plus facilement', 'plus simplement', 'en toute tranquilité',
        'avant-tout', 'autrement', 'naturellement', 'à la pointe', 'sans soucis', "à l'état pur",
        'à sa source', 'de manière sûre', 'en toute sécurité'
    )

    companySuffixes = ('SA', 'S.A.', 'SARL', 'S.A.R.L.', 'S.A.S.', 'et Fils')

    sirenFormat = "### ### ###"

    @classmethod
    def catchPhraseNoun(cls):
        """
        Returns a random catch phrase noun.
        """
        return cls.randomElement(cls.nouns)

    @classmethod
    def catchPhraseAttribute(cls):
        """
        Returns a random catch phrase attribute.
        """
        return cls.randomElement(cls.attributes)

    @classmethod
    def catchPhraseVerb(cls):
        """
        Returns a random catch phrase verb.
        """
        return cls.randomElement(cls.verbs)


    def catchPhrase(self):
        """
        :example 'integrate extensible convergence'
        """
        catchPhrase = u""
        while True:

            format= self.randomElement(self.catchPhraseFormats)
            catchPhrase = self.generator.parse(format)
            catchPhrase = catchPhrase[0].upper() + catchPhrase[1:]

            if self._isCatchPhraseValid(catchPhrase):
                break

        return catchPhrase


    # An array containing string which should not appear twice in a catch phrase
    wordsWhichShouldNotAppearTwice = ('sécurité', 'simpl')

    @classmethod
    def _isCatchPhraseValid(cls, catchPhrase):
        """
        Validates a french catch phrase.

        :param catchPhrase: The catch phrase to validate.
        """
        for word in cls.wordsWhichShouldNotAppearTwice:
            # Fastest way to check if a piece of word does not appear twice.
            beginPos = catchPhrase.find(word)
            endPos = catchPhrase.find(word,beginPos+1)

            if beginPos != -1 and beginPos != endPos: return False

        return True

    @classmethod
    def siren(cls):
        """
        Generates a siren number (9 digits).
        """
        return cls.numerify(cls.sirenFormat)


    @classmethod
    def siret(cls, maxSequentialDigits=2):
        """
        Generates a siret number (14 digits).
        It is in fact the result of the concatenation of a siren number (9 digits),
        a sequential number (4 digits) and a control number (1 digit) concatenation.
        If $maxSequentialDigits is invalid, it is set to 2.
        :param maxSequentialDigits The maximum number of digits for the sequential number (> 0 && <= 4).
        """
        if maxSequentialDigits > 4 or maxSequentialDigits <= 0:
            maxSequentialDigits = 2

        sequentialNumber = str(cls.randomNumber(maxSequentialDigits)).zfill(4)
        return cls.numerify( cls.siren() + ' ' + sequentialNumber + '#' )





