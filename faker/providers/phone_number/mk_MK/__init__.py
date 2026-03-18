from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    """Phone number provider for mk_MK locale (Macedonian).

    Country code: +389
    Skopje area code: 02
    Other area codes: 03x
    Mobile prefixes: 07x
    """

    formats = (
        "+389(0)#########",
        "+389(0)## ######",
        "+389(0)## ### ###",
        "+3892#########",
        "02#########",
        "02## ######",
        "02## ### ###",
        "070 ### ###",
        "071 ### ###",
        "072 ### ###",
        "075 ### ###",
        "076 ### ###",
        "077 ### ###",
        "078 ### ###",
        "+38970 ### ###",
        "+38971 ### ###",
        "+38972 ### ###",
    )
