from .. import ElementsType
from .. import Provider as PhoneNumberProvider


class Provider(PhoneNumberProvider):
    formats: ElementsType[str] = (
        "###-##-##",
        "### ## ##",
        "0## ### ## ##",
        "0## ###-##-##",
        "+380 ## ###-##-##",
        "+380 ## ###-##-##",
        "+380 (##) ###-##-##",
        "+380 ## ### ## ##",
    )

    # info: https://ru.wikipedia.org/wiki/MSISDN
    msisdn_formats: ElementsType[str] = ("############",)

    # info: https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9_%D0%BF%D0%BB%D0%B0%D0%BD_%D0%BD%D1%83%D0%BC%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%B8_%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D1%8B
    # info: https://en.wikipedia.org/wiki/Telephone_numbers_in_Ukraine
    country_calling_codes: ElementsType[str] = (
        "+38031",
        "+38032",
        "+38033",
        "+38034",
        "+38035",
        "+38036",
        "+38037",
        "+38038",

        "+38041",
        "+38043",
        "+38044",
        "+38045",
        "+38046",
        "+38047",
        "+38048",
        "+38049",

        "+38050",
        "+38051",
        "+38052",
        "+38053",
        "+38054",
        "+38055",
        "+38056",
        "+38057",

        "+38061",
        "+38062",
        "+38063",
        "+38063",
        "+38065",
        "+38066",
        "+38067",
        "+38068",
        "+38069",

        "+38070",
        "+38071",
        "+38072",
        "+38073",

        "+3800",

        "+38090",
        "+38091",
        "+38092",
        "+38093",
        "+38094",
        "+38095",
        "+38096",
        "+38097",
        "+38098",
        "+38099",
    )
