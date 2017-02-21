from ..en_US import Provider as CompanyProvider
from faker.utils.decorators import martianify


@martianify('catch_phrase_words', 'bsWords', 'company_suffixes')
class Provider(CompanyProvider):
    pass
