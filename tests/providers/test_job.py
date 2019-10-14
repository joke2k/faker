# coding=utf-8

from __future__ import unicode_literals

import unittest

import six

from faker import Faker


class TestJob(unittest.TestCase):
    """
    Test Job
    """

    def setUp(self):
        self.factory = Faker()

    def test_job(self):
        job = self.factory.job()
        assert isinstance(job, six.string_types)


class TestKoKR(unittest.TestCase):
    """
    Test Job ko_KR
    """

    def setUp(self):
        self.factory = Faker('ko_KR')

    def test_job(self):
        job = self.factory.job()
        assert isinstance(job, six.string_types)


class TestHuHU(unittest.TestCase):
    "Tests the job module in the Hungarian locale."

    def setUp(self):
        self.factory = Faker('hu_HU')

    def test_job(self):
        job = self.factory.job()
        assert isinstance(job, six.string_types)


class TestHyAm(unittest.TestCase):
    """ Tests jobs in the hy_AM locale """

    def setUp(self):
        self.factory = Faker('hy_AM')

    def test_job(self):
        job = self.factory.job()
        assert isinstance(job, six.string_types)


class TestDeDe(unittest.TestCase):
    """ Tests jobs in the de_DE locale """

    def setUp(self):
        self.factory = Faker('de_DE')

    def test_job(self):
        job = self.factory.job()
        assert isinstance(job, six.string_types)


class TestFrFr(unittest.TestCase):
    """ Tests jobs in the fr_FR locale """

    def setUp(self):
        self.factory = Faker('fr_FR')

    def test_job(self):
        job = self.factory.job()
        assert isinstance(job, six.string_types)


class TestElGr(unittest.TestCase):
    """ Tests jobs in the el_GR locale """

    def setUp(self):
        self.factory = Faker('el_GR')

    def test_job(self):
        job = self.factory.job()
        assert isinstance(job, six.string_types)


class TestPtPt(unittest.TestCase):
    """ Tests jobs in the pt_PT locale """

    def setUp(self):
        self.factory = Faker('pt_PT')

    def test_job(self):
        job = self.factory.job()
        assert isinstance(job, six.string_types)


class TestPtBR(unittest.TestCase):
    """ Tests jobs in the pt_BR locale """

    def setUp(self):
        self.factory = Faker('pt_BR')

    def test_job(self):
        job = self.factory.job()
        assert isinstance(job, six.string_types)
