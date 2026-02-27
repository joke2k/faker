from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``en_GB`` locale."""
    
    # UK IBANS start with GB, 2 check digits, a 4 char bank code, 
    # a 6 digit sort code, and a 8 digit account number.
    bban_format = "????##############"
    country_code = "GB"

    # Major UK Banks
    # Last verified February 2026. According to Google.
    banks = (
        "Barclays",
        "HSBC",
        "Lloyds Bank",
        "Metro Bank",
        "Monzo Bank",
        "Natwest",
        "Santander UK",
        "Nationwide Building Society",
        "Royal Bank of Scotland",
        "Standard Chartered",
        "Starling Bank",
        "TSB Bank",
    )

    def bank(self):
        """Generate a bank name."""

        # Randomly select and return one bank name from the BANKS tuple above.
        return self.random_element(self.banks)