import unittest
import warnings

from unittest.mock import patch

from faker import Faker


class TestPyint(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()
        Faker.seed(0)

    def test_pyint(self):
        self.assertIsInstance(self.fake.pyint(), int)

    def test_pyint_bounds(self):
        self.assertTrue(0 <= self.fake.pyint() <= 9999)

    def test_pyint_step(self):
        random_int = self.fake.pyint(step=2)
        self.assertEqual(0, random_int % 2)

    def test_pyint_bound_0(self):
        self.assertEqual(0, self.fake.pyint(min_value=0, max_value=0))

    def test_pyint_bound_positive(self):
        self.assertEqual(5, self.fake.pyint(min_value=5, max_value=5))

    def test_pyint_bound_negative(self):
        self.assertEqual(-5, self.fake.pyint(min_value=-5, max_value=-5))

    def test_pyint_range(self):
        self.assertTrue(0 <= self.fake.pyint(min_value=0, max_value=2) <= 2)


class TestPyfloat(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()
        Faker.seed(0)

    def test_pyfloat(self):
        result = self.fake.pyfloat()

        self.assertIsInstance(result, float)

    def test_left_digits(self):
        expected_left_digits = 10

        result = self.fake.pyfloat(left_digits=expected_left_digits)

        left_digits = len(str(abs(int(result))))
        self.assertGreaterEqual(expected_left_digits, left_digits)

    def test_right_digits(self):
        expected_right_digits = 10

        result = self.fake.pyfloat(right_digits=expected_right_digits)

        right_digits = len(('%r' % result).split('.')[1])
        self.assertGreaterEqual(expected_right_digits, right_digits)

    def test_positive(self):
        result = self.fake.pyfloat(positive=True)

        self.assertGreater(result, 0)
        self.assertEqual(result, abs(result))

    def test_min_value(self):
        min_values = (0, 10, -1000, 1000, 999999)

        for min_value in min_values:
            result = self.fake.pyfloat(min_value=min_value)
            self.assertGreaterEqual(result, min_value)

    def test_max_value(self):
        max_values = (0, 10, -1000, 1000, 999999)

        for max_value in max_values:
            result = self.fake.pyfloat(max_value=max_value)
            self.assertLessEqual(result, max_value)

    def test_max_value_should_be_greater_than_min_value(self):
        """
        An exception should be raised if min_value is greater than max_value
        """
        expected_message = 'Min value cannot be greater than max value'
        with self.assertRaises(ValueError) as raises:
            self.fake.pyfloat(min_value=100, max_value=0)

        message = str(raises.exception)
        self.assertEqual(message, expected_message)

    def test_max_value_and_positive(self):
        """
        Combining the max_value and positive keyword arguments produces
        numbers that obey both of those constraints.
        """

        result = self.fake.pyfloat(positive=True, max_value=100)
        self.assertLessEqual(result, 100)
        self.assertGreater(result, 0)

    def test_positive_and_min_value_incompatible(self):
        """
        An exception should be raised if positive=True is set, but
        a negative min_value is provided.
        """

        expected_message = (
            "Cannot combine positive=True with negative or zero min_value"
        )
        with self.assertRaises(ValueError) as raises:
            self.fake.pyfloat(min_value=-100, positive=True)

        message = str(raises.exception)
        self.assertEqual(message, expected_message)

    def test_positive_doesnt_return_zero(self):
        """
        Choose the right_digits and max_value so it's guaranteed to return zero,
        then watch as it doesn't because positive=True
        """
        result = self.fake.pyfloat(positive=True, right_digits=0, max_value=1)
        self.assertGreater(result, 0)


class TestPystrFormat(unittest.TestCase):

    def setUp(self):
        self.fake = Faker(includes=['tests.mymodule.en_US'])
        Faker.seed(0)

    def test_formatter_invocation(self):
        with patch.object(self.fake['en_US'], 'foo') as mock_foo:
            with patch('faker.providers.BaseProvider.bothify',
                       wraps=self.fake.bothify) as mock_bothify:
                mock_foo.return_value = 'barbar'
                value = self.fake.pystr_format('{{foo}}?#?{{foo}}?#?{{foo}}', letters='abcde')
                assert value.count('barbar') == 3
                assert mock_foo.call_count == 3
                mock_bothify.assert_called_once_with('barbar?#?barbar?#?barbar', letters='abcde')


class TestPython(unittest.TestCase):
    """Tests python generators"""
    def setUp(self):
        self.factory = Faker()

    def test_pybool(self):
        some_bool = self.factory.pybool()
        assert isinstance(some_bool, bool)

    def py_str(self):
        some_string = self.factory.pystr()
        assert isinstance(some_string, str)
        assert len(some_string) <= 20

        some_string = self.factory.pystr(min_chars=3)
        assert isinstance(some_string, str)
        assert len(some_string) >= 3
        assert len(some_string) <= 20

        some_string = self.factory.pystr(max_chars=5)
        assert isinstance(some_string, str)
        assert len(some_string) <= 5

        with self.assertRaises(AssertionError):
            self.factory.pystr(min_chars=6, max_chars=5)

        with self.assertRaises(AssertionError):
            self.factory.pystr(min_chars=5, max_chars=5)

    def test_pylist(self):
        with warnings.catch_warnings(record=True) as w:
            some_list = self.factory.pylist()
            assert len(w) == 0
        assert some_list
        assert isinstance(some_list, list)

    def test_pylist_types(self):
        with warnings.catch_warnings(record=True) as w:
            some_list = self.factory.pylist(10, True, [int])
            assert len(w) == 0
        assert some_list
        for item in some_list:
            assert isinstance(item, int)

        with warnings.catch_warnings(record=True) as w:
            some_list = self.factory.pylist(10, True, value_types=[int])
            assert len(w) == 0
        assert some_list
        for item in some_list:
            assert isinstance(item, int)

        with warnings.catch_warnings(record=True) as w:
            some_list = self.factory.pylist(10, True, int)
            assert len(w) == 1
        assert some_list
        for item in some_list:
            assert isinstance(item, int)

        with warnings.catch_warnings(record=True) as w:
            some_list = self.factory.pylist(10, True, int, float)
            assert len(w) == 1
        assert some_list
        for item in some_list:
            assert isinstance(item, (int, float))
