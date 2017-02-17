from ..en_US import Provider as PersonProvider
from faker.utils.decorators import martianify


@martianify('first_names_female', 'first_names_male', 'first_names',
            'last_names', 'prefixes_female', 'prefixes_male',
            'suffixes_female', 'suffixes_male')
class Provider(PersonProvider):
    pass
