__version__ = '0.1'

DEFAULT_LOCALE = 'en_US'

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

fake = Faker()
