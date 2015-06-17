# coding=utf-8

import bisect
from faker.generator import random

def random_sample():
    return random.uniform(0.0, 1.0)


def cumsum(it):
    total = 0
    for x in it:
        total += x
        yield total


def choice_distribution(a, p):
    assert len(a) == len(p)

    cdf = list(cumsum(p))
    normal = cdf[-1]
    cdf2 = [float(i) / float(normal) for i in cdf]
    uniform_sample = random_sample()
    idx = bisect.bisect_right(cdf2, uniform_sample)

    return a[idx]
