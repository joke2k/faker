from faker.providers import BaseProvider


class Provider(BaseProvider):
    def foo(self):
        return 'bar'
