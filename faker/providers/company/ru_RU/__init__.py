# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as CompanyProvider

class Provider(CompanyProvider):
    formats = (
        '{{company_prefix}} «{{last_name}}»',
        '{{company_prefix}} «{{last_name}} {{last_name}}»',
        '{{company_prefix}} «{{last_name}}-{{last_name}}»',
        '{{company_prefix}} «{{last_name}}, {{last_name}} и {{last_name}}»',
        '{{last_name}}',
    )

    company_prefixes = (
        'РАО', 'АО', 'ИП', 'НПО',
    )

    @classmethod
    def company_prefix(cls):
        return cls.random_element(cls.company_prefixes)
