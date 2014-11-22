import os


def list_module(module):
    path = os.path.dirname(module.__file__)
    return [i for i in os.listdir(path) if os.path.isdir(os.path.join(path, i))]