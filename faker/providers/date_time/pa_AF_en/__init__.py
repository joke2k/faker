from faker.providers.date_time import Provider as DateTimeProvider


class Provider(DateTimeProvider):
    """DateTime provider for English Afghanistan using Gregorian calendar."""
    
    # English day names (standard)
    day_names = (
        "Peelanay",   # Peelanay (Saturday)
        "Yonay",    # Yonay (Sunday)
        "Donay",    # Donay (Monday)
        "Manznay",   # Manznay (Tuesday)
        "Tsalornay",  # Tsalornay (Wednesday)
        "Pindznay",  # Pindznay (Thursday)
        "Juma",    # Juma (Friday)
    )
    
    # English month names (standard)
    month_names = (
        "",
        "", "Hamal", "Sawr", "Jawza", "Saratān", "Asad", "Sonbola",
        "Mizān", "Aqrab", "Qaws", "Jadi", "Dalwa", "Hut"
    )

    
    def day_of_week(self) -> str:
        """Return English day name."""
        day = self.date_object().weekday()  # 0 = Monday
        # Adjust so Saturday = 0 (Afghanistan week starts Saturday)
        afg_index = (day + 2) % 7
        return self.day_names[afg_index]
    
    def month_name(self) -> str:
        """Return English month name."""
        month = self.date_object().month
        return self.month_names[month]
