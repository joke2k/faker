from faker.utils import checksums

from .. import Provider as BaseProvider


class Provider(BaseProvider):
    """
    Faker provider for Indian Identifiers
    """

    aadhaar_id_formats = (
        '%##########',
    )

    def aadhaar_id(self):
        """
        Aadhaar is a 12 digit person identifier generated for residents of
        India.
        Details: https://en.wikipedia.org/wiki/Aadhaar
        Official Website: https://uidai.gov.in/my-aadhaar/about-your-aadhaar.html
        """

        aadhaar_digits = self.numerify(self.random_element(self.aadhaar_id_formats))
        checksum = checksums.calculate_luhn(aadhaar_digits)

        aadhaar_number = f'{aadhaar_digits}{checksum}'

        return aadhaar_number
