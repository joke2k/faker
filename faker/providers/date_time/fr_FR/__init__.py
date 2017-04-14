# coding: utf-8
from __future__ import unicode_literals

from .. import Provider as DateTimeProvider


class Provider(DateTimeProvider):

    @classmethod
    def day_of_week(cls):
        day = cls.date('%w')
        DAY_NAMES = {
            "0": "Dimanche",
            "1": "Lundi",
            "2": "Mardi",
            "3": "Mercredi",
            "4": "Jeudi",
            "5": "Vendredi",
            "6": "Samedi",
        }
        return DAY_NAMES[day]

    @classmethod
    def month_name(cls):
        month = cls.month()
        MONTH_NAMES = {
            "01": "Janvier",
            "02": "Février",
            "03": "Mars",
            "04": "Avril",
            "05": "Mai",
            "06": "Juin",
            "07": "Juillet",
            "08": "Août",
            "09": "Septembre",
            "10": "Octobre",
            "11": "Novembre",
            "12": "Décembre",
        }
        return MONTH_NAMES[month]
