from faker.providers.passport import ElementsType
from faker.providers.passport import Provider as PassportProvider


class Provider(PassportProvider):
    """Passport provider for mk_MK locale (Macedonian).

    Sources:
    - https://en.wikipedia.org/wiki/Macedonian_passport
    - https://en.wikipedia.org/wiki/Machine-readable_passport

    Passport types:
    - P  — Ordinary (burgundy cover, biometric)
    - PD — Diplomatic
    - PS — Official (службен)

    Number format: 1 uppercase letter + 7 digits (9-char MRZ field, padded with '<')
    ICAO/MRZ country code: MKD
    Validity: 2 years (under 4), 5 years (4–27), 10 years (27+)
    """

    # 1 letter + 7 digits — fits standard ICAO 9-char MRZ passport number field
    passport_number_formats: ElementsType = ("?#######",)
