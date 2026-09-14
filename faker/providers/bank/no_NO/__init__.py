from .. import Provider as BankProvider

#: Weights applied to the first ten BBAN digits to derive the MOD11 check digit.
MOD11_WEIGHTS = (6, 7, 8, 9, 4, 5, 6, 7, 8, 9)


class Provider(BankProvider):
    """Implement bank provider for ``no_NO`` locale."""

    bban_format = "###########"
    country_code = "NO"

    def bban(self) -> str:
        """Generate a valid BBAN with correct MOD11 check digit."""
        while True:
            first_10 = self.numerify("##########")
            check = sum(w * int(d) for w, d in zip(MOD11_WEIGHTS, first_10)) % 11
            # A remainder of 10 has no single-digit representation, so that
            # draw is discarded and another one taken.
            if check != 10:
                return first_10 + str(check)
