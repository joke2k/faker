from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    formats = (
        "{{company_limited_prefix}}{{last_name}} {{company_limited_suffix}}",
        "{{company_prefix}} {{last_name}}",
        "{{last_name}}-{{last_name}}",
        "{{last_name}}และ{{last_name}}",
        "{{last_name}}{{company_suffix}}",
    )

    company_prefixes = (
        "ห้างหุ้นส่วนจำกัด",
        "ห้างหุ้นส่วนสามัญ",
        "มูลนิธิ",
        "สมาคม",
        "ชมรม",
        "บมจ.",
        "หจก.",
        "บจก.",
    )

    company_suffixes = (
        "และบุตร",
        "กรุ๊ป",
    )

    company_limited_prefixes = (
        "บริษัท ",
        "บริษัทหลักทรัพย์ ",
        "กองทุนรวม",
        "ธนาคาร",
    )

    company_limited_suffixes = (
        "จำกัด",
        "จำกัด (มหาชน)",
    )

    def company_prefix(self):
        """
        :example 'ห้างหุ้นส่วนจำกัด'
        """
        return self.random_element(self.company_prefixes)

    def company_limited_prefix(self):
        """
        :example 'บริษัท'
        """
        return self.random_element(self.company_limited_prefixes)

    def company_limited_suffix(self):
        """
        :example 'จำกัด'
        """
        return self.random_element(self.company_limited_suffixes)
