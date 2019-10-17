# coding: utf-8
from __future__ import unicode_literals

from .. import Provider as DateTimeProvider


class Provider(DateTimeProvider):
    """Datetime generator for Vietnamese locale"""
    def day_of_week(self):
        day = self.date('%w')
        DAY_NAMES = {
            "0": "Chủ nhật",
            "1": "Thứ hai",
            "2": "Thứ ba",
            "3": "Thứ tư",
            "4": "Thứ năm",
            "5": "Thứ sáu",
            "6": "Thứ bảy",
        }
        return DAY_NAMES[day]

    def month_name(self):
        month = self.month()
        MONTH_NAMES = {
            "01": "Tháng một",
            "02": "Tháng hai",
            "03": "Tháng ba",
            "04": "Tháng tư",
            "05": "Tháng năm",
            "06": "Tháng sáu",
            "07": "Tháng bảy",
            "08": "Tháng tám",
            "09": "Tháng chín",
            "10": "Tháng mười",
            "11": "Tháng mười một",
            "12": "Tháng mười hai",
        }
        return MONTH_NAMES[month]
