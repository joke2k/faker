# faker/providers/company/es_PE/__init__.py

from collections import OrderedDict

from .. import Provider as CompanyProvider


class Provider(CompanyProvider):
    """
    Provider for company names for es_PE locale.
    Company naming scheme and probabilities are inspired by and/or based on
    existing companies in Peru.

    Sources:
    - https://www.gob.pe/295-tipos-de-empresa
    - General knowledge of Peruvian company structures.
    Accessed: 2026-02-07
    """

    # These formats are generic enough to apply well to Peru.
    Company naming scheme and probabilities are inspired by and/or based on
    existing companies in Peru.

    Sources:
    - https://www.gob.pe/295-tipos-de-empresa
    - General knowledge of Peruvian company structures.
    """

    # These formats are generic enough to apply well to Peru.
    formats = (
        "{{company_prefix}} {{last_name}} {{company_suffix}}",
        "{{company_type}} {{random_company_acronym}} {{company_suffix}}",
        "{{company_type}} {{last_name}} {{company_suffix}}",
        "{{company_type}} {{random_company_adjective}} {{company_suffix}}",
        "{{company_type}} {{last_name}} {{random_name_complements}} {{company_suffix}}",
        "{{last_name}} {{random_name_complements}} {{company_suffix}}",
        "{{last_name}} y {{last_name}} {{company_suffix}}",
        "{{first_name}} {{last_name}} {{last_name}} {{company_suffix}}",
    )

    # Common legal entity types in Peru, with S.A.C. and S.R.L. being very common.
    company_suffixes = OrderedDict(
        [
            ("S.A.C.", 0.40),  # Sociedad Anónima Cerrada
            ("S.R.L.", 0.25),  # Sociedad de Responsabilidad Limitada
            ("S.A.", 0.15),    # Sociedad Anónima
            ("E.I.R.L.", 0.10),# Empresa Individual de Responsabilidad Limitada
            ("S.A.A.", 0.05),  # Sociedad Anónima Abierta
            ("S.C.", 0.05),    # Sociedad Civil
        ]
    )

    # Prefixes are largely the same in Spanish-speaking countries.
    company_prefixes = (
        "Grupo",
        "Hermanos",
        "Hnos",
        "Familia",
        "Corporación",
    )

    # Common business sectors in Peru.
    company_types = (
        "Agroindustrial",
        "Alimentación",
        "Banca",
        "Comercial",
        "Comercializadora",
        "Constructora",
        "Consultoría",
        "Desarrollo",
        "Distribuciones",
        "Exportadora",
        "Financiera",
        "Hotelera",
        "Industrias",
        "Inmobiliaria",
        "Inversiones",
        "Logística",
        "Manufacturas",
        "Minería",
        "Pesquera",
        "Promotora",
        "Restaurante",
        "Servicios",
        "Soluciones",
        "Suministros",
        "Supermercados",
        "Talleres",
        "Tecnología",
        "Transportes",
    )

    # Universal complements.
    name_complements = (
        "& Asociados",
        "y Asociados",
        "e Hijos",
    )

    # Adjectives relevant to Peru.
    company_adjectives = (
        "Andina",
        "Andinos",
        "Globales",
        "Integrales",
        "Internacional",
        "Nacional",
        "del Norte",
        "del Pacífico",
        "Peruana",
        "Peruanos",
        "del Sur",
    )

    def company_type(self) -> str:
        return self.random_element(self.company_types)

    def company_suffix(self) -> str:
        return self.random_element(self.company_suffixes)

    def random_name_complements(self) -> str:
        return self.random_element(self.name_complements)

    def random_company_adjective(self) -> str:
        return self.random_element(self.company_adjectives)

    def random_company_acronym(self) -> str:
        letters = self.random_letters(self.random_int(2, 4))
        return "".join(letters).upper()

    def company_prefix(self) -> str:
        return self.random_element(self.company_prefixes)
>>>>>>> origin/feature/add-es_PE-locale
