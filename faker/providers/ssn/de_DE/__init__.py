from datetime import date
from string import ascii_uppercase
from typing import Optional

from .. import Provider as BaseProvider


class Provider(BaseProvider):
    """
    A Faker provider for the German VAT ID and the pension insurance number
    
    Sources:
    
    - http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
    - https://de.wikipedia.org/wiki/Versicherungsnummer
    """

    vat_id_formats = ("DE#########",)

    def __letter_to_digit_string(self, letter) -> str:
        digit = ascii_uppercase.index(letter) + 1
        if len(str(digit)) == 2:
            return str(digit)
        return "0" + str(digit)

    def __get_rvnr_checkdigit(self, rvnr) -> str:
        # replace the letter at index 8 with its corresponding number
        letter = rvnr[8]
        rvnr = rvnr[:8] + self.__letter_to_digit_string(letter) + rvnr[9:]

        # calculate the product of each digit with the corresponding factor
        factors = [2, 1, 2, 5, 7, 1, 2, 1, 2, 1, 2, 1]
        products = []
        for index, digit in enumerate(rvnr):
            products.append(int(digit) * factors[index])

        # calculate the digit sum for each product
        digit_sums = []
        for product in products:
            digit_sum = 0
            while product:
                digit_sum += product % 10
                product = product // 10
            digit_sums.append(digit_sum)

        # get the check digit by summing up the digit sums and calculating the modulo of 10
        return str(sum(digit_sums) % 10)

    def vat_id(self) -> str:
        """
        http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
        
        :return: A random German VAT ID
        """

        return self.bothify(self.random_element(self.vat_id_formats))

    def rvnr(self, birthdate: Optional[date] = None):
        """
        Pension insurance number (German: "Rentenversicherungsnummer", abbr. "RVNR")
        
        Source: https://de.wikipedia.org/wiki/Versicherungsnummer
        
        :return: A valid German pension insurance number
        """

        if not birthdate:
            birthdate: date = self.generator.date_object()
        format: str = f"##{birthdate.strftime('%d%m%y')}?##"
        rvnr: str = self.bothify(format, letters=ascii_uppercase)

        return rvnr + self.__get_rvnr_checkdigit(rvnr)
