from typing import Sequence

from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        "(+51) 9## ### ###",
        "(+51) 9########",
        "+51 9## ### ###",
        "519## ### ###",
        "519########",
        "9## ### ###",
        "9########",
    )

    def _create_phone_number(self, formats: Sequence[str]) -> str:
        pattern: str = self.random_element(formats)
        return self.numerify(self.generator.parse(pattern))

    def phone_number_pe(self) -> str:
        return self._create_phone_number(self.formats)
