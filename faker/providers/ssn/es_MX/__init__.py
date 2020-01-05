"""
SSN provider for es_MX.

This module adds a provider for mexican SSN, along with Unique Population
Registry Code (CURP) and Federal Taxpayer Registry ID (RFC).
"""

import random
import string

from .. import Provider as BaseProvider

ALPHABET = string.ascii_uppercase
ALPHANUMERIC = string.digits + ALPHABET
VOWELS = "AEIOU"
CONSONANTS = [
    letter
    for letter in ALPHABET
    if letter not in VOWELS
]

# https://es.wikipedia.org/wiki/Plantilla:Abreviaciones_de_los_estados_de_M%C3%A9xico
STATES_RENAPO = [
    "AS",
    "BC",
    "BS",
    "CC",
    "CS",
    "CH",
    "DF",
    "CL",
    "CM",
    "DG",
    "GT",
    "GR",
    "HG",
    "JC",
    "MC",
    "MN",
    "MS",
    "NT",
    "NL",
    "OC",
    "PL",
    "QO",
    "QR",
    "SP",
    "SL",
    "SR",
    "TC",
    "TS",
    "TL",
    "VZ",
    "YN",
    "ZS",
    "NE",  # Foreign Born
]

FORBIDDEN_WORDS = {
    "BUEI": "BUEX",
    "BUEY": "BUEX",
    "CACA": "CACX",
    "CACO": "CACX",
    "CAGA": "CAGX",
    "CAGO": "CAGX",
    "CAKA": "CAKX",
    "CAKO": "CAKX",
    "COGE": "COGX",
    "COJA": "COJX",
    "COJE": "COJX",
    "COJI": "COJX",
    "COJO": "COJX",
    "CULO": "CULX",
    "FETO": "FETX",
    "GUEY": "GUEX",
    "JOTO": "JOTX",
    "KACA": "KACX",
    "KACO": "KACX",
    "KAGA": "KAGX",
    "KAGO": "KAGX",
    "KOGE": "KOGX",
    "KOJO": "KOJX",
    "KAKA": "KAKX",
    "KULO": "KULX",
    "MAME": "MAMX",
    "MAMO": "MAMX",
    "MEAR": "MEAX",
    "MEAS": "MEAX",
    "MEON": "MEOX",
    "MION": "MIOX",
    "MOCO": "MOCX",
    "MULA": "MULX",
    "PEDA": "PEDX",
    "PEDO": "PEDX",
    "PENE": "PENX",
    "PUTA": "PUTX",
    "PUTO": "PUTX",
    "QULO": "QULX",
    "RATA": "RATX",
    "RUIN": "RUIN",
}

CURP_CHARACTERS = "0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"


def _reduce_digits(number):
    """
    Sum of digits of a number until sum becomes single digit.

    Example:
        658 => 6 + 5 + 8 = 19 => 1 + 9 = 10 => 1
    """
    if number == 0:
        return 0
    if number % 9 == 0:
        return 9

    return number % 9


def ssn_checksum(digits):
    """
    Calculate the checksum for the mexican SSN (IMSS).
    """
    return -sum(
        _reduce_digits(n * (i % 2 + 1))
        for i, n in enumerate(digits)
    ) % 10


def curp_checksum(characters):
    """
    Calculate the checksum for the mexican CURP.
    """
    start = 18
    return -sum(
        (start - i) * CURP_CHARACTERS.index(n)
        for i, n in enumerate(characters)
    ) % 10


class Provider(BaseProvider):
    """
    A Faker provider for the Mexican SSN, RFC and CURP
    """
    ssn_formats = ("###########",)

    def ssn(self):
        """
        Mexican Social Security Number, as given by IMSS.

        :return: a random Mexican SSN
        """
        office = self.random_int(min=1, max=99)
        birth_year = self.random_int(min=0, max=99)
        start_year = self.random_int(min=0, max=99)
        serial = self.random_int(min=1, max=9999)

        num = "{:02d}{:02d}{:02d}{:04d}".format(
            office,
            start_year,
            birth_year,
            serial,
        )

        check = ssn_checksum(map(int, num))
        num += str(check)

        return num

    def curp(self):
        """
        See https://es.wikipedia.org/wiki/Clave_%C3%9Anica_de_Registro_de_Poblaci%C3%B3n.

        :return: a random Mexican CURP (Unique Population Registry Code)
        """
        birthday = self.generator.date_of_birth()

        first_surname = random.choice(ALPHABET) + random.choice(VOWELS)
        second_surname = random.choice(ALPHABET)
        given_name = random.choice(ALPHABET)
        name_initials = first_surname + second_surname + given_name

        birth_date = birthday.strftime("%y%m%d")
        gender = random.choice("HM")
        state = random.choice(STATES_RENAPO)
        first_surname_inside = random.choice(CONSONANTS)
        second_surname_inside = random.choice(CONSONANTS)
        given_name_inside = random.choice(ALPHABET)

        # This character is assigned to avoid duplicity
        # It's normally '0' for those born < 2000
        # and 'A' for those born >= 2000
        assigned_character = "0" if birthday.year < 2000 else "A"

        name_initials = FORBIDDEN_WORDS.get(name_initials, name_initials)

        random_curp = (
            name_initials +
            birth_date +
            gender +
            state +
            first_surname_inside +
            second_surname_inside +
            given_name_inside +
            assigned_character
        )

        random_curp += str(curp_checksum(random_curp))

        return random_curp

    def rfc(self, natural=True):
        """
        See https://es.wikipedia.org/wiki/Registro_Federal_de_Contribuyentes

        :param natural: Whether to return the RFC of a natural person.
            Otherwise return the RFC of a legal person.
        :type natural: bool
        :return: a random Mexican RFC
        """
        birthday = self.generator.date_of_birth()

        if natural:
            first_surname = random.choice(ALPHABET) + random.choice(VOWELS)
            second_surname = random.choice(ALPHABET)
            given_name = random.choice(ALPHABET)
            name_initials = first_surname + second_surname + given_name
        else:
            name_initials = (
                self.random_uppercase_letter() +
                self.random_uppercase_letter() +
                self.random_uppercase_letter()
            )

        birth_date = birthday.strftime("%y%m%d")
        disambiguation_code = (
            random.choice(ALPHANUMERIC) +
            random.choice(ALPHANUMERIC) +
            random.choice(ALPHANUMERIC)
        )

        random_rfc = (
            name_initials +
            birth_date +
            disambiguation_code
        )

        return random_rfc
