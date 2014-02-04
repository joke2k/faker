AVAILABLE_LOCALES = [
    'en_US',
    'it_IT',
    'fr_FR',
    'pt_BR',
    'en_CA',
    'en_GB',
    'de_DE',
    'ru_RU'
] 
DEFAULT_LOCALE = AVAILABLE_LOCALES[0]

DEFAULT_PROVIDERS = (

    'lorem',
    'address',
    'person',
    'date_time',
    'company',
    'internet',
    'misc',
    'phone_number',
    'user_agent',
    'file',
    'python',
    'credit_card',
    'profile',
    'job',
    'image_placeholder'
)

from faker.generator import Generator
from faker.factory import Factory

Faker = Factory.create
