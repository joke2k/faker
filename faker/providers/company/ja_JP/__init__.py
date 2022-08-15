from typing import Optional

from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    formats = (
        "{{company_prefix}}{{last_name}}{{company_category}}",
        "{{last_name}}{{company_category}}{{company_prefix}}",
    )

    company_prefixes = ("株式会社", "有限会社", "合同会社")
    company_categories = (
        "水産",
        "農林",
        "鉱業",
        "建設",
        "食品",
        "印刷",
        "電気",
        "ガス",
        "情報",
        "通信",
        "運輸",
        "銀行",
        "保険",
    )

    def company_prefix(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        return self.random_element(self.company_prefixes, min_length, max_length)

    def company_category(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        return self.random_element(self.company_categories, min_length, max_length)
