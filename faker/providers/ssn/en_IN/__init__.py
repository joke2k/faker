import string

from faker.utils import checksums

from .. import Provider as BaseProvider

GSTIN_CHECKSUM_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
GSTIN_CHECKSUM_BASE = len(GSTIN_CHECKSUM_ALPHABET)


def calculate_gstin_checksum(gstin_without_checksum: str) -> str:
    """Calculate checksum character for a 14-character GSTIN prefix."""

    factor = 2
    total = 0

    for char in reversed(gstin_without_checksum):
        code_point = GSTIN_CHECKSUM_ALPHABET.index(char)
        addend = factor * code_point
        factor = 1 if factor == 2 else 2
        addend = (addend // GSTIN_CHECKSUM_BASE) + (addend % GSTIN_CHECKSUM_BASE)
        total += addend

    remainder = total % GSTIN_CHECKSUM_BASE
    check_code_point = (GSTIN_CHECKSUM_BASE - remainder) % GSTIN_CHECKSUM_BASE
    return GSTIN_CHECKSUM_ALPHABET[check_code_point]


class Provider(BaseProvider):
    """
    Faker provider for Indian Identifiers
    """

    aadhaar_id_formats = ("%##########",)
    pan_type_chars = tuple("CPHFATBLJG")
    gstin_entity_code_chars = tuple("123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def aadhaar_id(self) -> str:
        """
        Aadhaar is a 12 digit person identifier generated for residents of
        India.
        Details: https://en.wikipedia.org/wiki/Aadhaar
        Official Website: https://uidai.gov.in/my-aadhaar/about-your-aadhaar.html
        """

        aadhaar_digits = self.numerify(self.random_element(self.aadhaar_id_formats))
        checksum = checksums.calculate_luhn(int(aadhaar_digits))

        aadhaar_number = f"{aadhaar_digits}{checksum}"

        return aadhaar_number

    def pan(self) -> str:
        """
        Permanent Account Number (PAN) is a 10 character alphanumeric tax
        identifier issued in India.
        Details: https://en.wikipedia.org/wiki/Permanent_account_number
        """

        first_three = self.lexify("???", letters=string.ascii_uppercase)
        pan_type = self.random_element(self.pan_type_chars)
        holder_initial = self.random_uppercase_letter()
        serial = self.numerify("####")
        check_char = self.random_uppercase_letter()

        return f"{first_three}{pan_type}{holder_initial}{serial}{check_char}"

    def gstin(self) -> str:
        """
        Goods and Services Tax Identification Number (GSTIN) is a 15 character
        identifier used in India for GST registration.
        Details: https://en.wikipedia.org/wiki/Goods_and_Services_Tax_(India)
        """

        state_code = f"{self.random_int(min=1, max=38):02d}"
        entity_code = self.random_element(self.gstin_entity_code_chars)
        gstin_without_checksum = f"{state_code}{self.pan()}{entity_code}Z"
        checksum = calculate_gstin_checksum(gstin_without_checksum)

        return f"{gstin_without_checksum}{checksum}"
