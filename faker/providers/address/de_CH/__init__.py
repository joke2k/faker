from typing import Tuple

from .. import Provider as AddressProvider


class Provider(AddressProvider):
    city_formats = ("{{canton_name}}",)
    building_number_formats = ("%", "%#", "%#", "%#", "%##")
    street_suffixes = ["strasse"]
    street_name_formats = ("{{last_name}}{{street_suffix}}",)
    street_address_formats = ("{{street_name}} {{building_number}}",)
    address_formats = ("{{street_address}}\n{{postcode}} {{city}}",)
    postcode_formats = (
        "1###",
        "2###",
        "3###",
        "4###",
        "5###",
        "6###",
        "7###",
        "8###",
        "9###",
    )

    cantons = (
        ("AG", "Aargau"),
        ("AI", "Appenzell Innerrhoden"),
        ("AR", "Appenzell Ausserrhoden"),
        ("BE", "Bern"),
        ("BL", "Basel-Landschaft"),
        ("BS", "Basel-Stadt"),
        ("FR", "Freiburg"),
        ("GE", "Genf"),
        ("GL", "Glarus"),
        ("GR", "Graubünden"),
        ("JU", "Jura"),
        ("LU", "Luzern"),
        ("NE", "Neuenburg"),
        ("NW", "Nidwalden"),
        ("OW", "Obwalden"),
        ("SG", "St. Gallen"),
        ("SH", "Schaffhausen"),
        ("SO", "Solothurn"),
        ("SZ", "Schwyz"),
        ("TG", "Thurgau"),
        ("TI", "Tessin"),
        ("UR", "Uri"),
        ("VD", "Waadt"),
        ("VS", "Wallis"),
        ("ZG", "Zug"),
        ("ZH", "Zürich"),
    )

    def canton(self) -> Tuple[str, str]:
        """
        Randomly returns a swiss canton ('Abbreviated', 'Name').
        :example ('ZH', 'Zürich')
        """
        return self.random_element(self.cantons)

    def administrative_unit(self) -> str:
        """
        Randomly returns a Swiss canton name.
        :example 'Zürich'
        """
        return self.canton()[1]

    canton_name = administrative_unit

    def canton_code(self) -> str:
        """
        Randomly returns a Swiss canton code.
        :example 'ZH'
        """
        return self.canton()[0]
