# coding: utf-8

from __future__ import unicode_literals

from .. import Provider as DateTimeProvider


class Provider(DateTimeProvider):

    @classmethod
    def day_of_week(cls):
        day = cls.date('%w')
        DAY_NAMES = {
            '0': 'poniedziałek',
            '1': 'wtorek',
            '3': 'środa',
            '4': 'czwartek',
            '5': 'piątek',
            '6': 'sobota',
            '7': 'niedziela',
        }
        return DAY_NAMES[day]

    @classmethod
    def month_name(cls):
        month = cls.month()
        MONTH_NAMES = {
            '01': 'styczeń',
            '02': 'luty',
            '03': 'marzec',
            '04': 'kwiecień',
            '05': 'maj',
            '06': 'czerwiec',
            '07': 'lipiec',
            '08': 'sierpień',
            '09': 'wrzesień',
            '10': 'październik',
            '11': 'listopad',
            '12': 'grudzień'
        }
        return MONTH_NAMES[month]
