# coding=utf-8

from __future__ import unicode_literals

import unittest
import re

from faker import Faker
from faker.providers.user_agent import Provider as UaProvider


class TestUserAgent(unittest.TestCase):
    """ Tests user_agent """

    def setUp(self):
        self.fake = Faker()
        Faker.seed(0)
        self.ua = UaProvider(self.fake)

    def test_android_platform_token(self):
        for _ in range(0, 1000):
            assert re.match(r"^(Android) (\d+)(\.\d){0,2}", self.ua.android_platform_token())

    def test_ios_platform_token(self):
        for _ in range(0, 1000):
            assert re.match(r"^(iPhone|iPad); CPU (iPhone|iPad) OS (\d+)(_\d){0,2} like Mac OS X",
                            self.ua.ios_platform_token())
