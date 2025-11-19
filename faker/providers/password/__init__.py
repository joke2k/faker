import string
import random
import string
import numbers
from .. import BaseProvider

class Provider(BaseProvider):
    """Password generation provider"""
    password = []
    def generate_password(self, size: int) -> str:
        characters = string.ascii_letters+ string.digits + string.digits + string.punctuation + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(size))
        return password

