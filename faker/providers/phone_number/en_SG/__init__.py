from __future__ import unicode_literals
from .. import Provider as PhoneNumberProvider

'''
Based on https://github.com/missbossy/Faker/tree/singapore
'''


class Provider(PhoneNumberProvider):
    formats = (
        '+65-6###-####',
        '+65-9###-####',
        '9###-####',
        '9###-####',
        '9###-####',
        '8###-####',
        '6###-####',
        '6###-####',
    )
