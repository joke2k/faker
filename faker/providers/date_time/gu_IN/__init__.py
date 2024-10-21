from .. import Provider as DateTimeProvider


class Provider(DateTimeProvider):

    DAY_NAMES = {
        "0": "Ravivar",
        "1": "Somvar",
        "2": "Mangalvar",
        "3": "Budhvar",
        "4": "Guruvar",
        "5": "Shukravar",
        "6": "Shanivar",
    }

    DAY_NAMES_IN_GUJARATI = {
        "0": "રવિવાર",
        "1": "સોમવાર",
        "2": "મંગળવાર",
        "3": "બુધવાર",
        "4": "ગુરુવાર",
        "5": "શુક્રવાર",
        "6": "શનિવાર",
    }

    MONTH_NAMES = {
        "01": "Kartak",
        "02": "Magshar",
        "03": "Posh",
        "04": "Maha",
        "05": "Fagan",
        "06": "Chaitra",
        "07": "Vaishakh",
        "08": "Jeth",
        "09": "Ashadh",
        "10": "Shravan",
        "11": "Bhadarvo",
        "12": "Aaso",
    }

    MONTH_NAMES_IN_GUJARATI = {
        "01": "કારતક",
        "02": "માગશર",
        "03": "પોષ",
        "04": "મહા",
        "05": "ફાગણ",
        "06": "ચૈત્ર",
        "07": "વૈશાખ",
        "08": "જેઠ",
        "09": "અષાઢ",
        "10": "શ્રાવણ",
        "11": "ભાદરવો",
        "12": "આસો",
    }

    def day_of_week(self) -> str:
        day = self.date("%w")
        return self.DAY_NAMES[day]

    def month_name(self) -> str:
        month = self.month()
        return self.MONTH_NAMES[month]

    def day_of_week_in_guj(self) -> str:
        """Returns day of the week in `Gujarati`"""
        day = self.date("%w")
        return self.DAY_NAMES_IN_GUJARATI[day]

    def month_name_in_guj(self) -> str:
        """Returns month name in `Gujarati`"""
        month = self.month()
        return self.MONTH_NAMES_IN_GUJARATI[month]

    def month_in_guj(self) -> str:
        """Returns month name in `Gujarati`"""
        return self.month_name_in_guj()
