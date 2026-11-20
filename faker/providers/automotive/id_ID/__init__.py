import string

from .. import Provider as AutomotiveProvider


class Provider(AutomotiveProvider):
    """Implement automotive provider for ``id_ID`` locale.

    Sources:

    - https://id.wikipedia.org/wiki/Tanda_nomor_kendaraan_bermotor_Indonesia
    """

    # Region codes (kode wilayah) used on Indonesian license plates
    license_plate_prefixes = (
        # Sumatra
        "BL",
        "BB",
        "BK",
        "BA",
        "BM",
        "BP",
        "BH",
        "BG",
        "BN",
        "BD",
        "BE",
        # Java
        "A",
        "B",
        "D",
        "E",
        "F",
        "T",
        "Z",
        "G",
        "H",
        "K",
        "R",
        "AA",
        "AB",
        "AD",
        "L",
        "M",
        "N",
        "P",
        "S",
        "W",
        "AE",
        "AG",
        # Bali and Nusa Tenggara
        "DK",
        "DR",
        "EA",
        "DH",
        "EB",
        "ED",
        # Kalimantan
        "KB",
        "DA",
        "KH",
        "KT",
        "KU",
        # Sulawesi
        "DB",
        "DL",
        "DM",
        "DN",
        "DD",
        "DC",
        "DT",
        # Maluku and Papua
        "DE",
        "DG",
        "PA",
        "PB",
    )

    # The registration number has 1 to 4 digits and never starts with 0
    license_plate_number_formats = ("%", "%#", "%##", "%###")

    license_plate_suffix_formats = ("?", "??", "???")

    def license_plate(self) -> str:
        """Generate a license plate."""
        prefix: str = self.random_element(self.license_plate_prefixes)
        number = self.numerify(self.random_element(self.license_plate_number_formats))
        suffix = self.lexify(
            self.random_element(self.license_plate_suffix_formats),
            letters=string.ascii_uppercase,
        )
        return f"{prefix} {number} {suffix}"
