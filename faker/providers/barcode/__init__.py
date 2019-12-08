# coding=utf-8

from __future__ import unicode_literals

import re
from six import string_types

from .. import BaseProvider


class Provider(BaseProvider):

    upc_e_base_pattern = re.compile(r'^\d{6}$')
    upc_ae_pattern1 = re.compile(
        r'^(?P<number_system_digit>[01])'   # The first digit must be 0 or 1
        r'(?=\d{11}$)'                      # followed by 11 digits of which
        r'(?P<mfr_code>\d{2})'              # the first 2 digits make up the manufacturer code,
        r'(?:(?P<extra>[012])0{4})'         # if immediately followed by 00000, 10000, or 20000,
        r'(?P<product_code>\d{3})'          # a 3-digit product code,
        r'(?P<check_digit>\d)$',            # and finally a check digit.
    )
    upc_ae_pattern2 = re.compile(
        r'^(?P<number_system_digit>[01])'   # The first digit must be 0 or 1
        r'(?=\d{11}$)'                      # followed by 11 digits of which
        r'(?P<mfr_code>\d{3,4}?)'           # the first 3 or 4 digits make up the manufacturer code,
        r'(?:0{5})'                         # if immediately followed by 00000,
        r'(?P<product_code>\d{1,2})'        # a 2-digit or single digit product code,
        r'(?P<check_digit>\d)$',            # and finally a check digit.
    )
    upc_ae_pattern3 = re.compile(
        r'^(?P<number_system_digit>[01])'   # The first digit must be 0 or 1
        r'(?=\d{11}$)'                      # followed by 11 digits of which
        r'(?P<mfr_code>\d{5})'              # the first 5 digits make up the manufacturer code,
        r'(?:0{4}(?P<extra>[5-9]))'         # if immediately followed by 0000 and a 5, 6, 7, 8, or 9,
        r'(?P<check_digit>\d)$',            # and finally a check digit.
    )

    def _ean(self, length=13, leading_zero=None):
        if length not in (8, 13):
            raise AssertionError("length can only be 8 or 13")

        code = [self.random_digit() for _ in range(length - 1)]
        if leading_zero is True:
            code[0] = 0
        elif leading_zero is False:
            code[0] = self.random_int(1, 9)

        if length == 8:
            weights = [3, 1, 3, 1, 3, 1, 3]
        elif length == 13:
            weights = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]

        weighted_sum = sum(x * y for x, y in zip(code, weights))
        check_digit = (10 - weighted_sum % 10) % 10
        code.append(check_digit)

        return ''.join(str(x) for x in code)

    def _convert_upc_a2e(self, upc_a):
        """
        Converts a 12-digit UPC-A barcode to its 8-digit UPC-E equivalent

        Not all UPC-A barcodes can be converted.

        :param upc_a: UPC-A barcode to convert
        :return: UPC-E equivalent barcode
        """
        if not isinstance(upc_a, string_types):
            raise TypeError('`upc_a` is not a string')
        m1 = self.upc_ae_pattern1.match(upc_a)
        m2 = self.upc_ae_pattern2.match(upc_a)
        m3 = self.upc_ae_pattern3.match(upc_a)
        if not any([m1, m2, m3]):
            raise ValueError('`upc_a` has an invalid value')
        upc_e_template = '{number_system_digit}{mfr_code}{product_code}{extra}{check_digit}'
        if m1:
            upc_e = upc_e_template.format(**m1.groupdict())
        elif m2:
            groupdict = m2.groupdict()
            groupdict['extra'] = str(len(groupdict.get('mfr_code')))
            upc_e = upc_e_template.format(**groupdict)
        else:
            groupdict = m3.groupdict()
            groupdict['product_code'] = ''
            upc_e = upc_e_template.format(**groupdict)
        return upc_e

    def _upc_ae(self, base=None, number_system_digit=None):
        """
        Creates a 12-digit UPC-A barcode that can be converted to UPC-E

        Notes on this method:
        - Please view notes on `upc_a()` and `upc_e()` first.

        :param base: A 6-digit string
        :param number_system_digit: 0 or 1
        :return: 12-digit UPC-A barcode that can be converted to UPC-E
        """
        if isinstance(base, string_types) and self.upc_e_base_pattern.match(base):
            base = [int(x) for x in base]
        else:
            base = [self.random_int(0, 9) for _ in range(6)]
        if number_system_digit not in [0, 1]:
            number_system_digit = self.random_int(0, 1)

        if base[-1] <= 2:
            code = base[:2] + base[-1:] + [0] * 4 + base[2:-1]
        elif base[-1] <= 4:
            code = base[:base[-1]] + [0] * 5 + base[base[-1]:-1]
        else:
            code = base[:5] + [0] * 4 + base[-1:]

        code.insert(0, number_system_digit)
        weights = [3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]
        weighted_sum = sum(x * y for x, y in zip(code, weights))
        check_digit = (10 - weighted_sum % 10) % 10
        code.append(check_digit)
        return ''.join(str(x) for x in code)

    def ean(self, length=13):
        return self._ean(length)

    def ean8(self):
        return self._ean(8)

    def ean13(self, leading_zero=None):
        """
        Creates an EAN-13 barcode

        :param leading_zero: Leading digit will be 0 if True, 1-9 if False, and 0-9 otherwise
        :return: An EAN-13 barcode
        """
        return self._ean(13, leading_zero=leading_zero)

    def upc_a(self, upc_ae_mode=False, base=None, number_system_digit=None):
        """
        Creates a 12-digit UPC-A barcode

        Notes on UPC-A barcode and this method:
        - EAN-13 is a superset of UPC-A. Simply put, leading zero + UPC-A = EAN-13.
        - For the lack of a concise and better term, this provider uses the term "upc_ae" to mean
          that a UPC-A barcode can be converted to UPC-E.
        - If `upc_ae_mode` is enabled, this method will only return UPC-A barcodes that can be
          converted to UPC-E. In this mode the leading digit (number system) of the UPC-A barcode
          may only start with 0 or 1.
        - When `upc_ae_mode` is enabled, the `number_system_digit` may be explicitly set to 0 or 1.
          If it is not set or is invalid, either values will be chosen at random.
        - When `upc_ae_mode` is enabled, a 6-digit UPC-E string `base` may be explicitly set. If it
          is not set or is invalid, a random 6 digit combination will be used.
        - If `upc_ae_mode` is disabled, the values of `base` and `number_system_digit` are ignored.

        :param upc_ae_mode: Set to True explicitly to enable
        :param base: A 6-digit string
        :param number_system_digit: 0 or 1
        :return: 12-digit UPC-A barcode
        """
        if upc_ae_mode is True:
            return self._upc_ae(base=base, number_system_digit=number_system_digit)
        else:
            ean13 = self.ean13(leading_zero=True)
            return ean13[1:]

    def upc_e(self, base=None, number_system_digit=None, safe_mode=True):
        """
        Creates an 8-digit UPC-E barcode

        Notes on UPC-E barcode and this method:
        - UPC-E barcodes can be expressed in 6, 7, or 8-digit formats, but this method uses the
          8 digit format, since it is trivial to convert to the other two formats.
        - The first digit of the barcode denotes the number system used, either 0 or 1.
        - The last digit is the check digit (more on that below).
        - The remaining 6 digits are a bit more involved, but they are referred to as the `base`
          argument elsewhere in this provider (for the lack of a concise and better term).
        - Each UPC-E `base` have 2 UPC-A equivalents depending on the number system used.
        - If the value of `number_system_digit` is not 0 or 1, either values will be chosen at random.
        - A 6-digit string `base` may also be explicitly set. If invalid, it will be ignored, and a
          new value for `base` will be generated.
        - Internally, this method first generates a UPC-A barcode that can be converted to UPC-E, and
          then actually performs a conversion for the result. This is because both the number
          system and check digits of the UPC-E barcode are inherited from its UPC-A equivalent.
        - Then there is `safe_mode`. Enabling this guarantees that every UPC-E barcode generated can
          be converted to UPC-A, and that UPC-A value can be converted back again to UPC-E and still
          be equal to the original value. In other words, the statement a2e(e2a(e)) == e holds True.
        - As to why there is `safe_mode`, it is because there are some UPC-E values that share the
          same UPC-A equivalent. For example, any UPC-E barcode of the form abc0000d, abc0003d, and
          abc0004d share the same UPC-A value abc00000000d, but that UPC-A value will only convert
          to abc0000d because of (a) how UPC-E is just a zero-suppressed version of UPC-A and
          (b) the rules around the conversion.

        :param base: A 6-digit string
        :param number_system_digit: First digit of the barcode
        :param safe_mode: True or False. Guarantees that every UPC-E barcode generated can be
                          converted back-and-forth between UPC-A and UPC-E.
        :return: 8-digit UPC-E barcode
        """
        if safe_mode is not False:
            upc_ae = self._upc_ae(base=base, number_system_digit=number_system_digit)
            return self._convert_upc_a2e(upc_ae)
        else:
            upc_ae = self._upc_ae(base=base, number_system_digit=number_system_digit)
            return upc_ae[0] + ''.join(str(x) for x in base) + upc_ae[-1]
