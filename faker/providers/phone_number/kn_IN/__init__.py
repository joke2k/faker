from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    # Source references (accessed 2026-11-23):
    # - https://dot.gov.in/numbering-resources (Indian mobile numbers start with 6, 7, 8 or 9)
    # - https://en.wikipedia.org/wiki/List_of_dialling_codes_in_India (Karnataka STD codes:
    #   080 Bengaluru, 0821 Mysuru, 0824 Mangaluru, 0831 Belagavi, 0836 Hubballi-Dharwad)
    # Patterns are intended for structurally valid synthetic Karnataka numbers.
    formats = (
        "+91 6#########",
        "+91 7#########",
        "+91 8#########",
        "+91 9#########",
        "+91 9#### #####",
        "080-########",
        "0821-#######",
        "0824-#######",
        "0831-#######",
        "0836-#######",
    )
