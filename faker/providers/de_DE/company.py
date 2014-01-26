from __future__ import unicode_literals
from ..company import Provider as CompanyProvider


class Provider(CompanyProvider):
    formats = (
        '{{last_name}} {{company_suffix}}',
        '{{last_name}} {{last_name}} {{company_suffix}}',
        '{{last_name}}',
    )

    company_suffixes = (
    	'e.G.', 'e.V.', 'GbR', 'GbR', 'OHG mbH', 'GmbH & Co. OHG',
    	'AG & Co. OHG', 'GmbH', 'GmbH', 'GmbH', 'GmbH', 'AG', 'AG', 'AG',
    	'AG', 'KG', 'KG', 'KG', 'GmbH & Co. KG', 'GmbH & Co. KG',
    	'AG & Co. KG', 'Stiftung & Co. KG', 'KGaA', 'GmbH & Co. KGaA',
    	'AG & Co. KGaA', 'Stiftung & Co. KGaA'
    )
