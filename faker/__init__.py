AVAILABLE_LOCALES = [
    'en_US',
    'it_IT',
    'fr_FR',
    'pt_BR',
    'el_GR',
    'en_CA',
    'en_GB',
    'de_DE',
    'ru_RU',
    'cs_CZ',
    'fi_FI',
    'dk_DK',
    'es_MX',
    'es_ES',
    'pl_PL',
    'ko_KR',
    'zh_CN'
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
    'color',
)

from faker.generator import Generator
from faker.factory import Factory

Faker = Factory.create
