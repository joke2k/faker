# coding=utf-8

from __future__ import unicode_literals
import hashlib
import random
import string

from faker.providers.date_time import Provider as DatetimeProvider

from .. import BaseProvider


class Provider(BaseProvider):
    language_codes = ('cn', 'de', 'el', 'en', 'es', 'fr', 'it', 'pt', 'ru')

    @classmethod
    def boolean(cls, chance_of_getting_true=50):
        return random.randint(1, 100) <= chance_of_getting_true

    @classmethod
    def null_boolean(cls):
        return {
            0: None,
            1: True,
            -1: False
        }[random.randint(-1, 1)]

    @classmethod
    def md5(cls, raw_output=False):
        """
        Calculates the md5 hash of a given string
        :example 'cfcd208495d565ef66e7dff9f98764da'
        """
        res = hashlib.md5(str(random.random()).encode('utf-8'))
        if raw_output:
            return res.digest()
        return res.hexdigest()

    @classmethod
    def sha1(cls, raw_output=False):
        """
        Calculates the sha1 hash of a given string
        :example 'b5d86317c2a144cd04d0d7c03b2b02666fafadf2'
        """
        res = hashlib.sha1(str(random.random()).encode('utf-8'))
        if raw_output:
            return res.digest()
        return res.hexdigest()

    @classmethod
    def sha256(cls, raw_output=False):
        """
        Calculates the sha256 hash of a given string
        :example '85086017559ccc40638fcde2fecaf295e0de7ca51b7517b6aebeaaf75b4d4654'
        """
        res = hashlib.sha256(str(random.random()).encode('utf-8'))
        if raw_output:
            return res.digest()
        return res.hexdigest()

    def locale(self):
        return self.language_code() + '_' + self.country_code()

    @classmethod
    def country_code(cls):
        return cls.random_element(DatetimeProvider.countries)['code']

    @classmethod
    def language_code(cls):
        return cls.random_element(cls.language_codes)

    @classmethod
    def password(cls, length=10, special_chars=True, digits=True, upper_case=True, lower_case=True):
        """
        Generates a random password.
        @param length: Integer. Length of a password
        @param special_chars: Boolean. Whether to use special characters !@#$%^&*()_+
        @param digits: Boolean. Whether to use digits
        @param upper_case: Boolean. Whether to use upper letters
        @param lower_case: Boolean. Whether to use lower letters
        @return: String. Random password
        """
        chars = ""
        if special_chars:
            chars += "!@#$%^&*()_+"
        if digits:
            chars += string.digits
        if upper_case:
            chars += string.ascii_uppercase
        if lower_case:
            chars += string.ascii_lowercase
        return ''.join(random.choice(chars) for x in range(length))
