from typing import List

from .. import Provider as BaseProvider


class Provider(BaseProvider):
    INVALID_SSN_TYPE = "INVALID_SSN"
    SSN_TYPE = "SSN"
    ITIN_TYPE = "ITIN"
    EIN_TYPE = "EIN"

    def itin(self) -> str:
        """Generate a random United States Individual Taxpayer Identification Number (ITIN).

        An United States Individual Taxpayer Identification Number
        (ITIN) is a tax processing number issued by the Internal
        Revenue Service. It is a nine-digit number that always begins
        with the number 9 and has a range of 70-88 in the fourth and
        fifth digit. Effective April 12, 2011, the range was extended
        to include 900-70-0000 through 999-88-9999, 900-90-0000
        through 999-92-9999 and 900-94-0000 through 999-99-9999.
        https://www.irs.gov/individuals/international-taxpayers/general-itin-information
        """

        area = self.random_int(min=900, max=999)
        serial = self.random_int(min=0, max=9999)

        # The group number must be between 70 and 99 inclusively but not 89 or 93
        group: int = self.random_element([x for x in range(70, 100) if x not in [89, 93]])

        itin = f"{area:03d}-{group:02d}-{serial:04d}"
        return itin

    def ein(self) -> str:
        """Generate a random United States Employer Identification Number (EIN).

        An United States An Employer Identification Number (EIN) is
        also known as a Federal Tax Identification Number, and is
        used to identify a business entity. EINs follow a format of a
        two-digit prefix followed by a hyphen and a seven-digit sequence:
        ##-######

        https://www.irs.gov/businesses/small-businesses-self-employed/employer-id-numbers
        """

        # Only certain EIN Prefix values are assigned:
        #
        # https://www.irs.gov/businesses/small-businesses-self-employed/how-eins-are-assigned-and-valid-ein-prefixes

        ein_prefix_choices: List[str] = [
            "01",
            "02",
            "03",
            "04",
            "05",
            "06",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
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
            "47",
            "48",
            "50",
            "51",
            "52",
            "53",
            "54",
            "55",
            "56",
            "57",
            "58",
            "59",
            "60",
            "61",
            "62",
            "63",
            "64",
            "65",
            "66",
            "67",
            "68",
            "71",
            "72",
            "73",
            "74",
            "75",
            "76",
            "77",
            "80",
            "81",
            "82",
            "83",
            "84",
            "85",
            "86",
            "87",
            "88",
            "90",
            "91",
            "92",
            "93",
            "94",
            "95",
            "98",
            "99",
        ]

        ein_prefix: str = self.random_element(ein_prefix_choices)
        sequence = self.random_int(min=0, max=9999999)

        ein = f"{ein_prefix:s}-{sequence:07d}"
        return ein

    def invalid_ssn(self) -> str:
        """Generate a random invalid United States Social Security Identification Number (SSN).

        Invalid SSNs have the following characteristics:
        Cannot begin with the number 9
        Cannot begin with 666 in positions 1 - 3
        Cannot begin with 000 in positions 1 - 3
        Cannot contain 00 in positions 4 - 5
        Cannot contain 0000 in positions 6 - 9

        https://www.ssa.gov/kc/SSAFactSheet--IssuingSSNs.pdf

        Additionally, return an invalid SSN that is NOT a valid ITIN by excluding certain ITIN related "group" values
        """
        itin_group_numbers = [
            70,
            71,
            72,
            73,
            74,
            75,
            76,
            77,
            78,
            79,
            80,
            81,
            82,
            83,
            84,
            85,
            86,
            87,
            88,
            90,
            91,
            92,
            94,
            95,
            96,
            97,
            98,
            99,
        ]
        area = self.random_int(min=0, max=999)
        if area < 900 and area not in {666, 0}:
            random_group_or_serial = self.random_int(min=1, max=1000)
            if random_group_or_serial <= 500:
                group = 0
                serial = self.random_int(0, 9999)
            else:
                group = self.random_int(0, 99)
                serial = 0
        elif area in {666, 0}:
            group = self.random_int(0, 99)
            serial = self.random_int(0, 9999)
        else:
            group = self.random_element([x for x in range(0, 100) if x not in itin_group_numbers])
            serial = self.random_int(0, 9999)

        invalid_ssn = f"{area:03d}-{group:02d}-{serial:04d}"
        return invalid_ssn

    def ssn(self, taxpayer_identification_number_type: str = SSN_TYPE) -> str:
        """Generate a random United States Taxpayer Identification Number of the specified type.

        If no type is specified, a US SSN is returned.
        """

        if taxpayer_identification_number_type == self.ITIN_TYPE:
            return self.itin()
        elif taxpayer_identification_number_type == self.EIN_TYPE:
            return self.ein()
        elif taxpayer_identification_number_type == self.INVALID_SSN_TYPE:
            return self.invalid_ssn()
        elif taxpayer_identification_number_type == self.SSN_TYPE:

            # Certain numbers are invalid for United States Social Security
            # Numbers. The area (first 3 digits) cannot be 666 or 900-999.
            # The group number (middle digits) cannot be 00. The serial
            # (last 4 digits) cannot be 0000.

            area = self.random_int(min=1, max=899)
            if area == 666:
                area += 1
            group = self.random_int(1, 99)
            serial = self.random_int(1, 9999)

            ssn = f"{area:03d}-{group:02d}-{serial:04d}"
            return ssn

        else:
            raise ValueError(
                "taxpayer_identification_number_type must be one of 'SSN', 'EIN', 'ITIN'," " or 'INVALID_SSN'."
            )
