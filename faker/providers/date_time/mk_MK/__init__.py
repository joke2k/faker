from .. import Provider as DateTimeProvider


class Provider(DateTimeProvider):
    """Date/time provider for mk_MK locale (Macedonian)."""

    # Days of week in Macedonian
    DAY_NAMES = {
        "0": "Понеделник",
        "1": "Вторник",
        "2": "Среда",
        "3": "Четврток",
        "4": "Петок",
        "5": "Сабота",
        "6": "Недела",
    }

    # Months in Macedonian
    MONTH_NAMES = {
        "01": "Јануари",
        "02": "Февруари",
        "03": "Март",
        "04": "Април",
        "05": "Мај",
        "06": "Јуни",
        "07": "Јули",
        "08": "Август",
        "09": "Септември",
        "10": "Октомври",
        "11": "Ноември",
        "12": "Декември",
    }

    def day_of_week(self) -> str:
        return self.DAY_NAMES[self.date("%w")]

    def month_name(self) -> str:
        return self.MONTH_NAMES[self.month()]
