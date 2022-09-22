from faker.factory import Factory
from faker.generator import Generator
from faker.proxy import Faker

VERSION = "14.2.0"

__all__ = ("Factory", "Generator", "Faker")

_faker = Faker()
name = _faker.name
seed = Faker.seed