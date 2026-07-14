from .. import Provider as SsnProvider


class Provider(SsnProvider):
    """SSN provider for mk_MK locale (Macedonian).

    The Macedonian EMBG (Единствен матичен број на граѓанинот) is a 13-digit
    unique citizen identification number with the format:

        DDMMYYYRRGBBK

    where:
        DD    - day of birth (01-31)
        MM    - month of birth (01-12)
        YYY   - last 3 digits of year of birth
        RR    - region code (North Macedonia uses 41)
        G     - gender and century digit (0-4 female, 5-9 male; odd=1900s, even=2000s)
        BB    - sequence number within region/gender/day (00-99)
        K     - checksum digit (MOD 11)
    """

    # North Macedonia region code
    REGION_CODE = "41"

    @staticmethod
    def _checksum(digits: list) -> int:
        weights = [7, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
        total = sum(w * d for w, d in zip(weights, digits))
        remainder = 11 - (total % 11)
        if remainder in (10, 11):
            return 0
        return remainder

    def ssn(self) -> str:
        """Generate a valid Macedonian EMBG number."""
        rng = self.generator.random

        # Random birth date between 1950 and 2005
        birth_year = rng.randint(1950, 2005)
        birth_month = rng.randint(1, 12)
        # Simplified: use day range 1-28 to avoid invalid dates
        birth_day = rng.randint(1, 28)

        dd = f"{birth_day:02d}"
        mm = f"{birth_month:02d}"
        yyy = f"{birth_year % 1000:03d}"

        rr = self.REGION_CODE

        # Gender: 0-4 female (born 1900s: odd, 2000s: even), 5-9 male
        is_male = rng.choice([True, False])
        if is_male:
            g = rng.randint(5, 9)
        else:
            g = rng.randint(0, 4)

        bb = f"{rng.randint(0, 99):02d}"

        digits = [int(c) for c in dd + mm + yyy + rr + str(g) + bb]
        k = self._checksum(digits)

        return dd + mm + yyy + rr + str(g) + bb + str(k)
