from typing import Tuple

from ..es import Provider as PersonProvider


class Provider(PersonProvider):
    # Source: Instituto Nacional de Estadística e Informática (INEI),
    # "Censos y registros estadísticos" — https://www.inei.gob.pe
    # Source: Registro Nacional de Identidad y Estado Civil (RENIEC) — https://www.reniec.gob.pe
    # Source: Supplemental verification from Wikipedia — "List of common Peruvian given names"
    # Accessed: 2026-02-07

    # The name format in Peru is the same as in Spain: First Name(s) + Paternal Last Name + Maternal Last Name.
    # The formats from the es_ES provider are a good fit.
    formats_male: Tuple[str, ...] = (
        "{{first_name_male}} {{last_name}} {{last_name}}",
        "{{first_name_male}} {{last_name}} {{last_name}}",
        "{{first_name_male}} {{last_name}} {{last_name}}",
        "{{first_name_male}} {{last_name}}",
        "{{first_name_male}} {{last_name}}-{{last_name}}",
        "{{first_name_male}} {{first_name_male}} {{last_name}} {{last_name}}",
    )

    formats_female: Tuple[str, ...] = (
        "{{first_name_female}} {{last_name}} {{last_name}}",
        "{{first_name_female}} {{last_name}} {{last_name}}",
        "{{first_name_female}} {{last_name}} {{last_name}}",
        "{{first_name_female}} {{last_name}}",
        "{{first_name_female}} {{last_name}}-{{last_name}}",
        "{{first_name_female}} {{first_name_female}} {{last_name}} {{last_name}}",
    )

    formats: Tuple[str, ...] = formats_male + formats_female

    # First names from es_ES provider, with common Peruvian names added.
    first_names_male: Tuple[str, ...] = PersonProvider.first_names_male + (
        "André",
        "Brayan",
        "Claudio",
        "Dayron",
        "Deyvis",
        "Edison",
        "Gianluca",
        "Jefferson",
        "Jhair",
        "Joao",
        "Kevin",
        "Liam",
        "Paolo",
        "Renzo",
        "Thiago",
        "Yoshimar",
        "Yordy",
    )

    first_names_female: Tuple[str, ...] = PersonProvider.first_names_female + (
        "Almendra",
        "Antonella",
        "Briana",
        "Brunella",
        "Camila",
        "Danna",
        "Dayana",
        "Daysi",
        "Fiorella",
        "Gianella",
        "Kiara",
        "Luciana",
        "Micaela",
        "Pierina",
        "Valeska",
        "Ximena",
        "Yahaira",
        "Yajaira",
    )

    first_names: Tuple[str, ...] = first_names_male + first_names_female

    # Last names from es_ES provider, with common Peruvian last names added.
    # Includes names of Quechua and Aymara origin.
    last_names: Tuple[str, ...] = PersonProvider.last_names + (
        "Apaza",
        "Cahuana",
        "Ccanto",
        "Chagua",
        "Chambi",
        "Charca",
        "Chavez",
        "Chávez",
        "Choque",
        "Condori",
        "Guerrero",
        "Huaman",
        "Huamán",
        "Huaraca",
        "Inca",
        "Mamani",
        "Paucar",
        "Quispe",
        "Sánchez",
        "Tito",
        "Vargas",
        "Yucra",
    )

    # Prefixes are the same.
    prefixes: Tuple[str, ...] = ("de", "del")
