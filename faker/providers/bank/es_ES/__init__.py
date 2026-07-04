from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``es_ES`` locale."""

    country_code = "ES"
    # entity (4) + office (4) + two control digits (2) + account number (10)
    bban_format = "####################"

    # Weights used to compute the two CCC (Código Cuenta Cliente) control digits.
    _control_digit_weights = (1, 2, 4, 8, 5, 10, 9, 7, 3, 6)

    def bban(self) -> str:
        """Generate a BBAN with valid Spanish CCC control digits.

        The two control digits inside the BBAN validate the entity/office code
        and the account number respectively, so that the generated IBAN passes
        country-level (not just ISO 13616 mod-97) validation.
        """
        entity_and_office = self.numerify("########")
        account_number = self.numerify("##########")
        # The first control digit protects the entity/office code, padded to ten
        # digits with two leading zeros; the second protects the account number.
        first_digit = self._control_digit(f"00{entity_and_office}")
        second_digit = self._control_digit(account_number)
        return f"{entity_and_office}{first_digit}{second_digit}{account_number}"

    def _control_digit(self, digits: str) -> int:
        """Compute a single CCC control digit for a ten-digit string."""
        total = sum(int(digit) * weight for digit, weight in zip(digits, self._control_digit_weights))
        control = 11 - (total % 11)
        if control == 10:
            return 1
        if control == 11:
            return 0
        return control
