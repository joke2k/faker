import operator

from collections import OrderedDict

from .. import Provider as BaseProvider


def nit_check_digit(nit: str) -> str:
    """
    Calculate the check digit of a NIT.

    The check digit is calculated by multiplying the reversed digits of a NIT
    by (3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71), respectively,
    adding the results and applying MOD 11. If the result is greater than or equal
    to 2, the check digit is 11 minus the result. Otherwise, the check digit is the
    result.
    """
    reversed_nit = nit[::-1]
    digits = (int(digit) for digit in reversed_nit)
    multipliers = (3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71)
    value = sum(map(operator.mul, digits, multipliers)) % 11
    if value >= 2:
        value = 11 - value
    return str(value)


class Provider(BaseProvider):
    nuip_formats = OrderedDict(
        [
            ("10########", 0.25),
            ("11########", 0.25),
            ("12########", 0.1),
            ("%!######", 0.4),
        ]
    )

    legal_person_nit_formats = [
        "8########",
        "9########",
    ]

    def nuip(self) -> str:
        """
        https://es.wikipedia.org/wiki/C%C3%A9dula_de_Ciudadan%C3%ADa_(Colombia)
        :example: '1095312769'
        """
        return self.numerify(self.random_element(self.nuip_formats))

    natural_person_nit = nuip

    def natural_person_nit_with_check_digit(self) -> str:
        """
        :example: '1095312769-0'
        """
        nit = self.natural_person_nit()
        check_digit = nit_check_digit(nit)
        return f"{nit}-{check_digit}"

    def legal_person_nit(self) -> str:
        """
        https://es.wikipedia.org/wiki/N%C3%BAmero_de_Identificaci%C3%B3n_Tributaria
        :example: '967807269'
        """
        return self.numerify(self.random_element(self.legal_person_nit_formats))

    def legal_person_nit_with_check_digit(self) -> str:
        """
        :example: '967807269-7'
        """
        nit = self.legal_person_nit()
        check_digit = nit_check_digit(nit)
        return f"{nit}-{check_digit}"
