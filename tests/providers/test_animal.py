# coding=utf-8
from __future__ import unicode_literals
import unittest
from faker import Faker
from tests import string_types

class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.factory = Faker()

    def test_animal(self):
        animal = self.factory.animal()
        assert isinstance(animal, string_types)