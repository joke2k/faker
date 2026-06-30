from decimal import Decimal

from .. import Provider as GeoProvider


class Provider(GeoProvider):
    """Geo provider for mk_MK locale (Macedonian).

    Sources:
    - https://en.wikipedia.org/wiki/Geography_of_North_Macedonia
      Bounding box: lat 40.85°N – 42.37°N, lon 20.45°E – 23.03°E
      Center (Skopje): lat 41.9981°N, lon 21.4254°E
    """

    def local_latitude(self) -> Decimal:
        """Return a latitude within North Macedonia's bounding box."""
        return self.coordinate(center=41.6, radius=0.75)

    def local_longitude(self) -> Decimal:
        """Return a longitude within North Macedonia's bounding box."""
        return self.coordinate(center=21.74, radius=1.29)
