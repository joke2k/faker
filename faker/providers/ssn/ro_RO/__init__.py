from .. import Provider as BaseProvider


def ssn_checksum(number: str) -> int:
    """
    Calculate the checksum for the romanian SSN (CNP).
    """
    weights = (2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9)
    check = sum(w * int(n) for w, n in zip(weights, number)) % 11
    return 1 if check == 10 else check


def vat_checksum(number: str) -> int:
    """
    Calculate the check digit for romanian VAT numbers.
    """
    weights = (7, 5, 3, 2, 1, 7, 5, 3, 2)
    number = (9 - len(number)) * "0" + number
    check = 10 * sum(w * int(n) for w, n in zip(weights, number))
    return check % 11 % 10


class Provider(BaseProvider):
    """
    A Faker provider for the Romanian VAT IDs
    """

    vat_id_formats = (
        "RO1########",
        "RO2########",
        "RO3########",
        "RO4########",
        "RO5########",
        "RO6########",
        "RO7########",
        "RO8########",
        "RO9########",
        "1########",
        "2########",
        "3########",
        "4########",
        "5########",
        "6########",
        "7########",
        "8########",
        "9########",
    )

    def vat_id(self) -> str:
        """
        https://ro.wikipedia.org/wiki/Cod_de_identificare_fiscal%C4%83
        :return: A random Romanian VAT ID
        """
        vat = self.bothify(self.random_element(self.vat_id_formats))
        coutry = ""
        if vat.startswith("RO"):
            coutry = "RO"
            vat = vat[2:]
        check = vat_checksum(vat)
        vat += str(check)
        return coutry + vat

    ssn_formats = ("#############",)

    def ssn(self) -> str:
        """
        Romanian Social Security Number.

        :return: a random Romanian SSN
        """
        gender = self.random_int(min=1, max=8)
        year = self.random_int(min=0, max=99)
        month = self.random_int(min=1, max=12)
        day = self.random_int(min=1, max=31)
        county = int(
            self.random_element(
                [
                    "1",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                    "10",
                    "11",
                    "12",
                    "13",
                    "14",
                    "15",
                    "16",
                    "17",
                    "18",
                    "19",
                    "20",
                    "21",
                    "22",
                    "23",
                    "24",
                    "25",
                    "26",
                    "27",
                    "28",
                    "29",
                    "30",
                    "31",
                    "32",
                    "33",
                    "34",
                    "35",
                    "36",
                    "37",
                    "38",
                    "39",
                    "40",
                    "41",
                    "42",
                    "43",
                    "44",
                    "45",
                    "46",
                    "51",
                    "52",
                ]
            )
        )
        serial = self.random_int(min=1, max=999)

        num = f"{gender:01d}{year:02d}{month:02d}{day:02d}{county:02d}{serial:03d}"

        check = ssn_checksum(num)
        num += str(check)
        return num
