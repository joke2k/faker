import bisect

from random import Random
from typing import Generator, Iterable, List, Optional, TypeVar

from faker.generator import random as mod_random


def random_sample(random: Optional[Random] = None) -> float:
    if random is None:
        random = mod_random
    return random.uniform(0.0, 1.0)


def cumsum(it: Iterable[float]) -> Generator[float, None, None]:
    total: float = 0
    for x in it:
        total += x
        yield total


T = TypeVar('T')


def choices_distribution_unique(
        a: List[T], p: List[float], random: Optional[Random] = None, length: int = 1,
) -> List[T]:
    # As of Python 3.7, there isn't a way to sample unique elements that takes
    # weight into account.
    if random is None:
        random = mod_random

    assert len(a) == len(p)
    assert len(a) >= length, "You can't request more unique samples than elements in the dataset."

    choices = []
    items = list(a)
    probabilities = list(p)
    for i in range(length):
        cdf = list(cumsum(probabilities))
        normal = cdf[-1]
        cdf2 = [float(i) / float(normal) for i in cdf]
        uniform_sample = random_sample(random=random)
        idx = bisect.bisect_right(cdf2, uniform_sample)
        item = items[idx]
        choices.append(item)
        probabilities.pop(idx)
        items.pop(idx)
    return choices


def choices_distribution(a: List[T], p: List[float], random: Optional[Random] = None, length: int = 1) -> List[T]:
    if random is None:
        random = mod_random

    assert len(a) == len(p)

    if hasattr(random, 'choices'):
        choices = random.choices(a, weights=p, k=length)
        return choices
    else:
        choices = []

        cdf = list(cumsum(p))
        normal = cdf[-1]
        cdf2 = [float(i) / float(normal) for i in cdf]
        for i in range(length):
            uniform_sample = random_sample(random=random)
            idx = bisect.bisect_right(cdf2, uniform_sample)
            item = a[idx]
            choices.append(item)
        return choices
