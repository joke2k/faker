# _*_ coding: utf-8 _*_
from __future__ import unicode_literals
from ..phone_number import Provider as PhoneNumberProvider

class Provider(PhoneNumberProvider):
    phonenumber_prefix = [134, 135, 136, 137, 138, 139, 147, 150,
                          151, 152, 157, 158, 159, 182, 187, 188,
                          130, 131, 132, 145, 155, 156, 185, 186,
                          145, 133, 153, 180, 181, 189]
    formats = [str(i) + "########" for i in phonenumber_prefix]

    @classmethod
    def phonenumber_prefix(cls):
        return cls.numerify(cls.random_element(cls.formats))
