import datetime

from .. import Provider as SsnProvider


class Provider(SsnProvider):
    def ssn(self, min_age: int = 0, max_age: int = 105) -> str:
        """
        Returns 11 character Latvian personal identity code (Personas kods).
        This function assigns random age to person.

        Personal code consists of eleven characters of the form DDMMYYCZZZQ, where
        DDMMYY is the date of birth, C the century sign, ZZZ the individual
        number and Q the control character (checksum). The number for the
        century is either 0 (1800–1899), 1 (1900–1999), or 2 (2000–2099).
        """

        def _checksum(ssn_without_checksum):
            weights = [1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            weighted_sum = sum(int(digit) * weight for digit, weight in zip(ssn_without_checksum, weights))
            reminder = (1 - weighted_sum) % 11
            if reminder == 10:
                return 0
            elif reminder < -1:
                return reminder + 11
            return reminder

        age = datetime.timedelta(days=self.generator.random.randrange(min_age * 365, max_age * 365))
        birthday = datetime.date.today() - age
        ssn_date = "%02d%02d%s" % (
            birthday.day,
            birthday.month,
            str(birthday.year)[-2:],
        )
        century = self._get_century_code(birthday.year)  # Century
        suffix = self.generator.random.randrange(111, 999)
        checksum = _checksum(f"{ssn_date}{century:01d}{suffix:03d}")
        ssn = f"{ssn_date}-{century:01d}{suffix:03d}{checksum:01d}"
        return ssn

    @staticmethod
    def _get_century_code(year: int) -> int:
        """Returns the century code for a given year"""
        if 2000 <= year < 3000:
            code = 2
        elif 1900 <= year < 2000:
            code = 1
        elif 1800 <= year < 1900:
            code = 0
        else:
            raise ValueError("SSN do not support people born before the year 1800 or after the year 2999")
        return code

    """
    A Faker provider for the Latvian VAT IDs
    """

    vat_id_formats = ("LV###########",)

    def vat_id(self) -> str:
        """
        http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
        :return: a random Latvian VAT ID
        """

        return self.bothify(self.random_element(self.vat_id_formats))
