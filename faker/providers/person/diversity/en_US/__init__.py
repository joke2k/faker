from faker import Faker
from faker.providers.person.en_US import Provider as BaseProvider


class DiversityProvider(BaseProvider):
    first_names = ....

fake = Faker()
fake.add_provider(DiversityProvider)

fake.name()
