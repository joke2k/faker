import random

from datetime import *

from .. import ElementsType
from .. import Provider as PassportProvider


class Provider(PassportProvider):
    """Implement passport provider for ``en_US`` locale.

    Sources:

    - https://travel.state.gov/content/travel/en/passports/passport-help/next-generation-passport.html
    - https://www.vitalrecordsonline.com/glossary/passport-book-number
    """

    passport_number_formats = (
        # NGP
        "?########",
        # Pre-NGP
        "#########",
    )

    def passport_Dates(self, birthday):
        """Generates a formatted date of birth, issue, and expiration dates.
        issue and expiration dates are conditioned to fall within U.S. standards of 5 and 10 year expirations


        The ``birthday`` argument is a datetime.date object representing a date of birth.

        Sources:

        - https://travel.state.gov/content/travel/en/passports/passport-help/faqs.html#:~:text=If%20you%20were%20age%2016,front%20of%20your%20passport%20card.
        """
        birth_date = birthday.strftime("%d ") + birthday.strftime("%b ") + birthday.strftime("%Y")
        today = date.today()
        age = (today - birthday).days // 365
        if age < 16:
            EXPIRY_YEARS = 5
            issue_date = self.generator.date_time_between(today - timedelta(days=EXPIRY_YEARS * 365 - 1), today)
            if age < 5:
                issue_date = self.generator.date_time_between(birthday, today)
            expiry_date = issue_date.replace(year=issue_date.year + EXPIRY_YEARS)

            issue_date_fromat = issue_date.strftime("%d ") + issue_date.strftime("%b ") + issue_date.strftime("%Y")
            expiry_date_format = expiry_date.strftime("%d ") + expiry_date.strftime("%b ") + expiry_date.strftime("%Y")
            return birth_date, issue_date_fromat, expiry_date_format
        elif age >= 26:
            EXPIRY_YEARS = 10
            issue_date = self.generator.date_time_between(today - timedelta(days=EXPIRY_YEARS * 365 - 1), today)
            expiry_date = issue_date.replace(year=issue_date.year + EXPIRY_YEARS)
            issue_date_fromat = issue_date.strftime("%d ") + issue_date.strftime("%b ") + issue_date.strftime("%Y")
            expiry_date_format = expiry_date.strftime("%d ") + expiry_date.strftime("%b ") + expiry_date.strftime("%Y")
            return birth_date, issue_date_fromat, expiry_date_format

        else:
            EXPIRY_YEARS = 10
            issue_date = self.generator.date_time_between(today - timedelta(days=EXPIRY_YEARS * 365 - 1), today)
            age_issue = (issue_date.date() - birthday).days // 365

            if age_issue < 16:
                EXPIRY_YEARS = 5
                issue_date = self.generator.date_time_between(
                    today - timedelta(days=EXPIRY_YEARS * 365 - 1), birthday + timedelta(days=16 * 365 - 1)
                )
                expiry_date = issue_date.replace(year=issue_date.year + EXPIRY_YEARS)

                issue_date_fromat = issue_date.strftime("%d ") + issue_date.strftime("%b ") + issue_date.strftime("%Y")
                expiry_date_format = (
                    expiry_date.strftime("%d ") + expiry_date.strftime("%b ") + expiry_date.strftime("%Y")
                )
                return birth_date, issue_date_fromat, expiry_date_format

            expiry_date = issue_date.replace(year=issue_date.year + EXPIRY_YEARS)
            issue_date_fromat = issue_date.strftime("%d ") + issue_date.strftime("%b ") + issue_date.strftime("%Y")
            expiry_date_format = expiry_date.strftime("%d ") + expiry_date.strftime("%b ") + expiry_date.strftime("%Y")
            return birth_date, issue_date_fromat, expiry_date_format

    def passport_gender(self, seed=None):
        """Generates a string representing the sex displayed on a passport

        Sources:

        - https://williamsinstitute.law.ucla.edu/publications/x-gender-markers-passports/
        """
        if seed != None:
            random.seed(seed)

        genders = ["M", "F", "X"]
        gender = random.choices(genders, weights=[0.493, 0.493, 0.014], k=1)[0]
        return gender

    def passport_full(self):
        """Generates a formatted sting with US Passport information"""
        DOB = self.passport_DOB()
        birth_date, issue_date, expiry_date = self.passport_Dates(DOB)
        sex = self.passport_gender()
        given_name, surname = self.passport_owner(gender=sex)
        number = self.passport_number()

        full_rep = (
            """surname: {f_n}\ngiven name:{s_n}\nsex: {s}\nDOB: {DOB}\nissued: {i}\nexpires: {e}\nnumber: {n}\n"""
        )
        full_rep = full_rep.format(
            f_n=given_name, s_n=surname, s=sex, DOB=birth_date, i=issue_date, e=expiry_date, n=number
        )
        return full_rep
