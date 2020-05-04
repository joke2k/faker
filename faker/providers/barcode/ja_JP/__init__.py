from .. import Provider as BarcodeProvider


class Provider(BarcodeProvider):
    # Source of GS1 country codes: https://gs1.org/standards/id-keys/company-prefix
    local_prefixes = (4, 5), (4, 9)

    def jan(self, length=13):
        """
        Japanese local EAN barcodes are called JAN-codes https://www.dsri.jp/jan/about_jan.html
        This method is an alias and just calls
        :meth:`localized_ean()<faker.providers.barcode.Provider.localized_ean>` under the hood

        :param length:
        :return:
        """
        return self.localized_ean(length)

    def jan8(self):
        """
        Japanese local EAN barcodes are called JAN-codes https://www.dsri.jp/jan/about_jan.html
        This method is an alias and just calls
        :meth:`localized_ean8()<faker.providers.barcode.Provider.localized_ean8>` under the hood

        :return:
        """
        return self.localized_ean8()

    def jan13(self):
        """
        Japanese local EAN barcodes are called JAN-codes https://www.dsri.jp/jan/about_jan.html
        This method is an alias and just calls
        :meth:`localized_ean13()<faker.providers.barcode.Provider.localized_ean13>` under the hood

        :return:
        """
        return self.localized_ean13()
