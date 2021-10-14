import re

from string import ascii_uppercase

from .. import BaseProvider

localized = True
VIN_CHARS = 'ABCDEFGHJKLMNPRSTUVWXYZ0123456789'

class Provider(BaseProvider):
    """Implement default automotive provider for Faker."""

    license_formats = ()

    def license_plate(self):
        """Generate a license plate."""
        temp = re.sub(r'\?',
                      lambda x: self.random_element(ascii_uppercase),
                      self.random_element(self.license_formats))
        return self.numerify(temp)

    def vin(self):
        """ Generate a vin """
        temp = self.random_element(self.vin_formats)
        return self.bothify(temp, VIN_CHARS)
