# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as SsnProvider


class Provider(SsnProvider):
    ssn_formats = ("?#########",)

    @classmethod
    def ssn(cls):
        return cls.bothify(cls.random_element(cls.ssn_formats)).upper()
