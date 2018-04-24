# coding=utf-8

from __future__ import unicode_literals
from collections import OrderedDict

from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_female = OrderedDict((
        ('{{last_name}}{{first_name_female}}', 1.00),
    ))
    formats_male = OrderedDict((
        ('{{last_name}}{{first_name_male}}', 1.00),
    ))

    formats = formats_male.copy()
    formats.update(formats_female)

    # https://ko.wikipedia.org/wiki/%ED%95%9C%EA%B5%AD%EC%9D%98_%EC%84%B1%EC%94%A8%EC%99%80_%EC%9D%B4%EB%A6%84
    first_names_female = OrderedDict((
        ('영자', 1),
        ('정자', 1),
        ('순자', 1),
        ('정숙', 1),
        ('영숙', 1),
        ('영희', 1),
        ('미경', 1),
        ('미숙', 1),
        ('경희', 1),
        ('미영', 1),
        ('미정', 1),
        ('은주', 1),
        ('지영', 1),
        ('은정', 1),
        ('지혜', 1),
        ('지은', 1),
        ('수진', 1),
        ('유진', 1),
        ('민지', 1),
        ('수빈', 1),
        ('서연', 1),
        ('민서', 1),
        ('서현', 1),
        ('지민', 1),
        ('지우', 1),
    ))

    first_names_male = OrderedDict((
        ('영수', 1),
        ('영호', 1),
        ('영식', 1),
        ('정웅', 1),
        ('영철', 1),
        ('영길', 1),
        ('정수', 1),
        ('성수', 1),
        ('성호', 1),
        ('정호', 1),
        ('정훈', 1),
        ('성훈', 1),
        ('성진', 1),
        ('상훈', 1),
        ('지훈', 1),
        ('성민', 1),
        ('현우', 1),
        ('동현', 1),
        ('준영', 1),
        ('준호', 1),
        ('민준', 1),
        ('준혁', 1),
        ('지후', 1),
        ('서준', 1),
        ('주원', 1),
    ))

    first_names = first_names_male.copy()
    first_names.update(first_names_female)

    # https://ko.wikipedia.org/wiki/%ED%95%9C%EA%B5%AD%EC%9D%98_%EC%84%B1%EC%94%A8
    last_names = OrderedDict((
        ('김', 0.216),
        ('이', 0.148),
        ('박', 0.085),
        ('정', 0.049),
        ('최', 0.047),
        ('조', 0.029),
        ('강', 0.025),
        ('윤', 0.021),
        ('장', 0.021),
        ('임', 0.020),
        ('한', 0.019),
        ('오', 0.019),
        ('서', 0.019),
        ('신', 0.018),
        ('권', 0.018),
    ))
