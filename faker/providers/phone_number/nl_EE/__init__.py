# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    country_code = '372'
    formats = (
        '32# ####',
        '33# ####',
        '34# ####',
        '35# ####',
        '38# ####',
        '39# ####',
        '40## ####',
        '43# ####',
        '44# ####',
        '45# ####',
        '48# ####',
        '5## ####',
        '5### ####',
        '6## ####',
        '7## ####',
        '81## ####',
        '82## ####',
        '83## ####',
        '88# ####',
        '901 ####',
    )
