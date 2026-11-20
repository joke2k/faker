from collections import OrderedDict
from typing import Optional

from .. import Provider as BaseProvider

_RIF_TYPE_VALUES = {
    "V": 4,
    "E": 8,
    "J": 12,
    "P": 16,
    "G": 20,
}
_RIF_WEIGHTS = (3, 2, 7, 6, 5, 4, 3, 2)
_RIF_CHECK_DIGITS = "00987654321"


def rif_check_digit(letter: str, digits: str) -> str:
    """
    Calculate the check digit of a Venezuelan RIF.

    :example: rif_check_digit("J", "40123456") == "9"
    """
    if letter not in _RIF_TYPE_VALUES:
        raise ValueError(f"Invalid RIF type: {letter}")
    if len(digits) != 8 or any(digit not in "0123456789" for digit in digits):
        raise ValueError("RIF digits must contain exactly 8 numeric digits")

    value = _RIF_TYPE_VALUES[letter] + sum(weight * int(digit) for weight, digit in zip(_RIF_WEIGHTS, digits))
    return _RIF_CHECK_DIGITS[value % 11]


class Provider(BaseProvider):
    """
    A Faker provider for Venezuelan identity card numbers and RIFs.

    Sources:

    - https://es.wikipedia.org/wiki/C%C3%A9dula_de_identidad_(Venezuela)
    - https://github.com/arthurdejong/python-stdnum/blob/master/stdnum/ve/rif.py
    """

    minimum_cedula_v: int = 1_000_000
    maximum_cedula_v: int = 35_999_999
    minimum_cedula_e: int = 80_000_000
    maximum_cedula_e: int = 99_999_999
    cedula_types = OrderedDict([("V", 0.9), ("E", 0.1)])
    rif_types = ("V", "E", "J", "P", "G")

    def cedula(self, cedula_type: Optional[str] = None) -> str:
        """
        Generate a Venezuelan identity card number.

        :param cedula_type: The type of identity card, either 'V' (Venezuelan) or 'E' (foreigner).
        :example: 'V-12345678'
        """
        if cedula_type is None:
            cedula_type = self.random_element(self.cedula_types)
        if cedula_type == "V":
            number = self.random_int(self.minimum_cedula_v, self.maximum_cedula_v)
        elif cedula_type == "E":
            number = self.random_int(self.minimum_cedula_e, self.maximum_cedula_e)
        else:
            raise ValueError(f"Invalid identity card type: {cedula_type}")
        return f"{cedula_type}-{number}"

    def ssn(self) -> str:
        """
        Generate a Venezuelan identity card number.

        :example: 'V-12345678'
        """
        return self.cedula()

    def rif(self, rif_type: Optional[str] = None) -> str:
        """
        Generate a Venezuelan RIF with its check digit.

        :param rif_type: The RIF type, one of 'V', 'E', 'J', 'P', or 'G'.
        :example: 'J-40123456-9'
        """
        if rif_type is None:
            rif_type = self.random_element(self.rif_types)
        if rif_type not in self.rif_types:
            raise ValueError(f"Invalid RIF type: {rif_type}")

        if rif_type in ("V", "E"):
            digits = self.cedula(rif_type).split("-", 1)[1].zfill(8)
        else:
            digits = str(self.random_int(0, 99_999_999)).zfill(8)

        check_digit = rif_check_digit(rif_type, digits)
        return f"{rif_type}-{digits}-{check_digit}"

    def vat_id(self) -> str:
        """
        Generate a Venezuelan company RIF.

        :example: 'J-40123456-9'
        """
        return self.rif("J")
