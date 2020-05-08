import datetime
import random

from faker.utils.checksums import calculate_luhn

from .. import Provider as SsnProvider


class Provider(SsnProvider):

    @staticmethod
    def _org_to_vat(org_id):
        org_id = org_id.replace('-', '')
        if len(org_id) == 10:
            org_id = '16' + org_id
        return 'SE{}01'.format(org_id)

    def ssn(self, min_age=18, max_age=90, long=False, dash=True):
        """
        Returns a 10 or 12 (long=True) digit Swedish SSN, "Personnummer".

        It consists of 10 digits in the form (CC)YYMMDD-SSSQ, where
        YYMMDD is the date of birth, SSS is a serial number
        and Q is a control character (Luhn checksum).

        Specifying dash=False will give a purely numeric string, suitable
        for writing direct to databases.

        http://en.wikipedia.org/wiki/Personal_identity_number_(Sweden)
        """

        age = datetime.timedelta(
            days=self.generator.random.randrange(min_age * 365, max_age * 365))
        birthday = datetime.datetime.now() - age
        yr_fmt = '%Y' if long else '%y'
        pnr_date = birthday.strftime('{}%m%d'.format(yr_fmt))
        chk_date = pnr_date[2:] if long else pnr_date
        suffix = str(self.generator.random.randrange(0, 999)).zfill(3)
        luhn_checksum = str(calculate_luhn(chk_date + suffix))
        hyphen = '-' if dash else ''
        pnr = '{}{}{}{}'.format(pnr_date, hyphen, suffix, luhn_checksum)

        return pnr

    ORG_ID_DIGIT_1 = (1, 2, 3, 5, 6, 7, 8, 9)

    def org_id(self, long=False, dash=True):
        """
        Returns a 10 or 12 digit Organisation ID for a Swedish
        company.
        (In Swedish) https://sv.wikipedia.org/wiki/Organisationsnummer
        """
        first_digits = list(self.ORG_ID_DIGIT_1)
        random.shuffle(first_digits)
        onr_one = str(first_digits.pop())
        onr_one += str(self.generator.random.randrange(0, 9)).zfill(1)
        onr_one += str(self.generator.random.randrange(20, 99))
        onr_one += str(self.generator.random.randrange(0, 99)).zfill(2)
        onr_two = str(self.generator.random.randrange(0, 999)).zfill(3)
        luhn_checksum = str(calculate_luhn(onr_one + onr_two))
        prefix = '16' if long else ''
        hyphen = '-' if dash else ''

        org_id = '{}{}{}{}{}'.format(prefix, onr_one, hyphen, onr_two, luhn_checksum)
        return org_id

    def vat_id(self):
        """
        http://ec.europa.eu/taxation_customs/vies/faq.html#item_11
        :return: A random Swedish VAT ID, based on a valid Org ID
        """
        oid = self.org_id(long=True, dash=False)
        vid = Provider._org_to_vat(oid)
        return vid

    def org_and_vat_id(self, long=False, dash=True):
        """Returns matching Org ID and VAT number"""
        oid = self.org_id(long=long, dash=dash)
        vid = Provider._org_to_vat(oid)
        return oid, vid
