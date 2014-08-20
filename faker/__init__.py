# coding=utf-8

VERSION = '0.4.2'


AVAILABLE_LOCALES = [
    'bg_BG',
    'cs_CZ',
    'de_DE',
    'dk_DK',
    'el_GR',
    'en_CA',
    'en_GB',
    'en_US',
    'es_ES',
    'es_MX',
    'fa_IR',
    'fi_FI',
    'fr_FR',
    'hi_IN',
    'it_IT',
    'ko_KR',
    'lt_LT',
    'lv_LV',
    'nl_NL',
    'pl_PL',
    'pt_BR',
    'ru_RU',
    'sl_SI',
    'zh_CN',
    'zh_TW'
]

DEFAULT_LOCALE = 'en_US'

DEFAULT_PROVIDERS = (
    'address',
    'color',
    'company',
    'credit_card',
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

from faker.generator import Generator
from faker.factory import Factory

Faker = Factory.create
