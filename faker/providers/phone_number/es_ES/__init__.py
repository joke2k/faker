import itertools

from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    """
    According to official specs:
    https://avancedigital.mineco.gob.es/es-ES/Servicios/Numeracion/Documents/Guia_Numeracion.pdf
    """

    PREFIXES = (
        "6##",
        "70#",
        "71#",
        "72#",
        "73#",
        "74#",
        # 75-79 unassigned
        "800",
        "803",
        "806",
        "807",
        # 801, 802, 804, 805, 808, 809 unassigned
        "81#",
        "820",
        "821",
        "822",
        "823",
        "824",
        "825",
        "826",
        "827",
        "828",
        # 829 unassigned
        "83#",
        # 840 unassigned
        "841",
        "842",
        "843",
        "844",
        "845",
        "846",
        "847",
        "848",
        "849",
        "85#",
        "86#",
        # 870 unassigned
        "871",
        "872",
        "873",
        "874",
        "875",
        "876",
        "877",
        "878",
        "879",
        "880",
        "881",
        "882",
        "883",
        "884",
        "885",
        "886",
        "887",
        "888",
        # 889-899 unassigned
        "900",
        "901",
        "902",
        # 903-909 unassigned
        "91#",
        "920",
        "921",
        "922",
        "923",
        "924",
        "925",
        "926",
        "927",
        "928",
        # 929 unassigned
        "93#",
        # 940 unassigned
        "941",
        "942",
        "943",
        "944",
        "945",
        "946",
        "947",
        "948",
        "949",
        "95#",
        "96#",
        # 970 unassigned
        "971",
        "972",
        "973",
        "974",
        "975",
        "976",
        "977",
        "978",
        "979",
        "980",
        "981",
        "982",
        "983",
        "984",
        "985",
        "986",
        "987",
        "988",
        # 989-999 unassigned
    )
    PHONE_FORMATS = (
        "+34 xxx ### ###",
        "+34 xxx######",
        "+34 xxx ## ## ##",
        "+34xxx ### ###",
        "+34xxx######",
        "+34xxx ## ## ##",
    )
    formats = tuple(
        phone_format.replace("xxx", prefix)
        for (prefix, phone_format) in itertools.product(PREFIXES, PHONE_FORMATS)
    )
