# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider

class Provider(PhoneNumberProvider):
    country_code ='45'
    formats = (
        '(0)##########',
        '(0)#### ######',
        '(0) #### ######',
        '(0) #########',
        '(0)#### #####',
        '0##########',
        '0#########',
        '0#### ######',
        '0#### #####',
        '(0####) ######',
        '(0####) #####',
    )
