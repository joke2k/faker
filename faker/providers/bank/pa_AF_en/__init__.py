from .. import Provider as BankProvider
import random


class Provider(BankProvider):
    """Afghan Bank provider in English"""

    country_code = "AF"
    bban_format = "AF################"

    swift_bank_codes = (
        "DAAF", "AZBK", "KBLK", "MWBK", "PSBK",
        "AUAF", "FMBK", "STCA", "BMIA", "GHZN",
    )
    swift_location_codes = ("KA", "HE", "LO", "PA", "KU", "BE", "FA", "ZA", "JO", "GH")
    swift_branch_codes = ("001", "002", "003", "004", "005", "ATM", "HQ", "BR1", "BR2")

    banks = (
        "Da Afghanistan Bank",
        "Azizi Bank",
        "Kabul Bank",
        "Maiwand Bank",
        "Pashtany Bank",
        "Afghan United Bank",
        "First MicroFinance Bank",
        "Standard Chartered Bank Afghanistan",
        "Bank-e-Millie Afghan",
        "Ghazanfar Bank",
    )
    def bank_name(self):
        return random.choice(self.banks)

    def account_number(self):
        return "AF" + "".join(str(random.randint(0, 9)) for _ in range(16))

    def swift_code(self):
        bank_code = random.choice(self.swift_bank_codes)
        location = random.choice(self.swift_location_codes)
        branch = random.choice(self.swift_branch_codes)
        return f"{bank_code}{location}{branch}"
