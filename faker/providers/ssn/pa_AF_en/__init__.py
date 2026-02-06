from faker.utils import checksums
from .. import Provider as BaseProvider


class Provider(BaseProvider):
    """
    Afghan National ID – Format: XXXX-XXX-XXX-XXX
    Example: 2222-323-423-432
    """

    afghan_id_formats = ("%#############",)  # 12 base digits

    def afghan_id(self, separator: str = "-") -> str:
        """
        Generates Afghan National ID.

        Format:
            2222-323-423-432
        """

        # 12-digit base
        base = self.numerify(self.random_element(self.afghan_id_formats))

        # Luhn checksum on the 13th digit
        checksum = checksums.calculate_luhn(base)
        full = f"{base}{checksum}"  # 13 digits total

        # Enforce XXXX-XXX-XXX-XXX
        return (
            full[0:4] + separator +
            full[4:7] + separator +
            full[7:10] + separator +
            full[10:13]
        )
