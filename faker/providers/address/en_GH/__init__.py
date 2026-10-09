from .. import Provider as AddressProvider


class Provider(AddressProvider):
    city_formats = ("{{city}}",)
    street_name_formats = ("{{street_name}}",)
    street_address_formats = ("{{street_name}} {{building_number}}",)
    address_formats = ("{{street_address}}\n{{city}}",)
    building_number_formats = ("##", "###", "###")
    street_names = (
        "Oxford Street",
        "Liberation Road",
        "Independence Avenue",
        "Kwame Nkrumah Avenue",
        "George Bush Highway",
        "Cantonments Road",
        "Tema Motorway",
        "Ring Road",
        "Spintex Road",
        "Accra-Tema Highway",
        "Kumasi Road",
        "Airport Road",
    )
    cities = (
        "Accra",
        "Kumasi",
        "Tamale",
        "Takoradi",
        "Tema",
        "Cape Coast",
        "Sunyani",
        "Ho",
        "Bolgatanga",
        "Wa",
        "Koforidua",
        "Obuasi",
        "Sekondi",
        "Techiman",
        "Tarkwa",
        "Berekum",
        "Sefwi Wiawso",
        "Bibiani",
        "Mampong",
        "Axim",
        "Dunkwa-on-Offin",
        "Keta",
        "Salaga",
        "Bawku",
        "Navrongo",
        "Kpandu",
        "Hohoe",
        "Nalerigu",
        "Yendi",
        "Bimbilla",
        "Wenchi",
        "Dodi Papase",
        "Kintampo",
    )
    countries = ("Ghana",)
