from .. import ElementsType
from .. import Provider as PassportProvider


class Provider(PassportProvider):
    """Implement passport provider for ``de_AT`` locale.

    Sources:

    - https://www.bmi.gv.at/607/Reisepass.aspx
    """

    passport_number_formats: ElementsType[str] = (
        "?#######",
        "??#######",
    )
