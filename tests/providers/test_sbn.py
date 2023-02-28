import pytest

from faker.providers.sbn import SBN9
from faker.providers.sbn.en_US import Provider as SBNProvider
from faker.providers.sbn.rules import RegistrantRule


class TestISBN9:
    def test_check_digit_is_correct(self):
        sbn = SBN9(registrant="340", publication="01381")
        assert sbn.check_digit == "X"
        sbn = SBN9(registrant="06", publication="230125")
        assert sbn.check_digit == "2"
        sbn = SBN9(registrant="10103", publication="202")
        assert sbn.check_digit == "3"

    def test_format_length(self):
        sbn = SBN9(registrant="4516", publication="7331")
        assert len(sbn.format()) == 9
        sbn = SBN9(registrant="451", publication="10036")
        assert len(sbn.format()) == 9


class TestProvider:
    prov = SBNProvider(None)

    def test_reg_pub_separation(self):
        r1 = RegistrantRule("0000000", "0000001", 1)
        r2 = RegistrantRule("0000002", "0000003", 2)
        assert self.prov._registrant_publication("00000000", [r1, r2]) == (
            "0",
            "0000000",
        )
        assert self.prov._registrant_publication("00000010", [r1, r2]) == (
            "0",
            "0000010",
        )
        assert self.prov._registrant_publication("00000019", [r1, r2]) == (
            "0",
            "0000019",
        )
        assert self.prov._registrant_publication("00000020", [r1, r2]) == (
            "00",
            "000020",
        )
        assert self.prov._registrant_publication("00000030", [r1, r2]) == (
            "00",
            "000030",
        )
        assert self.prov._registrant_publication("00000031", [r1, r2]) == (
            "00",
            "000031",
        )
        assert self.prov._registrant_publication("00000039", [r1, r2]) == (
            "00",
            "000039",
        )

    def test_rule_not_found(self):
        with pytest.raises(Exception):
            r = RegistrantRule("0000000", "0000001", 1)
            self.prov._registrant_publication("0000002", [r])
