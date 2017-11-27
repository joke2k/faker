# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as SsnProvider


class Provider(SsnProvider):

    # in order to create a valid SIN we need to provide a number that passes a simple modified Luhn Algorithmn checksum
    # this function essentially reverses the checksum steps to create a random
    # valid SIN (Social Insurance Number)
    def ssn(self):

        # create an array of 8 elements initialized randomly
        digits = self.generator.random.sample(range(10), 8)

        # All of the digits must sum to a multiple of 10.
        # sum the first 8 and set 9th to the value to get to a multiple of 10
        digits.append(10 - (sum(digits) % 10))

        # digits is now the digital root of the number we want multiplied by the magic number 121 212 121
        # reverse the multiplication which occurred on every other element
        for i in range(1, len(digits), 2):
            if digits[i] % 2 == 0:
                digits[i] = (digits[i] / 2)
            else:
                digits[i] = (digits[i] + 9) / 2

        # build the resulting SIN string
        sin = ""
        for i in range(0, len(digits), 1):
            sin += str(digits[i])
            # add a space to make it conform to normal standards in Canada
            if i % 3 == 2:
                sin += " "

        # finally return our random but valid SIN
        return sin
