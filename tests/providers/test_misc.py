import unittest
import uuid

from faker import Faker

class TestMisc(unittest.TestCase):
    """Tests miscellaneous generators"""
    def setUp(self):
        self.factory = Faker()

    def test_uuid4(self):
        uuid4 = self.factory.uuid4()
        assert uuid4
        assert isinstance(uuid4, str)

    def test_uuid4_uuid_object(self):
        uuid4 = self.factory.uuid4(uuid_object=True)
        assert uuid4
        assert isinstance(uuid4, uuid.UUID)
