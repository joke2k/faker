from typing import Tuple

from .. import BaseProvider

localized = True


class Provider(BaseProvider):
    ssn_formats: Tuple[str, ...] = ("###-##-####",)

    def ssn(self) -> str:
        return self.bothify(self.random_element(self.ssn_formats))
