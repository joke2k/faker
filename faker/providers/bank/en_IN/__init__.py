from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``en_IN`` locale.
    Source: https://en.wikipedia.org/wiki/List_of_banks_in_India
    """

    country_code = "IN"

    # Bank codes used by Indian banks in their SWIFT (BIC) and IFSC codes.
    swift_bank_codes = (
        "BARB",  # Bank of Baroda
        "BKID",  # Bank of India
        "CBIN",  # Central Bank of India
        "CNRB",  # Canara Bank
        "FDRL",  # Federal Bank
        "HDFC",  # HDFC Bank
        "IBKL",  # IDBI Bank
        "ICIC",  # ICICI Bank
        "IDIB",  # Indian Bank
        "INDB",  # IndusInd Bank
        "IOBA",  # Indian Overseas Bank
        "KKBK",  # Kotak Mahindra Bank
        "MAHB",  # Bank of Maharashtra
        "PUNB",  # Punjab National Bank
        "SBIN",  # State Bank of India
        "UBIN",  # Union Bank of India
        "UCBA",  # UCO Bank
        "UTIB",  # Axis Bank
        "YESB",  # Yes Bank
    )

    banks = (
        "Bank of Baroda",
        "Bank of India",
        "Bank of Maharashtra",
        "Canara Bank",
        "Central Bank of India",
        "Indian Bank",
        "Indian Overseas Bank",
        "Punjab National Bank",
        "Punjab and Sind Bank",
        "Union Bank of India",
        "UCO Bank",
        "State Bank of India",
        "Axis Bank",
        "Bandhan Bank",
        "CSB Bank",
        "City Union Bank",
        "DCB Bank",
        "Dhanlaxmi Bank",
        "Federal Bank",
        "HDFC Bank",
        "ICICI Bank",
        "IDBI Bank",
        "IDFC First Bank",
        "IndusInd Bank",
        "Jammu & Kashmir Bank",
        "Karnataka Bank",
        "Karur Vysya Bank",
        "Kotak Mahindra Bank",
        "Nainital Bank",
        "RBL Bank",
        "South Indian Bank",
        "Tamilnad Mercantile Bank",
        "Yes Bank",
    )

    def bank(self) -> str:
        """Generate a bank name."""
        return self.random_element(self.banks)
