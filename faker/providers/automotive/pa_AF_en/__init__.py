import random
from faker.providers import BaseProvider

class Provider(BaseProvider):
    """
    Afghan automotive license plate provider for pa_AF locale.
    Generates custom Afghan-style license plates.
    """

    # All Afghan provinces short codes
    provinces = [
        "BD", "BG", "BL", "BM", "PY", "PK", "PR", "PN", "TK",
        "DK", "JZ", "AR", "ZB", "SM", "SP", "GR", "GZ", "FR",
        "FA", "KB", "KP", "KN", "KR", "LG", "MD", "NM", "NG",
        "NR", "HL", "HR", "KH"
    ]

    # Your custom license plate formats
    license_formats = (
        "{} ####",      # e.g., BD 1234
        "{} ### ##",    # e.g., BG 123 45
        "{} ## ###",    # e.g., BL 12 345
        "{} #### ##",   # e.g., BM 1234 56
    )

    def license_plate(self):
        """Return a randomly generated Afghan-style license plate."""
        province = random.choice(self.provinces)
        pattern = random.choice(self.license_formats)
        plate = pattern.format(province)

        # Replace # with random digits
        plate = ''.join([str(random.randint(0, 9)) if c == '#' else c for c in plate])
        return plate
