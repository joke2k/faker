from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    """
    According to official specs:
    https://www.bcn.cl/leychile/navegar?i=173931
    https://www.itu.int/itudoc/itu-t/number/c/chl/76483_ww9-es.doc
    https://www.subtel.gob.cl/base_numeracion/tabla_numeracion_ido_idd.xlsx
    """

    formats = (
        "+56 2 2%## ####",  # santiago landline
        "+56 2 3%## ####",
        "+56 {{ landline_code }} 2%# ####",  # national landlines and VoIP
        "+56 {{ landline_code }} 3%# ####",
        "+56 9 {{ cellphone_block }}%## ####",  # cell phones
        "+56 {{ special_code }} %## ###",  # special
    )

    landline_codes = (
        "32",  # Valparaíso
        "33",  # Quillota
        "34",  # Los Andes
        "35",  # San Antonio
        "41",  # Concepción
        "42",  # Chillán
        "43",  # Los Ángeles
        "45",  # Temuco
        "51",  # La Serena
        "52",  # Copiapó
        "53",  # Ovalle
        "55",  # Antofagasta
        "57",  # Iquique
        "58",  # Arica
        "61",  # Punta Arenas
        "63",  # Valdivia
        "64",  # Osorno
        "65",  # Puerto Montt
        "67",  # Coyhaique
        "71",  # Talca
        "72",  # Rangagua
        "73",  # Linares
        "75",  # Curicó
        "44",  # VoIP
    )

    special_codes = (
        "600",  # Nationalwide
        "800",  # Nationalwide, toll-free
    )

    cellphone_blocks = ("2", "3", "4", "5", "6", "7", "8", "9")

    def landline_code(self) -> str:
        return self.numerify(self.random_element(self.landline_codes))

    def cellphone_block(self) -> str:
        return self.random_element(self.cellphone_blocks)

    def special_code(self) -> str:
        return self.numerify(self.random_element(self.special_codes))

    def phone_number(self) -> str:
        return self.numerify(self.generator.parse(self.random_element(self.formats)))
