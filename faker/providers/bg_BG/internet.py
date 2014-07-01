# coding=utf-8
from __future__ import unicode_literals
from ..internet import Provider as InternetProvider

import re


class Provider(InternetProvider):

    user_name_formats = (
        '{{last_name_female}}.{{first_name_female}}',
        '{{last_name_male}}.{{first_name_male}}',
        '{{last_name_male}}.{{first_name_male}}',
        '{{first_name_male}}.{{last_name_male}}',
        '{{first_name}}##',
        '?{{last_name}}',
        '{{first_name}}{{year}}'
    )

    @staticmethod
    def _to_ascii(string):
        replacements = (
        	('Б', 'b'), ('Г', 'r'), ('Д', 'd'), ('Ж', 'zh'), ('З', 'z'), ('И', 'i'),
			('Й', 'i'), ('Л', 'l'), ('П', 'p'), ('Ф', 'f'), ('Ц', 'ts'), ('Ч', 'ch'),
			('Ш', 'sh'), ('Щ', 'sht'), ('Ъ', 'u'), ('Ь', ''), ('Ю', 'yu'), ('Я', 'ya'),
			('б', 'b'), ('в', 'v'), ('д', 'd'), ('ж', 'zh'), ('з', 'z'), ('и', 'i'),
			('й', 'i'), ('к', 'k'), ('л', 'l'), ('м', 'm'), ('н', 'n'), ('п', 'p'),
			('т', 't'), ('ф', 'f'), ('ц', 'ts'), ('ч', 'ch'), ('ш', 'sh'), ('щ', 'sht'),
			('ъ', 'u'), ('ь', ''), ('ю', 'yu'), ('я', 'ya'), ('Б', 'b'), ('Г', 'r'),
			('Д', 'd'), ('Ж', 'zh'), ('З', 'z'), ('И', 'i'), ('Й', 'i'), ('Л', 'l'),
			('П', 'p'), ('Ф', 'f'), ('Ц', 'ts'), ('Ч', 'ch'), ('Ш', 'sh'), ('Щ', 'sht'),
			('Ъ', 'u'), ('Ь', ''), ('Ю', 'yu'), ('Я', 'ya'), ('б', 'b'), ('в', 'v'),
			('д', 'd'), ('ж', 'zh'), ('з', 'z'), ('и', 'i'), ('й', 'i'), ('к', 'k'),
			('л', 'l'), ('м', 'm'), ('н', 'n'), ('п', 'p'), ('т', 't'), ('ф', 'f'),
			('ц', 'ts'), ('ч', 'ch'), ('ш', 'sh'), ('щ', 'sht'), ('ъ', 'u'), ('ь', ''),
			('ю', 'yu'), ('я', 'ya')
		)

        for search, replace in replacements:
            string = string.replace(search, replace)

        return string

    email_formats = (
    	'{{user_name}}@{{free_email_domain}}',
    	'{{user_name}}@{{domain_name}}')

    free_email_domains = (
    	'gmail.com', 'yahoo.com', 'hotmail.com', 'mail.bg', 'abv.bg', 'dir.bg'
    )

    tlds = ('bg', 'com', 'biz', 'info', 'net', 'org', 'edu')

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

    def domain_name(self):
        return self.domain_word() + '.' + self.tld()

    def tld(self):
        return self.random_element(self.tlds)
