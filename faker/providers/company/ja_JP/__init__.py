# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    formats = (
        '{{company_prefix}}{{last_name}}{{category}}',
        '{{last_name}}{{category}}{{company_prefix}}',
    )

    company_prefixes = ('株式会社', '有限会社', '合同会社')
    categories = ('水産', '農林', '鉱業', '建設', '食品', '印刷', '電気', 'ガス', '情報', '通信', '運輸', '銀行', '保険')

    def company_prefix(self):
        return self.random_element(self.company_prefixes)

    def category(self):
        return self.random_element(self.categories)
