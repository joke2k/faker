# coding=utf-8

import bisect
from faker.generator import random as mod_random


def random_sample(random=None):
    if random is None:
        random = mod_random
    return random.uniform(0.0, 1.0)


def cumsum(it):
    total = 0
    for x in it:
        total += x
        yield total


def choice_distribution(a, p, random=None):
    if random is None:
        random = mod_random

    assert len(a) == len(p)

    if hasattr(random, 'choices'):
        return random.choices(a, weights=p)[0]
    else:
        cdf = list(cumsum(p))
        normal = cdf[-1]
        cdf2 = [float(i) / float(normal) for i in cdf]
        uniform_sample = random_sample(random=random)
        idx = bisect.bisect_right(cdf2, uniform_sample)
        return a[idx]
