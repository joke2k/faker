from ..la import Provider as LoremProvider
from faker.utils.decorators import martianify


@martianify('word_list')
class Provider(LoremProvider):
    pass
