import re

from string import ascii_uppercase

from .. import BaseProvider, ElementsType

localized = True


class Provider(BaseProvider):
    """Implement default automotive provider for Faker."""

    license_formats: ElementsType = ()

    def license_plate(self) -> str:
        """Generate a license plate."""
        temp = re.sub(
            r"\?",
            lambda x: self.random_element(ascii_uppercase),
            self.random_element(self.license_formats),
        )
        return self.numerify(temp)
