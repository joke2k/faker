# coding=utf-8
from __future__ import unicode_literals
from ..internet import Provider as InternetProvider

import re


class Provider(InternetProvider):

    tlds = ('com', 'com', 'com', 'net', 'org', 'no', 'no', 'no', 'no', 'no')

    @staticmethod
    def _to_ascii(string):
        replacements = (
            ('æ', 'ae'), ('Æ', 'Ae'),
            ('ø', 'oe'), ('Ø', 'Oe'),
            ('å', 'aa'), ('Å', 'Aa'),
            ('ä', 'ae'), ('Ä', 'Ae'),
            ('ö', 'oe'), ('Ö', 'Oe'),
            ('ü', 'ue'), ('Ü', 'Ue'),
        )
        for search, replace in replacements:
            string = string.replace(search, replace)

        return string

    def user_name(self):
        pattern = self.random_element(self.user_name_formats)
        return self._to_ascii(
            self.bothify(self.generator.parse(pattern)
        ).lower())

    def domain_word(self):
        company = self.generator.format('company')
        company_elements = company.split(' ')
        company = self._to_ascii(company_elements.pop(0))
        return re.sub(r'\W', '', company).lower()
