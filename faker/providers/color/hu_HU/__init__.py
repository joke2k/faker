from faker.providers import BaseProvider


class Provider(BaseProvider):
    """Implement color provider for ``hu_HU`` locale."""

    safe_colors = (
        'fekete', 'bordó', 'zöld', 'királykék', 'oliva',
        'bíbor', 'kékeszöld', 'citromzöld', 'kék', 'ezüst',
        'szürke', 'sárga', 'mályva', 'akvamarin', 'fehér',
    )
