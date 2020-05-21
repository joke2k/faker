from .. import Provider as BarcodeProvider


class Provider(BarcodeProvider):
    # Source of GS1 country codes: https://gs1.org/standards/id-keys/company-prefix
    local_prefixes = (4, 5), (4, 9)

    def jan(self, length=13):
        """Generate a JAN barcode of the specified length

        Japanese local EAN barcodes are called JAN-codes https://www.dsri.jp/jan/about_jan.html

        This method is an alias and just calls
        :meth:`localized_ean()<faker.providers.barcode.ja_JP.Provider.localized_ean>` under the hood

        :sample:
        :sample: length=8
        :sample: length=13
        """
        return self.localized_ean(length)

    def jan8(self):
        """Generate a 8 digit JAN barcode

        This method is an alias and just calls
        :meth:`localized_ean8()<faker.providers.barcode.ja_JP.Provider.localized_ean8>` under the hood

        :sample:
        """
        return self.localized_ean8()

    def jan13(self):
        """Generate a 13 digit JAN barcode

        This method is an alias and just calls
        :meth:`localized_ean13()<faker.providers.barcode.ja_JP.Provider.localized_ean13>` under the hood

        :sample:
        """
        return self.localized_ean13()
