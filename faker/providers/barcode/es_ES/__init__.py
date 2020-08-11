from .. import Provider as BarcodeProvider


class Provider(BarcodeProvider):
    # Source of GS1 country codes: https://gs1.org/standards/id-keys/company-prefix
    local_prefixes = ((8, 4),)
