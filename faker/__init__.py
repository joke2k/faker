AVAILABLE_LOCALES = ['en_US', 'it_IT', 'fr_FR', 'pt_BR']

DEFAULT_LOCALE = AVAILABLE_LOCALES[0]

DEFAULT_PROVIDERS = (
    'lorem',
    'address',
    'person',
    'date_time',
    'company',
    'internet',
    'miscelleneous',
    'phone_number',
    'user_agent',
    'file',
    'python',
    'credit_card',
)

from faker.generator import Generator
from faker.factory import Factory

Faker = Factory.create
