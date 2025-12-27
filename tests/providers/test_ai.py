import pytest

from faker import Faker
from faker.providers.ai import Provider as AiProvider


@pytest.fixture
def faker():
    return Faker()


class TestAiProvider:
    """Test AI provider methods"""

    def test_ai_model(self, faker):
        for _ in range(100):
            result = faker.ai_model()
            assert isinstance(result, str)
            assert result in AiProvider.ai_models

    def test_ai_company(self, faker):
        for _ in range(100):
            result = faker.ai_company()
            assert isinstance(result, str)
            assert result in AiProvider.ai_companies

    def test_ai_model_architecture(self, faker):
        for _ in range(100):
            result = faker.ai_model_architecture()
            assert isinstance(result, str)
            assert result in AiProvider.ai_model_architectures

    def test_ml_framework(self, faker):
        for _ in range(100):
            result = faker.ml_framework()
            assert isinstance(result, str)
            assert result in AiProvider.ml_frameworks

    def test_ai_task(self, faker):
        for _ in range(100):
            result = faker.ai_task()
            assert isinstance(result, str)
            assert result in AiProvider.ai_tasks

    def test_ai_model_parameter(self, faker):
        for _ in range(100):
            result = faker.ai_model_parameter()
            assert isinstance(result, str)
            assert result in AiProvider.ai_model_parameters

    def test_ai_dataset(self, faker):
        for _ in range(100):
            result = faker.ai_dataset()
            assert isinstance(result, str)
            assert result in AiProvider.ai_datasets
