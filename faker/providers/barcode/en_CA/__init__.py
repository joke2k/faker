from itertools import product

# Canada uses UPC too
from ..en_US import Provider as BarcodeProvider


class Provider(BarcodeProvider):
    # Source of GS1 country codes: https://gs1.org/standards/id-keys/company-prefix
    local_prefixes = (
        # The source above doesn't specify prefixes 00~01, 06~09 to be used in Canada also,
        # but it's referenced in numerous pages e.g.: https://www.nationwidebarcode.com/upc-country-codes/
        *product((0,), range(2)),
        *product((0,), range(6, 10)),
        (7, 5),
    )
