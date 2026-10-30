from .. import Provider as BankProvider


class Provider(BankProvider):
    """Bank provider for mk_MK locale (Macedonian).

    Sources:
    - https://en.wikipedia.org/wiki/IBAN#IBAN_formats_by_country
      MK IBAN: MK + 2 check digits + 3-digit bank code + 10-digit account + 2 national check digits
      Total BBAN length: 15 digits/chars (3 bank + 10 account + 2 check)
    - https://en.wikipedia.org/wiki/List_of_banks_in_North_Macedonia
    """

    bban_format = "###############"
    country_code = "MK"

    banks = (
        "Народна банка на Република Северна Македонија",
        "Силк Роуд банка",
        "Халк банка",
        "Шпаркасе банка",
        "Капитал банка",
        "Комерцијална банка",
        "Развојна банка на Северна Македонија",
        "НЛБ банка",
        "ПроКредит банка",
        "Централна кооперативна банка",
        "Алта банка",
        "Стопанска банка",
        "Универзална инвестициона банка",
        "ТТК банка",
    )

    def bban(self) -> str:
        # The 2 national check digits are ISO 7064 MOD 97-10 over bank code + account.
        number = self.numerify("#############")
        return number + f"{98 - int(number) * 100 % 97:02}"
