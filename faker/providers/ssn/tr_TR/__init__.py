# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as BaseProvider


class Provider(BaseProvider):
    # Source:
    # Turkey Republic National Number is identity number.
    # Identity number contains 11 numbers,
    # First number can't be zero
    # Eleventh number is result of division after sum first number

    def ssn(self):
        """
        :example '89340691651'
        """
        first_part = self.random_element((1, 2, 3, 4, 5, 6, 7, 8, 9))
        middle_part = self.bothify('#########')
        last_part = sum(list(map(lambda x: int(x), '{0}{1}'.format(first_part, middle_part)))) % 10
        return '{}{}{}'.format(first_part, middle_part, last_part)
