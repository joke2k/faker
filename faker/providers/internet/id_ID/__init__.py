# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as InternetProvider


class Provider(InternetProvider):
    tlds = ('com', 'com', 'com', 'net', 'org', 'id', 'ac.id', 'co.id', 'or.id', 'sch.id', 'web.id')
