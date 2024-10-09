from .. import Provider as DateTimeProvider


class Provider(DateTimeProvider):
    # Sourse: https://www.ganmarteba.ge/
    DAY_NAMES = {
        "0": "კვირა",
        "1": "ორშაბათი",
        "2": "სამშაბათი",
        "3": "ოთხშაბათი",
        "4": "ხუთშაბათი",
        "5": "პარასკევი",
        "6": "შაბათი",
    }

    MONTH_NAMES = {
        "01": "იანვარი",
        "02": "თებერვალი",
        "03": "მარტი",
        "04": "აპრილი",
        "05": "მაისი",
        "06": "ივნისი",
        "07": "ივლისი",
        "08": "აგვისტო",
        "09": "სექტემბერი",
        "10": "ოქტომბერი",
        "11": "ნოემბერი",
        "12": "დეკემბერი",
    }

    def day_of_week(self):
        day = self.date("%w")
        return self.DAY_NAMES[day]

    def month_name(self):
        month = self.month()
        return self.MONTH_NAMES[month]
