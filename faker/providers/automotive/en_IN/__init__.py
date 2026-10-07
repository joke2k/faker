import string
from typing import Tuple

from .. import Provider as AutomotiveProvider


class Provider(AutomotiveProvider):
    """Implement automotive provider for ``en_IN`` locale.

    Vehicle registration in India is governed by the Ministry of Road Transport
    and Highways (MoRTH) under Rule 50 and 51 of the Central Motor Vehicles Rules
    (CMVR), 1989, as well as the Central Motor Vehicles (Twentieth Amendment) Rules,
    2021 for the Bharat Series (BH series).

    Sources:

    - https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_India
    - Central Motor Vehicles Rules, 1989 (Rules 50 & 51)
    - Ministry of Road Transport and Highways (MoRTH) Bharat Series notification (G.S.R. 594(E), 2021)
    """

    state_codes: Tuple[str, ...] = (
        # 28 States
        "AP",  # Andhra Pradesh
        "AR",  # Arunachal Pradesh
        "AS",  # Assam
        "BR",  # Bihar
        "CG",  # Chhattisgarh
        "GA",  # Goa
        "GJ",  # Gujarat
        "HR",  # Haryana
        "HP",  # Himachal Pradesh
        "JH",  # Jharkhand
        "KA",  # Karnataka
        "KL",  # Kerala
        "MP",  # Madhya Pradesh
        "MH",  # Maharashtra
        "MN",  # Manipur
        "ML",  # Meghalaya
        "MZ",  # Mizoram
        "NL",  # Nagaland
        "OD",  # Odisha
        "PB",  # Punjab
        "RJ",  # Rajasthan
        "SK",  # Sikkim
        "TN",  # Tamil Nadu
        "TS",  # Telangana
        "TR",  # Tripura
        "UP",  # Uttar Pradesh
        "UK",  # Uttarakhand
        "WB",  # West Bengal
        # 8 Union Territories
        "AN",  # Andaman and Nicobar Islands
        "CH",  # Chandigarh
        "DH",  # Dadra and Nagar Haveli and Daman and Diu
        "DL",  # Delhi
        "JK",  # Jammu and Kashmir
        "LA",  # Ladakh
        "LD",  # Lakshadweep
        "PY",  # Puducherry
    )

    # In BH-series registration, the letters 'I' and 'O' are omitted to avoid confusion with digits 1 and 0.
    bh_series_letters: str = "".join(c for c in string.ascii_uppercase if c not in ("I", "O"))

    standard_license_formats: Tuple[str, ...] = (
        "{{state_code}} {{rto_code}} {{series_code}} {{registration_number}}",
        "{{state_code}} {{rto_code}} {{single_series_code}} {{registration_number}}",
        "{{state_code}} {{rto_code}} {{registration_number}}",
    )

    license_formats: Tuple[str, ...] = standard_license_formats

    def state_code(self) -> str:
        """Generate a 2-letter Indian state or union territory code."""
        return self.random_element(self.state_codes)

    def rto_code(self) -> str:
        """Generate a 2-digit RTO district code (01-99)."""
        return f"{self.random_int(1, 99):02d}"

    def series_code(self) -> str:
        """Generate a 2-letter series code."""
        return self.lexify("??", letters=string.ascii_uppercase)

    def single_series_code(self) -> str:
        """Generate a 1-letter series code."""
        return self.lexify("?", letters=string.ascii_uppercase)

    def registration_number(self) -> str:
        """Generate a 4-digit unique registration number (0001-9999)."""
        return f"{self.random_int(1, 9999):04d}"

    def standard_license_plate(self) -> str:
        """Generate a standard Indian vehicle registration plate.

        Format: SS DD XX ####
        - SS: 2-letter State/UT code
        - DD: 2-digit RTO district code
        - XX: Optional series code (1-2 letters)
        - ####: 4-digit unique number (0001-9999)

        :example: 'MH 12 AB 1234'
        """
        pattern: str = self.random_element(self.standard_license_formats)
        return self.generator.parse(pattern)

    def bharat_series_license_plate(self) -> str:
        """Generate a Bharat Series (BH series) vehicle license plate.

        Format: YY BH #### XX
        - YY: 2-digit registration year
        - BH: Literal 'BH'
        - ####: 4-digit unique number (0001-9999)
        - XX: 2 letters (excluding 'I' and 'O')

        :example: '22 BH 1234 AA'
        """
        year = f"{self.random_int(21, 26):02d}"
        number = self.registration_number()
        series = self.lexify("??", letters=self.bh_series_letters)
        return f"{year} BH {number} {series}"

    def license_plate(self) -> str:
        """Generate an Indian vehicle license plate.

        Generates either a standard state-registered plate (~90% probability)
        or a Bharat Series (BH) plate (~10% probability).

        :example: 'MH 12 AB 1234'
        :example: '22 BH 1234 AA'
        """
        if self.random_int(1, 10) == 1:
            return self.bharat_series_license_plate()
        return self.standard_license_plate()
