# coding=utf-8

from .. import Provider as CreditCardProvider
from .. import CreditCard
from collections import OrderedDict


class Provider(CreditCardProvider):

    # https://way2pay.ir/21653
    prefix_ansar = ["627381"]
    prefix_iran_zamin = ["505785"]
    prefix_hekmat = ["636949"]
    prefix_keshavarzi = ["603770"]
    prefix_shahr = ["502806"]
    prefix_mehr_eghtesad = ["606373"]
    prefix_sarmayeh = ["639607"]
    prefix_post_bank = ["627760"]
    prefix_tose = ["628157"]
    prefix_eghtesad_novin = ["627412"]
    prefix_meli = ["603799"]
    prefix_pasargad = ["502229"]
    prefix_tourism_bank = ["505416"]
    prefix_ghavamin = ["639599"]
    prefix_day = ["502938"]
    prefix_mellat = ["610433"]
    prefix_tejarat = ["585983"]
    prefix_moasse_mellal = ["606256"]
    prefix_saman_bank = ["621986"]
    prefix_kosar = ["505801"]
    prefix_refah = ["589463"]
    prefix_saderat = ["603761"]
    prefix_tat = ["621986"]
    prefix_sina = ["639346"]
    prefix_kar_afarin = ["627488"]
    prefix_sepah = ["589210"]
    prefix_maskan = ["628023"]
    prefix_parsian = ["622106"]
    prefix_bim = ["627961"]

    credit_card_types = OrderedDict((
        ('ansar', CreditCard(u'انصار', prefix_ansar, 16, security_code='CVV2')),
        ('iran_zamin', CreditCard(u'ایران زمین', prefix_iran_zamin, 16, security_code='CVV2')),
        ('hekmat', CreditCard(u'حکمت', prefix_hekmat, 16, security_code='CVV2')),
        ('keshavarzi', CreditCard(u'کشاورزی', prefix_keshavarzi, 16, security_code='CVV2')),
        ('shahr', CreditCard(u'شهر', prefix_shahr, 16, security_code='CVV2')),
        ('mehre_ghtesad', CreditCard(u'مهراقتصاد', prefix_mehr_eghtesad, 16, security_code='CVV2')),
        ('sarmayeh', CreditCard(u'سرمایه', prefix_sarmayeh, 16, security_code='CVV2')),
        ('post_bank', CreditCard(u'پست بانک', prefix_post_bank, 16, security_code='CVV2')),
        ('tose', CreditCard(u'توسعه', prefix_tose, 16, security_code='CVV2')),
        ('eghtesad_novin', CreditCard(u'اقتصاد نوین', prefix_eghtesad_novin, 16, security_code='CVV2')),
        ('meli', CreditCard(u'ملی', prefix_meli, 16, security_code='CVV2')),
        ('pasargad', CreditCard(u'پاسارگاد', prefix_pasargad, 16, security_code='CVV2')),
        ('tourism_bank', CreditCard(u'گردشگری', prefix_tourism_bank, 16, security_code='CVV2')),
        ('ghavamin', CreditCard(u'قوامین', prefix_ghavamin, 16, security_code='CVV2')),
        ('day', CreditCard(u'دی', prefix_day, 16, security_code='CVV2')),
        ('mellat', CreditCard(u'ملت', prefix_mellat, 16, security_code='CVV2')),
        ('tejarat', CreditCard(u'تجارت', prefix_tejarat, 16, security_code='CVV2')),
        ('mellal', CreditCard(u'ملل', prefix_moasse_mellal, 16, security_code='CVV2')),
        ('saman', CreditCard(u'سامان', prefix_saman_bank, 16, security_code='CVV2')),
        ('kosar', CreditCard(u'کوثر', prefix_kosar, 16, security_code='CVV2')),
        ('refah', CreditCard(u'رفاه', prefix_refah, 16, security_code='CVV2')),
        ('saderat', CreditCard(u'صادرات', prefix_saderat, 16, security_code='CVV2')),
        ('tat', CreditCard(u'تات', prefix_tat, 16, security_code='CVV2')),
        ('sina', CreditCard(u'سینا', prefix_sina, 16, security_code='CVV2')),
        ('kar_afarin', CreditCard(u'کار آفرین', prefix_kar_afarin, 16, security_code='CVV2')),
        ('sepah', CreditCard(u'سپه', prefix_sepah, 16, security_code='CVV2')),
        ('maskan', CreditCard(u'مسکن', prefix_maskan, 16, security_code='CVV2')),
        ('parsian', CreditCard(u'پارسیان', prefix_parsian, 16, security_code='CVV2')),
        ('bim', CreditCard(u'صنعت و معدن', prefix_bim, 16, security_code='CVV2')),
    ))

    def credit_card_expire(self, start='now', end='+3y', date_format='%y/%m'):
        expire_date = self.generator.date_time_between(start, end)
        return expire_date.strftime(date_format)
