# coding=utf-8
from __future__ import unicode_literals
from ..internet import Provider as InternetProvider

import re


class Provider(InternetProvider):

    user_name_formats = (
        '{{last_name_female}}.{{first_name_female}}',
        '{{last_name_female}}.{{first_name_female}}',
        '{{last_name_male}}.{{first_name_male}}',
        '{{last_name_male}}.{{first_name_male}}',
        '{{first_name_female}}.{{last_name_female}}',
        '{{first_name_male}}.{{last_name_male}}',
        '{{first_name}}##',
        '?{{last_name}}',
        '?{{last_name}}',
        '?{{last_name}}',
    )

    email_formats = ('{{user_name}}@{{free_email_domain}}', )

    free_email_domains = (
        'seznam.cz', 'gmail.com', 'email.cz', 'post.cz', 'chello.cz', 'centrum.cz', 'volny.cz',
    )

    tlds = ('cz', 'com', 'cz')

    @staticmethod
    def _to_ascii(string):
        replacements = (
            ('á', 'a'), ('Á', 'A'),
            ('č', 'c'), ('Č', 'C'),
            ('ď', 'd'), ('Ď', 'D'),
            ('é', 'e'), ('É', 'E'),
            ('ě', 'e'), ('Ě', 'E'),
            ('í', 'i'), ('Í', 'I'),
            ('ň', 'n'), ('Ň', 'N'),
            ('ď', 'd'), ('Ď', 'D'),
            ('ť', 't'), ('Ť', 'T'),
            ('ó', 'o'), ('Ó', 'O'),
            ('ř', 'r'), ('Ř', 'R'),
            ('š', 's'), ('Š', 'S'),
            ('ť', 't'), ('Ť', 'T'),
            ('ú', 'u'), ('Ú', 'U'),
            ('ů', 'u'), ('Ů', 'U'),
            ('ý', 'y'), ('Ý', 'Y'),
            ('ž', 'z'), ('Ž', 'Z'),
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
