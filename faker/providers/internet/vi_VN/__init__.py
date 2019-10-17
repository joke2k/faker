# coding=utf-8

from .. import Provider as InternetProvider


class Provider(InternetProvider):
    """Internet generator for Vietnamese locale"""

    tlds = ('com', 'com.vn', 'org', 'org.vn', 'net',
            'net.vn', 'biz', 'info', 'edu', 'edu.vn')
