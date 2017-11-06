# coding=utf-8

from .. import BaseProvider

import string
from string import ascii_uppercase
import re

localized = True

class Provider(BaseProvider):
    
    ALPHA = {c: str(ord(c) % 55) for c in string.ascii_uppercase}

     # see https://en.wikipedia.org/wiki/International_Bank_Account_Number
    bban_format = '????#############'
    country_code = 'GB'

    def bank_country(self):
        return self.country_code

    def bban(self):
        temp = re.sub(r'\?',
            lambda x: self.random_element(ascii_uppercase), 
            self.bban_format)
        return self.numerify(temp)

    def iban(self):
        bban = self.bban()

        check = bban + self.country_code + '00'
        check = int(''.join(self.ALPHA.get(c, c) for c in check))
        check = 98 - (check % 97)
        check = str(check).zfill(2)

        return self.country_code + check + bban
