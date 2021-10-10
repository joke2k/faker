from .. import Provider as DateTimeProvider


class Provider(DateTimeProvider):

    DAY_NAMES = {
        "0": "রবিবার",
        "1": "সোমবার",
        "2": "মঙ্গলবার",
        "3": "বুধবার",
        "4": "বৃহস্পতিবার",
        "5": "শুক্রবার",
        "6": "শনিবার",
    }

    MONTH_NAMES = {
        "01": "জানুয়ারি",
        "02": "ফেব্রুয়ারি",
        "03": "মার্চ",
        "04": "এপ্রিল",
        "05": "মে",
        "06": "জুন",
        "07": "জুলাই",
        "08": "আগস্ট",
        "09": "সেপ্টেম্বর",
        "10": "অক্টোবর",
        "11": "নভেম্বর",
        "12": "ডিসেম্বর",
    }

    def day_of_week(self) -> str:
        day = self.date("%w")
        return self.DAY_NAMES[day]

    def month_name(self) -> str:
        month = self.month()
        return self.MONTH_NAMES[month]
