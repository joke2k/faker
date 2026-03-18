from .. import Provider as AutomotiveProvider


class Provider(AutomotiveProvider):
    """Automotive provider for mk_MK locale (Macedonian).

    Sources:
    - https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_North_Macedonia

    Standard format: XX NNNN YY
    where XX = two-letter regional code, NNNN = 4-digit number, YY = two letters

    Notes:
    - Letters Q, W, X, Y are NOT used (no Cyrillic equivalents).
    - Country identifier changed from MK to NMK in February 2019 (Prespa Agreement).
    """

    # All 34 official regional codes as of 2020
    # Sources: original 1993 codes + expansions in 2012, 2013, 2015, 2019, 2020
    license_plate_prefixes = (
        "BE",  # Berovo
        "BT",  # Bitola
        "DB",  # Debar
        "DE",  # Delčevo
        "DH",  # Demir Hisar
        "DK",  # Demir Kapija
        "GE",  # Gevgelija
        "GV",  # Gostivar
        "KA",  # Kavadarci
        "KI",  # Kičevo
        "KO",  # Kočani
        "KP",  # Kriva Palanka
        "KR",  # Kratovo
        "KS",  # Kruševo
        "KU",  # Kumanovo
        "MB",  # Makedonski Brod
        "MK",  # Makedonska Kamenica (municipality)
        "NE",  # Negotino
        "OH",  # Ohrid
        "PE",  # Pehčevo
        "PP",  # Prilep
        "PS",  # Probištip
        "RA",  # Radoviš
        "RE",  # Resen
        "SK",  # Skopje
        "SN",  # Sveti Nikole
        "SR",  # Strumica
        "ST",  # Štip
        "SU",  # Struga
        "TE",  # Tetovo
        "VA",  # Valandovo
        "VE",  # Veles
        "VI",  # Vinica
        "VV",  # Vevčani
    )

    # Latin letters used on plates — Q, W, X, Y are excluded (no Cyrillic equivalents)
    license_plate_suffix_letters = "ABCDEFGHIJKLMNOPRSTUVZ"

    def license_plate(self) -> str:
        prefix = self.random_element(self.license_plate_prefixes)
        number = self.numerify("####")
        suffix = self.random_element(
            self.license_plate_suffix_letters
        ) + self.random_element(self.license_plate_suffix_letters)
        return f"{prefix} {number} {suffix}"
