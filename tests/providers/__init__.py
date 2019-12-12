import unittest
from faker import Faker


class BaseProviderTestCase(unittest.TestCase):
    def setUp(self):
        self.fake = Faker('en_US')
        Faker.seed(0)

    def test_random_digit_or_empty(self):
        ret = self.fake.random_digit_or_empty()
        assert isinstance(ret, int)
        assert 0 <= ret <= 9

        Faker.seed(1)
        assert self.fake.random_digit_or_empty() == ''

    def test_random_digit_not_null_or_empty(self):
        ret = self.fake.random_digit_not_null_or_empty()
        assert isinstance(ret, int)
        assert 0 <= ret <= 9

        Faker.seed(1)
        assert self.fake.random_digit_not_null_or_empty() == ''

    def test_randomize_nb_elements(self):
        assert self.fake.randomize_nb_elements(number=1, le=True, ge=True) == 1

        assert self.fake.randomize_nb_elements(le=True, ge=True) == 10

        assert self.fake.randomize_nb_elements(min=42) == 42
        assert self.fake.randomize_nb_elements(max=1) == 1

        number = 9999
        random_times = 100
        lower_bound = int(number * 0.6)
        upper_bound = int(number * 1.4)

        for _ in range(random_times):
            res = self.fake.randomize_nb_elements(number=number, le=True)
            assert res >= lower_bound
            assert res <= number, "'{}' is not <= than '{}'".format(res, number)

        for _ in range(random_times):
            res = self.fake.randomize_nb_elements(number=number, ge=True)
            assert res >= number
            assert res <= upper_bound

        for _ in range(random_times):
            res = self.fake.randomize_nb_elements(number=number)
            assert res >= lower_bound
            assert res <= upper_bound
