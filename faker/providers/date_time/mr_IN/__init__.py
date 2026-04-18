from .. import Provider as DateTimeProvider


class Provider(DateTimeProvider):
    # Source references (accessed 2026-04-18):
    # - https://mr.wikipedia.org/wiki/वार: (Marathi weekday naming)
    # - https://mr.wikipedia.org/wiki/महिने: (Marathi month naming)
    # Data is normalized for synthetic locale generation.
    DAY_NAMES = {
        "0": "रविवार",
        "1": "सोमवार",
        "2": "मंगळवार",
        "3": "बुधवार",
        "4": "गुरुवार",
        "5": "शुक्रवार",
        "6": "शनिवार",
    }

    MONTH_NAMES = {
        "01": "जानेवारी",
        "02": "फेब्रुवारी",
        "03": "मार्च",
        "04": "एप्रिल",
        "05": "मे",
        "06": "जून",
        "07": "जुलै",
        "08": "ऑगस्ट",
        "09": "सप्टेंबर",
        "10": "ऑक्टोबर",
        "11": "नोव्हेंबर",
        "12": "डिसेंबर",
    }

    def day_of_week(self) -> str:
        day = self.date("%w")
        return self.DAY_NAMES[day]

    def month_name(self) -> str:
        month = self.month()
        return self.MONTH_NAMES[month]
