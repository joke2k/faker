from .. import Provider as DateTimeProvider


class Provider(DateTimeProvider):
    DAY_NAMES = {
        "0": "Dushanba",
        "1": "Seshanba",
        "2": "Chorshanba",
        "3": "Payshanba",
        "4": "Juma",
        "5": "Shanba",
        "6": "Yakshanba",
    }

    MONTH_NAMES = {
        "01": "Yanvar",
        "02": "Fevral",
        "03": "Mart",
        "04": "Aprel",
        "05": "May",
        "06": "Iyun",
        "07": "Iyul",
        "08": "Avgust",
        "09": "Sentabr",
        "10": "Oktabr",
        "11": "Noyabr",
        "12": "Dekabr",
    }

    def day_of_week(self) -> str:
        day = self.date("%w")
        return self.DAY_NAMES[day]

    def month_name(self) -> str:
        month = self.month()
        return self.MONTH_NAMES[month]
