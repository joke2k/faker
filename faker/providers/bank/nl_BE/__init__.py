from .. import Provider as BankProvider

# Belgian bank codes (3-digit identifiers) known to be valid
# in the National Bank of Belgium registry.
_VALID_BANK_CODES = (
    "000",
    "001",
    "002",
    "003",
    "004",
    "005",
    "006",
    "007",
    "008",
    "009",
    "010",
    "011",
    "012",
    "013",
    "014",
    "015",
    "016",
    "017",
    "018",
    "019",
    "020",
    "021",
    "022",
    "023",
    "024",
    "025",
    "026",
    "027",
    "028",
    "029",
    "030",
    "031",
    "032",
    "033",
    "034",
    "035",
    "036",
    "037",
    "038",
    "039",
    "040",
    "041",
    "042",
    "043",
    "044",
    "045",
    "046",
    "047",
    "048",
    "049",
    "050",
    "051",
    "052",
    "053",
    "054",
    "055",
    "056",
    "057",
    "058",
    "059",
    "060",
    "061",
    "062",
    "063",
    "064",
    "065",
    "066",
    "067",
    "068",
    "069",
    "070",
    "071",
    "072",
    "073",
    "074",
    "075",
    "076",
    "077",
    "078",
    "079",
    "080",
    "081",
    "082",
    "083",
    "084",
    "085",
    "086",
    "087",
    "088",
    "089",
    "090",
    "091",
    "092",
    "093",
    "094",
    "095",
    "096",
    "097",
    "098",
    "099",
    "100",
    "101",
    "102",
    "103",
    "104",
    "105",
    "106",
    "107",
    "108",
    "109",
    "110",
    "111",
    "113",
    "114",
    "115",
    "116",
    "119",
    "120",
    "121",
    "122",
    "123",
    "124",
    "125",
    "126",
    "127",
    "129",
    "130",
    "131",
    "132",
    "133",
    "134",
    "137",
    "140",
    "141",
    "142",
    "143",
    "144",
    "145",
    "146",
    "147",
    "148",
    "149",
    "150",
    "171",
    "175",
    "176",
    "185",
    "189",
    "190",
    "191",
    "192",
    "193",
    "194",
    "195",
    "196",
    "624",
    "625",
    "630",
    "631",
    "634",
    "635",
    "636",
    "638",
    "640",
    "642",
    "643",
    "644",
    "645",
    "646",
    "647",
    "648",
    "649",
    "650",
    "651",
    "652",
    "653",
    "654",
    "657",
    "658",
    "725",
    "860",
    "890",
)


class Provider(BankProvider):
    """Implement bank provider for `nl_BE` locale.

    Information about the Belgian banks can be found on the website
    of the National Bank of Belgium:
    https://www.nbb.be/nl/betalingen-en-effecten/betalingsstandaarden/bankidentificatiecodes
    """

    bban_format = "############"
    country_code = "BE"

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

    def bban(self) -> str:
        """Generate a valid BBAN."""
        account_number = self._generate_account_number()
        check_digits = self._calculate_mod97(account_number)
        return f"{account_number}{check_digits}"

    def iban(self) -> str:
        """Generate a valid IBAN."""
        bban = self.bban()
        iban_check_digits = self._calculate_iban_check_digits(bban)
        return f"{self.country_code}{iban_check_digits}{bban}"

    def _generate_account_number(self) -> str:
        """Generate a random 10-digit account number."""
        return self.random_element(_VALID_BANK_CODES) + self.numerify("#######")

    def _calculate_mod97(self, account_number: str) -> str:
        """Calculate the mod 97 check digits for a given account number."""
        remainder = int(account_number) % 97
        return str(remainder).zfill(2) if remainder != 0 else "97"

    def _calculate_iban_check_digits(self, bban: str) -> str:
        """Calculate the IBAN check digits using mod 97 algorithm."""
        raw_iban = f"{bban}{self.country_code}00"
        numeric_iban = "".join(str(ord(char) - 55) if char.isalpha() else char for char in raw_iban)
        check_digits = 98 - (int(numeric_iban) % 97)
        return str(check_digits).zfill(2)
