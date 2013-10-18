# coding=utf-8
from __future__ import unicode_literals
from ..internet import Provider as InternetProvider


class Provider(InternetProvider):
    safe_email_tlds = ('com', 'net', 'br', 'br')
    free_email_domains = ('gmail.com', 'hotmail.com', 'yahoo.com.br', 'uol.com.br', 'bol.com.br', 'ig.com.br')
    tlds = ('com', 'com', 'com', 'net', 'org', 'br', 'br', 'br')

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
        return self._to_ascii(super(Provider, self).user_name())