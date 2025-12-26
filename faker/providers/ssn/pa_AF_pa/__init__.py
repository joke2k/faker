from faker.utils import checksums
from .. import Provider as BaseProvider


class Provider(BaseProvider):
    """
    Faker provider for Afghan National Identifiers (Pashto)
    """

    # Afghan national ID format: 9 digits
    afghan_id_formats = ("%########",)  # tuple with one format

    def afghan_id(self) -> str:
        """
        Generates a random Afghan National ID.

        Format: 9 digits + 1 checksum digit (Luhn)
        """
        # Generate first 9 digits
        id_digits = self.numerify(self.random_element(self.afghan_id_formats))

        # Compute Luhn checksum for last digit
        checksum = checksums.calculate_luhn(id_digits)

        # Return full Afghan ID
        return f"{id_digits}{checksum}"
