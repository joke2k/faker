import pytest

from faker import Faker
from faker.exceptions import UniquenessException


class TestSelectiveUniqueness:
    def setup_method(self):
        self.fake = Faker()
        self.fake.unique.clear()

    def test_exclude_types_excludes_bools(self):
        """Test that excluded types can return duplicates."""
        proxy = self.fake.unique.exclude_types([bool])
        
        # Should be able to call pybool many times without exhaustion
        # (only 2 possible values: True/False)
        for _ in range(10):
            val = proxy.pybool()
            assert isinstance(val, bool)
        
        # Should not raise UniquenessException

    def test_exclude_types_still_enforces_other_types(self):
        """Test that non-excluded types still enforce uniqueness."""
        proxy = self.fake.unique.exclude_types([bool])
        
        # Names should still be unique
        names = [proxy.first_name() for _ in range(5)]
        assert len(set(names)) == 5, "Names should all be unique"

    def test_exclude_types_with_limited_values(self):
        """Test that excluding types prevents exhaustion."""
        proxy = self.fake.unique.exclude_types([bool])
        
        # This should work fine even though there are only 2 boolean values
        bools = [proxy.pybool() for _ in range(100)]
        assert all(isinstance(b, bool) for b in bools)

    def test_without_exclusion_bools_exhaust(self):
        """Test that without exclusion, bools still exhaust as before."""
        self.fake.unique.clear()
        
        # Should be able to get True and False
        b1 = self.fake.unique.pybool()
        b2 = self.fake.unique.pybool()
        assert b1 != b2  # One True, one False
        
        # Third call should raise
        with pytest.raises(UniquenessException):
            self.fake.unique.pybool()

    def test_exclude_types_chainable(self):
        """Test that exclude_types returns a new proxy that can be used."""
        proxy1 = self.fake.unique.exclude_types([bool])
        proxy2 = self.fake.unique.exclude_types([int])
        
        # Both should be independent
        assert proxy1 is not proxy2
        assert proxy1._excluded_types == (bool,)
        assert proxy2._excluded_types == (int,)

    def test_exclude_multiple_types(self):
        """Test excluding multiple types at once."""
        proxy = self.fake.unique.exclude_types([bool, int])
        
        # Bools should not enforce uniqueness
        for _ in range(10):
            proxy.pybool()
        
        # Ints should not enforce uniqueness
        for _ in range(10):
            proxy.pyint(min_value=0, max_value=1)  # Only 2 values

    def test_exclude_types_shares_seen_dict(self):
        """Test that excluded proxy shares the seen dictionary."""
        self.fake.unique.clear()
        
        # Get a unique name through original proxy
        name1 = self.fake.unique.first_name()
        
        # Create excluded proxy and try to get same name
        proxy = self.fake.unique.exclude_types([bool])
        name2 = proxy.first_name()
        
        # Should not be the same (shares seen dict)
        assert name1 != name2

    def test_exclude_types_preserves_across_locales(self):
        """Test that exclusions work with locale proxying."""
        fake_multi = Faker(['en_US', 'fr_FR'])
        proxy = fake_multi.unique.exclude_types([bool])
        
        # Should work with locale selection
        for _ in range(10):
            proxy['en_US'].pybool()
