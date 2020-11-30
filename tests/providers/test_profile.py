import unittest

from faker import Faker


class TestProfileProvider(unittest.TestCase):
    """Test profile provider methods"""

    num_samples = 10

    def setUp(self):
        self.fake = Faker()
        Faker.seed(0)

    def test_simple_profile(self):
        for _ in range(self.num_samples):
            profile = self.fake.simple_profile()
            assert isinstance(profile, dict)
            assert len(profile["username"]) >= 1
            assert profile["sex"] in ["F", "M"]

        profile = self.fake.simple_profile(sex="F")
        assert profile["sex"] == "F"
        profile = self.fake.simple_profile(sex="M")
        assert profile["sex"] == "M"

    def test_profile(self):
        for _ in range(self.num_samples):
            profile = self.fake.profile()
            assert isinstance(profile, dict)
            assert len(profile["username"]) >= 1
            assert profile["sex"] in ["F", "M"]
            assert "website" in profile.keys()

        profile = self.fake.profile(sex="F")
        assert profile["sex"] == "F"
        profile = self.fake.profile(sex="M")
        assert profile["sex"] == "M"

        profile = self.fake.profile(fields=["ssn", "name"])
        assert len(profile) == 2
        assert "ssn" in profile.keys()
        assert "name" in profile.keys()

        profile = self.fake.profile(fields=[])
        assert len(profile) > 0
        assert "ssn" in profile.keys()

        profile = self.fake.profile(fields=["secret_org"])
        assert len(profile) == 0
