# coding=utf-8
from __future__ import unicode_literals
from ..internet import Provider as InternetProvider


class Provider(InternetProvider):
    safe_email_tlds = ('com', 'net', 'fr', 'fr')
    free_email_domains = (
    'voila.fr', 'gmail.com', 'hotmail.fr', 'yahoo.fr', 'laposte.net', 'free.fr', 'sfr.fr', 'orange.fr', 'bouygtel.fr',
    'club-internet.fr', 'dbmail.com', 'live.com', 'ifrance.com', 'noos.fr', 'tele2.fr', 'tiscali.fr', 'wanadoo.fr')
    tlds = ('com', 'com', 'com', 'net', 'org', 'fr', 'fr', 'fr')

    @staticmethod
    def _to_ascii(string):
        replacements = (
            (u'à', u'a'), (u'À', u'A'), (u'ç', u'c'), (u'Ç', u'c'), (u'é', u'e'), (u'É', u'E'), (u'è', u'e'),
            (u'È', u'E'), (u'ë', u'e'), (u'Ë', u'E'), (u'ï', u'i'), (u'Ï', u'I'), (u'î', u'i'), (u'Î', u'I'),
            (u'ô', u'o'), (u'Ô', u'O'), (u'ù', u'u'), (u'Ù', u'U'),
        )
        for search, replace in replacements:
            string = string.replace(search, replace)

        return string

    def user_name(self):
        pattern = self.random_element(self.user_name_formats)
        return self._to_ascii(self.bothify(self.generator.parse(pattern))).lower()

    def domain_word(self):
        company = self.generator.format('company')
        company_elements = company.split(' ')
        company = company_elements[0]
        company = company.replace(" ", "")

        return self._to_ascii(company).lower()