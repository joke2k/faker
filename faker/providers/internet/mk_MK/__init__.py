from .. import Provider as InternetProvider


class Provider(InternetProvider):
    """Internet provider for mk_MK locale (Macedonian)."""

    user_name_formats = (
        "{{last_name_female}}.{{first_name_female}}",
        "{{last_name_male}}.{{first_name_male}}",
        "{{first_name_female}}.{{last_name_female}}",
        "{{first_name_male}}.{{last_name_male}}",
        "{{first_name}}##",
        "?{{last_name}}",
        "{{first_name}}{{year}}",
    )

    email_formats = (
        "{{user_name}}@{{free_email_domain}}",
        "{{user_name}}@{{domain_name}}",
    )

    free_email_domains = (
        "gmail.com",
        "yahoo.com",
        "hotmail.com",
        "on.net.mk",
        "t.mk",
        "telekom.mk",
        "neotel.mk",
        "alfa.mk",
        "mail.mk",
        "mtel.mk",
    )

    tlds = ("mk", "com", "net", "org", "edu", "gov.mk", "com.mk")

    # Macedonian Cyrillic → ASCII transliteration for usernames/domains
    replacements = (
        ("а", "a"),
        ("б", "b"),
        ("в", "v"),
        ("г", "g"),
        ("д", "d"),
        ("ѓ", "gj"),
        ("е", "e"),
        ("ж", "zh"),
        ("з", "z"),
        ("ѕ", "dz"),
        ("и", "i"),
        ("ј", "j"),
        ("к", "k"),
        ("л", "l"),
        ("љ", "lj"),
        ("м", "m"),
        ("н", "n"),
        ("њ", "nj"),
        ("о", "o"),
        ("п", "p"),
        ("р", "r"),
        ("с", "s"),
        ("т", "t"),
        ("ќ", "kj"),
        ("у", "u"),
        ("ф", "f"),
        ("х", "h"),
        ("ц", "ts"),
        ("ч", "ch"),
        ("џ", "dzh"),
        ("ш", "sh"),
        ("А", "a"),
        ("Б", "b"),
        ("В", "v"),
        ("Г", "g"),
        ("Д", "d"),
        ("Ѓ", "gj"),
        ("Е", "e"),
        ("Ж", "zh"),
        ("З", "z"),
        ("Ѕ", "dz"),
        ("И", "i"),
        ("Ј", "j"),
        ("К", "k"),
        ("Л", "l"),
        ("Љ", "lj"),
        ("М", "m"),
        ("Н", "n"),
        ("Њ", "nj"),
        ("О", "o"),
        ("П", "p"),
        ("Р", "r"),
        ("С", "s"),
        ("Т", "t"),
        ("Ќ", "kj"),
        ("У", "u"),
        ("Ф", "f"),
        ("Х", "h"),
        ("Ц", "ts"),
        ("Ч", "ch"),
        ("Џ", "dzh"),
        ("Ш", "sh"),
    )
