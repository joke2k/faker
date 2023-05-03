from datetime import *
from faker.providers.person.en_US import Provider as EnUSPersonProvider

female_first_name = EnUSPersonProvider.first_names_female
male_first_name = EnUSPersonProvider.first_names_male
nb_first_name = EnUSPersonProvider.first_names_nonbinary
last_name = EnUSPersonProvider.last_names



class TestPassportProvider:
    def testDOB(self, faker, num_samples):
        for _ in range(num_samples):
            DOB = faker.passport_DOB()
            age = (date.today() - DOB).days // 365
            assert isinstance(DOB,date)
            assert age<=115
            assert age>=0

    def testOwnerNames(self, faker, num_samples):
        for _ in range(num_samples):
            given_name, surname = faker.passport_owner('F')
            assert given_name in female_first_name
            assert surname in last_name

            given_name, surname = faker.passport_owner('M')
            assert given_name in male_first_name
            assert surname in last_name

            given_name, surname = faker.passport_owner('X')
            assert given_name in nb_first_name
            assert surname in last_name
    
    def testNumFormat(self, faker, num_samples):
        for _ in range(num_samples):
            pass_number = faker.passport_number()
            if pass_number[0].isalpha():
                assert pass_number[1:].isdigit()
            else:
                assert pass_number.isdigit()
            assert len(pass_number) ==9

class TestEnUS:
    def testDates(self,faker):
        age4 = date.today() - timedelta(days=4 * 365)
        age12 = date.today() - timedelta(days=12 * 365)
        age17 = date.today() - timedelta(days=17 * 365)
        age23 = date.today() - timedelta(days=23 * 365)
        age30 = date.today() - timedelta(days=30 * 365)

        birthdays = [(age4,4), (age12,12), (age17,17), (age23,23), (age30,30)]

        for birthday in birthdays:
            birth_date_f, issue_date_f, expiry_date_f = faker.passport_Dates(birthday[0])
            birth_date = datetime.strptime(birth_date_f, '%d %b %Y').date()
            issue_date = datetime.strptime(issue_date_f, '%d %b %Y').date()
            expiry_date = datetime.strptime(expiry_date_f, '%d %b %Y').date()

            if birthday[1]<16:
                assert (expiry_date - issue_date).days // 365 == 5
            elif birthday[1]>=26:
                assert (expiry_date - issue_date).days // 365 == 10
            else:
                assert (expiry_date - issue_date).days // 365 in (5,10)
            
            assert expiry_date > issue_date
            assert birth_date < issue_date
        
    def testGender(self,faker,num_samples):
        sexes = []
        for _ in range(num_samples):
            assert faker.passport_gender(7899) in ['M','F','X']

    def testfull(self,faker,num_samples):
        for _ in range(num_samples):
            pass_data = faker.passport_full().split("\n")
            assert pass_data[0] in last_name
            assert pass_data[2] in ['M','F','X']
            if pass_data[2] == 'M':
                assert pass_data[1] in male_first_name
            elif pass_data[2] == 'F':
                assert pass_data[1] in female_first_name
            elif pass_data[2] == 'X':
                assert pass_data[1] in nb_first_name

