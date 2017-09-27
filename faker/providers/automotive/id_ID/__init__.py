# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as AutomotiveProvider

class Provider(AutomotiveProvider):
    # from https://en.wikipedia.org/wiki/United_States_license_plate_designs_and_serial_formats#Current_standard-issue_passenger_plate_designs_and_serial_formats
    license_formats = (
        '? ### ??',
        '? ### ???',
        '?? ### ??',
        '?? ### ???',
        '? #### ??',
        '? #### ???',
        '?? #### ??',
        '?? #### ???',
    )