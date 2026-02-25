from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``el_GR`` locale."""

    bban_format = "#######################"
    country_code = "GR"

    # Major GR banks (with a head office in Greece)
    # Source:
    # - https://www.bankofgreece.gr/en/main-tasks/supervision/supervised-institutions
    # Last verified: January 2026
    banks = (
        "Aegean Baltic Bank",
        "Alpha Bank",
        "Credia Bank",
        "Eurobank",
        "Optima Bank",
        "SNAPPI",
        "Vivabank",
        "Εθνική Τράπεζα",
        "Συνεταιριστική Τράπεζα Θεσσαλίας",
        "Συνεταιριστική Τράπεζα Καρδίτσας",
        "Συνεταιριστική Τράπεζα Χανίων",
        "Τράπεζα Ηπείρου",
        "Τράπεζα Πειραιώς",
    )
