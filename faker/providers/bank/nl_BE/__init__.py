from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``nl_BE`` locale.

    Information about the Belgian banks can be found on the website
    of the National Bank of Belgium:
    https://www.nbb.be/nl/betalingen-en-effecten/betalingsstandaarden/bankidentificatiecodes
    """

    bban_format = "############"
    country_code = "BE"

    def bban(self) -> str:
        """Generate a Basic Bank Account Number (BBAN).

        Belgian BBAN format: PPPP NNNN NNNN NN
        - PPPP: Bank code (4 digits)
        - NNNN NNNN NN: Account number with 2 national check digits (Mod 97-10)

        :sample:
        """
        # Generate 10 random digits (4 bank code + 6 account number)
        bban_without_check = self.numerify("##########")

        # Calculate national check digits using Mod 97-10 algorithm
        remainder = 0
        for digit in bban_without_check:
            remainder = (remainder * 10 + int(digit)) % 97
        check_digits = str((98 - remainder) % 97).zfill(2)

        return bban_without_check + check_digits

    banks = (
        "Argenta Spaarbank",
        "AXA Bank",
        "Belfius Bank",
        "BNP Paribas Fortis",
        "Bpost Bank",
        "Crelan",
        "Deutsche Bank AG",
        "ING België",
        "KBC Bank",
    )
    swift_bank_codes = (
        "ARSP",
        "AXAB",
        "BBRU",
        "BPOT",
        "DEUT",
        "GEBA",
        "GKCC",
        "KRED",
        "NICA",
    )
    swift_location_codes = (
        "BE",
        "B2",
        "99",
        "21",
        "91",
        "23",
        "3X",
        "75",
        "2X",
        "22",
        "88",
        "B1",
        "BX",
        "BB",
    )
    swift_branch_codes = [
        "203",
        "BTB",
        "CIC",
        "HCC",
        "IDJ",
        "IPC",
        "MDC",
        "RET",
        "VOD",
        "XXX",
    ]

    def bank(self) -> str:
        """Generate a bank name."""
        return self.random_element(self.banks)
