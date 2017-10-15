from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    # Source: https://en.wikipedia.org/wiki/Telephone_numbers_in_the_United_Kingdom

    cellphone_formats = (
        '+44 7### ######',
        '+44 7#########',
        '07### ######',
        '07#########',
    )

    formats = (
        '+44(0)##########',
        '+44(0)#### ######',
        '+44(0)#########',
        '+44(0)#### #####',
        '0##########',
        '0#########',
        '0#### ######',
        '0#### #####',
        '(0####) ######',
        '(0####) #####',
    )

    def cellphone_number(self):
        pattern = self.random_element(self.cellphone_formats)
        return self.numerify(self.generator.parse(pattern))
