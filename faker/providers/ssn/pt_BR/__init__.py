#  -*- coding: utf-8 -*-

from __future__ import unicode_literals
from .. import Provider as SsnProvider


def checksum(digits):
    s = 0
    p = len(digits) + 1
    for i in range(0, len(digits)):
        s += digits[i] * p
        p -= 1

    reminder = s % 11
    if reminder == 0 or reminder == 1:
        return 1
    else:
        return 11 - reminder


class Provider(SsnProvider):
    """
    Provider for Brazilian SSN also known in Brazil as CPF.
    There are two methods Provider.ssn and Provider.cpf
    The snn returns a valid number with numbers only
    The cpf return a valid number formatted with brazilian mask. eg nnn.nnn.nnn-nn
    """

    def ssn(self):
        digits = self.generator.random.sample(range(10), 9)

        dv = checksum(digits)
        digits.append(dv)
        digits.append(checksum(digits))

        return ''.join(map(str, digits))

    def cpf(self):
        c = self.ssn()
        return c[:3] + '.' + c[3:6] + '.' + c[6:9] + '-' + c[9:]
