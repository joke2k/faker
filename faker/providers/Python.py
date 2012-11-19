from . import BaseProvider
from .Lorem import Provider as Lorem

class Provider(BaseProvider):

    @classmethod
    def dict(cls, count=50):
        """
         Use this function to generate data, returns a touple containing
         a list, a dictionary and a nested dictionary.
         """
        l = []; d = {}; nd = {}
        for i in range(count):
            d[Lorem.word()] = Lorem.words(10)
            l.append(Lorem.words(3))
            nd[Lorem.word()] = {i: Lorem.word(), i+1: [Lorem.words(2), Lorem.words(4), Lorem.words(3)], i+2: {i: Lorem.words(3), i+1: Lorem.words(4), i+2: [Lorem.words(2), Lorem.words(3)]}}

        return l, d, nd