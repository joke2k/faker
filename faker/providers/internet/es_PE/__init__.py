from .. import Provider as InternetProvider


class Provider(InternetProvider):
    """
    Internet provider for es_PE locale.

    Sources:
    - TLD usage and registrations: local domain stats and common usage (.pe)
    - General conventions: ICANN and local registry (.pe)
    Accessed: 2026-02-07
    """

    # Safe TLDs for generating emails
    safe_email_tlds = ("com", "net", "org", "pe")

    # Top-level domains for Peru, with .com and .pe being the most common.
    tlds = ("com", "com", "com", "net", "org", "pe", "pe", "pe")
