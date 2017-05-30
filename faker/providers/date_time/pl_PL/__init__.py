# coding: utf-8

from __future__ import unicode_literals

from .. import Provider as DateTimeProvider


class Provider(DateTimeProvider):

    DAY_NAMES = {
        '0': 'poniedziałek',
        '1': 'wtorek',
        '2': 'środa',
        '3': 'czwartek',
        '4': 'piątek',
        '5': 'sobota',
        '6': 'niedziela',
    }

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

    @classmethod
    def day_of_week(cls):
        day = cls.date('%w')
        return cls.DAY_NAMES[day]

    @classmethod
    def month_name(cls):
        month = cls.month()
        return cls.MONTH_NAMES[month]
