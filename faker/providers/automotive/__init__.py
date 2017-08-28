# coding=utf-8

localized = True

from .. import BaseProvider
from string import ascii_uppercase
import re

class Provider(BaseProvider):
    license_formats = ()

    def license_plate(self):
        temp = re.sub(r'\?',
            lambda x: self.random_element(ascii_uppercase),
            self.random_element(self.license_formats))
        return self.numerify(temp)
