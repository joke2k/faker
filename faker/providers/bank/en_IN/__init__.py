from string import ascii_uppercase, digits

from .. import Provider as BankProvider


class Provider(BankProvider):
    """Implement bank provider for ``en_IN`` locale.
    Source: https://en.wikipedia.org/wiki/List_of_banks_in_India
    """

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

    # Real four-letter IFSC bank codes used as the prefix of every branch's
    # code (e.g. ``SBIN`` for State Bank of India, ``UTIB`` for Axis Bank).
    ifsc_bank_codes = (
        "SBIN",  # State Bank of India
        "HDFC",  # HDFC Bank
        "ICIC",  # ICICI Bank
        "PUNB",  # Punjab National Bank
        "BARB",  # Bank of Baroda
        "CNRB",  # Canara Bank
        "UBIN",  # Union Bank of India
        "IOBA",  # Indian Overseas Bank
        "IDIB",  # Indian Bank
        "MAHB",  # Bank of Maharashtra
        "UCBA",  # UCO Bank
        "UTIB",  # Axis Bank (formerly UTI Bank)
        "KKBK",  # Kotak Mahindra Bank
        "YESB",  # Yes Bank
        "INDB",  # IndusInd Bank
        "FDRL",  # Federal Bank
        "IDFB",  # IDFC First Bank
        "KARB",  # Karnataka Bank
        "SIBL",  # South Indian Bank
        "RATN",  # RBL Bank
        "BKID",  # Bank of India
        "CBIN",  # Central Bank of India
        "PSIB",  # Punjab and Sind Bank
        "IBKL",  # IDBI Bank
    )

    def bank(self) -> str:
        """Generate a bank name."""
        return self.random_element(self.banks)

    def ifsc(self) -> str:
        """Generate an Indian Financial System Code (IFSC).

        An IFSC is the 11-character code that identifies a bank branch for
        electronic transfers (NEFT/RTGS/IMPS). It is made up of a four-letter
        bank code, a reserved ``0``, and a six-character branch code, e.g.
        ``SBIN0000123``.
        """
        bank_code = self.random_element(self.ifsc_bank_codes)
        branch_code = self.lexify("??????", letters=ascii_uppercase + digits)
        return f"{bank_code}0{branch_code}"
