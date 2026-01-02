# faker/providers/automotive/es_PE/__init__.py

from .. import Provider as AutomotiveProvider


class Provider(AutomotiveProvider):
    """
    Implement automotive provider for ``es_PE`` locale.

    Sources:
    - https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Peru

    .. |license_plate_modern| replace::
       :meth:`license_plate_modern() <faker.providers.automotive.es_PE.Provider.license_plate_modern>`

    .. |license_plate_previous| replace::
       :meth:`license_plate_previous() <faker.providers.automotive.es_PE.Provider.license_plate_previous>`
    """

    # Format from 2010 onwards (most common)
    license_format_modern = "???-###"
    
    # Format from 1995 to 2010
    license_format_previous = "??-####"

    def license_plate_modern(self) -> str:
        """
        Generate a modern Peruvian license plate (format: LLL-NNN).
        This format has been in use since 2010.
        """
        return self.bothify(self.license_format_modern)

    def license_plate_previous(self) -> str:
        """
        Generate a previous-generation Peruvian license plate (format: LL-NNNN).
        This format was in use from 1995 to 2010.
        """
        return self.bothify(self.license_format_previous)

    def license_plate(self) -> str:
        """
        Generate a random Peruvian license plate.

        This method randomly chooses between the modern format (75% chance)
        and the previous format (25% chance) to generate the result.
        """
        if self.generator.random.randint(1, 4) > 1:
            return self.license_plate_modern()
        return self.license_plate_previous()
