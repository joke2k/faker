# coding=utf-8
import unittest

from faker.injections.random_injectrion import RandomInjection


class RandomInjectionTest(unittest.TestCase):

    def setUp(self):
        self.random = RandomInjection()

    def test_set_sequence_list(self):
        sequence = [12, 1, 3]
        self.random.set_sequence(sequence)
        sequence.append(None)
        assert [self.random.get_element() for _ in range(len(sequence))] == sequence

    def test_set_sequence_str(self):
        sequence = '13645'
        self.random.set_sequence(sequence)
        sequence = list(map(int, list(sequence)))
        sequence.append(None)
        assert [self.random.get_element() for _ in range(len(sequence))] == sequence

    def test_randint(self):
        sequence = [124, 5, 8]
        self.random.set_sequence(sequence)
        sequence.append(None)
        assert [self.random.randint(1, 2) for _ in range(len(sequence))] == sequence

    def test_randrange(self):
        sequence = [4, 3, 355]
        self.random.set_sequence(sequence)
        sequence.append(None)
        assert [self.random.randrange(2) for _ in range(len(sequence))] == sequence
