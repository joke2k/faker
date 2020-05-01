from .. import Provider as BarCodeProvider


class Provider(BarCodeProvider):
    # Source of GS1 country codes: https://gs1.org/standards/id-keys/company-prefix
    local_prefixes = (4, 5), (4, 9)

    def jan(self, length=13):
        return self.localized_ean(length)

    def jan8(self):
        return self.localized_ean8()

    def jan13(self):
        return self.localized_ean13()
