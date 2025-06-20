from .. import Provider as ISBNProvider


class Provider(ISBNProvider):
    rules = {
        # EAN prefix
        "978": {
            # Registration group for Brazil
            "85": [
                # Registrant rule (min, max, registrant length)
                # These rules are based on typical Brazilian ISBN patterns
                # Note: The exact rules may need adjustment based on official Brazilian ISBN agency data
                ("0000000", "1999999", 2),
                ("2000000", "2999999", 3),
                ("3000000", "3999999", 4),
                ("4000000", "4999999", 5),
                ("5000000", "5999999", 6),
                ("6000000", "6999999", 7),
                ("7000000", "7999999", 3),
                ("8000000", "8999999", 4),
                ("9000000", "9999999", 5),
            ],
        },
    } 