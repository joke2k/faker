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
