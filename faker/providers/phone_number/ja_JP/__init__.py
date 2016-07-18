# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    country_code = '81'
    formats = (
        '070-####-####',
        '080-####-####',
        '090-####-####',
        '##-####-####',
    )
