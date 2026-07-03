from .. import Provider as AutomotiveProvider


class Provider(AutomotiveProvider):
    """Implement automotive provider for the ``en_IN`` locale.

    Sources:

    - https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_India
    """

    # State and union territory codes forming the first block of a registration mark.
    license_plate_state_codes = (
        "AN",  # Andaman and Nicobar Islands
        "AP",  # Andhra Pradesh
        "AR",  # Arunachal Pradesh
        "AS",  # Assam
        "BR",  # Bihar
        "CG",  # Chhattisgarh
        "CH",  # Chandigarh
        "DL",  # Delhi
        "DN",  # Dadra and Nagar Haveli and Daman and Diu
        "GA",  # Goa
        "GJ",  # Gujarat
        "HP",  # Himachal Pradesh
        "HR",  # Haryana
        "JH",  # Jharkhand
        "JK",  # Jammu and Kashmir
        "KA",  # Karnataka
        "KL",  # Kerala
        "LA",  # Ladakh
        "LD",  # Lakshadweep
        "MH",  # Maharashtra
        "ML",  # Meghalaya
        "MN",  # Manipur
        "MP",  # Madhya Pradesh
        "MZ",  # Mizoram
        "NL",  # Nagaland
        "OD",  # Odisha
        "PB",  # Punjab
        "PY",  # Puducherry
        "RJ",  # Rajasthan
        "SK",  # Sikkim
        "TN",  # Tamil Nadu
        "TR",  # Tripura
        "TS",  # Telangana
        "UK",  # Uttarakhand
        "UP",  # Uttar Pradesh
        "WB",  # West Bengal
    )

    # Series letters exclude I and O to avoid confusion with the digits 1 and 0.
    license_plate_series_letters = "ABCDEFGHJKLMNPQRSTUVWXYZ"

    license_plate_formats = (
        # Standard format, e.g. "MH 12 AB 1234".
        "{{plate_state}} {{plate_rto}} {{plate_series}} {{plate_number}}",
        # Bharat (BH) series, introduced in 2021, e.g. "22 BH 1234 AB".
        "{{plate_bh_year}} BH {{plate_number}} {{plate_series_bh}}",
    )

    def license_plate(self) -> str:
        """Generate a license plate."""
        pattern: str = self.random_element(self.license_plate_formats)
        return self.generator.parse(pattern)

    def plate_state(self) -> str:
        """Generate a state or union territory code."""
        return self.random_element(self.license_plate_state_codes)

    def plate_rto(self) -> str:
        """Generate a two-digit RTO (registering authority) code."""
        return f"{self.random_int(1, 99):02d}"

    def _series(self, length: int) -> str:
        return "".join(self.random_element(self.license_plate_series_letters) for _ in range(length))

    def plate_series(self) -> str:
        """Generate a one to three letter series code."""
        return self._series(self.random_int(1, 3))

    def plate_series_bh(self) -> str:
        """Generate a two-letter series code for the BH series."""
        return self._series(2)

    def plate_number(self) -> str:
        """Generate a four-digit vehicle number."""
        return f"{self.random_int(1, 9999):04d}"

    def plate_bh_year(self) -> str:
        """Generate a two-digit registration year for the BH series."""
        return f"{self.random_int(21, 26):02d}"
