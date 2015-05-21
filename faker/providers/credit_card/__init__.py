# coding=utf-8

from __future__ import unicode_literals

import re

from faker.providers.date_time import Provider as DateTimeProvider
from .. import BaseProvider


class CreditCard(object):
    valid_characters_pattern = re.compile('^[0-9 ]*$')

    def __init__(self, name, prefixes, length=16, security_code='CVC', security_code_length=3):
        self.name = name
        self.prefixes = prefixes
        self.length = length
        self.security_code = security_code
        self.security_code_length = security_code_length


class Provider(BaseProvider):

    visa_prefix_list = [['4', '5', '3', '9'],
                        ['4', '5', '5', '6'],
                        ['4', '9', '1', '6'],
                        ['4', '5', '3', '2'],
                        ['4', '9', '2', '9'],
                        ['4', '0', '2', '4', '0', '0', '7', '1'],
                        ['4', '4', '8', '6'],
                        ['4', '7', '1', '6'],
                        ['4']]

    mastercard_prefix_list = [['5', '1'],
                              ['5', '2'],
                              ['5', '3'],
                              ['5', '4'],
                              ['5', '5']]

    amex_prefix_list = [['3', '4'],
                        ['3', '7']]

    discover_prefix_list = [['6', '0', '1', '1']]

    diners_prefix_list = [['3', '0', '0'],
                          ['3', '0', '1'],
                          ['3', '0', '2'],
                          ['3', '0', '3'],
                          ['3', '6'],
                          ['3', '8']]

    enroute_prefix_list = [['2', '0', '1', '4'],
                           ['2', '1', '4', '9']]

    jcb16_prefix_list = [['3', '0', '8', '8'],
                         ['3', '0', '9', '6'],
                         ['3', '1', '1', '2'],
                         ['3', '1', '5', '8'],
                         ['3', '3', '3', '7'],
                         ['3', '5', '2', '8']]

    jcb15_prefix_list = [['2', '1', '0', '0'],
                         ['1', '8', '0', '0']]

    voyager_prefix_list = [['8', '6', '9', '9']]

    credit_card_types = {
        'mastercard':   CreditCard('Mastercard',        mastercard_prefix_list, 16, 'CVV', 4),
        'visa16':       CreditCard('VISA 16 digit',     visa_prefix_list),
        'visa13':       CreditCard('VISA 13 digit',     visa_prefix_list, 13),
        'amex':         CreditCard('American Express',  amex_prefix_list, 15),
        'discover':     CreditCard('Discover',          discover_prefix_list),
        'diners':       CreditCard('Diners Club / Carte Blanche', diners_prefix_list, 14),
        'enroute':      CreditCard('enRoute',           enroute_prefix_list, 15),
        'jcb15':        CreditCard('JCB 15 digit',      jcb16_prefix_list, 15),
        'jcb16':        CreditCard('JCB 16 digit',      jcb15_prefix_list),
        'voyager':      CreditCard('Voyager',           voyager_prefix_list, 15),
    }
    credit_card_types['visa'] = credit_card_types['visa16']
    credit_card_types['jcb'] = credit_card_types['jcb16']

    @classmethod
    def credit_card_provider(cls, card_type=None):
        if card_type is None:
            card_type = cls.random_element(cls.credit_card_types.keys())
        return cls._credit_card_type(card_type).name

    @classmethod
    def credit_card_number(cls, card_type=None, validate=False, max_check=10):
        card = cls._credit_card_type(card_type)
        number = ''
        for i in range(0, max_check):
            number = cls._generate_number(cls.random_element(card.prefixes), card.length)
            if not validate or cls._validate_credit_card_number(card, number):
                break
        return number

    @classmethod
    def credit_card_expire(cls, start='now', end='+10y', date_format='%m/%y'):
        expire_date = DateTimeProvider.date_time_between(start, end)
        return expire_date.strftime(date_format)

    def credit_card_full(self, card_type=None, validate=False, max_check=10):
        card = self._credit_card_type(card_type)
        template = """
{provider}
{owner}
{number}  {expire_date}
{security}: {security_nb}""".format(
            provider=card.name,
            owner=self.generator.parse("{{first_name}} {{last_name}}"),
            number=self.credit_card_number(card, validate, max_check),
            expire_date=self.credit_card_expire(),
            security=card.security_code,
            security_nb=self.credit_card_security_code(card)
        )
        return self.generator.parse(template)

    @classmethod
    def credit_card_security_code(cls, card_type=None):
        return cls.random_number(cls._credit_card_type(card_type).security_code_length)

    @classmethod
    def _credit_card_type(cls, card_type=None):
        """returns a random credit card type instance"""
        if card_type is None:
            card_type = cls.random_element(cls.credit_card_types.keys())
        elif isinstance(card_type, CreditCard):
            return card_type
        return cls.credit_card_types[card_type]

    @classmethod
    def _generate_number(cls, prefix, length):
        """
        'prefix' is the start of the CC number as a string, any number of digits.
        'length' is the length of the CC number to generate. Typically 13 or 16
        """
        # add list() to copy prefixes
        number = list(prefix)
        # generate digits
        while len(number) < (length - 1):
            number.append(str(cls.random_digit()))

        # Calculate sum
        tot = 0
        pos = 0

        reversed_number = []
        reversed_number.extend(number)
        reversed_number.reverse()

        while pos < length - 1:
            odd = int(reversed_number[pos]) * 2
            if odd > 9:
                odd -= 9
            tot += odd
            if pos != (length - 2):
                tot += int(reversed_number[pos+1])
            pos += 2
        # Calculate check digit
        check_digit = ((tot / 10 + 1) * 10 - tot) % 10
        number.append(str(check_digit))
        return ''.join(number)

    @classmethod
    def _validate_credit_card_number(cls, card, number):
        if card.valid_characters_pattern.match(number) is not None:
            return cls._validate_luhn_checksum(number)
        return False

    @staticmethod
    def _validate_luhn_checksum(number_as_string):
        """ checks to make sure that the card passes a luhn mod-10 checksum """

        number = 0
        num_digits = len(number_as_string)
        odd_even = num_digits & 1

        for i in range(0, num_digits):
            digit = int(number_as_string[i])

            if not ((i & 1) ^ odd_even):
                digit *= 2
            if digit > 9:
                digit -= 9
            number += digit
        return (number % 10) == 0
