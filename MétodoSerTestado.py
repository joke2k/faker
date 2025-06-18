from faker.providers import BaseProvider
import random
import string

class Provider(BaseProvider):
    def passport_number(self):
    
        letters = ''.join(random.choices(string.ascii_uppercase, k=2))
        numbers = ''.join(random.choices(string.digits, k=7))
        return letters + numbers
