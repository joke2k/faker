from ..en_US import Provider as AddressProvider
from faker.utils.decorators import martianify


@martianify('city_prefixes', 'city_suffixes', 'street_suffixes', 'states',
            'states_abbr', 'military_state_abbr', 'military_ship_prefix',
            'military_apo_format', 'military_dpo_format',
            'secondary_address_formats')
class Provider(AddressProvider):
    pass
