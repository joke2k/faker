from __future__ import unicode_literals
from . import BaseProvider


class Provider(BaseProvider):

    placeholder_services = (
        "http://placekitten.com/{width}/{height}",
        "http://placehold.it/{width}x{height}",
        "http://flickholdr.com/{width}/{height}",
        "http://www.lorempixum.com/{width}/{height}",
        "http://placedog.com/{width}/{height}",
        "http://dummyimage.com/{width}x{height}",
    )
    

    @classmethod
    def image_placeholder(cls, width=None, height=None):
        """
        Returns URL to placeholder image
        Example: http://placehold.it/640x480
        """
        width_ = width or cls.random_int(max=1024)
        height_ = height or cls.random_int(max=1024)
        placeholder_url = cls.random_element(cls.placeholder_services)
        return placeholder_url.format(width=width_, height=height_)
