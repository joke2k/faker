# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    formats = (
        '{{last_name}} {{company_suffix}}',
        '{{last_name}} {{last_name}} {{company_suffix}}',
        '{{last_name}}'
    )

    company_suffixes = (
        'Kft',
        'és Tsa',
        'Kht',
        'ZRT',
        'NyRT',
        'BT'
    )

    @classmethod
    def company_suffix(cls):
        return cls.random_element(cls.company_suffixes)
