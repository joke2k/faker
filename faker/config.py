# coding=utf-8
from faker.utils.loading import find_available_locales

DEFAULT_LOCALE = 'en_US'

DEFAULT_PROVIDERS = (
    'address',
    'barcode',
    'color',
    'company',
    'credit_card',
    'currency',
    'date_time',
    'file',
    'internet',
    'job',
    'lorem',
    'misc',
    'person',
    'profile',
    'python',
    'phone_number',
    'ssn',
    'user_agent',
)

AVAILABLE_LOCALES = find_available_locales(DEFAULT_PROVIDERS)
