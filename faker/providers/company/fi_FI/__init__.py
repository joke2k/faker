from __future__ import unicode_literals
from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    formats = (
        '{{last_name}} {{company_suffix}}',
        '{{last_name}} {{last_name}} {{company_suffix}}',
        '{{last_name}} {{last_name}} {{company_suffix}}',
        '{{last_name}}'
    )

    company_suffixes = (
        'As Oy', 'Tmi', 'Oy', 'Oyj', 'Ky', 'Osk', 'ry'
    )
