from .. import Provider as SsnProvider


def checksum(digits: str) -> int:
    """
    Calculates the check digit of a South Korean resident registration number from its first 12 digits.
    """
    weights = (2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5)
    return (11 - sum(int(digit) * weight for digit, weight in zip(digits, weights)) % 11) % 10


class Provider(SsnProvider):
    def ssn(self) -> str:
        """
        Returns a South Korean resident registration number (주민등록번호) of the form YYMMDD-SRRNNNC.

        YYMMDD is the date of birth, S the sex and century digit (1 or 2 for 1900-1999, 3 or 4 for 2000-2099),
        RR the region code, NNN the serial number and C the check digit.

        https://en.wikipedia.org/wiki/Resident_registration_number
        """
        birth_date = self.generator.date_of_birth()
        sex_and_century = self.random_element((1, 2) if birth_date.year < 2000 else (3, 4))
        region = self.random_int(0, 95)
        serial = self.random_int(0, 999)

        digits = f"{birth_date:%y%m%d}{sex_and_century}{region:02d}{serial:03d}"

        return f"{digits[:6]}-{digits[6:]}{checksum(digits)}"
