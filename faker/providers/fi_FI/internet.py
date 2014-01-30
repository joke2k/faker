# coding=utf-8
from __future__ import unicode_literals
from ..internet import Provider as InternetProvider

import re

class Provider(InternetProvider):

    free_email_domains = (
        'gmail.com', 'googlemail.com', 'hotmail.com', 'suomi24.fi', 
        'kolumbus.fi', 'luukku.com', 'surffi.net'
    )
    
    tlds = ('com', 'com', 'com', 'fi', 'fi', 'net', 'org')

    @staticmethod
    def _to_ascii(string):
        replacements = (
            ('ä', 'a'), ('Ä', 'A'),
            ('ö', 'o'), ('O', 'O'),
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
