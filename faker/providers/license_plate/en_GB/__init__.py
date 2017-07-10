# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as LicensePlateProvider


class Provider(LicensePlateProvider):
    # from https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_the_United_Kingdom
    formats = (
            '??## ???',
            '??##???'
        )