import pytest

from faker import Faker
from faker.providers.healthcare import Provider as HealthcareProvider


@pytest.fixture
def faker():
    return Faker()


class TestHealthcareProvider:
    """Test healthcare provider methods"""

    def test_disease(self, faker):
        for _ in range(100):
            result = faker.disease()
            assert isinstance(result, str)
            assert result in HealthcareProvider.diseases

    def test_icd10_code(self, faker):
        for _ in range(100):
            result = faker.icd10_code()
            assert isinstance(result, str)
            assert result in HealthcareProvider.icd10_codes

    def test_medical_specialty(self, faker):
        for _ in range(100):
            result = faker.medical_specialty()
            assert isinstance(result, str)
            assert result in HealthcareProvider.medical_specialties

    def test_hospital_department(self, faker):
        for _ in range(100):
            result = faker.hospital_department()
            assert isinstance(result, str)
            assert result in HealthcareProvider.hospital_departments

    def test_generic_drug(self, faker):
        for _ in range(100):
            result = faker.generic_drug()
            assert isinstance(result, str)
            assert result in HealthcareProvider.generic_drugs

    def test_brand_drug(self, faker):
        for _ in range(100):
            result = faker.brand_drug()
            assert isinstance(result, str)
            assert result in HealthcareProvider.brand_drugs

    def test_symptom(self, faker):
        for _ in range(100):
            result = faker.symptom()
            assert isinstance(result, str)
            assert result in HealthcareProvider.symptoms

    def test_blood_type(self, faker):
        for _ in range(100):
            result = faker.blood_type()
            assert isinstance(result, str)
            assert result in HealthcareProvider.blood_types

    def test_allergy(self, faker):
        for _ in range(100):
            result = faker.allergy()
            assert isinstance(result, str)
            assert result in HealthcareProvider.allergies

    def test_medical_procedure(self, faker):
        for _ in range(100):
            result = faker.medical_procedure()
            assert isinstance(result, str)
            assert result in HealthcareProvider.medical_procedures

    def test_insurance_plan(self, faker):
        for _ in range(100):
            result = faker.insurance_plan()
            assert isinstance(result, str)
            assert result in HealthcareProvider.insurance_plans

    def test_vital_sign(self, faker):
        for _ in range(100):
            result = faker.vital_sign()
            assert isinstance(result, str)
            assert result in HealthcareProvider.vital_signs

    def test_diagnosis(self, faker):
        for _ in range(100):
            result = faker.diagnosis()
            assert isinstance(result, str)
            assert "(" in result
            assert ")" in result
