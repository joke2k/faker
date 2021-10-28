from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    formats = (
        "{{last_name}} {{company_suffix}}",
        "{{last_name}} {{last_name}} {{company_suffix}}",
        "{{large_company}}",
    )
    # Source: https://www.capital.com.tr/listeler/capital-500
    large_companies = (
        "Tüpraş",
        "Türk Hava Yolları",
        "Petrol Ofisi",
        "Opet",
        "BİM",
        "Ford Otosan",
        "Arçelik",
        "Vestel",
        "Toyota Otomotiv",
        "Oyak Renault",
        "A101 Yeni Mağzacılık",
        "Turkcell",
        "Türk Telekom",
        "Anadolu Efes",
        "Migros",
        "LC Waikiki",
        "Peak Games",
        "Masomo",
        "EnerjiSA",
        "Tofaş",
        "Şişecam",
        "Selçuk Ecza",
        "ŞOK Marketler",
        "Petkim",
        "Limak İnşaat",
        "Aselsan",
        "Havelsan",
        "Roketsan",
        "Şişecam",
    )
    company_suffixes = (
        "A.Ş.",
        "Ltd.",
        "Şti.",
    )

    def large_company(self) -> str:
        """
        :example: 'Peak Games'
        """
        return self.random_element(self.large_companies)
