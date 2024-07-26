from .. import Provider as DateTimeProvider

class Provider(DateTimeProvider):
    DAY_NAMES = {
        "0": "Chủ Nhật",
        "1": "Thứ Hai",
        "2": "Thứ Ba",
        "3": "Thứ Tư",
        "4": "Thứ Năm",
        "5": "Thứ Sáu",
        "6": "Thứ Bảy",
    }

    MONTH_NAMES = {
        "01": "Tháng Một",
        "02": "Tháng Hai",
        "03": "Tháng Ba",
        "04": "Tháng Tư",
        "05": "Tháng Năm",
        "06": "Tháng Sáu",
        "07": "Tháng Bảy",
        "08": "Tháng Tám",
        "09": "Tháng Chín",
        "10": "Tháng Mười",
        "11": "Tháng Mười Một",
        "12": "Tháng Mười Hai",
    }

    def day_of_week(self):
        day = self.date("%w")
        return self.DAY_NAMES[day]

    def month_name(self):
        month = self.month()
        return self.MONTH_NAMES[month]
