# coding=utf-8

from __future__ import unicode_literals
import hashlib
import string
import uuid
import os

from faker.generator import random
from faker.providers.date_time import Provider as DatetimeProvider

from .. import BaseProvider


class Provider(BaseProvider):
    # Language codes from ISO 639-1
    language_codes = (
        'aa', 'ab', 'ae', 'af', 'ak', 'am', 'an', 'ar', 'as', 'av', 'ay', 'az',
        'ba', 'be', 'bg', 'bh', 'bi', 'bm', 'bn', 'bo', 'br', 'bs', 'ca', 'ce',
        'ch', 'co', 'cr', 'cs', 'cu', 'cv', 'cy', 'da', 'de', 'dv', 'dz', 'ee',
        'el', 'en', 'eo', 'es', 'et', 'eu', 'fa', 'ff', 'fi', 'fj', 'fo', 'fr',
        'fy', 'ga', 'gd', 'gl', 'gn', 'gu', 'gv', 'ha', 'he', 'hi', 'ho', 'hr',
        'ht', 'hu', 'hy', 'hz', 'ia', 'id', 'ie', 'ig', 'ii', 'ik', 'io', 'is',
        'it', 'iu', 'ja', 'jv', 'ka', 'kg', 'ki', 'kj', 'kk', 'kl', 'km', 'kn',
        'ko', 'kr', 'ks', 'ku', 'kv', 'kw', 'ky', 'la', 'lb', 'lg', 'li', 'ln',
        'lo', 'lt', 'lu', 'lv', 'mg', 'mh', 'mi', 'mk', 'ml', 'mn', 'mr', 'ms',
        'mt', 'my', 'na', 'nb', 'nd', 'ne', 'ng', 'nl', 'nn', 'no', 'nr', 'nv',
        'ny', 'oc', 'oj', 'om', 'or', 'os', 'pa', 'pi', 'pl', 'ps', 'pt', 'qu',
        'rm', 'rn', 'ro', 'ru', 'rw', 'sa', 'sc', 'sd', 'se', 'sg', 'si', 'sk',
        'sl', 'sm', 'sn', 'so', 'sq', 'sr', 'ss', 'st', 'su', 'sv', 'sw', 'ta',
        'te', 'tg', 'th', 'ti', 'tk', 'tl', 'tn', 'to', 'tr', 'ts', 'tt', 'tw',
        'ty', 'ug', 'uk', 'ur', 'uz', 've', 'vi', 'vo', 'wa', 'wo', 'xh', 'yi',
        'yo', 'za', 'zh', 'zu'
    )

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
    def binary(cls, length=(1 * 1024 * 1024)):
        """ Returns random binary blob.

        Default blob size is 1 Mb.
        """
        return os.urandom(length)

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

    @classmethod
    def locale(cls):
        return cls.language_code() + '_' + cls.country_code()

    @classmethod
    def country_code(cls):
        return cls.random_element(DatetimeProvider.countries)['code']

    @classmethod
    def language_code(cls):
        return cls.random_element(cls.language_codes)

    @classmethod
    def uuid4(cls):
        """
        Generates a random UUID4 string.
        """
        return str(uuid.uuid4())

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
        choices = ""
        required_tokens = []
        if special_chars:
            required_tokens.append(random.choice("!@#$%^&*()_+"))
            choices += "!@#$%^&*()_+"
        if digits:
            required_tokens.append(random.choice(string.digits))
            choices += string.digits
        if upper_case:
            required_tokens.append(random.choice(string.ascii_uppercase))
            choices += string.ascii_uppercase
        if lower_case:
            required_tokens.append(random.choice(string.ascii_lowercase))
            choices += string.ascii_lowercase

        assert len(required_tokens) <= length, "Required length is shorter than required characters"

        # Generate a first version of the password
        chars = [random.choice(choices) for x in range(length)]

        # Pick some unique locations
        random_indexes = set()
        while len(random_indexes) < len(required_tokens):
            random_indexes.add(random.randint(0, len(chars) - 1))

        # Replace them with the required characters
        for i, index in enumerate(random_indexes):
            chars[index] = required_tokens[i]

        return ''.join(chars)