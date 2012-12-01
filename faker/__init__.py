__version__ = '0.2'

AVAILABLE_LOCALES = ['en_US','it_IT','fr_FR']

DEFAULT_LOCALE = AVAILABLE_LOCALES[0]

DEFAULT_PROVIDERS = (
    'Lorem',
    'Address',
    'Person',
    'DateTime',
    'Company',
    'Internet',
    'Miscelleneous',
    'PhoneNumber',
    'UserAgent',
    'File',
    'Python',
)

from faker.generator import  Generator
from faker.factory import  Factory

def Faker(*args,**kwargs):
    return Factory.create(*args,**kwargs)
