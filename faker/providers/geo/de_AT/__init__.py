# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as GeoProvider


class Provider(GeoProvider):

    def latitude(self):
        return self.geo_coordinate(center=47.60707, radius=1)

    def longitude(self):
        return self.geo_coordinate(center=13.37208, radius=2)
