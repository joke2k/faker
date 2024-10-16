from typing import Tuple

from faker.typing import SexLiteral

from .. import Provider as PassportProvider


class Provider(PassportProvider):
    def passport_owner(self, gender: SexLiteral = "M") -> Tuple[str, str]:
        given_name, surname = super().passport_owner(gender)
        return surname, given_name
