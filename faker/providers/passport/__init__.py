import re

from string import ascii_uppercase

from .. import BaseProvider, ElementsType

localized = True


class Provider(BaseProvider):
    """Implement default Passport provider for Faker."""
    nationality: ElementsType = ()
    passport_number_formats: ElementsType = ()

    def nationality(self)-> str:
        return self.nationality
    
    def passport_owner(self):
        given_name = self.generator.parse("{{first_name}} ")
        surname  = self.generator.parse("{{last_name}} ")
        return given_name, surname
    
    def passport_number(self) -> str:
        """Generate a passport number"""
        temp = re.sub(
            r"\?",
            lambda x: self.random_element(ascii_uppercase),
            self.random_element(self.passport_number_formats),
        )
        return self.numerify(temp)