from .. import Provider as InternetProvider

class Provider(InternetProvider):
    
    # Safe TLDs for generating emails
    safe_email_tlds = ("com", "net", "org", "pe")
    
    # Top-level domains for Peru, with .com and .pe being the most common.
    tlds = ("com", "com", "com", "net", "org", "pe", "pe", "pe")

    # Replacements for Spanish accented characters are the same.
    # This helps in generating clean user names and domain names.
    replacements = (
        ("à", "a"),
        ("â", "a"),
        ("ã", "a"),
        ("á", "a"),
        ("ç", "c"),
        ("é", "e"),
        ("ê", "e"),
        ("í", "i"),
        ("ô", "o"),
        ("ö", "o"),
        ("õ", "o"),
        ("ó", "o"),
        ("ú", "u"),
    )
