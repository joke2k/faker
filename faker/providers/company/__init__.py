# coding=utf-8

from __future__ import unicode_literals
from .. import BaseProvider


localized = True


class Provider(BaseProvider):
    formats = ['{{last_name}} {{company_suffix}}', ]

    company_suffixes = ['Ltd', ]

    def company(self):
        """
        :example 'Acme Ltd'
        """
        pattern = self.random_element(self.formats)
        return self.generator.parse(pattern)

    @classmethod
    def company_suffix(cls):
        """
        :example 'Ltd'
        """
        return cls.random_element(cls.company_suffixes)
