from .. import Provider as AutomotiveProvider


class Provider(AutomotiveProvider):
    """Implement automotive provider for ``ar_DZ`` locale.

    Sources:

    - https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Algeria
    """

    WILAYA_CODES = tuple(f"{i:02d}" for i in range(1, 59))
    VEHICLE_CLASSES = tuple("123456789")

    def license_plate(self) -> str:
        serial = self.numerify("#####")
        vehicle_class = self.random_element(self.VEHICLE_CLASSES)
        year = self.numerify("##")
        wilaya = self.random_element(self.WILAYA_CODES)
        return f"{serial} {vehicle_class}{year} {wilaya}"
