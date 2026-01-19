from .. import Provider as AutomotiveProvider


class Provider(AutomotiveProvider):
    """Implement automotive provider for ``fr_FR`` locale.

    Sources:

    - https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_France
    """

    license_formats = (
        # New format (since 2009): AA-999-AA
        "??-###-??",
        # Old format (pre-2009): 999-AAA-99 (kept for historical compatibility)
        "###-???-##",
    )

    def license_plate_new_format(self) -> str:
        """Generate a French license plate in the new format (AA-999-AA) used since 2009.
        
        Returns:
            A license plate in the format AA-999-AA (e.g., AB-123-CD)
        """
        return self.bothify("??-###-??").upper()

    def license_plate_old_format(self) -> str:
        """Generate a French license plate in the old format (999-AAA-99) used before 2009.
        
        Returns:
            A license plate in the format 999-AAA-99 (e.g., 123-ABC-45)
        """
        return self.bothify("###-???-##").upper()
