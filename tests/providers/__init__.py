import unittest
from faker import Faker
from faker.providers import BaseProvider


class BaseProviderTestCase(unittest.TestCase):
    def setUp(self):
        self.factory = Faker('en_US')
        self.factory.seed(0)
        self.provider = BaseProvider(generator=self.factory)

    def test_random_digit_or_empty(self):
        ret = self.provider.random_digit_or_empty()
        assert isinstance(ret, int)
        assert ret >= 0 and ret <= 9

        self.factory.seed(1)
        assert self.provider.random_digit_or_empty() == ''

    def test_random_digit_not_null_or_empty(self):
        ret = self.provider.random_digit_not_null_or_empty()
        assert isinstance(ret, int)
        assert ret >= 0 and ret <= 9

        self.factory.seed(1)
        assert self.provider.random_digit_not_null_or_empty() == ''

    def test_randomize_nb_elements(self):
        assert self.provider.randomize_nb_elements(number=1, le=True, ge=True) == 1

        assert self.provider.randomize_nb_elements(le=True, ge=True) == 10

        number = 9999
        random_times = 100
        lower_bound = int(number * 0.6)
        upper_bound = int(number * 1.4)

        for _ in range(random_times):
            res = self.provider.randomize_nb_elements(number=number, le=True)
            assert res >= lower_bound
            assert res <= number, "'{}' is not <= than '{}'".format(res, number)

        for _ in range(random_times):
            res = self.provider.randomize_nb_elements(number=number, ge=True)
            assert res >= number
            assert res <= upper_bound

        for _ in range(random_times):
            res = self.provider.randomize_nb_elements(number=number)
            assert res >= lower_bound
            assert res <= upper_bound
