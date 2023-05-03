import re
import random
from datetime import *
from string import ascii_uppercase

from .. import BaseProvider, ElementsType

localized = True


class Provider(BaseProvider):
    """Implement default Passport provider for Faker."""
    passport_number_formats: ElementsType = ()

    def Dates(self):
        
        birthday = self.generator.date_of_birth()
        birth_date = birthday.strftime("%d ") +birthday.strftime("%b ") + birthday.strftime("%Y")
        today = date.today()
        age = (today-birthday).days//365 
        if age<16:
            EXPIRY_YEARS = 5
            issue_date = self.generator.date_time_between(today - timedelta(days=EXPIRY_YEARS*365 -1), today)
            if age<5:
                issue_date = self.generator.date_time_between(birthday, today)
            expiry_date = issue_date + timedelta(days=EXPIRY_YEARS*365)

            issue_date_fromat = issue_date.strftime("%d ") +issue_date.strftime("%b ") + issue_date.strftime("%Y")
            expiry_date_format = expiry_date.strftime("%d ") +expiry_date.strftime("%b ") + expiry_date.strftime("%Y")
            return birth_date, issue_date_fromat, expiry_date_format
        elif age>=26:
            EXPIRY_YEARS = 10
            issue_date = self.generator.date_time_between(today - timedelta(days=EXPIRY_YEARS*365 -1), today)
            expiry_date = issue_date + timedelta(days=EXPIRY_YEARS*365)
            issue_date_fromat = issue_date.strftime("%d ") +issue_date.strftime("%b ") + issue_date.strftime("%Y")
            expiry_date_format = expiry_date.strftime("%d ") +expiry_date.strftime("%b ") + expiry_date.strftime("%Y")
            return birth_date, issue_date_fromat, expiry_date_format
        
        else:
            EXPIRY_YEARS = 10
            issue_date = self.generator.date_time_between(today - timedelta(days=EXPIRY_YEARS*365 -1), today)
            age_issue = (issue_date.date()-birthday).days//365 

            if age_issue<16:
                EXPIRY_YEARS = 5
                issue_date = self.generator.date_time_between(
                    today - timedelta(days=EXPIRY_YEARS*365 -1), birthday+timedelta(days=16*365 -1))
                expiry_date = issue_date + timedelta(days=EXPIRY_YEARS*365)

                issue_date_fromat = issue_date.strftime("%d ") +issue_date.strftime("%b ") + issue_date.strftime("%Y")
                expiry_date_format = expiry_date.strftime(
                    "%d ") +expiry_date.strftime("%b ") + expiry_date.strftime("%Y")
                return birth_date, issue_date_fromat, expiry_date_format
            
            expiry_date = issue_date + timedelta(days=EXPIRY_YEARS*365)
            issue_date_fromat = issue_date.strftime("%d ") +issue_date.strftime("%b ") + issue_date.strftime("%Y")
            expiry_date_format = expiry_date.strftime("%d ") +expiry_date.strftime("%b ") + expiry_date.strftime("%Y")
            return birth_date, issue_date_fromat, expiry_date_format

        
    
    def passport_owner(self):
        genders = ['M','F','X']
        gender = random.choices(genders, weights=[0.493,0.493,0.014],k=1)[0]
        if gender == 'M':
            given_name = self.generator.parse("{{first_name_male}} ")
            surname  = self.generator.parse("{{last_name_male}} ")
        elif gender == 'F':
            given_name = self.generator.parse("{{first_name_female}} ")
            surname  = self.generator.parse("{{last_name_female}} ")
        else:
            given_name = self.generator.parse("{{first_name_nonbinary}} ")
            surname  = self.generator.parse("{{last_name_nonbinary}} ")
            
        return given_name, surname, gender
    
    def passport_number(self) -> str:
        """Generate a passport number"""
        temp = re.sub(
            r"\?",
            lambda x: self.random_element(ascii_uppercase),
            self.random_element(self.passport_number_formats),
        )
        return self.numerify(temp)