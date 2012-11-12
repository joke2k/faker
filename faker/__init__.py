from faker import providers

PROVIDERS_PACKAGE = providers.__package__

DEFAULT_LOCALE = 'en_US'

DEFAULT_PROVIDERS = (
    'Lorem', 'Address', 'Person', 'DateTime', 'Company', 'Internet', 'Miscelleneous', 'PhoneNumber', 'UserAgent'
    )

from faker.generator import  Generator
from faker.factory import  Factory

faker = Factory.create()

