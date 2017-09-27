# coding: utf-8

from __future__ import unicode_literals
from .. import Provider as DateTimeProvider

class Provider(DateTimeProvider):

    def day_of_week(self):
        day = self.date('%w')
        DAY_NAMES = {
            "0": "senin",
            "1": "selasa",
            "2": "rabu",
            "3": "kamis",
            "4": "jumat",
            "5": "sabtu",
            "6": "minggu",
        }

        return DAY_NAMES[day]

    def month_name(self):
        month = self.month()
        MONTH_NAMES = {
            "01": "januari",
            "02": "februari",
            "03": "maret",
            "04": "april",
            "05": "mei",
            "06": "juni",
            "07": "juli",
            "08": "agustus",
            "09": "september",
            "10": "oktober",
            "11": "november",
            "12": "desember",
        }

        return MONTH_NAMES[month]
