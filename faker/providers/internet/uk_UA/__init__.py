# coding=utf-8
from __future__ import unicode_literals

from .. import Provider as InternetProvider


class Provider(InternetProvider):
    free_email_domains = [
        'email.ua', 'gmail.com', 'gov.ua', 'i.ua', 'meta.ua', 'ukr.net'
    ]
    tlds = ['com', 'info', 'net', 'org', 'ua', 'укр']
