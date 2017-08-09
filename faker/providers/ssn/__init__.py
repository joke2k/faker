# coding=utf-8
from __future__ import unicode_literals
localized = True

from .. import BaseProvider


class Provider(BaseProvider):
    ssn_formats = ("###-##-####",)

    def ssn(self):
        return self.bothify(self.random_element(self.ssn_formats))
