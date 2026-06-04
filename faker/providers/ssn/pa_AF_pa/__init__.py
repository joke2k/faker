from faker.utils import checksums
from .. import Provider as BaseProvider


class Provider(BaseProvider):

    afghan_id_formats = ("%#############",)

    def afghan_id(self, separator: str = "-") -> str:
        base = self.numerify(self.random_element(self.afghan_id_formats))
        checksum = checksums.calculate_luhn(base)
        full = f"{base}{checksum}"

        return (
            full[0:4] + separator +
            full[4:7] + separator +
            full[7:10] + separator +
            full[10:13]
        )