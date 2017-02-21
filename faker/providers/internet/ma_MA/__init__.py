from ..en_US import Provider as InternetProvider
from faker.utils.decorators import martianify


@martianify('free_email_domains', 'tlds', 'uri_pages', 'uri_paths',
            'uri_extensions')
class Provider(InternetProvider):
    pass
