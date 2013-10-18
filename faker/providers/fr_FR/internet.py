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
            ('à', 'a'), ('À', 'A'), ('ç', 'c'), ('Ç', 'c'), ('é', 'e'), ('É', 'E'), ('è', 'e'),
            ('È', 'E'), ('ë', 'e'), ('Ë', 'E'), ('ï', 'i'), ('Ï', 'I'), ('î', 'i'), ('Î', 'I'),
            ('ô', 'o'), ('Ô', 'O'), ('ù', ''), ('Ù', 'U'),
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