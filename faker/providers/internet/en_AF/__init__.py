from .. import Provider as InternetProvider


class Provider(InternetProvider):
    """Internet provider for Afghanistan (English Pashto locale)."""

    # Used by fake.safe_email()
    safe_email_tlds = ("com", "net", "org", "af")

    # Used by fake.free_email()
    free_email_domains = (
        "gmail.com",
        "yahoo.com",
        "hotmail.com",
        "outlook.com",
        "mail.af",
        "kabulmail.af",
        "afghanmail.af",
        "pashtomail.af",
    )

    # Used by fake.domain_name()
    tlds = (
        "com", "com", "com",
        "net", "org",
        "af", "af", "af",
    )
