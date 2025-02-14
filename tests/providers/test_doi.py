import re

from faker import Faker


def test_doi():
    fake = Faker()

    # Test standard DOI
    doi = fake.doi()
    assert doi.startswith("10.")
    # DOI format: 10.{registrant}/{suffix}
    assert re.match(r"^10\.\d{4,9}/[a-z0-9]+$", doi)


def test_doi_es_ES():
    # Test Spanish locale no longer returns Spanish IDs
    fake = Faker("es_ES")
    doi = fake.doi()

    # Should follow DOI format, not Spanish ID format
    assert doi.startswith("10.")
    assert re.match(r"^10\.\d{4,9}/[a-z0-9]+$", doi)
    # Make sure it's not returning Spanish IDs
    assert not re.match(r"^[XYZ]\d{7}[A-Z]$", doi)  # NIE format
    assert not re.match(r"^\d{8}[A-Z]$", doi)  # NIF format
