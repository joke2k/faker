import re

from datetime import date, datetime, timedelta

from faker.providers.person.en_US import Provider as EnUSPersonProvider
from faker.providers.person.ru_RU import Provider as RuRuPersonProvider


class TestBaseProvider:

    def test_dob(self, faker, num_samples):
        for _ in range(num_samples):
            dob = faker.passport_dob()
            age = (date.today() - dob).days // 365
            assert isinstance(dob, date)
            assert age <= 115
            assert age >= 0

    def test_owner_names(self, faker, num_samples):
        for _ in range(num_samples):
            given_name, surname = faker.passport_owner("F")
            assert given_name in EnUSPersonProvider.first_names_female
            assert surname in EnUSPersonProvider.last_names

            given_name, surname = faker.passport_owner("M")
            assert given_name in EnUSPersonProvider.first_names_male
            assert surname in EnUSPersonProvider.last_names

            given_name, surname = faker.passport_owner("X")
            assert given_name in EnUSPersonProvider.first_names_nonbinary
            assert surname in EnUSPersonProvider.last_names

    def test_num_formats(self, faker, num_samples):
        for _ in range(num_samples):
            pass_number = faker.passport_number()

            if pass_number[0].isalpha():
                assert pass_number[1:].isdigit()
            else:
                assert pass_number.isdigit()

            assert len(pass_number) == 9


class TestEnUS:
    def test_dates(self, faker, num_samples=20):
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

    def test_gender(self, faker, num_samples=100):
        for _ in range(num_samples):
            assert faker.passport_gender(7899) in ["M", "F", "X"]

    def test_full(self, faker, num_samples=100):
        for _ in range(num_samples):
            pass_data = faker.passport_full().split("\n")
            assert pass_data[1] in EnUSPersonProvider.last_names
            assert pass_data[2] in ["M", "F", "X"]
            if pass_data[2] == "M":
                assert pass_data[0] in EnUSPersonProvider.first_names_male
            elif pass_data[2] == "F":
                assert pass_data[0] in EnUSPersonProvider.first_names_female
            elif pass_data[2] == "X":
                assert pass_data[0] in EnUSPersonProvider.first_names_nonbinary


class TestRuRu:

    def test_owner_names(self, faker, num_samples):
        for _ in range(num_samples):
            last_name, first_name_with_middle = faker.passport_owner("F")
            first_name, middle_name = first_name_with_middle.split()
            assert last_name in RuRuPersonProvider.last_names_female
            assert first_name in RuRuPersonProvider.first_names_female
            assert middle_name in RuRuPersonProvider.middle_names_female

            last_name, first_name_with_middle = faker.passport_owner("M")
            first_name, middle_name = first_name_with_middle.split()
            assert last_name in RuRuPersonProvider.last_names_male
            assert first_name in RuRuPersonProvider.first_names_male
            assert middle_name in RuRuPersonProvider.middle_names_male

            last_name, first_name_with_middle = faker.passport_owner("X")
            first_name, middle_name = first_name_with_middle.split()
            assert last_name in RuRuPersonProvider.last_names_male
            assert first_name in RuRuPersonProvider.first_names_male
            assert middle_name in RuRuPersonProvider.middle_names_male

    def test_number(self, faker, num_samples):
        ru_passport_regex_1 = re.compile(r"\d\d \d\d \d{6}")
        ru_passport_regex_2 = re.compile(r"\d{4} \d{6}")

        for _ in range(num_samples):
            number = faker.passport_number()

            assert sum(map(lambda x: x.isdigit(), number)) == 4 + 6
            assert ru_passport_regex_1.match(number) or ru_passport_regex_2.match(number)
