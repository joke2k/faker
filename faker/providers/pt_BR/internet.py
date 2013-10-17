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
            (u'à', u'a'), (u'À', u'A'), (u'ç', u'c'), (u'Ç', u'c'), (u'é', u'e'), (u'É', u'E'), (u'è', u'e'),
            (u'È', u'E'), (u'ë', u'e'), (u'Ë', u'E'), (u'ï', u'i'), (u'Ï', u'I'), (u'î', u'i'), (u'Î', u'I'),
            (u'ô', u'o'), (u'Ô', u'O'), (u'ù', u'u'), (u'Ù', u'U'),
        )
        for search, replace in replacements:
            string = string.replace(search, replace)

        return string

    def user_name(self):
        return self._to_ascii(super(Provider, self).user_name())