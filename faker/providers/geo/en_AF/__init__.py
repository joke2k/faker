from decimal import Decimal
from typing import Any, Tuple

from .. import Provider as GeoProvider


class Provider(GeoProvider):
    """
    Afghanistan geo coordinates provider.
    """

    # Afghanistan bounding polygon (approx rectangle)
    poly = (
        ("29.3772", "60.5176"),  # Nimroz (SW)
        ("38.4909", "74.8893"),  # Badakhshan (NE)
        ("36.7384", "60.0522"),  # Herat (NW)
        ("30.1440", "69.4948"),  # Kandahar (SE)
    )

    #: Places the generated coordinate is labelled with.
    places = (
        "Kabul", "Kandahar", "Herat", "Mazar-e Sharif", "Jalalabad",
        "Kunduz", "Ghazni", "Lashkargah", "Taloqan", "Puli Khumri",
        "Khost", "Sheberghan", "Charikar", "Gardez", "Farah",
    )

    def local_latlng(self, *args: Any, **kwargs: Any) -> Tuple[str, str, str]:
        """A coordinate inside Afghanistan, with the nearest named place."""
        return (
            str(self.local_latitude()),
            str(self.local_longitude()),
            self.random_element(self.places),
        )

    def local_latitude(self) -> Decimal:
        latitudes = [int(Decimal(t[0]) * 1000000) for t in self.poly]
        return Decimal(
            str(self.generator.random.randint(min(latitudes), max(latitudes)) / 1000000)
        ).quantize(Decimal("0.000001"))

    def local_longitude(self) -> Decimal:
        longitudes = [int(Decimal(t[1]) * 1000000) for t in self.poly]
        return Decimal(
            str(self.generator.random.randint(min(longitudes), max(longitudes)) / 1000000)
        ).quantize(Decimal("0.000001"))
