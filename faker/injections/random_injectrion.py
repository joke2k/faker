# coding=utf-8

import random


class RandomInjection(random.Random):

    def __init__(self, *args, **kwargs):
        super(RandomInjection, self).__init__(*args, **kwargs)
        self.sequence = iter([])

    def set_sequence(self, sequence):
        if type(sequence) == str:
            sequence = list(sequence)

        self.sequence = iter(list(map(int, sequence)))

    def get_element(self):
        return next(self.sequence, None)

    def randint(self, a, b):
        return self.get_element()

    def randrange(self, start, stop=None, step=1, _int=int, _maxwidth=None):
        return self.get_element()

