import pytest

from faker import Faker
from faker.providers.ecommerce import Provider as EcommerceProvider


@pytest.fixture
def faker():
    return Faker()


class TestEcommerceProvider:
    """Test e-commerce provider methods"""

    def test_product_category(self, faker):
        for _ in range(100):
            result = faker.product_category()
            assert isinstance(result, str)
            assert result in EcommerceProvider.product_categories

    def test_product_name(self, faker):
        for _ in range(100):
            result = faker.product_name()
            assert isinstance(result, str)
            assert "Item" in result

    def test_shipping_carrier(self, faker):
        for _ in range(100):
            result = faker.shipping_carrier()
            assert isinstance(result, str)
            assert result in EcommerceProvider.shipping_carriers

    def test_payment_method(self, faker):
        for _ in range(100):
            result = faker.payment_method()
            assert isinstance(result, str)
            assert result in EcommerceProvider.payment_methods

    def test_order_status(self, faker):
        for _ in range(100):
            result = faker.order_status()
            assert isinstance(result, str)
            assert result in EcommerceProvider.order_statuses

    def test_customer_type(self, faker):
        for _ in range(100):
            result = faker.customer_type()
            assert isinstance(result, str)
            assert result in EcommerceProvider.customer_types

    def test_return_reason(self, faker):
        for _ in range(100):
            result = faker.return_reason()
            assert isinstance(result, str)
            assert result in EcommerceProvider.return_reasons

    def test_sku(self, faker):
        for _ in range(100):
            result = faker.sku()
            assert isinstance(result, str)
            assert "-" in result
            parts = result.split("-")
            assert len(parts) == 3

    def test_order_id(self, faker):
        for _ in range(100):
            result = faker.order_id()
            assert isinstance(result, str)
            assert result.startswith("ORD-")

    def test_tracking_number(self, faker):
        for _ in range(100):
            result = faker.tracking_number()
            assert isinstance(result, str)
            assert len(result) >= 14

    def test_coupon_code(self, faker):
        for _ in range(100):
            result = faker.coupon_code()
            assert isinstance(result, str)
            assert len(result) >= 4

    def test_price(self, faker):
        for _ in range(100):
            result = faker.price()
            assert isinstance(result, str)
            assert result.startswith("$")
            assert "." in result

    def test_discount_percentage(self, faker):
        for _ in range(100):
            result = faker.discount_percentage()
            assert isinstance(result, str)
            assert result.endswith("%")

    def test_review_rating(self, faker):
        for _ in range(100):
            result = faker.review_rating()
            assert isinstance(result, int)
            assert 1 <= result <= 5
