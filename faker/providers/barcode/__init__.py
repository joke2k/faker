from .. import BaseProvider

localized = True


class Provider(BaseProvider):
    # Source of GS1 country codes: https://gs1.org/standards/id-keys/company-prefix
    local_prefixes = ()

    def _ean(self, length=13, prefixes=()):
        if length not in (8, 13):
            raise AssertionError("length can only be 8 or 13")

        code = [self.random_digit() for _ in range(length - 1)]

        if prefixes:
            prefix = self.random_element(prefixes)
            code[:len(prefix)] = map(int, prefix)

        if length == 8:
            weights = [3, 1, 3, 1, 3, 1, 3]
        elif length == 13:
            weights = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3]

        weighted_sum = sum(x * y for x, y in zip(code, weights))
        check_digit = (10 - weighted_sum % 10) % 10
        code.append(check_digit)

        return ''.join(str(x) for x in code)

    def ean(self, length=13, prefixes=()):
        """Generate an EAN barcode of the specified ``length``.

        The value of ``length`` can only be ``8`` or ``13`` (default)  which will
        create an EAN-8 or an EAN-13 barcode respectively.

        If ``prefixes`` are specified, the result will begin with one of the sequence in ``prefixes``

        :sample: length=13
        :sample: length=8
        :sample: prefixes=('00',)
        :sample: prefixes=('45', '49')
        """
        return self._ean(length, prefixes=prefixes)

    def ean8(self, prefixes=()):
        """Generate an EAN-8 barcode.

        This method uses :meth:`ean() <faker.providers.barcode.Provider.ean>` under the
        hood with the ``length`` argument explicitly set to ``8``.

        If ``prefixes`` are specified, the result will begin with one of the sequence in ``prefixes``

        :sample:
        :sample: prefixes=('00',)
        :sample: prefixes=('45', '49')
        """
        return self._ean(8, prefixes=prefixes)

    def ean13(self, prefixes=()):
        """Generate an EAN-13 barcode.

        If ``prefixes`` are specified, the result will begin with one of the sequence in ``prefixes``.

        This method uses :meth:`ean() <faker.providers.barcode.Provider.ean>` under the
        hood with the ``length`` argument explicitly set to ``13``.

        .. note::

            Codes starting with a leading zero are treated specially in some barcode readers.

            For more information about compatibility with UPC-A codes, see
            :meth:`en_US.ean13() <faker.providers.barcode.en_US.Provider.ean13>`

        :sample:
        :sample: prefixes=('00',)
        :sample: prefixes=('45', '49')
        """

        return self._ean(13, prefixes=prefixes)

    def localized_ean(self, length=13):
        """Generate a localized EAN barcode of the specified ``length``.

        The value of ``length`` can only be ``8`` or ``13`` (default)  which will
        create an EAN-8 or an EAN-13 barcode respectively.

        This method uses :meth:`ean() <faker.providers.barcode.Provider.ean>` under the
        hood with the ``prefixes`` argument explicitly set to ``self.local_prefixes``.

        :sample:
        :sample: length=13
        :sample: length=8
        """
        return self._ean(length, prefixes=self.local_prefixes)

    def localized_ean8(self):
        """Generate a localized EAN-8 barcode.

        This method uses :meth:`localized_ean() <faker.providers.barcode.Provider.ean>` under the
        hood with the ``length`` argument explicitly set to ``8``.

        :sample:
        """
        return self.localized_ean(8)

    def localized_ean13(self):
        """Generate a localized EAN-13 barcode.

        This method uses :meth:`localized_ean() <faker.providers.barcode.Provider.ean>` under the
        hood with the ``length`` argument explicitly set to ``13``.

        :sample:
        """
        return self.localized_ean(13)
