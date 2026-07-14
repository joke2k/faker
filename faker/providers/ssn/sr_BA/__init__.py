from typing import Optional

from .. import Provider as BaseProvider


def calculate_checksum(ssn_without_checksum: str) -> Optional[int]:
    """
    Calculate JMB control digit for a 12-digit SSN prefix.

    Formula:
    7·A1 + 6·A2 + 5·A3 + 4·A4 + 3·A5 + 2·A6 + 7·A7 + 6·A8 + 5·A9 + 4·A10 + 3·A11 + 2·A12
    """

    weights = (7, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 2)
    digits = [int(char) for char in ssn_without_checksum]

    weighted_sum = sum(weight * digit for weight, digit in zip(weights, digits))
    remainder = weighted_sum % 11

    if remainder == 0:
        return 0
    if remainder == 1:
        return None
    return 11 - remainder


class Provider(BaseProvider):
    """
    Bosnia and Herzegovina JMB provider.
    """

    # registration area codes with list of places
    # https://sr.wikipedia.org/sr-el/Јединствени_матични_број_грађана#Босна_и_Херцеговина
    registration_areas = (
        (
            "11",
            (
                "Banja Luka",
                "Celinac",
                "Gradiska",
                "Istocni Drvar",
                "Jezero",
                "Knezevo",
                "Kostajnica",
                "Kotor Varos",
                "Kozarska Dubica",
                "Krupa na Uni",
                "Kupres",
                "Laktasi",
                "Mrkonjic Grad",
                "Novi Grad",
                "Ostra Luka",
                "Petrovac",
                "Prijedor",
                "Prnjavor",
                "Ribnik",
                "Srbac",
                "Sipovo",
            ),
        ),
        (
            "12",
            (
                "Bijeljina",
                "Brod",
                "Derventa",
                "Doboj",
                "Donji Zabar",
                "Lopare",
                "Modrica",
                "Pelagicevo",
                "Petrovo",
                "Teslic",
                "Ugljevik",
                "Vukosavlje",
                "Samac",
            ),
        ),
        (
            "13",
            (
                "Bileca",
                "Berkovici",
                "Bratunac",
                "Cajnice",
                "Foca",
                "Gacko",
                "Han Pijesak",
                "Istocna Ilidza",
                "Istocni Mostar",
                "Istocni Stari Grad",
                "Istocno Novo Sarajevo",
                "Kalinovik",
                "Ljubinje",
                "Milici",
                "Nevesinje",
                "Novo Gorazde",
                "Osmaci",
                "Pale",
                "Rogatica",
                "Rudo",
                "Srebrenica",
                "Sokolac",
                "Sekovici",
                "Trebinje",
                "Trnovo",
                "Visegrad",
                "Vlasenica",
                "Zvornik",
            ),
        ),
        ("14", ("Brcko Distrikt Bosne i Hercegovine",)),
        (
            "15",
            (
                "Capljina",
                "Citluk",
                "Grude",
                "Jablanica",
                "Konjic",
                "Ljubuski",
                "Mostar",
                "Neum",
                "Posusje",
                "Prozor",
                "Ravno",
                "Stolac",
                "Siroki Brijeg",
            ),
        ),
        (
            "16",
            (
                "Bihac",
                "Bosanska Krupa",
                "Bosanski Petrovac",
                "Bosansko Grahovo",
                "Buzim",
                "Cazin",
                "Drvar",
                "Glamoc",
                "Kljuc",
                "Kupres",
                "Livno",
                "Sanski Most",
                "Tomislavgrad",
                "Velika Kladusa",
            ),
        ),
        (
            "17",
            (
                "Centar Sarajevo",
                "Foca",
                "Gorazde",
                "Hadzici",
                "Ilidza",
                "Ilijas",
                "Novo Sarajevo",
                "Pale",
                "Sarajevo Novi Grad",
                "Sarajevo Stari Grad",
                "Trnovo",
                "Vogosca",
            ),
        ),
        (
            "18",
            (
                "Banovici",
                "Celic",
                "Doboj-Istok",
                "Domaljevac-Samac",
                "Gracanica",
                "Gradacac",
                "Kalesija",
                "Kladanj",
                "Lukavac",
                "Odzak",
                "Orasje",
                "Sapna",
                "Srebrenik",
                "Teocak",
                "Tuzla",
                "Zivinice",
            ),
        ),
        (
            "19",
            (
                "Bugojno",
                "Breza",
                "Busovaca",
                "Doboj-Jug",
                "Dobretici",
                "Donji Vakuf",
                "Fojnica",
                "Gornji Vakuf",
                "Jajce",
                "Kakanj",
                "Kiseljak",
                "Kresevo",
                "Maglaj",
                "Novi Travnik",
                "Olovo",
                "Travnik",
                "Tesanj",
                "Usora",
                "Vares",
                "Visoko",
                "Vitez",
                "Zavidovici",
                "Zenica",
                "Zepce",
            ),
        ),
    )

    def ssn(self) -> str:
        """
        Generates a 13-digit Bosnia and Herzegovina SSN (JMB - Jedinstveni maticni broj).
        - https://mup.vladars.rs/lat/mup-servisi/jmb#jumptopost
        - https://sr.wikipedia.org/sr-el/Јединствени_матични_број_грађана

        Structure: DD MM YYY RR BBB K
        - DD: day of month
        - MM: month
        - YYY: last three digits of year
        - RR: registration area code (10-19 for Bosnia and Herzegovina)
        - BBB: personal number where 000-499 for males and 500-999 for females
        - K: control digit
        """
        birth_date = self.generator.date_of_birth(minimum_age=0, maximum_age=100)
        registration_area = self.random_element(self.registration_areas)[0]
        personal_number = self.random_int(min=0, max=999)

        while True:
            ssn_without_checksum = (
                f"{birth_date.day:02d}{birth_date.month:02d}{birth_date.year % 1000:03d}"
                f"{registration_area}{personal_number:03d}"
            )
            checksum = calculate_checksum(ssn_without_checksum)

            if checksum is not None:
                return f"{ssn_without_checksum}{checksum}"

            personal_number = (personal_number + 1) % 1000
