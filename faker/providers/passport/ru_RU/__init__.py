from typing import Tuple

from .. import Provider as PassportProvider


class Provider(PassportProvider):
    def passport_owner(self, gender: str = "M") -> Tuple[str, str]:
        given_name, surname = super().passport_owner(gender)
        return surname, given_name
