import pytest
from faker.providers.animals.constants import animals

@pytest.fixture
def animal_names():
    return [animal['common_name'] for animal in animals]

@pytest.fixture
def animal_scientific_names():
    return [animal['scientific_name'] for animal in animals]

def test_animal(faker):
    animal = faker.animal()
    assert animal is not None

def test_animal_name(faker,animal_names):
    name = faker.animal_name()
    assert name in animal_names


def test_animal_name_scientific(faker,animal_scientific_names):
    name_scientific = faker.animal_name_scientific()
    assert name_scientific in animal_scientific_names


def test_bird(faker):
    animal = faker.bird()
    assert animal['class'] == 'birds'


def test_fish(faker):
    animal = faker.fish()
    assert animal['class'] == 'fish'


def test_mammal(faker):
    animal = faker.mammal()
    assert animal['class'] == 'mammals'


def test_reptile(faker):
    animal = faker.reptile()
    assert animal['class'] == 'reptiles'


def test_amphibian(faker):
    animal = faker.amphibian()
    assert animal['class'] == 'amphibians'


