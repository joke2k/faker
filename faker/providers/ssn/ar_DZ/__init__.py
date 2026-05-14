from .. import Provider as SsnProvider


class Provider(SsnProvider):
    """
    Sources:

    - https://fr.wikipedia.org/wiki/Num%C3%A9ro_d%27identification_national_(Alg%C3%A9rie)
    - https://github.com/itshakim213/dz-nin-checker
    """

    def _control_key(self, base: str) -> str:
        """Compute the 2-digit control key via modified Luhn over 16 digits."""
        total, alternate = 0, False
        for i in range(len(base) - 1, -1, -1):
            d = int(base[i]) * (2 if alternate else 1)
            total += d - 9 if d > 9 else d
            alternate = not alternate
        remainder = total % 10
        return f"{(0 if remainder == 0 else 10 - remainder):02d}"

    def ssn(self) -> str:
        """Generate an Algerian National Identification Number (NIN).

        Structure (18 digits):

        - 1 digit  – nationality: ``1`` = Algerian, ``2`` = dual nationality
        - 1 digit  – sex: ``0`` = male, ``1`` = female
        - 3 digits – last three digits of the birth-registration year
        - 4 digits – commune code (wilaya 01–58 + commune 01–20)
        - 5 digits – birth-certificate act number
        - 2 digits – annual register serial number
        - 2 digits – control key (modified Luhn)
        """
        nationality = self.random_element(("1", "2"))
        sex = self.random_element(("0", "1"))
        year_code = f"{self.random_int(min=1950, max=2006) % 1000:03d}"
        wilaya = self.random_int(min=1, max=58)
        commune_code = f"{wilaya:02d}{self.random_int(min=1, max=20):02d}"
        act_code = f"{self.random_int(min=1, max=99999):05d}"
        register_code = f"{self.random_int(min=1, max=99):02d}"
        base = nationality + sex + year_code + commune_code + act_code + register_code
        return base + self._control_key(base)
