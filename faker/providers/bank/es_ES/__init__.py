from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``es_ES`` locale."""

    bban_format = "####################"
    country_code = "ES"

    @staticmethod
    def _ccc_control_digit(number: str) -> str:
        # Spanish CCC control digit (weights 2**i mod 11).
        check = sum(int(n) * 2**i for i, n in enumerate(number)) % 11
        return str(check if check < 2 else 11 - check)

    def bban(self) -> str:
        # Spanish CCC: bank (4) + branch (4) + 2 control digits + account (10).
        # The control digits are computed, not random, so the BBAN passes
        # country-level validation (ISO 13616 alone does not cover them).
        bank = self.numerify("####")
        branch = self.numerify("####")
        account = self.numerify("##########")
        control = self._ccc_control_digit("00" + bank + branch) + self._ccc_control_digit(account)
        return bank + branch + control + account
