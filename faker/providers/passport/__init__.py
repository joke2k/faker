import re

from datetime import *
from string import ascii_uppercase

from .. import BaseProvider, ElementsType

localized = True


class Provider(BaseProvider):
    """Implement default Passport provider for Faker."""

    passport_number_formats: ElementsType = ()

    def passport_DOB(self):
        """Generate a datetime date of birth."""
        birthday = self.generator.date_of_birth()
        return birthday

    def passport_owner(self, gender="X"):
        """Generate a given_name and surname for a passport owner
        The ``gender`` argument is the sex of a passport owner which is a one character string that is either male, female, or non-binary.
        """
        if gender == "M":
            given_name = self.generator.parse("{{first_name_male}} ")
            surname = self.generator.parse("{{last_name_male}} ")
        elif gender == "F":
            given_name = self.generator.parse("{{first_name_female}} ")
            surname = self.generator.parse("{{last_name_female}} ")
        else:
            given_name = self.generator.parse("{{first_name_nonbinary}} ")
            surname = self.generator.parse("{{last_name_nonbinary}} ")

        return given_name, surname

    def passport_number(self) -> str:
        """Generate a passport number by replacing tokens to be alphanumeric"""
        temp = re.sub(
            r"\?",
            lambda x: self.random_element(ascii_uppercase),
            self.random_element(self.passport_number_formats),
        )
        return self.numerify(temp)
