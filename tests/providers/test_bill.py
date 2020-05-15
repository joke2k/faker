import re
import unittest
from faker import Faker
from faker.providers.bill.fa_IR.checker import check_bill_id


class TestBillFaIrProvider(unittest.TestCase):
    """ Test bill in fa_IR locale """

    def setUp(self):
        self.fake = Faker('fa-IR')
        Faker.seed(0)

    def test_bill_name(self):
        bill_name = self.fake.bill_name()
        assert re.match("^[\u0600-\u06FF ]+$", bill_name)

    def test_provider_name(self):
        bill_provider = self.fake.bill_name()
        assert re.match("^[\u0600-\u06FF ]+$", bill_provider)

    def test_bill_id(self):
        bill_id = self.fake.bill_id()
        assert isinstance(bill_id, str)
        assert check_bill_id(bill_id)

    def test_payment_id(self):
        payment_id = self.fake.bill_payment_id()
        assert isinstance(payment_id, str)

    def test_full(self):
        bill_full = self.fake.bill_full()
        assert isinstance(bill_full, str)
