from .. import Provider as InternetProvider


class Provider(InternetProvider):
    """Implement internet provider for ``en_IN`` locale.

    Second-level domains under ``.in`` are listed by the registry:
    https://www.registry.in/policies
    """

    free_email_domains = (
        "gmail.com",
        "yahoo.com",
        "yahoo.co.in",
        "hotmail.com",
        "outlook.com",
        "rediffmail.com",
    )

    tlds = (
        "com",
        "com",
        "com",
        "in",
        "in",
        "co.in",
        "co.in",
        "net",
        "org",
        "net.in",
        "org.in",
        "firm.in",
        "biz",
        "info",
    )
