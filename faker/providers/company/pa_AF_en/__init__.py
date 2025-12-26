import random
from .. import Provider as CompanyProvider

class Provider(CompanyProvider):
    """Afghanistan companies in English."""

    companies = (
        "Afghan Telecom",
        "Afghan Wireless Communication Company",
        "Roshan Telecom",
        "Azizi Bank",
        "Bank-e-Millie Afghan",
        "Da Afghanistan Bank",
        "First MicroFinance Bank-Afghanistan",
        "Ariana Afghan Airlines",
        "Kam Air",
        "East Horizon Airlines",
        "Khyber Afghan Airlines",
        "Moby Media Group",
        "Pajhwok Afghan News",
        "Ariana TV",
        "New Kabul Bank",
        "Pashtany Bank",
        "Baghlan Sugar Factory",
        "Bayat Power",
        "AZ Corporation",
        "Salam Afghan Telecom",
        "ATOMA Telecom",
    )

    def company(self):
        return random.choice(self.companies)
