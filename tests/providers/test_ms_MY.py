import pytest 
from faker import Faker

@pytest.fixture
def faker():
    return Faker("ms_MY")

class TestMsMY:
    def test_person_name(self, faker):
        name = faker.name()
        assert isinstance(name, str)
        assert len(name) > 0

    def test_first_name_male(self, faker):
        name = faker.first_name_male()
        assert isinstance(name, str)

    def test_first_name_female(self, faker):
        name = faker.first_name_female()
        assert isinstance(name, str)
    
    def test_last_name(self, faker):
        name = faker.last_name()
        assert isinstance(name, str)