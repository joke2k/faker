# Data source
#
# Ethiopia national numbering plan: mobile prefixes 09 (Ethio Telecom) and 07 (Safaricom Ethiopia);
# international format country code +251 with trunk prefix 0 omitted.
# https://en.wikipedia.org/wiki/Telephone_numbers_in_Ethiopia (retrieved 2026-03-29)

from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats = (
        "09########",
        "+2519########",
        "07########",
        "+2517########",
    )
