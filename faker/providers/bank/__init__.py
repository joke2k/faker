import re
import string

from string import ascii_uppercase

from .. import BaseProvider

localized = True
default_locale = 'en_GB'


class Provider(BaseProvider):
    """
    Provider for IBAN/BBAN: it generates valid (valid length, valid checksum)
    IBAN/BBANs for the given country. But the ids of the banks are random and
    not valid banks! Same for account numbers.
    """

    ALPHA = {c: str(ord(c) % 55) for c in string.ascii_uppercase}

    # see https://en.wikipedia.org/wiki/International_Bank_Account_Number
    bban_format = '????#############'
    country_code = 'GB'

    def bank_country(self):
        return self.country_code

    def bban(self):
        temp = re.sub(r'\?',
                      lambda x: self.random_element(ascii_uppercase),
                      self.bban_format)
        return self.numerify(temp)

    def iban(self):
        bban = self.bban()

        check = bban + self.country_code + '00'
        check = int(''.join(self.ALPHA.get(c, c) for c in check))
        check = 98 - (check % 97)
        check = str(check).zfill(2)

        return self.country_code + check + bban

    def swift8(self, use_dataset=False):
        """Generate an 8-digit SWIFT code

        This method uses :meth:`swift() <faker.providers.bank.Provider.swift>` under the hood
        with the ``length`` argument set to ``8`` and with the ``primary`` argument omitted.
        All 8-digit SWIFT codes already refer to the primary branch/office.

        :sample:
        :sample: use_dataset=True
        """
        return self.swift(length=8, use_dataset=use_dataset)

    def swift11(self, primary=None, use_dataset=False):
        """Generate an 11-digit SWIFT code

        This method uses :meth:`swift() <faker.providers.bank.Provider.swift>` under the hood
        with the ``length`` argument set to ``11``. If ``primary`` is set to ``True``, the SWIFT
        code will always end with ``XXX``. All 11-digit SWIFT codes use this convention to refer
        to the primary branch/office.

        :sample:
        :sample: use_dataset=True
        """
        return self.swift(length=11, primary=primary, use_dataset=use_dataset)

    def swift(self, length=None, primary=None, use_dataset=False):
        """Generate a SWIFT code

        SWIFT codes, reading from left to right, are composed of a 4 alphabet character bank code,
        a 2 alphabet character country code, a 2 alphanumeric location code, and an optional 3
        alphanumeric branch code. This means SWIFT codes can only have 8 or 11 characters, so the
        value of ``length`` can only be ``None`` or the integers ``8`` or ``11``. If the value is
        ``None``, then a value of ``8`` or ``11`` will randomly be assigned.

        Because all 8-digit SWIFT codes already refer to the primary branch/office, the ``primary``
        argument only has an effect if the value of ``length`` is ``11``. If ``primary`` is ``True``
        and ``length`` is ``11``, the 11-digit SWIFT codes generated will always end in ``XXX`` to
        denote that they belong to primary branches/offices.

        For extra authenticity, localized providers may opt to include SWIFT bank codes, location
        codes, and branch codes used in their respective locales. If ``use_dataset`` is ``True``,
        this method will generate SWIFT codes based on those locale-specific codes if included. If
        those codes were not included, then it will behave as if ``use_dataset`` were ``False``,
        and in that mode, all those codes will just be randomly generated as per the specification.

        :sample:
        :sample: length=8
        :sample: length=8, use_dataset=True
        :sample: length=11
        :sample: length=11, primary=True
        :sample: length=11, use_dataset=True
        :sample: length=11, primary=True, use_dataset=True
        """

        if length is None:
            length = self.random_element((8, 11))
        if length not in (8, 11):
            raise AssertionError('length can only be 8 or 11')

        if use_dataset and hasattr(self, 'swift_bank_codes'):
            bank_code = self.random_element(self.swift_bank_codes)
        else:
            bank_code = self.lexify('????', letters=string.ascii_uppercase)

        if use_dataset and hasattr(self, 'swift_location_codes'):
            location_code = self.random_element(self.swift_location_codes)
        else:
            location_code = self.lexify('??', letters=string.ascii_uppercase + string.digits)

        if length == 8:
            return bank_code + self.country_code + location_code

        if primary:
            branch_code = 'XXX'
        elif use_dataset and hasattr(self, 'swift_branch_codes'):
            branch_code = self.random_element(self.swift_branch_codes)
        else:
            branch_code = self.lexify('???', letters=string.ascii_uppercase + string.digits)

        return bank_code + self.country_code + location_code + branch_code
