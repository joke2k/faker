# isbn_provider_ps_af.py  (Pashto - ps_AF)

from .. import Provider as ISBNProvider


class Provider(ISBNProvider):
    """Custom ISBN provider for Pashto Afghanistan locale."""

    rules = {
        # EAN prefix
        "978": {
            # Registration group: English-speaking (0) and Pakistan (969) – commonly used in Afghanistan
            "0": [
                ("0000000", "1999999", 2),
                ("2000000", "2279999", 3),
                ("2280000", "2289999", 4),
                ("2290000", "6479999", 3),
                ("6480000", "6489999", 7),
                ("6490000", "6999999", 3),
                ("7000000", "8499999", 4),
                ("8500000", "8999999", 5),
                ("9000000", "9499999", 6),
                ("9500000", "9999999", 7),
            ],
            "969": [  # Pakistan group – frequently used for Afghan publications
                ("000000", "299999", 3),
                ("300000", "599999", 4),
                ("600000", "899999", 5),
                ("900000", "999999", 6),
            ],
        },
        "979": {  # ISBN-13 alternative prefix (less common but valid)
            "0": [
                ("0000000", "1999999", 4),
                ("2000000", "5999999", 5),
                ("6000000", "8999999", 6),
                ("9000000", "9999999", 7),
            ],
        }
    }