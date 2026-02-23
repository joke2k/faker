from .. import Provider as InternetProvider


class Provider(InternetProvider):
    free_email_domains = (
        "gmail.com",
        "hotmail.com",
        "yahoo.com",
        # Hungarian free email providers: https://madweb.hu/a-7-legjobb-ingyenesen-hasznalhato-e-mail-szolgaltatas/ under section Magyar e-mail szolgáltatók: aka Hungarian email providers:
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
        ("ó", "i"),
        ("ő", "o"),
        ("ú", "u"),
        ("ű", "u"),
    )
