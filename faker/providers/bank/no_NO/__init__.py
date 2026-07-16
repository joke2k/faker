from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``no_NO`` locale."""

    bban_format = "###########"
    country_code = "NO"

    def bban(self) -> str:
        """Generate a valid BBAN with correct MOD11 check digit."""
        for _ in range(100):
            first_10 = self.numerify("##########")
            weights = (6, 7, 8, 9, 4, 5, 6, 7, 8, 9)
            check = sum(w * int(d) for w, d in zip(weights, first_10)) % 11
            if check != 10:
                return first_10 + str(check)
        return first_10 + "0"
