from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    """Company provider for fr_DZ locale (Algeria, French-language)."""

    # Sources:
    #   - https://www.commerce.gov.dz/fr/choix-de-la-forme-juridique-de-votre-entreprise-1
    formats = (
        "{{last_name}} {{company_suffix}}",
        "{{last_name}} {{last_name}} {{company_suffix}}",
        "{{last_name}} et Associés",
        "{{last_name}} & {{last_name}}",
        "{{last_name}}",
    )

    company_suffixes = (
        "SARL",
        "S.A.R.L.",
        "SPA",
        "S.P.A.",
        "EURL",
        "E.U.R.L.",
        "SNC",
        "S.N.C.",
        "SCS",
        "S.C.S.",
        "SEM",
        "EP",
        "EPIC",
    )

    catch_phrase_formats = ("{{catch_phrase_noun}} {{catch_phrase_verb}} {{catch_phrase_attribute}}",)

    nouns = (
        "la qualité",
        "l'excellence",
        "la confiance",
        "le développement",
        "la croissance",
        "l'innovation",
        "la performance",
        "le progrès",
        "la réussite",
        "le service",
        "la sécurité",
        "le partenariat",
    )

    verbs = (
        "de réussir",
        "d'avancer",
        "d'évoluer",
        "de se développer",
        "d'innover",
        "de progresser",
        "d'investir",
        "de construire",
        "d'atteindre vos objectifs",
        "de concrétiser vos projets",
    )

    attributes = (
        "ensemble",
        "durablement",
        "efficacement",
        "avec confiance",
        "en toute sécurité",
        "pour demain",
        "pour l'avenir",
        "au service du pays",
        "au cœur du développement",
        "avec excellence",
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
