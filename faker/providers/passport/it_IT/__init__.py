from .. import ElementsType
from .. import Provider as PassportProvider


class Provider(PassportProvider):
    """Implement passport provider for ``it_IT``.

    Sources:

    - https://www.poliziadistato.it/articolo/10301
    - https://www.poliziadistato.it/statics/32/note_tecniche.pdf
    """

    electronic_passport_number_formats: ElementsType[str] = (
        # standard passaporto elettronico (elettronic passport)
        # Format: 2 letters, 7 digits (e.g., YA1234567), used from 2010 on
        "??#######",
    )

    def passport_number(self) -> str:
        """
        Generate a valid Italian passport number

        The format consist in 2 uppercase letters followed by 7 digits.
        """

        # select the passport number format
        format = self.random_element(self.electronic_passport_number_formats)

        return self.bothify(format).upper()
