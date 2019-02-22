from faker.utils.distribution import choices_distribution, choices_distribution_unique
from faker.utils.datasets import add_dicts
from faker.generator import random
import unittest
import json
import os

TEST_DIR = os.path.dirname(__file__)


class UtilsTestCase(unittest.TestCase):
    def test_choice_distribution(self):
        a = ('a', 'b', 'c', 'd')
        p = (0.5, 0.2, 0.2, 0.1)

        sample = choices_distribution(a, p)[0]
        assert sample in a

        with open(os.path.join(TEST_DIR, 'random_state.json'), 'r') as fh:
            random_state = json.load(fh)
        random_state[1] = tuple(random_state[1])

        random.setstate(random_state)
        samples = choices_distribution(a, p, length=100)
        a_pop = len([i for i in samples if i == 'a'])
        b_pop = len([i for i in samples if i == 'b'])
        c_pop = len([i for i in samples if i == 'c'])
        d_pop = len([i for i in samples if i == 'd'])

        boundaries = []
        tolerance = 5
        for probability in p:
            boundaries.append([100 * probability + tolerance,  100 * probability - tolerance])

        assert boundaries[0][0] > a_pop > boundaries[0][1]
        assert boundaries[1][0] > b_pop > boundaries[1][1]
        assert boundaries[2][0] > c_pop > boundaries[2][1]
        assert boundaries[3][0] > d_pop > boundaries[3][1]

    def test_choices_distribution_unique(self):
        a = ('a', 'b', 'c', 'd')
        p = (0.25, 0.25, 0.25, 0.25)
        with self.assertRaises(AssertionError):
            choices_distribution_unique(a, p, length=5)

        samples = choices_distribution_unique(a, p, length=4)
        assert len(set(samples)) == len(samples)

    def test_add_dicts(self):
        t1 = {'a': 1, 'b': 2}
        t2 = {'b': 1, 'c': 3}
        t3 = {'d': 4}

        result = add_dicts(t1, t2, t3)
        assert result == {'a': 1, 'c': 3, 'b': 3, 'd': 4}
