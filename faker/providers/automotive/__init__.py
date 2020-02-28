import re

from string import ascii_uppercase

from .. import BaseProvider

localized = True


class Provider(BaseProvider):
    license_formats = ()

    def license_plate(self):
        temp = re.sub(r'\?',
                      lambda x: self.random_element(ascii_uppercase),
                      self.random_element(self.license_formats))
        return self.numerify(temp)
