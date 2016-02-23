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
    language_codes = ('zh', 'de', 'el', 'en', 'es', 'fr', 'it', 'pt', 'ru')

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

    def locale(self):
        return self.language_code() + '_' + self.country_code()

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
