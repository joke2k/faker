from ..en_US import Provider as JobProvider
from faker.utils.decorators import martianify


@martianify('jobs')
class Provider(JobProvider):
    pass
