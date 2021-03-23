import sys
import random

weighting = [10, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

def validate(abn):
    """
    Validate that the provided number is indeed an ABN.
    """
    values = map(int, list(abn))
    values[0] -= 1
    total = sum([x * w for (x, w) in zip(values, weighting)])
    return total % 89 == 0

def abn():
    """
    Generate a random ABN
    """
    value = ''.join([str(int(random.random() * 10)) for i in range(9)])
    temp = list('00%s' % value)
    total = sum([w * x for (w,x) in zip(weighting, map(int, temp))])
    remainder = total % 89
    prefix = 10 + (89 - remainder)
    abn = '%s%s' % (prefix, value)
    assert validate(abn), '%s is not a valid ABN' % abn
    return abn

sys.stdout.write(abn())