from ..th import Provider as AddressProvider


class Provider(AddressProvider):

    building_number_formats = (
        "###",
        "##",
        "#",
        "###/#",
        "###/##",
        "##/#",
        "##/##",
        "#/#",
    )

    street_prefixes = [
        "ถนน",
        "ซอย",
        "ตรอก",
    ]

    postcode_formats = (
        # as per https://en.wikipedia.org/wiki/Postal_codes_in_Thailand
        "1###0",
        "2###0",
        "3###0",
        "4###0",
        "5###0",
        "6###0",
        "7###0",
        "8###0",
        "9###0",
    )
