import pytest

from faker import Faker
from faker.providers import DynamicProvider


class TestDynamicProvider:
    def test_without_dynamic(self):
        faker = Faker()
        with pytest.raises(
            AttributeError,
            match="'Generator' object has no attribute 'medical_profession'",
        ):
            faker.medical_profession()

    def test_with_dynamic(self):
        faker = Faker()
        elements = ["dr.", "doctor", "nurse", "surgeon", "clerk"]
        provider_name = "medical_profession"

        medical_professions_provider = DynamicProvider(
            provider_name=provider_name,
            elements=elements,
        )

        faker.add_provider(medical_professions_provider)

        assert faker.medical_profession() in elements

    def test_dynamic_with_special_provider_name(self):
        elements = ["dr.", "doctor", "nurse", "surgeon", "clerk"]
        provider_name = "__special__"  # The provider name cannot start with __

        with pytest.raises(
            ValueError,
            match="Provider name cannot start with __ as it would be ignored by Faker",
        ):
            DynamicProvider(
                provider_name=provider_name,
                elements=elements,
            )

    def test_dynamic_with_empty_elements(self):
        elements = []
        provider_name = "my_provider"
        provider = DynamicProvider(
            provider_name=provider_name,
            elements=elements,
        )
        faker = Faker()
        faker.add_provider(provider)

        with pytest.raises(
            ValueError,
            match="Elements should be a list of values the provider samples from",
        ):
            faker.my_provider()

    def test_dynamic_add_element(self):
        elements = []
        provider_name = "my_provider"
        provider = DynamicProvider(
            provider_name=provider_name,
            elements=elements,
        )
        faker = Faker()
        faker.add_provider(provider)

        provider.add_element("one")
        provider.add_element("two")

        assert faker.my_provider() in ("one", "two")
