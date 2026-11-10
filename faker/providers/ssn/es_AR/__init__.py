from .. import ElementsType
from .. import Provider as BaseProvider


def cuit_check_digit(digits: str) -> int:
    """
    Calculate the check digit of a CUIT or CUIL from its first 10 digits.

    Each digit is multiplied by (5, 4, 3, 2, 7, 6, 5, 4, 3, 2), the products are added,
    and the check digit is 11 minus the sum MOD 11, with 11 becoming 0.
    A result of 10 means the number has no valid check digit with that prefix.
    """
    weights = (5, 4, 3, 2, 7, 6, 5, 4, 3, 2)
    total = sum(int(digit) * weight for digit, weight in zip(digits, weights))
    return (11 - total % 11) % 11


def cuit_with_check_digit(prefix: str, number: int, fallback_prefix: str) -> str:
    """
    Build a formatted CUIT or CUIL from a type prefix and an 8-digit number.

    When the prefix gives a check digit of 10, the fallback prefix is used instead,
    which turns 20 and 27 into 23 and 30 into 33.
    """
    body = f"{number:08d}"
    check = cuit_check_digit(prefix + body)
    if check == 10:
        prefix = fallback_prefix
        check = cuit_check_digit(prefix + body)
    return f"{prefix}-{body}-{check}"


class Provider(BaseProvider):
    """
    A Faker provider for Argentine identity numbers: DNI, CUIL and CUIT.

    Sources:

    - https://es.wikipedia.org/wiki/Clave_%C3%9Anica_de_Identificaci%C3%B3n_Tributaria - Prefixes and
      check digit calculation, last checked 2026-10-13
    """

    minimum_dni = 1000000
    maximum_dni = 59999999
    minimum_company_number = 50000000
    maximum_company_number = 79999999
    person_prefixes: ElementsType[str] = ("20", "27")

    def dni(self) -> str:
        """
        :return: a random DNI (Documento Nacional de Identidad) number
        :example: '34567890'
        """
        return str(self.random_int(self.minimum_dni, self.maximum_dni))

    def cuil(self) -> str:
        """
        :return: a random CUIL (Código Único de Identificación Laboral) of a person
        :example: '20-34567890-6'
        """
        number = self.random_int(self.minimum_dni, self.maximum_dni)
        return cuit_with_check_digit(self.random_element(self.person_prefixes), number, "23")

    def company_cuit(self) -> str:
        """
        :return: a random CUIT (Clave Única de Identificación Tributaria) of a company
        :example: '30-71234567-1'
        """
        number = self.random_int(self.minimum_company_number, self.maximum_company_number)
        return cuit_with_check_digit("30", number, "33")

    def cuit(self) -> str:
        """
        :return: a random CUIT of a person or a company. A person's CUIT is the same number as their CUIL.
        :example: '20-34567890-6'
        """
        return self.random_element((self.cuil, self.company_cuit))()

    def ssn(self) -> str:
        return self.cuil()

    def vat_id(self) -> str:
        return self.cuit()
