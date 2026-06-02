from datetime import date
from typing import List, Optional

from .. import Provider as BaseProvider


class Provider(BaseProvider):
    """
    A Faker provider for the Austrian VAT IDs
    """

    vat_id_formats = ("ATU########",)

    def vat_id(self) -> str:
        """
        http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
        :return: a random Austrian VAT ID
        """

        return self.bothify(self.random_element(self.vat_id_formats))

    def __get_check_digit(self, ssn_without_checkdigit: str) -> int:
        factors: List[int] = [3, 7, 9, 5, 8, 4, 2, 1, 6]
        ssn_numbers: List[int] = [int(char) for char in ssn_without_checkdigit]

        sum: int = 0
        for index, factor in enumerate(factors):
            sum += ssn_numbers[index] * factor

        check_digit = sum % 11

        return check_digit

    def ssn(self, birthdate: Optional[date] = None) -> str:
        """
        Source: https://de.wikipedia.org/wiki/Sozialversicherungsnummer#Berechnung
        :return: a random valid Austrian social security number
        """
        _birthdate = birthdate or self.generator.date_object()
        format: str = f"%##{_birthdate:%d%m%y}"
        ssn: str = self.numerify(format)
        check_digit: int = self.__get_check_digit(ssn)

        while check_digit > 9:
            ssn = self.numerify(format)
            check_digit = self.__get_check_digit(ssn)

        return ssn[:3] + str(self.__get_check_digit(ssn)) + ssn[3:]
