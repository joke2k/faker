import unittest

from faker import Faker


class TestGlobal(unittest.TestCase):
    """Test emoji provider methods"""

    def setUp(self):
        self.fake = Faker()  # No locale specified, gets global for this provider
        Faker.seed(0)

    def test_emoji(self):
        emoji = self.fake.emoji()
        assert isinstance(emoji, str)
