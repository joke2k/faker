# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as BaseProvider


class Provider(BaseProvider):

    def ssn(self):
        # Certain numbers are invalid for U.S. SSNs. The area (first 3 digits)
        # cannot be 666 or 900-999. The group number (middle digits) cannot be
        # 00. The serial (last 4 digits) cannot be 0000
        area = self.random_int(min=1, max=899)
        if area == 666:
            area += 1
        group = self.random_int(1, 99)
        serial = self.random_int(1, 9999)

        ssn = "{0:03d}-{1:02d}-{2:04d}".format(area, group, serial)
        return ssn
