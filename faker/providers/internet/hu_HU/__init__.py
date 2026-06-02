from .. import Provider as InternetProvider


class Provider(InternetProvider):
    free_email_domains = (
        "gmail.com",
        "hotmail.com",
        "yahoo.com",
        # Hungarian free email providers (Magyar e-mail szolgáltatók):
        # https://madweb.hu/a-7-legjobb-ingyenesen-hasznalhato-e-mail-szolgaltatas/
        "freemail.hu",
        "citromail.hu",
        "indamail.hu",
        "mailbox.hu",
    )

    tlds = (
        "hu",
        "com",
        "com.hu",
        "info",
        "org",
        "net",
        "biz",
    )

    replacements = (
        ("ö", "o"),
        ("ü", "u"),
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ő", "o"),
        ("ú", "u"),
        ("ű", "u"),
    )
