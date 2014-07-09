# coding=utf-8

from __future__ import unicode_literals
from ..internet import Provider as InternetProvider

from faker.utils.decorators import slugify_domain


class Provider(InternetProvider):

    free_email_domains = (
        'aol.de', 'gmail.com', 'gmx.de', 'googlemail.com', 'hotmail.de',
        'web.de', 'yahoo.de',
    )
    tlds = ('com', 'com', 'com', 'net', 'org', 'de', 'de', 'de', )

    @staticmethod
    def _to_ascii(string):
        # ``slugify`` doesn't replace `ß` and normalize
        # other glyphs as single letters
        replacements = (
            ('ä', 'ae'), ('Ä', 'Ae'),
            ('ö', 'oe'), ('Ö', 'Oe'),
            ('ü', 'ue'), ('Ü', 'Ue'),
            ('ß', 'ss'),
        )
        for search, replace in replacements:
            string = string.replace(search, replace)
        return string

    @slugify_domain
    def user_name(self):
        pattern = self.random_element(self.user_name_formats)
        return self._to_ascii(
            self.bothify(self.generator.parse(pattern)))

    @slugify_domain
    def domain_word(self):
        company = self.generator.format('company')
        company_elements = company.split(' ')
        company = self._to_ascii(company_elements.pop(0))
        return company
