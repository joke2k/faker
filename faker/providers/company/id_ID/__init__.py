from __future__ import unicode_literals
from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    formats = (
        '{{company_prefix}} {{last_name}}',
        '{{company_prefix}} {{last_name}} {{last_name}}',
        '{{company_prefix}} {{last_name}} {{company_suffix}}',
        '{{company_prefix}} {{last_name}} {{last_name}} {{company_suffix}}',
    )

    company_prefixes = (
        'PT', 'CV', 'UD', 'PD', 'Perum',
    )

    company_suffixes = (
        '(Persero) Tbk', 'Tbk',
    )

    def company_prefix(self):
        return self.random_element(self.company_prefixes)