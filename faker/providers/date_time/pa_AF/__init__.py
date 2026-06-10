from faker.providers.date_time import Provider as DateTimeProvider


class Provider(DateTimeProvider):
    """DateTime provider for Pashto Afghanistan using Gregorian calendar."""

    # Pashto day names (starting from Saturday)
    day_names = (
        "پيلنۍ",   # Saturday
        "يونۍ",    # Sunday
        "دونۍ",    # Monday
        "منځنۍ",   # Tuesday
        "څلورنۍ",  # Wednesday
        "پينځنۍ",  # Thursday
        "جمعه",    # Friday
    )

    # Pashto month names (approximate mapping to Gregorian)
    month_names = (
        "",
        "وری",      # ~ January
        "غويی",     # ~ February
        "غبرګولی",  # ~ March
        "چنګاښ",    # ~ April
        "زمری",     # ~ May
        "وږی",      # ~ June
        "تله",      # ~ July
        "لړم",      # ~ August
        "لیندۍ",    # ~ September
        "مرغومی",   # ~ October
        "سلواغه",   # ~ November
        "کب",       # ~ December
    )

    def day_of_week(self) -> str:
        """Return Pashto day name."""
        day = self.date_object().weekday()  # 0 = Monday
        afg_index = (day + 2) % 7  # Shift so Saturday = 0
        return self.day_names[afg_index]

    def month_name(self) -> str:
        """Return Pashto month name."""
        month = self.date_object().month
        return self.month_names[month]
