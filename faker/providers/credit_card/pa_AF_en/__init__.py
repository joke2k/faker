from collections import OrderedDict
from faker.typing import CreditCard
from .. import Provider as CreditCardProvider

class Provider(CreditCardProvider):
    """Implement credit card provider for English Afghanistan locale.
    Note: Afghanistan banks primarily issue international Visa and Mastercard debit/credit cards.
    Specific local prefixes are limited and mostly international (e.g., Visa starts with 4).
    This provider uses realistic patterns based on major Afghan banks issuing Visa/Mastercard.
    CVV is called CVV2 in Afghanistan as well.
    """

    # Example prefixes based on common international cards issued in Afghanistan
    prefix_visa = ["4"]
    prefix_mastercard = ["51", "52", "53", "54", "55"]

    prefix_aib = ["4"]  # Afghanistan International Bank - Visa
    prefix_azizi = ["51"]  # Azizi Bank - Mastercard example
    prefix_millie = ["4"]
    prefix_new_kabul = ["4"]
    prefix_islamic = ["52"]
    prefix_ghazanfar = ["53"]

    credit_card_types = OrderedDict((
        ("aib", CreditCard("Afghanistan International Bank", prefix_aib, 16, security_code="CVV2")),
        ("azizi", CreditCard("Azizi Bank", prefix_azizi, 16, security_code="CVV2")),
        ("millie", CreditCard("Bank-e-Millie Afghan", prefix_millie, 16, security_code="CVV2")),
        ("new_kabul", CreditCard("New Kabul Bank", prefix_new_kabul, 16, security_code="CVV2")),
        ("islamic", CreditCard("Islamic Bank of Afghanistan", prefix_islamic, 16, security_code="CVV2")),
        ("ghazanfar", CreditCard("Ghazanfar Bank", prefix_ghazanfar, 16, security_code="CVV2")),
        ("visa", CreditCard("Visa", prefix_visa, 16, security_code="CVV2")),
        ("mastercard", CreditCard("Mastercard", prefix_mastercard, 16, security_code="CVV2")),
    ))