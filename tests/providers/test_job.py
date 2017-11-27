# coding=utf-8

from __future__ import unicode_literals

import unittest

from faker import Faker

from tests import string_types


class TestJob(unittest.TestCase):
    """
    Test Job
    """

    def setUp(self):
        self.factory = Faker()

    def test_job(self):
        job = self.factory.job()
        assert isinstance(job, string_types)


class TestKoKR(unittest.TestCase):
    """
    Test Job ko_KR
    """

    def setUp(self):
        self.factory = Faker('ko_KR')

    def test_job(self):
        job = self.factory.job()
        assert isinstance(job, string_types)


class TestHuHU(unittest.TestCase):
    "Tests the job module in the Hungarian locale."

    def setUp(self):
        self.factory = Faker('hu_HU')

    def test_job(self):
        job = self.factory.job()
        assert isinstance(job, string_types)
