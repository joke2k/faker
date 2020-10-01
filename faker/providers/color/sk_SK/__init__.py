from faker.providers import BaseProvider


class Provider(BaseProvider):
    """Implement color provider for ``sk_SK`` locale."""

    safe_colors = (
        'čierna', 'gaštanová', 'zelená', 'námornícka', 'olivová',
        'fialová', 'zelenomodrá', 'limetková', 'modrá', 'strieborná',
        'sivá', 'žltá', 'fuchsiová', 'aquamarinová', 'biela',
    )
