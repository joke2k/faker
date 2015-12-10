# coding=utf-8

from __future__ import unicode_literals

import unittest

from faker import Factory
from email_validator import validate_email


class zh_CN_FactoryTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = Factory.create(locale='zh_CN')

    def test_email(self):
        email = self.factory.email()
        validate_email(email, check_deliverability=False)
