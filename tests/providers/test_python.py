import decimal
import sys
import unittest
import warnings

from collections import Counter
from typing import Iterable, Optional, Type, Union
from unittest.mock import patch

import pytest

from faker import Faker


@pytest.mark.parametrize("object_type", (None, bool, str, float, int, tuple, set, list, Iterable, dict))
def test_pyobject(
    object_type: Optional[
        Union[
            Type[bool],
            Type[str],
            Type[float],
            Type[int],
            Type[tuple],
            Type[set],
            Type[list],
            Type[Iterable],
            Type[dict],
        ]
    ],
) -> None:
    random_object = Faker().pyobject(object_type=object_type)
    if object_type is None:
        assert random_object is None
    else:
        assert isinstance(random_object, object_type)


@pytest.mark.parametrize("object_type", (object, type, callable))
def test_pyobject_with_unknown_object_type(object_type):
    with pytest.raises(ValueError, match=f"Object type `{object_type}` is not supported by `pyobject` function"):
        assert Faker().pyobject(object_type=object_type)


@pytest.mark.parametrize(
    "mock_random_number_source, right_digits, expected_decimal_part",
    (
        ("1234567", 5, "12345"),
        ("1234567", 0, "1"),  # This is kinda interesting - same as 1 digit
        ("1234567", 1, "1"),
        ("1234567", 2, "12"),
        ("0123", 1, "1"),
    ),
)
def test_pyfloat_right_and_left_digits_positive(mock_random_number_source, right_digits, expected_decimal_part):
    # Remove the randomness from the test by mocking the `BaseProvider.random_number` value
    def mock_random_number(self, digits=None, fix_len=False):
        return int(mock_random_number_source[: digits or 1])

    with patch("faker.providers.BaseProvider.random_number", mock_random_number):
        result = Faker().pyfloat(left_digits=1, right_digits=right_digits, positive=True)
        decimal_part = str(result).split(".")[1]
        assert decimal_part == expected_decimal_part


def test_pyfloat_right_or_left_digit_overflow():
    max_float_digits = sys.float_info.dig
    faker = Faker()

    # Make random_int always return the maximum value input - makes it easy to reason about the code below
    def mock_random_int(self, min=0, max=9999, step=1):
        return max

    # Remove the randomness from the test by mocking the `BaseProvider.random_number` value
    def mock_random_number(self, digits=None, fix_len=False):
        return int("12345678901234567890"[: digits or 1])

    with patch("faker.providers.BaseProvider.random_int", mock_random_int):
        with patch("faker.providers.BaseProvider.random_number", mock_random_number):
            # A bit too much, but ~half on either side
            with pytest.raises(ValueError, match="Asking for too many digits"):
                faker.pyfloat(
                    left_digits=max_float_digits // 2 + 1,
                    right_digits=max_float_digits // 2 + 1,
                )

            # Asking for max digits on either side also fails, because we need one digit on the other side, i.e.
            # 0.123123123, or 123123123.0 (at least needs to lead with `0.` or trail with `.0`).
            with pytest.raises(ValueError, match="Asking for too many digits"):
                faker.pyfloat(left_digits=max_float_digits)
            with pytest.raises(ValueError, match="Asking for too many digits"):
                faker.pyfloat(right_digits=max_float_digits)

            # Just the right amount of max digits on either side
            result = faker.pyfloat(left_digits=max_float_digits - 1)
            assert str(abs(result)) == "12345678901234.1"
            result = faker.pyfloat(right_digits=max_float_digits - 1)
            assert str(abs(result)) == "1.12345678901234"


@pytest.mark.skipif(sys.version_info < (3, 10), reason="Only relevant for Python 3.10 and later.")
@pytest.mark.parametrize(
    ("min_value", "max_value"),
    [
        (1.5, None),
        (-1.5, None),
        (None, -1.5),
        (None, 1.5),
        (-1.5, 1.5),
    ],
)
@pytest.mark.parametrize(("left_digits"), [None, 5])
@pytest.mark.parametrize(("right_digits"), [None, 5])
@pytest.mark.filterwarnings(
    # Convert the warning to an error for this test
    r"error:non-integer arguments to randrange\(\):DeprecationWarning"
)
def test_float_min_and_max_value_does_not_crash(
    left_digits: Optional[int],
    right_digits: Optional[int],
    min_value: Optional[float],
    max_value: Optional[float],
):
    """
    Float arguments to randrange are deprecated from Python 3.10. This is a regression
    test to check that `pydecimal` does not cause a crash on any code path.
    """
    Faker().pydecimal(left_digits, right_digits, min_value=min_value, max_value=max_value)


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

        right_digits = len(("%r" % result).split(".")[1])
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

    def test_min_value_and_left_digits(self):
        """
        Combining the min_value and left_digits keyword arguments produces
        numbers that obey both of those constraints.
        """

        result = self.fake.pyfloat(left_digits=1, min_value=0)
        self.assertLess(result, 10)
        self.assertGreaterEqual(result, 0)

    def test_max_value(self):
        max_values = (0, 10, -1000, 1000, 999999)

        for max_value in max_values:
            result = self.fake.pyfloat(max_value=max_value)
            self.assertLessEqual(result, max_value)

    def test_max_value_zero_and_left_digits(self):
        """
        Combining the max_value and left_digits keyword arguments produces
        numbers that obey both of those constraints.
        """

        result = self.fake.pyfloat(left_digits=2, max_value=0)
        self.assertLessEqual(result, 0)
        self.assertGreater(result, -100)

    def test_max_value_should_be_greater_than_min_value(self):
        """
        An exception should be raised if min_value is greater than max_value
        """
        expected_message = "Min value cannot be greater than max value"
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

    def test_max_and_min_value_positive_with_decimals(self):
        """
        Combining the max_value and min_value keyword arguments with
        positive values for each produces numbers that obey both of
        those constraints.
        """
        for _ in range(1000):
            result = self.fake.pyfloat(min_value=100.123, max_value=200.321)
            self.assertLessEqual(result, 200.321)
            self.assertGreaterEqual(result, 100.123)

    def test_max_and_min_value_negative(self):
        """
        Combining the max_value and min_value keyword arguments with
        negative values for each produces numbers that obey both of
        those constraints.
        """

        result = self.fake.pyfloat(max_value=-100, min_value=-200)
        self.assertLessEqual(result, -100)
        self.assertGreaterEqual(result, -200)

    def test_max_and_min_value_negative_with_decimals(self):
        """
        Combining the max_value and min_value keyword arguments with
        negative values for each produces numbers that obey both of
        those constraints.
        """
        for _ in range(1000):
            result = self.fake.pyfloat(max_value=-100.123, min_value=-200.321)
            self.assertLessEqual(result, -100.123)
            self.assertGreaterEqual(result, -200.321)

    def test_positive_and_min_value_incompatible(self):
        """
        An exception should be raised if positive=True is set, but
        a negative min_value is provided.
        """

        expected_message = "Cannot combine positive=True with negative or zero min_value"
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

    @pytest.mark.skipif(sys.version_info < (3, 10), reason="Only relevant for Python 3.10 and later.")
    @pytest.mark.filterwarnings(
        # Convert the warning to an error for this test
        r"error:non-integer arguments to randrange\(\):DeprecationWarning"
    )
    def test_float_min_and_max_value_does_not_warn(self):
        """
        Float arguments to randrange are deprecated from Python 3.10. This is a regression
        test to check that `pyfloat` does not cause a deprecation warning.
        """
        self.fake.pyfloat(min_value=-1.0, max_value=1.0)

    def test_float_min_and_max_value_with_same_whole(self):
        self.fake.pyfloat(min_value=2.3, max_value=2.5)


class TestPyDict(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()
        Faker.seed(0)

    def test_pydict_with_default_nb_elements(self):
        result = self.fake.pydict()

        self.assertEqual(len(result), 10)

    def test_pydict_with_valid_number_of_nb_elements(self):
        result = self.fake.pydict(nb_elements=5)

        self.assertEqual(len(result), 5)

    def test_pydict_with_invalid_number_of_nb_elements(self):
        nb_elements = 10000

        words_list_count = len(self.fake.get_words_list())
        warning_msg = (
            f"Number of nb_elements is greater than the number of words in the list."
            f" {words_list_count} words will be used."
        )
        with pytest.warns(RuntimeWarning, match=warning_msg):
            result = self.fake.pydict(nb_elements=nb_elements)
            self.assertEqual(len(result), words_list_count)


class TestPydecimal(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()
        Faker.seed(0)

    def test_pydecimal(self):
        result = self.fake.pydecimal()

        self.assertIsInstance(result, decimal.Decimal)

    def test_left_digits(self):
        expected_left_digits = 10

        result = self.fake.pydecimal(left_digits=expected_left_digits)

        left_digits = len(str(abs(int(result))))
        self.assertGreaterEqual(expected_left_digits, left_digits)

    def test_left_digits_can_be_zero(self):
        expected_left_digits = 0

        result = self.fake.pydecimal(left_digits=expected_left_digits)

        left_digits = int(result)
        self.assertEqual(expected_left_digits, left_digits)

    def test_right_digits(self):
        expected_right_digits = 10

        result = self.fake.pydecimal(right_digits=expected_right_digits)

        right_digits = len(str(result).split(".")[1])
        self.assertGreaterEqual(expected_right_digits, right_digits)

    def test_positive(self):
        result = self.fake.pydecimal(positive=True)

        self.assertGreater(result, 0)
        abs_result = -result if result < 0 else result  # abs() result returns scientific notation
        self.assertEqual(result, abs_result)

    def test_min_value(self):
        min_values = (0, 10, -1000, 1000, 999999)

        for min_value in min_values:
            result = self.fake.pydecimal(min_value=min_value)
            self.assertGreaterEqual(result, min_value)

    def test_min_value_always_returns_a_decimal(self):
        min_values = (0, 10, -1000, 1000, 999999)

        for min_value in min_values:
            result = self.fake.pydecimal(min_value=min_value)
            self.assertIsInstance(result, decimal.Decimal)

    def test_min_value_and_left_digits(self):
        """
        Combining the min_value and left_digits keyword arguments produces
        numbers that obey both of those constraints.
        """

        result = self.fake.pydecimal(left_digits=1, min_value=0)
        self.assertLess(result, 10)
        self.assertGreaterEqual(result, 0)

    def test_max_value(self):
        max_values = (0, 10, -1000, 1000, 999999)

        for max_value in max_values:
            result = self.fake.pydecimal(max_value=max_value)
            self.assertLessEqual(result, max_value)

    def test_max_value_always_returns_a_decimal(self):
        max_values = (0, 10, -1000, 1000, 999999)

        for max_value in max_values:
            result = self.fake.pydecimal(max_value=max_value)
            self.assertIsInstance(result, decimal.Decimal)

    def test_max_value_zero_and_left_digits(self):
        """
        Combining the max_value and left_digits keyword arguments produces
        numbers that obey both of those constraints.
        """

        result = self.fake.pydecimal(left_digits=2, max_value=0)
        self.assertLessEqual(result, 0)
        self.assertGreater(result, -100)

    def test_max_value_should_be_greater_than_min_value(self):
        """
        An exception should be raised if min_value is greater than max_value
        """
        expected_message = "Min value cannot be greater than max value"
        with self.assertRaises(ValueError) as raises:
            self.fake.pydecimal(min_value=100, max_value=0)

        message = str(raises.exception)
        self.assertEqual(message, expected_message)

    def test_max_value_and_positive(self):
        """
        Combining the max_value and positive keyword arguments produces
        numbers that obey both of those constraints.
        """

        result = self.fake.pydecimal(positive=True, max_value=100)
        self.assertLessEqual(result, 100)
        self.assertGreater(result, 0)

    def test_max_and_min_value_negative(self):
        """
        Combining the max_value and min_value keyword arguments with
        negative values for each produces numbers that obey both of
        those constraints.
        """

        result = self.fake.pydecimal(max_value=-100, min_value=-200)
        self.assertLessEqual(result, -100)
        self.assertGreaterEqual(result, -200)

    def test_positive_and_min_value_incompatible(self):
        """
        An exception should be raised if positive=True is set, but
        a negative min_value is provided.
        """

        expected_message = "Cannot combine positive=True with negative or zero min_value"
        with self.assertRaises(ValueError) as raises:
            self.fake.pydecimal(min_value=-100, positive=True)

        message = str(raises.exception)
        self.assertEqual(message, expected_message)

    def test_positive_doesnt_return_zero(self):
        """
        Choose the right_digits and max_value so it's guaranteed to return zero,
        then watch as it doesn't because positive=True
        """
        result = self.fake.pydecimal(positive=True, right_digits=0, max_value=1)
        self.assertGreater(result, 0)

    def test_min_value_zero_doesnt_return_negative(self):
        Faker.seed("1")
        result = self.fake.pydecimal(left_digits=3, right_digits=2, min_value=0, max_value=999)
        self.assertGreater(result, 0)

    def test_min_value_one_hundred_doesnt_return_negative(self):
        Faker.seed("1")
        result = self.fake.pydecimal(left_digits=3, right_digits=2, min_value=100, max_value=999)
        self.assertGreater(result, 100)

    def test_min_value_minus_one_doesnt_return_positive(self):
        Faker.seed("5")
        result = self.fake.pydecimal(left_digits=3, right_digits=2, min_value=-999, max_value=0)
        self.assertLess(result, 0)

    def test_min_value_minus_one_hundred_doesnt_return_positive(self):
        Faker.seed("5")
        result = self.fake.pydecimal(left_digits=3, right_digits=2, min_value=-999, max_value=-100)
        self.assertLess(result, -100)

    def test_min_value_10_pow_1000_return_greater_number(self):
        Faker.seed("2")
        result = self.fake.pydecimal(min_value=10**1000)
        self.assertGreater(result, 10**1000)

    def test_min_value_and_max_value_have_different_signs_return_evenly_distributed_values(self):
        result = []
        boundary_value = 10
        for _ in range(1000):
            result.append(self.fake.pydecimal(min_value=-boundary_value, max_value=boundary_value, right_digits=0))
        self.assertEqual(len(Counter(result)), 2 * boundary_value + 1)

    def test_min_value_and_max_value_negative_return_evenly_distributed_values(self):
        result = []
        min_value = -60
        max_value = -50
        for _ in range(1000):
            result.append(self.fake.pydecimal(min_value=min_value, max_value=max_value, right_digits=0))
        self.assertGreater(len(Counter(result)), max_value - min_value)

    def test_min_value_and_max_value_positive_return_evenly_distributed_values(self):
        result = []
        min_value = 50
        max_value = 60
        for _ in range(1000):
            result.append(self.fake.pydecimal(min_value=min_value, max_value=max_value, right_digits=0))
        self.assertGreater(len(Counter(result)), max_value - min_value)

    def test_min_value_float_returns_correct_digit_number(self):
        Faker.seed("6")
        result = self.fake.pydecimal(left_digits=1, right_digits=1, min_value=0.2, max_value=0.3)
        self.assertEqual(decimal.Decimal("0.2"), result)

    def test_max_value_float_returns_correct_digit_number(self):
        Faker.seed("3")
        result = self.fake.pydecimal(left_digits=1, right_digits=1, min_value=0.2, max_value=0.3)
        self.assertEqual(decimal.Decimal("0.3"), result)


class TestPystr(unittest.TestCase):
    def setUp(self):
        self.fake = Faker(includes=["tests.mymodule.en_US"])
        Faker.seed(0)

    def test_no_parameters(self):
        some_string = self.fake.pystr()
        assert isinstance(some_string, str)
        assert len(some_string) <= 20

    def test_lower_length_limit(self):
        some_string = self.fake.pystr(min_chars=3)
        assert isinstance(some_string, str)
        assert len(some_string) >= 3
        assert len(some_string) <= 20

    def test_upper_length_limit(self):
        some_string = self.fake.pystr(max_chars=5)
        assert isinstance(some_string, str)
        assert len(some_string) <= 5

    def test_invalid_length_limits(self):
        with self.assertRaises(AssertionError):
            self.fake.pystr(min_chars=6, max_chars=5)

    def test_exact_length(self):
        some_string = self.fake.pystr(min_chars=5, max_chars=5)
        assert isinstance(some_string, str)
        assert len(some_string) == 5

    def test_prefix(self):
        some_string = self.fake.pystr(prefix="START_")
        assert isinstance(some_string, str)
        assert some_string.startswith("START_")
        assert len(some_string) == 26

    def test_suffix(self):
        some_string = self.fake.pystr(suffix="_END")
        assert isinstance(some_string, str)
        assert some_string.endswith("_END")
        assert len(some_string) == 24

    def test_prefix_and_suffix(self):
        some_string = self.fake.pystr(min_chars=9, max_chars=20, prefix="START_", suffix="_END")
        assert isinstance(some_string, str)
        assert some_string.startswith("START_")
        assert some_string.endswith("_END")
        assert len(some_string) >= 19


class TestPystrFormat(unittest.TestCase):
    def setUp(self):
        self.fake = Faker(includes=["tests.mymodule.en_US"])
        Faker.seed(0)

    def test_formatter_invocation(self):
        with patch.object(self.fake["en_US"].factories[0], "foo") as mock_foo:
            with patch("faker.providers.BaseProvider.bothify", wraps=self.fake.bothify) as mock_bothify:
                mock_foo.return_value = "barbar"
                value = self.fake.pystr_format("{{foo}}?#?{{foo}}?#?{{foo}}", letters="abcde")
                assert value.count("barbar") == 3
                assert mock_foo.call_count == 3
                mock_bothify.assert_called_once_with("barbar?#?barbar?#?barbar", letters="abcde")


class TestPython(unittest.TestCase):
    """Tests python generators"""

    def setUp(self):
        self.factory = Faker()

    def test_pybool_return_type(self):
        some_bool = self.factory.pybool()
        assert isinstance(some_bool, bool)

    def __test_pybool_truth_probability(
        self,
        truth_probability: int,
        deviation_threshold: int = 5,
        iterations: int = 999,
    ):
        truth_count_expected = iterations * truth_probability / 100
        truth_count_actual = 0

        for iteration in range(iterations):
            boolean = self.factory.pybool(truth_probability=truth_probability)
            assert isinstance(boolean, bool)
            if boolean is True:
                truth_count_actual += 1

        deviation_absolute = abs(truth_count_expected - truth_count_actual)
        deviation_percentage = deviation_absolute / iterations * 100

        # Increase `deviation_threshold` value in case this assertion becomes flaky.
        assert deviation_percentage <= deviation_threshold

    def test_pybool_truth_probability_zero(self):
        self.__test_pybool_truth_probability(0, deviation_threshold=0)

    def test_pybool_truth_probability_twenty_five(self):
        self.__test_pybool_truth_probability(25)

    def test_pybool_truth_probability_fifty(self):
        self.__test_pybool_truth_probability(50)

    def test_pybool_truth_probability_seventy_five(self):
        self.__test_pybool_truth_probability(75)

    def test_pybool_truth_probability_hundred(self):
        self.__test_pybool_truth_probability(100, deviation_threshold=0)

    def __test_pybool_invalid_truth_probability(self, truth_probability: int):
        with pytest.raises(ValueError) as exception:
            self.factory.pybool(truth_probability=truth_probability)

        message_expected = "Invalid `truth_probability` value: must be between `0` and `100` inclusive"
        message_actual = str(exception.value)
        assert message_expected == message_actual

    def test_pybool_truth_probability_less_than_zero(self):
        self.__test_pybool_invalid_truth_probability(-1)

    def test_pybool_truth_probability_more_than_hundred(self):
        self.__test_pybool_invalid_truth_probability(101)

    def test_pytuple(self):
        with warnings.catch_warnings(record=True) as w:
            some_tuple = Faker().pytuple()
            assert len(w) == 0
        assert some_tuple
        assert isinstance(some_tuple, tuple)

    def test_pytuple_size(self):
        def mock_pyint(self, *args, **kwargs):
            return 1

        with patch("faker.providers.python.Provider.pyint", mock_pyint):
            some_tuple = Faker().pytuple(nb_elements=3, variable_nb_elements=False, value_types=[int])
            assert some_tuple == (1, 1, 1)

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
            assert len(w) == 2
        assert some_list
        for item in some_list:
            assert isinstance(item, (int, float))
