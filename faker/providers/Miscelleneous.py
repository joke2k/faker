from . import BaseProvider
from . import DateTime
import random
import hashlib


class Provider(BaseProvider):

    languageCodes = ('cn','de','en','es','fr','it','pt','ru')

    @classmethod
    def boolean(cls, chanceOfGettingTrue=50):
        return random.randint(1,100) <= chanceOfGettingTrue

    @classmethod
    def nullBoolean(cls):
        return {
            0: None,
            1: True,
            -1: False
        }[random.randint(-1,1)]

    @classmethod
    def md5(cls, raw_output=False):
        """
        Calculates the md5 hash of a given string
        :example 'cfcd208495d565ef66e7dff9f98764da'
        """
        res = hashlib.md5(str(random.random()))
        if raw_output:
            return res.digest()
        return res.hexdigest()

    @classmethod
    def sha1(cls, raw_output=False):
        """
        Calculates the sha1 hash of a given string
        :example 'b5d86317c2a144cd04d0d7c03b2b02666fafadf2'
        """
        res = hashlib.sha1(str(random.random()))
        if raw_output:
            return res.digest()
        return res.hexdigest()

    @classmethod
    def sha256(cls, raw_output=False):
        """
        Calculates the sha256 hash of a given string
        :example '85086017559ccc40638fcde2fecaf295e0de7ca51b7517b6aebeaaf75b4d4654'
        """
        res = hashlib.sha256(str(random.random()))
        if raw_output:
            return res.digest()
        return res.hexdigest()

    def locale(self):
        return self.languageCode() + '_' + self.countryCode()


    @classmethod
    def countryCode(cls):
        return cls.randomElement( DateTime.Provider.countries )['code']

    @classmethod
    def languageCode(cls):
        return cls.randomElement( cls.languageCodes )

