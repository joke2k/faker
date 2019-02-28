import unittest
import warnings

from faker import Faker


class TestPython(unittest.TestCase):
    """Tests python generators"""
    def setUp(self):
        self.factory = Faker()

    def test_pybool(self):
        some_bool = self.factory.pybool()
        assert isinstance(some_bool, bool)

    def test_pyint(self):
        some_int = self.factory.pyint()
        assert isinstance(some_int, int)

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
