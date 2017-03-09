import unittest
from faker.providers.isbn.en_US import Provider as ISBNProvider
from faker.providers.isbn import ISBN13
from faker.providers.isbn.rules import RegistrantRule


class TestISBN13(unittest.TestCase):

    def test_check_digit_is_correct(self):
        isbn = ISBN13(ean='978', group='1', registrant='4516', publication='7331')
        assert isbn.check_digit == '9'
        isbn = ISBN13(ean='978', group='1', registrant='59327', publication='599')
        assert isbn.check_digit == '0'
        isbn = ISBN13(ean='978', group='1', registrant='4919', publication='2757')
        assert isbn.check_digit == '1'

    def test_format_length(self):
        isbn = ISBN13(ean='978', group='1', registrant='4516', publication='7331')
        assert len(isbn.format()) == 13


class TestProvider(unittest.TestCase):

    def setUp(self):
        self.prov = ISBNProvider(None)

    def test_reg_pub_separation(self):
        r1 = RegistrantRule('0000000', '0000001', 1)
        r2 = RegistrantRule('0000002', '0000003', 2)
        assert self.prov._registrant_publication('0000000', [r1, r2]) == ('0', '000000')
        assert self.prov._registrant_publication('0000002', [r1, r2]) == ('00', '00002')

    def test_rule_not_found(self):
        with self.assertRaises(Exception):
            r = RegistrantRule('0000000', '0000001', 1)
            self.prov._registrant_publication('0000002', [r])

