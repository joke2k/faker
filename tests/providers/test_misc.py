import unittest
import uuid
import six

from faker import Faker


class TestMisc(unittest.TestCase):
    """Tests miscellaneous generators"""
    def setUp(self):
        self.factory = Faker()

    def test_uuid4(self):
        uuid4 = self.factory.uuid4()
        assert uuid4
        assert isinstance(uuid4, six.string_types)

    def test_uuid4_int(self):
        uuid4 = self.factory.uuid4(cast_to=int)
        assert uuid4
        assert isinstance(uuid4, six.integer_types)

    def test_uuid4_uuid_object(self):
        uuid4 = self.factory.uuid4(cast_to=lambda x: x)
        assert uuid4
        assert isinstance(uuid4, uuid.UUID)

    def test_uuid4_seedability(self):
        for _ in range(10):
            random_seed = self.factory.random_int()
            baseline_fake = Faker()
            baseline_fake.seed(random_seed)
            expected_uuids = [baseline_fake.uuid4() for i in range(1000)]

            new_fake = Faker()
            new_fake.seed(random_seed)
            new_uuids = [new_fake.uuid4() for i in range(1000)]
            assert new_uuids == expected_uuids
