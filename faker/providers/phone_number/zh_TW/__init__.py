# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider

# phone number from https://en.wikipedia.org/wiki/Telephone_numbers_in_Taiwan

class Provider(PhoneNumberProvider):
    country_code = '886'
    formats = ('(0#) %#######',
               '0#-%#######',
               '0## %#######',
               '09########',
               '09##-######',
               '0#-%######',
               '0# %######')
