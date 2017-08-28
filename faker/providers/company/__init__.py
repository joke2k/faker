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

    def company_suffix(self):
        """
        :example 'Ltd'
        """
        return self.random_element(self.company_suffixes)
