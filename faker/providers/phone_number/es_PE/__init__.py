from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    """
    Phone number provider for es_PE locale.

    Sources:
    - https://en.wikipedia.org/wiki/Telephone_numbers_in_Peru
    - https://www.mtc.gob.pe/comunicaciones/telefonia_fija.html
    Accessed: 2026-02-07
    """

    # Mobile numbers in Peru are 9 digits long and always start with 9.
    mobile_formats = (
        # Local format
        "9## ### ###",
        "9########",
        # International format
        "+51 9## ### ###",
    )

    # Landline numbers have a 1-digit area code for Lima/Callao (1)
    # and a 2-digit area code for other departments.
    # The total length is 9 digits including the area code.
    lima_landline_formats = (
        # Local format
        "(1) ###-####",
        "1#######",
        # International format
        "+51 1 ###-####",
    )

    # A selection of major provincial area codes.
    province_area_codes = (
        "41",  # Amazonas
        "43",  # Áncash
        "83",  # Apurímac
        "54",  # Arequipa
        "66",  # Ayacucho
        "76",  # Cajamarca
        "84",  # Cusco
        "62",  # Huánuco
        "56",  # Ica
        "64",  # Junín
        "44",  # La Libertad
        "74",  # Lambayeque
        "65",  # Loreto
        "73",  # Piura
        "51",  # Puno
        "52",  # Tacna
    )

    # Formats for provincial landlines.
    province_landline_formats = (
        # Local format
        "({}) ###-###",
        "{}######",
        # International format
        "+51 {} ###-###",
    )

    def mobile_number(self) -> str:
        """
        Returns a random 9-digit mobile phone number.
        """
        pattern = self.random_element(self.mobile_formats)
        return self.numerify(pattern)

    def landline_number(self) -> str:
        """
        Returns a random 9-digit landline phone number, which can be
        from Lima or another province.
        """
        # Give Lima a higher chance as it has the largest population.
        if self.generator.random.randint(1, 3) == 1:
            # Generate a Lima number
            pattern = self.random_element(self.lima_landline_formats)
            return self.numerify(pattern)
        else:
            # Generate a provincial number
            area_code = self.random_element(self.province_area_codes)
            pattern = self.random_element(self.province_landline_formats).format(area_code)
            return self.numerify(pattern)

    def phone_number(self) -> str:
        """
        Returns a random phone number, with a higher probability of it
        being a mobile number.
        """
        if self.generator.random.randint(1, 4) > 1:
            return self.mobile_number()
        return self.landline_number()
>>>>>>> origin/feature/add-es_PE-locale
