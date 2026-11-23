from .. import Provider as DateTimeProvider


class Provider(DateTimeProvider):
    # Source references (accessed 2026-11-23):
    # - https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-dates-full/main/kn/ca-gregorian.json
    #   (Kannada weekday and Gregorian month names)
    DAY_NAMES = {
        "0": "ಭಾನುವಾರ",
        "1": "ಸೋಮವಾರ",
        "2": "ಮಂಗಳವಾರ",
        "3": "ಬುಧವಾರ",
        "4": "ಗುರುವಾರ",
        "5": "ಶುಕ್ರವಾರ",
        "6": "ಶನಿವಾರ",
    }

    MONTH_NAMES = {
        "01": "ಜನವರಿ",
        "02": "ಫೆಬ್ರವರಿ",
        "03": "ಮಾರ್ಚ್",
        "04": "ಏಪ್ರಿಲ್",
        "05": "ಮೇ",
        "06": "ಜೂನ್",
        "07": "ಜುಲೈ",
        "08": "ಆಗಸ್ಟ್",
        "09": "ಸೆಪ್ಟೆಂಬರ್",
        "10": "ಅಕ್ಟೋಬರ್",
        "11": "ನವೆಂಬರ್",
        "12": "ಡಿಸೆಂಬರ್",
    }

    def day_of_week(self) -> str:
        day = self.date("%w")
        return self.DAY_NAMES[day]

    def month_name(self) -> str:
        month = self.month()
        return self.MONTH_NAMES[month]
