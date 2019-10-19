# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as AutomotiveProvider

class Provider(AutomotiveProvider):
    # https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_India
    license_formats = (
        '?? ## ?? ####'     #e.g for Delhi - DL 01 ZE 1234 ; ?-corresponds to letter #- corresponds to number (1-9)
                            #not included Union territories , only states
    )

