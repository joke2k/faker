# coding=utf-8
from __future__ import unicode_literals
localized = True

from .. import BaseProvider


class Provider(BaseProvider):
    ssn_formats = ("###-##-####",)

    @classmethod
    def ssn(cls):
        return cls.bothify(cls.random_element(cls.ssn_formats))
