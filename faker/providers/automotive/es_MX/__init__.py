from collections import OrderedDict
from typing import Optional

from .. import Provider as AutomotiveProvider


class Provider(AutomotiveProvider):
    """Implement automotive provider for the ``es_MX`` locale.

    Mexican license plates are issued by each of the 32 federal entities
    (31 states plus Mexico City). Since 24 June 2016 the National Public
    Security System (SESNSP) coordinates a unified serial scheme so that the
    same combination is never repeated across the country. The dominant
    serial format for private vehicles is ``ABC-123-A`` (three letters, three
    digits and one trailing letter). Mexico City keeps its own historic
    ``A12-ABC`` layout, and a sizeable share of vehicles still carry plates
    issued under the older ``ABC-12-34`` (three letters, two digits, two
    digits) format used before the 2016 standardisation.

    The letters ``I``, ``O`` and ``Q`` are excluded from the serial in order
    to avoid confusion with the digits ``1`` and ``0``.

    Sources:

    - https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Mexico
    - https://es.wikipedia.org/wiki/Matr%C3%ADculas_automovil%C3%ADsticas_de_M%C3%A9xico
    - https://en.wikipedia.org/wiki/ISO_3166-2:MX
    """

    # Letters allowed in the serial. The Mexican standard drops ``I``, ``O``
    # and ``Q`` to avoid confusion with the digits ``1`` and ``0``.
    license_plate_letters = "ABCDEFGHJKLMNPRSTUVWXYZ"

    # ISO 3166-2:MX code -> official name for the 32 federal entities that
    # issue license plates. Names follow the official ``es`` spelling.
    license_plate_states = OrderedDict(
        [
            ("AGU", "Aguascalientes"),
            ("BCN", "Baja California"),
            ("BCS", "Baja California Sur"),
            ("CAM", "Campeche"),
            ("CHP", "Chiapas"),
            ("CHH", "Chihuahua"),
            ("CMX", "Ciudad de México"),
            ("COA", "Coahuila de Zaragoza"),
            ("COL", "Colima"),
            ("DUR", "Durango"),
            ("GUA", "Guanajuato"),
            ("GRO", "Guerrero"),
            ("HID", "Hidalgo"),
            ("JAL", "Jalisco"),
            ("MEX", "Estado de México"),
            ("MIC", "Michoacán de Ocampo"),
            ("MOR", "Morelos"),
            ("NAY", "Nayarit"),
            ("NLE", "Nuevo León"),
            ("OAX", "Oaxaca"),
            ("PUE", "Puebla"),
            ("QUE", "Querétaro"),
            ("ROO", "Quintana Roo"),
            ("SLP", "San Luis Potosí"),
            ("SIN", "Sinaloa"),
            ("SON", "Sonora"),
            ("TAB", "Tabasco"),
            ("TAM", "Tamaulipas"),
            ("TLA", "Tlaxcala"),
            ("VER", "Veracruz de Ignacio de la Llave"),
            ("YUC", "Yucatán"),
            ("ZAC", "Zacatecas"),
        ]
    )

    # ISO 3166-2:MX abbreviations of the 32 federal entities. Provided so
    # callers can generate state-aware data.
    license_plate_state_abbrs = tuple(license_plate_states.keys())

    # Distribution of the layouts in circulation. The post-2016 national
    # format is the most common one being issued today, followed by the
    # legacy format that is still seen on many vehicles, with Mexico City's
    # historic layout making up the remainder.
    license_formats = OrderedDict(
        [
            ("{{license_plate_unified}}", 0.6),
            ("{{license_plate_old}}", 0.3),
            ("{{license_plate_cdmx}}", 0.1),
        ]
    )

    def _serial_letters(self, count: int) -> str:
        """Return ``count`` random letters from the allowed alphabet."""
        return "".join(self.random_elements(self.license_plate_letters, length=count, use_weighting=False))

    def license_plate_unified(self) -> str:
        """Generate a plate using the unified national format ``ABC-123-A``.

        This is the standardised private-vehicle serial coordinated nationally
        since 24 June 2016.
        """
        return f"{self._serial_letters(3)}-{self.numerify('###')}-{self._serial_letters(1)}"

    def license_plate_old(self) -> str:
        """Generate a plate using the legacy format ``ABC-12-34``.

        This three-letter, two-digit, two-digit layout was the most common
        private-vehicle serial before the 2016 standardisation and remains in
        circulation.
        """
        return f"{self._serial_letters(3)}-{self.numerify('##')}-{self.numerify('##')}"

    def license_plate_cdmx(self) -> str:
        """Generate a Mexico City (CDMX) plate using the ``A12-ABC`` format."""
        return f"{self._serial_letters(1)}{self.numerify('##')}-{self._serial_letters(3)}"

    # Layouts used by motorcycle plates. The national standard is ``A123B``
    # (one letter, three digits, one letter); Mexico City uses ``1234 A``.
    motorcycle_license_formats = OrderedDict(
        [
            ("{{motorcycle_license_plate_national}}", 0.85),
            ("{{motorcycle_license_plate_cdmx}}", 0.15),
        ]
    )

    def license_plate(self) -> str:
        """Generate a Mexican license plate.

        The layout is chosen at random following the weights declared in
        :attr:`license_formats`.
        """
        return self.generator.parse(self.random_element(self.license_formats))

    def motorcycle_license_plate_national(self) -> str:
        """Generate a motorcycle plate using the national format ``A123B``."""
        return f"{self._serial_letters(1)}{self.numerify('###')}{self._serial_letters(1)}"

    def motorcycle_license_plate_cdmx(self) -> str:
        """Generate a Mexico City motorcycle plate using the ``1234 A`` format."""
        return f"{self.numerify('####')} {self._serial_letters(1)}"

    def motorcycle_license_plate(self) -> str:
        """Generate a Mexican motorcycle license plate.

        The layout is chosen at random following the weights declared in
        :attr:`motorcycle_license_formats`.
        """
        return self.generator.parse(self.random_element(self.motorcycle_license_formats))

    # Layouts used by public transport (taxi) plates. Both the
    # ``D-123-ABC`` and ``12-34-ABC`` patterns are in use for commercial
    # passenger vehicles.
    public_transport_license_formats = OrderedDict(
        [
            ("{{public_transport_license_plate_lettered}}", 0.5),
            ("{{public_transport_license_plate_numbered}}", 0.5),
        ]
    )

    def public_transport_license_plate_lettered(self) -> str:
        """Generate a taxi plate using the ``D-123-ABC`` format."""
        return f"{self._serial_letters(1)}-{self.numerify('###')}-{self._serial_letters(3)}"

    def public_transport_license_plate_numbered(self) -> str:
        """Generate a taxi plate using the ``12-34-ABC`` format."""
        return f"{self.numerify('##')}-{self.numerify('##')}-{self._serial_letters(3)}"

    def public_transport_license_plate(self) -> str:
        """Generate a Mexican public transport (taxi) license plate.

        The layout is chosen at random following the weights declared in
        :attr:`public_transport_license_formats`.
        """
        return self.generator.parse(self.random_element(self.public_transport_license_formats))

    def license_plate_state_abbr(self) -> str:
        """Return the ISO 3166-2 code of a random federal entity."""
        return self.random_element(self.license_plate_state_abbrs)

    def license_plate_state(self) -> str:
        """Return the official name of a random federal entity."""
        return self.license_plate_states[self.license_plate_state_abbr()]

    def license_plate_by_state(self, state_abbr: Optional[str] = None) -> str:
        """Generate a license plate prefixed with a federal entity code.

        If a value for ``state_abbr`` is provided it is used as the prefix
        regardless of validity. If ``None`` a valid ISO 3166-2 code is chosen
        at random. The result has the form ``"<state_abbr> <plate>"`` where
        ``<plate>`` follows the unified national layout.
        """
        state_abbr = state_abbr if state_abbr is not None else self.license_plate_state_abbr()
        return f"{state_abbr} {self.license_plate_unified()}"
