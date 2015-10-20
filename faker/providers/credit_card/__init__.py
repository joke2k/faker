# coding=utf-8

from __future__ import unicode_literals

from faker.providers.date_time import Provider as DateTimeProvider
from .. import BaseProvider


class CreditCard(object):

    def __init__(self, name, prefixes, length=16, security_code='CVC', security_code_length=3):
        self.name = name
        self.prefixes = prefixes
        self.length = length
        self.security_code = security_code
        self.security_code_length = security_code_length


class Provider(BaseProvider):

    prefix_maestro = ['5018', '5020', '5038', '5612', '5893', '6304', '6759', '6761', '6762', '6763', '0604', '6390']
    prefix_mastercard = ['51', '52', '53', '54', '55']
    prefix_visa = ['4']
    prefix_amex = ['34', '37']
    prefix_discover = ['6011']
    prefix_diners = ['300', '301', '302', '303', '304', '305']
    prefix_jcb16 = ['3088', '3096', '3112', '3158', '3337', '3528']
    prefix_jcb15 = ['2100', '1800']
    prefix_voyager = ['8699']

    credit_card_types = {
        'maestro':      CreditCard('Maestro',           prefix_maestro, 12, security_code='CVV'),
        'mastercard':   CreditCard('Mastercard',        prefix_mastercard, 16, security_code='CVV'),
        'visa16':       CreditCard('VISA 16 digit',     prefix_visa),
        'visa13':       CreditCard('VISA 13 digit',     prefix_visa, 13),
        'amex':         CreditCard('American Express',  prefix_amex, 15, security_code='CID', security_code_length=4),
        'discover':     CreditCard('Discover',          prefix_discover),
        'diners':       CreditCard('Diners Club / Carte Blanche', prefix_diners, 14),
        'jcb15':        CreditCard('JCB 15 digit',      prefix_jcb15, 15),
        'jcb16':        CreditCard('JCB 16 digit',      prefix_jcb16),
        'voyager':      CreditCard('Voyager',           prefix_voyager, 15),
    }
    credit_card_types['visa'] = credit_card_types['visa16']
    credit_card_types['jcb'] = credit_card_types['jcb16']

    luhn_lookup = {'0': 0, '1': 2, '2': 4, '3': 6, '4': 8,
                   '5': 1, '6': 3, '7': 5, '8': 7, '9': 9}

    @classmethod
    def credit_card_provider(cls, card_type=None):
        """ Returns the provider's name of the credit card. """
        if card_type is None:
            card_type = cls.random_element(cls.credit_card_types.keys())
        return cls._credit_card_type(card_type).name

    @classmethod
    def credit_card_number(cls, card_type=None):
        """ Returns a valid credit card number. """
        card = cls._credit_card_type(card_type)
        prefix = cls.random_element(card.prefixes)
        number = cls._generate_number(prefix, card.length)
        return number

    @classmethod
    def credit_card_expire(cls, start='now', end='+10y', date_format='%m/%y'):
        expire_date = DateTimeProvider.date_time_between(start, end)
        return expire_date.strftime(date_format)

    def credit_card_full(self, card_type=None):
        card = self._credit_card_type(card_type)

        tpl = ('{provider}\n'
               '{owner}\n'
               '{number} {expire_date}\n'
               '{security}: {security_nb}\n')

        tpl = tpl.format(provider = card.name,
                         owner = self.generator.parse("{{first_name}} {{last_name}}"),
                         number = self.credit_card_number(card),
                         expire_date = self.credit_card_expire(),
                         security = card.security_code,
                         security_nb = self.credit_card_security_code(card))

        return self.generator.parse(tpl)

    @classmethod
    def credit_card_security_code(cls, card_type=None):
        """ Returns a security code string. """
        sec_len = cls._credit_card_type(card_type).security_code_length
        return cls.numerify('#' * sec_len)

    @classmethod
    def _credit_card_type(cls, card_type=None):
        """ Returns a random credit card type instance. """
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
        number = prefix
        # Generate random char digits
        number += '#' * (length - len(prefix) - 1)
        number = cls.numerify(number)
        reverse = number[::-1]
        # Calculate sum
        tot = 0
        pos = 0
        while pos < length - 1:
            tot += Provider.luhn_lookup[reverse[pos]]
            if pos != (length - 2):
                tot += int(reverse[pos+1])
            pos += 2
        # Calculate check digit
        check_digit = (10 - (tot % 10)) % 10
        number += str(check_digit)
        return number

