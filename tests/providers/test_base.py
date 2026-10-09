from collections import OrderedDict

import pytest

from faker import Faker


class TestRandomElements:
    @pytest.mark.parametrize("unique, use_weighting", [(False, False), (False, True), (True, True)])
    def test_replaced_ordered_dict_key(self, unique, use_weighting):
        fake = Faker()
        elements = OrderedDict([("old", 1)])
        assert fake.random_elements(elements, length=1, unique=unique, use_weighting=use_weighting) == ["old"]

        elements.clear()
        elements["new"] = 1

        assert fake.random_elements(elements, length=1, unique=unique, use_weighting=use_weighting) == ["new"]

    @pytest.mark.parametrize("unique", [False, True])
    def test_added_ordered_dict_key(self, unique):
        fake = Faker()
        elements = OrderedDict([("old", 1)])
        assert fake.random_elements(elements, length=1, unique=unique, use_weighting=True) == ["old"]

        elements["old"] = 0
        elements["new"] = 1

        assert fake.random_elements(elements, length=1, unique=unique, use_weighting=True) == ["new"]

    @pytest.mark.parametrize("unique", [False, True])
    def test_removed_ordered_dict_key(self, unique):
        fake = Faker()
        elements = OrderedDict([("keep", 1), ("remove", 0)])
        assert fake.random_elements(elements, length=1, unique=unique, use_weighting=True) == ["keep"]

        del elements["remove"]

        assert fake.random_elements(elements, length=1, unique=unique, use_weighting=True) == ["keep"]

    @pytest.mark.parametrize("unique", [False, True])
    def test_reordered_ordered_dict_keys_keep_their_weights(self, unique):
        fake = Faker()
        elements = OrderedDict([("selected", 1), ("excluded", 0)])
        assert fake.random_elements(elements, length=1, unique=unique, use_weighting=True) == ["selected"]

        elements.move_to_end("selected")

        assert fake.random_elements(elements, length=1, unique=unique, use_weighting=True) == ["selected"]
