# coding=utf-8

from __future__ import unicode_literals
from .. import BaseProvider


class Provider(BaseProvider):

    def _ean(self, length=13, *, no_leading_zero=False, force_leading_zero=False):
        if length not in (8, 13):
            raise AssertionError("length can only be 8 or 13")
        if no_leading_zero is True and force_leading_zero is True:
            raise AssertionError('`no_leading_zero` is True but `force_leading_zero` is True')

        code = [self.random_digit() for _ in range(length - 1)]
        if no_leading_zero is True:
            code[0] = self.random_int(1, 9)
        elif force_leading_zero is True:
            code[0] = 0

        if length == 8:
            weights = [3, 1, 3, 1, 3, 1, 3]
        elif length == 13:
            weights = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]

        weighted_sum = sum(x * y for x, y in zip(code, weights))
        check_digit = (10 - weighted_sum % 10) % 10
        code.append(check_digit)

        return ''.join(str(x) for x in code)

    def ean(self, length=13):
        return self._ean(length)

    def ean8(self):
        return self._ean(8)

    def ean13(self, *, no_leading_zero=False, force_leading_zero=False):
        """
        Creates an EAN-13 barcode

        Notes on this method:
        - Obviously, `no_leading_zero` and `force_leading_zero` cannot be both set to True.
        - If `no_leading_zero` is True, no EAN-13 barcodes generated will lead with zero. This flag
          can be used to work around scanners that cannot properly handle such barcodes.
        - If `force_leading_zero` is True, EAN-13 barcodes generated will always lead with zero,
          and as a result, the barcodes become UPC-A compatible. Just drop the leading zeroes.
        - Any other non-boolean value supplied to `no_leading_zero` and `force_leading_zero` will
          be treated as False, and therefore, providing the default behavior.

        :param no_leading_zero: True or False
        :param force_leading_zero: True or False
        :return: An EAN-13 barcode
        """
        return self._ean(13, no_leading_zero=no_leading_zero, force_leading_zero=force_leading_zero)
