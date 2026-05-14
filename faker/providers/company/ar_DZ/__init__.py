from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    """Company provider for ar_DZ locale (Algeria, Arabic-language)."""

    # Sources:
    #   - https://www.commerce.gov.dz/fr/choix-de-la-forme-juridique-de-votre-entreprise-1
    formats = (
        "{{last_name}} {{company_suffix}}",
        "{{last_name}} {{last_name}} {{company_suffix}}",
        "مجمع {{last_name}}",
        "{{last_name}}",
    )

    company_suffixes = (
        "ش.ذ.م.م",
        "ش.م.",
        "م.ذ.م.م",
        "ش.ت.",
        "ش.ت.ب.",
        "م.ع.",
        "م.ع.ا.ت.",
    )

    catch_phrase_formats = ("{{catch_phrase_noun}} {{catch_phrase_verb}} {{catch_phrase_attribute}}",)

    nouns = (
        "الجودة",
        "التميّز",
        "الثقة",
        "التطوير",
        "النمو",
        "الابتكار",
        "الأداء",
        "التقدّم",
        "النجاح",
        "الخدمة",
        "الأمان",
        "الشراكة",
    )

    verbs = (
        "للنجاح",
        "للتطوير",
        "للتقدّم",
        "للابتكار",
        "للبناء",
        "للاستثمار",
        "لتحقيق أهدافك",
        "لإنجاز مشاريعك",
        "للنهوض بالاقتصاد",
        "لخدمة الوطن",
    )

    attributes = (
        "معاً",
        "بكفاءة",
        "بثقة",
        "بامتياز",
        "باستدامة",
        "في خدمة الجزائر",
        "نحو المستقبل",
        "من أجل غدٍ أفضل",
        "في قلب التنمية",
        "بجودة عالية",
    )

    def catch_phrase(self) -> str:
        pattern: str = self.random_element(self.catch_phrase_formats)
        return self.generator.parse(pattern)

    def catch_phrase_noun(self) -> str:
        return self.random_element(self.nouns)

    def catch_phrase_verb(self) -> str:
        return self.random_element(self.verbs)

    def catch_phrase_attribute(self) -> str:
        return self.random_element(self.attributes)
