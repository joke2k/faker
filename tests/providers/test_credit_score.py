#  -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import re

from faker import Faker


class TestEnUS(unittest.TestCase):
    def setUp(self):
        self.factory = Faker("en_US")
        self.factory.seed(0)

    def test_random_credit_score(self):
        for _ in range(100):
            credit_score = self.factory.credit_score()
            assert 300 <= credit_score <= 850

    def test_credit_score_of_a_specific_type(self):
        for _ in range(100):
            credit_score = self.factory.credit_score("fico8")
            assert 300 <= credit_score <= 850

    def test_random_credit_score_provider(self):
        for _ in range(100):
            provider = self.factory.credit_score_provider()
            assert provider in ("FICO", "Experian", "Equifax", "TransUnion")

    def test_credit_score_provider_of_a_specific_type(self):
        for _ in range(100):
            provider = self.factory.credit_score_provider("fico5")
            assert provider == "Equifax"

    def test_random_credit_score_name(self):
        for _ in range(100):
            name = self.factory.credit_score_name()
            assert name in (
                "FICO Score 8",
                "Equifax Beacon 5.0",
                "Experian/Fair Isaac Risk Model V2SM",
                "TransUnion FICO Risk Score, Classic 04",
            )

    def test_credit_score_name_of_a_specific_type(self):
        for _ in range(100):
            name = self.factory.credit_score_name("fico5")
            assert name == "Equifax Beacon 5.0"

    def test_random_credit_score_full(self):
        """ Output looks like this (provider/model is random):
        Equifax Beacon 5.0
        Equifax
        660
        """
        for _ in range(100):
            output = self.factory.credit_score_full()
            assert re.match(r".+\n.+\n\d{3}\n", output)

    def test_credit_score_full_of_a_specific_type(self):
        """ Output looks like this:
        Equifax Beacon 5.0
        Equifax
        660
        """
        for _ in range(100):
            output = self.factory.credit_score_full("fico5")
            assert re.match(r"Equifax Beacon 5\.0\nEquifax\n\d{3}\n", output)
