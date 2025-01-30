from datetime import date
from string import ascii_uppercase
from typing import Optional

from faker.utils.checksums import luhn_checksum

from .. import Provider as BaseProvider


class Provider(BaseProvider):
    """
    A Faker provider for the German VAT ID and the pension insurance number

    Sources:

    - http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
    - https://de.wikipedia.org/wiki/Versicherungsnummer
    """

    vat_id_formats = ("DE#########",)

    def __letter_to_digit_string(self, letter: str) -> str:
        digit = ascii_uppercase.index(letter) + 1
        if len(str(digit)) == 2:
            return str(digit)
        return "0" + str(digit)

    def __get_rvnr_checkdigit(self, rvnr: str) -> str:
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

    def rvnr(self, birthdate: Optional[date] = None) -> str:
        """
        Pension insurance number (German: "Rentenversicherungsnummer", abbr. "RVNR")

        Source: https://de.wikipedia.org/wiki/Versicherungsnummer

        :return: A valid German pension insurance number
        """
        _birthdate = birthdate or self.generator.date_object()
        format: str = f"##{_birthdate.strftime('%d%m%y')}?##"
        rvnr: str = self.bothify(format, letters=ascii_uppercase)

        return rvnr + self.__get_rvnr_checkdigit(rvnr)

    def kvnr(self) -> str:
        """
        German health insurance number ("Krankenversichertennummer", abbr. "KVNR")

        Source: https://de.wikipedia.org/wiki/Krankenversichertennummer

        :return: a random health insurance number
        """

        letter_number: str = str(self.random_int(min=1, max=26))
        if len(letter_number) == 1:
            letter_number = "0" + letter_number

        first_part_format: str = letter_number + "########"
        first_part: str = self.numerify(first_part_format)
        first_checkdigit: int = luhn_checksum(int(first_part[::-1]))
        second_part_format: str = "#########"
        second_part: str = self.numerify(second_part_format)

        kvnr: str = first_part + str(first_checkdigit) + second_part
        kvnr_checkdigit: int = luhn_checksum(int(kvnr[::-1]))
        kvnr = kvnr + str(kvnr_checkdigit)

        letter: str = ascii_uppercase[int(letter_number) - 1]
        kvnr = letter + kvnr[2:]

        return kvnr
