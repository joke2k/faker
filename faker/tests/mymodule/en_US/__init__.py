from __future__ import unicode_literals
from faker.providers import BaseProvider


class Provider(BaseProvider):
    def foo(self):
        return 'bar'
