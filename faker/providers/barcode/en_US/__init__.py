import re

from itertools import product

from .. import Provider as BarcodeProvider


class Provider(BarcodeProvider):
    # Source of GS1 country codes: https://gs1.org/standards/id-keys/company-prefix
    local_prefixes = (
        *product((0,), range(10)),
        *product((1,), range(4)),
    )

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

    def ean13(self, leading_zero=None, prefixes=()):
        """Generate an EAN-13 barcode.

        If ``leading_zero`` is ``True``, the leftmost digit of the barcode will be set
        to ``0``. If ``False``, the leftmost digit cannot be ``0``. If ``None`` (default),
        the leftmost digit can be any digit.

        If ``prefixes`` are specified, the result will begin with one of the sequence in ``prefixes``.
        This option overrides the option ``leading_zero``

        .. note::

            EAN-13 barcode that starts with a zero can be converted to UPC-A
            by dropping the leading zero. This may cause problems with readers that treat
            all of these code as UPC-A codes and drop the first digit when reading it.

            You can set the argument ``prefixes`` ( or ``leading_zero`` for convenience) explicitly
            to avoid or force the generated barcode to start with a zero.

            You can also generate actual UPC-A barcode with
            :meth:`upc_a() <faker.providers.barcode.en_US.Provider.upc_a>`.

        This method uses :meth:`ean() <faker.providers.barcode.en_US.Provider.ean>` under the
        hood with the ``length`` argument explicitly set to ``13``.

        :sample:
        :sample: leading_zero=False
        :sample: leading_zero=True
        :sample: prefixes=('00',)
        :sample: prefixes=('45', '49')
        """
        if not prefixes:
            if leading_zero is True:
                prefixes = ((0,),)
            elif leading_zero is False:
                prefixes = ((self.random_int(1, 9),),)

        return super().ean13(prefixes=prefixes)

    def _convert_upc_a2e(self, upc_a):
        """
        Convert a 12-digit UPC-A barcode to its 8-digit UPC-E equivalent.

        Note that not all UPC-A barcodes can be converted.
        """
        if not isinstance(upc_a, str):
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
        Create a 12-digit UPC-A barcode that can be converted to UPC-E.

        The expected value of ``base`` is a 6-digit string. If any other value is
        provided, this method will use a random 6-digit string instead.

        The expected value of ``number_system_digit`` is the integer ``0`` or ``1``.
        If any other value is provided, this method will randomly choose from the two.

        Please also view notes on `upc_a()` and `upc_e()` for more details.
        """
        if isinstance(base, str) and self.upc_e_base_pattern.match(base):
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

    def upc_a(self, upc_ae_mode=False, base=None, number_system_digit=None):
        """Generate a 12-digit UPC-A barcode.

        The value of ``upc_ae_mode`` controls how barcodes will be generated. If ``False``
        (default), barcodes are not guaranteed to have a UPC-E equivalent. In this mode,
        the method uses :meth:`ean13 <faker.providers.barcode.Provider.ean13>` under the hood,
        and the values of ``base`` and ``number_system_digit`` will be ignored.

        If ``upc_ae_mode`` is ``True``, the resulting barcodes are guaranteed to have a UPC-E
        equivalent, and the values of ``base`` and ``number_system_digit`` will be used to
        control what is generated.

        Under this mode, ``base`` is expected to have a 6-digit string value. If any other value
        is supplied, a random 6-digit string will be used instead. As for ``number_system_digit``,
        the expected value is a ``0`` or a ``1``. If any other value is provided, this method
        will randomly choose from the two.

        .. important::

           When ``upc_ae_mode`` is enabled, you might encounter instances where different values
           of ``base`` (e.g. ``'120003'`` and ``'120004'``) produce the same UPC-A barcode. This
           is normal, and the reason lies within the whole conversion process. To learn more about
           this and what ``base`` and ``number_system_digit`` actually represent, please refer
           to :meth:`upc_e() <faker.providers.barcode.Provider.upc_e>`.

        :sample:
        :sample: upc_ae_mode=True, number_system_digit=0
        :sample: upc_ae_mode=True, number_system_digit=1
        :sample: upc_ae_mode=True, base='123456', number_system_digit=0
        :sample: upc_ae_mode=True, base='120003', number_system_digit=0
        :sample: upc_ae_mode=True, base='120004', number_system_digit=0
        """
        if upc_ae_mode is True:
            return self._upc_ae(base=base, number_system_digit=number_system_digit)
        else:
            ean13 = self.ean13(leading_zero=True)
            return ean13[1:]

    def upc_e(self, base=None, number_system_digit=None, safe_mode=True):
        """Generate an 8-digit UPC-E barcode.

        UPC-E barcodes can be expressed in 6, 7, or 8-digit formats, but this method uses the
        8 digit format, since it is trivial to convert to the other two formats. The first digit
        (starting from the left) is controlled by ``number_system_digit``, and it can only be a
        ``0`` or a ``1``. The last digit is the check digit that is inherited from the UPC-E barcode's
        UPC-A equivalent. The middle six digits are collectively referred to as the ``base`` (for a
        lack of a better term).

        On that note, this method uses ``base`` and ``number_system_digit`` to first generate a
        UPC-A barcode for the check digit, and what happens next depends on the value of ``safe_mode``.
        The argument ``safe_mode`` exists, because there are some UPC-E values that share the same
        UPC-A equivalent. For example, any UPC-E barcode of the form ``abc0000d``, ``abc0003d``, and
        ``abc0004d`` share the same UPC-A value ``abc00000000d``, but that UPC-A value will only convert
        to ``abc0000d`` because of (a) how UPC-E is just a zero-suppressed version of UPC-A and (b) the
        rules around the conversion.

        If ``safe_mode`` is ``True`` (default), this method performs another set of conversions to
        guarantee that the UPC-E barcodes generated can be converted to UPC-A, and that UPC-A
        barcode can be converted back to the original UPC-E barcode. Using the example above, even
        if the bases ``120003`` or ``120004`` are used, the resulting UPC-E barcode will always
        use the base ``120000``.

        If ``safe_mode`` is ``False``, then the ``number_system_digit``, ``base``, and the computed
        check digit will just be concatenated together to produce the UPC-E barcode, and attempting
        to convert the barcode to UPC-A and back again to UPC-E will exhibit the behavior described
        above.

        :sample:
        :sample: base='123456'
        :sample: base='123456', number_system_digit=0
        :sample: base='123456', number_system_digit=1
        :sample: base='120000', number_system_digit=0
        :sample: base='120003', number_system_digit=0
        :sample: base='120004', number_system_digit=0
        :sample: base='120000', number_system_digit=0, safe_mode=False
        :sample: base='120003', number_system_digit=0, safe_mode=False
        :sample: base='120004', number_system_digit=0, safe_mode=False
        """
        if safe_mode is not False:
            upc_ae = self._upc_ae(base=base, number_system_digit=number_system_digit)
            return self._convert_upc_a2e(upc_ae)
        else:
            upc_ae = self._upc_ae(base=base, number_system_digit=number_system_digit)
            return upc_ae[0] + ''.join(str(x) for x in base) + upc_ae[-1]
