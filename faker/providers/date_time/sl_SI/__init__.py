# coding: utf-8
from __future__ import unicode_literals

from .. import Provider as DateTimeProvider


class Provider(DateTimeProvider):

    @classmethod
    def day_of_week(cls):
        day = cls.date('%w')
        DAY_NAMES = {
            "0": "Nedelja",
            "1": "Ponedeljek",
            "2": "Torek",
            "3": "Sreda",
            "4": "Četrtek",
            "5": "Petek",
            "6": "Sobota",
        }
        return DAY_NAMES[day]

    @classmethod
    def month_name(cls):
        month = cls.month()
        MONTH_NAMES = {
            "01": "Januar",
            "02": "Februar",
            "03": "Marec",
            "04": "April",
            "05": "Maj",
            "06": "Junij",
            "07": "Julij",
            "08": "Avgust",
            "09": "September",
            "10": "Oktober",
            "11": "November",
            "12": "December",
        }
        return MONTH_NAMES[month]
