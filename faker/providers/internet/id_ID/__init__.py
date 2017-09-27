# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as InternetProvider


class Provider(InternetProvider):
    safe_email_tlds = ('com', 'net', 'id', 'id')
    tlds = ('com', 'com', 'com', 'net', 'org', 'id', 'id', 'id')
