# coding=utf-8
from .. import Provider as CompanyProvider


def regon_checksum(digits):
    """
    Calculates and returns a control digit for given list of digits basing on REGON standard.
    """
    weights_for_check_digit = [8, 9, 2, 3, 4, 5, 6, 7]
    check_digit = 0

    for i in range(0, 8):
        check_digit += weights_for_check_digit[i] * digits[i]

    check_digit %= 11

    if check_digit == 10:
        check_digit = 0

    return check_digit


class Provider(CompanyProvider):

    @classmethod
    def regon(cls):
        """
        Returns 9 character Polish National Business Registry Number,
        Polish: Rejestr Gospodarki Narodowej - REGON.

        https://pl.wikipedia.org/wiki/REGON
        """
        voivodeship_number = cls.random_int(0, 49) * 2 + 1
        regon_digits = [int(voivodeship_number / 10), voivodeship_number % 10]

        for _ in range(6):
            regon_digits.append(cls.random_digit())

        regon_digits.append(regon_checksum(regon_digits))

        return ''.join(str(digit) for digit in regon_digits)
