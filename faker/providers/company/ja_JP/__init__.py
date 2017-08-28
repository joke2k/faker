# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    formats = (
        '{{company_prefix}} {{last_name}}',
    )

    company_prefixes = ('株式会社', '有限会社', '合同会社')

    def company_prefix(self):
        return self.random_element(self.company_prefixes)
