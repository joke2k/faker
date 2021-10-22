import bisect
import itertools

from random import Random
from typing import Generator, Iterable, Optional, Sequence, TypeVar

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


T = TypeVar("T")


def choices_distribution_unique(
    a: Sequence[T],
    p: Optional[Sequence[float]],
    random: Optional[Random] = None,
    length: int = 1,
) -> Sequence[T]:
    # As of Python 3.7, there isn't a way to sample unique elements that takes
    # weight into account.
    if random is None:
        random = mod_random

    assert p is not None
    assert len(a) == len(p)
    assert len(a) >= length, "You can't request more unique samples than elements in the dataset."

    choices = []
    items = list(a)
    probabilities = list(p)
    for i in range(length):
        cdf = tuple(cumsum(probabilities))
        normal = cdf[-1]
        cdf2 = [i / normal for i in cdf]
        uniform_sample = random_sample(random=random)
        idx = bisect.bisect_right(cdf2, uniform_sample)
        item = items[idx]
        choices.append(item)
        probabilities.pop(idx)
        items.pop(idx)
    return choices


def choices_distribution(
    a: Sequence[T],
    p: Optional[Sequence[float]],
    random: Optional[Random] = None,
    length: int = 1,
) -> Sequence[T]:
    if random is None:
        random = mod_random

    if p is not None:
        assert len(a) == len(p)

    if hasattr(random, "choices"):
        if length == 1 and p is None:
            return [random.choice(a)]
        else:
            return random.choices(a, weights=p, k=length)
    else:
        choices = []

        if p is None:
            p = itertools.repeat(1, len(a))  # type: ignore

        cdf = list(cumsum(p))  # type: ignore
        normal = cdf[-1]
        cdf2 = [i / normal for i in cdf]
        for i in range(length):
            uniform_sample = random_sample(random=random)
            idx = bisect.bisect_right(cdf2, uniform_sample)
            item = a[idx]
            choices.append(item)
        return choices
