from datetime import date, datetime, timedelta

from faker.providers.person.en_US import Provider as EnUSPersonProvider

female_first_name = list(EnUSPersonProvider.first_names_female.keys())
male_first_name = list(EnUSPersonProvider.first_names_male.keys())
nb_first_name = list(EnUSPersonProvider.first_names_nonbinary.keys())
last_name = list(EnUSPersonProvider.last_names.keys())


class TestPassportProvider:
    def testDOB(self, faker, num_samples=100):
        for _ in range(num_samples):
            dob = faker.passport_dob()
            age = (date.today() - dob).days // 365
            assert isinstance(dob, date)
            assert age <= 115
            assert age >= 0

    def testOwnerNames(self, faker, num_samples=100):
        for _ in range(num_samples):
            given_name, surname = faker.passport_owner("F")
            assert given_name in female_first_name
            assert surname in last_name

            given_name, surname = faker.passport_owner("M")
            assert given_name in male_first_name
            assert surname in last_name

            given_name, surname = faker.passport_owner("X")
            assert given_name in nb_first_name
            assert surname in last_name

    def testNumFormat(self, faker, num_samples=100):
        for _ in range(num_samples):
            pass_number = faker.passport_number()
            if pass_number[0].isalpha():
                assert pass_number[1:].isdigit()
            else:
                assert pass_number.isdigit()
            assert len(pass_number) == 9


class TestEnUS:
    def testDates(self, faker, num_samples=20):
        age4 = date.today() - timedelta(days=4 * 365)
        age12 = date.today() - timedelta(days=12 * 365)
        age17 = date.today() - timedelta(days=17 * 365)
        age23 = date.today() - timedelta(days=23 * 365)
        age30 = date.today() - timedelta(days=30 * 365)

        birthdays = [(age4, 4), (age12, 12), (age17, 17), (age23, 23), (age30, 30)]
        for _ in range(num_samples):
            for birthday in birthdays:
                birth_date_f, issue_date_f, expiry_date_f = faker.passport_dates(birthday[0])
                birth_date = datetime.strptime(birth_date_f, "%d %b %Y").date()
                issue_date = datetime.strptime(issue_date_f, "%d %b %Y").date()
                expiry_date = datetime.strptime(expiry_date_f, "%d %b %Y").date()

                if birthday[1] < 21:
                    assert (expiry_date - issue_date).days // 365 == 5
                else:
                    assert (expiry_date - issue_date).days // 365 == 10

                assert expiry_date > issue_date
                assert birth_date < issue_date

    def testGender(self, faker, num_samples=100):
        for _ in range(num_samples):
            assert faker.passport_gender(7899) in ["M", "F", "X"]

    def testfull(self, faker, num_samples=100):
        for _ in range(num_samples):
            pass_data = faker.passport_full().split("\n")
            assert pass_data[1] in last_name
            assert pass_data[2] in ["M", "F", "X"]
            if pass_data[2] == "M":
                assert pass_data[0] in male_first_name
            elif pass_data[2] == "F":
                assert pass_data[0] in female_first_name
            elif pass_data[2] == "X":
                assert pass_data[0] in nb_first_name
