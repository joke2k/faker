import datetime
import re
import unittest

from unittest import mock

from faker import Faker
from faker.providers.person.ar_AA import Provider as ArProvider
from faker.providers.person.az_AZ import Provider as AzAzProvider
from faker.providers.person.cs_CZ import Provider as CsCZProvider
from faker.providers.person.en import Provider as EnProvider
from faker.providers.person.en_GB import Provider as EnGBProvider
from faker.providers.person.en_IE import Provider as EnIEProvider
from faker.providers.person.en_IN import Provider as EnINProvider
from faker.providers.person.en_PK import Provider as EnPKprovider
from faker.providers.person.en_US import Provider as EnUSProvider
from faker.providers.person.es import Provider as EsProvider
from faker.providers.person.es_CO import Provider as EsCOProvider
from faker.providers.person.et_EE import Provider as EtEEProvider
from faker.providers.person.fi_FI import Provider as FiProvider
from faker.providers.person.fr_BE import Provider as FrBEProvider
from faker.providers.person.ga_IE import Provider as GaIEProvider
from faker.providers.person.gu_IN import Provider as GuINProvider
from faker.providers.person.he_IL import Provider as HeILProvider
from faker.providers.person.hi_IN import Provider as HiINProvider
from faker.providers.person.hy_AM import Provider as HyAmProvider
from faker.providers.person.lv_LV import Provider as LvProvider
from faker.providers.person.ne_NP import Provider as NeProvider
from faker.providers.person.nl_BE import Provider as NlBEProvider
from faker.providers.person.or_IN import Provider as OrINProvider
from faker.providers.person.pl_PL import Provider as PlPLProvider
from faker.providers.person.pl_PL import checksum_identity_card_number as pl_checksum_identity_card_number
from faker.providers.person.pt_PT import Provider as PtPtProvider
from faker.providers.person.ru_RU import Provider as RuProvider
from faker.providers.person.ru_RU import translit
from faker.providers.person.sk_SK import Provider as SkSKProvider
from faker.providers.person.sv_SE import Provider as SvSEProvider
from faker.providers.person.sw import Provider as SwProvider
from faker.providers.person.ta_IN import Provider as TaINProvider
from faker.providers.person.th_TH import Provider as ThThProvider
from faker.providers.person.uk_UA import Provider as UkUAProvider
from faker.providers.person.uk_UA import translit as UkUATranslit
from faker.providers.person.vi_VN import Provider as ViVNProvider
from faker.providers.person.yo_NG import Provider as YoNGProvider
from faker.providers.person.zh_CN import Provider as ZhCNProvider
from faker.providers.person.zh_TW import Provider as ZhTWProvider
from faker.providers.person.zu_ZA import Provider as ZuZAProvider


class TestAr(unittest.TestCase):
    """Tests person in the ar locale"""

    def setUp(self):
        self.fake = Faker("ar")
        Faker.seed(0)

    def test_first_name(self):
        # General first name
        name = self.fake.first_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in ArProvider.first_names

        # Females first name
        name = self.fake.first_name_female()
        assert name
        self.assertIsInstance(name, str)
        assert name in ArProvider.first_names
        assert name in ArProvider.first_names_female

        # Male first name
        name = self.fake.first_name_male()
        assert name
        self.assertIsInstance(name, str)
        assert name in ArProvider.first_names
        assert name in ArProvider.first_names_male

    def test_last_name(self):
        # There's no gender-specific last name in Arabic.
        assert not hasattr(ArProvider, "last_names_male")
        assert not hasattr(ArProvider, "last_names_female")
        # All last names apply for all genders.
        assert hasattr(ArProvider, "last_names")

        # General last name.
        name = self.fake.last_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in ArProvider.last_names

        # Females last name.
        name = self.fake.last_name_female()
        assert name
        self.assertIsInstance(name, str)
        assert name in ArProvider.last_names
        assert name in ArProvider.last_names

        # Male last name.
        name = self.fake.last_name_male()
        assert name
        self.assertIsInstance(name, str)
        assert name in ArProvider.last_names
        assert name in ArProvider.last_names


class TestAzAz(unittest.TestCase):
    """Tests for az_AZ locale person provider"""

    def setUp(self):
        self.fake = Faker("az")
        Faker.seed(0)

    def test_first_name(self):
        # General first name
        name = self.fake.first_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in AzAzProvider.first_names

        # Females first name
        name = self.fake.first_name_female()
        assert name
        self.assertIsInstance(name, str)
        assert name in AzAzProvider.first_names
        assert name in AzAzProvider.first_names_female

        # Male first name
        name = self.fake.first_name_male()
        assert name
        self.assertIsInstance(name, str)
        assert name in AzAzProvider.first_names
        assert name in AzAzProvider.first_names_male

    def test_last_name(self):
        # General last name.
        name = self.fake.last_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in AzAzProvider.last_names

        # Females last name.
        name = self.fake.last_name_female()
        assert name
        self.assertIsInstance(name, str)
        assert name in AzAzProvider.last_names_female + AzAzProvider.last_names_unisex

        # Females only last name.
        name = self.fake.last_name_unique_to_female()
        assert name
        self.assertIsInstance(name, str)
        assert name in AzAzProvider.last_names_female

        # Male last name.
        name = self.fake.last_name_male()
        assert name
        self.assertIsInstance(name, str)
        assert name in AzAzProvider.last_names_male + AzAzProvider.last_names_unisex

        # Male only last name.
        name = self.fake.last_name_unique_to_male()
        assert name
        self.assertIsInstance(name, str)
        assert name in AzAzProvider.last_names_male


class TestCsCZ(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("cs_CZ")
        Faker.seed(0)

    def test_name_male(self):
        male_name = self.fake.name_male()
        name_parts = male_name.split(" ")
        first_name, last_name = "", ""
        if len(name_parts) == 2:
            first_name = name_parts[0]
            last_name = name_parts[1]
        elif len(name_parts) == 4:
            first_name = name_parts[1]
            last_name = name_parts[2]
        elif len(name_parts) == 3:
            if name_parts[-1] in CsCZProvider.suffixes:
                first_name = name_parts[0]
                last_name = name_parts[1]
            else:
                first_name = name_parts[1]
                last_name = name_parts[2]
        assert first_name in CsCZProvider.first_names_male
        assert last_name in CsCZProvider.last_names_male

    def test_name_female(self):
        female_name = self.fake.name_female()
        name_parts = female_name.split(" ")
        first_name, last_name = "", ""
        if len(name_parts) == 2:
            first_name = name_parts[0]
            last_name = name_parts[1]
        elif len(name_parts) == 4:
            first_name = name_parts[1]
            last_name = name_parts[2]
        elif len(name_parts) == 3:
            if name_parts[-1] in CsCZProvider.suffixes:
                first_name = name_parts[0]
                last_name = name_parts[1]
            else:
                first_name = name_parts[1]
                last_name = name_parts[2]
        assert first_name in CsCZProvider.first_names_female
        assert last_name in CsCZProvider.last_names_female


class TestEn(unittest.TestCase):
    """Tests person in the en locale"""

    def setUp(self):
        self.fake = Faker("en")
        Faker.seed(0)

    def test_suffix(self):
        # Traditional suffix -- provider does not offer a nonbinary suffix at this time
        suffix = self.fake.suffix()
        self.assertIsInstance(suffix, str)
        assert suffix in EnProvider.suffixes_male or suffix in EnProvider.suffixes_female


class TestEnGB(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("en_GB")
        Faker.seed(0)

    def test_first_name_female(self):
        name = self.fake.first_name_female()
        assert name in EnGBProvider.first_names_female

    def test_first_name_male(self):
        name = self.fake.first_name_male()
        assert name in EnGBProvider.first_names_male

    def test_name_female(self):
        full_name = self.fake.name_female()
        first_name = self.get_first_name_from_full_name(full_name)
        assert first_name in EnGBProvider.first_names_female

    def test_name_male(self):
        full_name = self.fake.name_male()
        first_name = self.get_first_name_from_full_name(full_name)
        assert first_name in EnGBProvider.first_names_male

    def get_first_name_from_full_name(self, full_name):
        names = full_name.split(" ")
        if len(names) == 2:
            return names[0]
        return names[1]


class TestEnIE(unittest.TestCase):
    """Tests person in the en-IE locale"""

    def setUp(self):
        self.fake = Faker("en-ie")
        self.provider = EnIEProvider
        Faker.seed(0)

    def test_first_name(self):
        # General first name
        name = self.fake.first_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.first_names

        # Females first name
        name = self.fake.first_name_female()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.first_names
        assert name in self.provider.first_names_female

        # Male first name
        name = self.fake.first_name_male()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.first_names
        assert name in self.provider.first_names_male

    def test_last_name(self):
        assert not hasattr(self.provider, "last_names_male")
        assert not hasattr(self.provider, "last_names_female")
        # All last names apply for all genders.
        assert hasattr(self.provider, "last_names")

        # General last name.
        name = self.fake.last_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.last_names

        # Females last name.
        name = self.fake.last_name_female()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.last_names
        assert name in self.provider.last_names

        # Male last name.
        name = self.fake.last_name_male()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.last_names


class TestEnIN(unittest.TestCase):
    """Tests person in the en_IN locale"""

    def setUp(self):
        self.fake = Faker("en_IN")
        Faker.seed(0)

    def test_first_name(self):
        """Verify that gender specific names are set correctly"""

        name = self.fake.first_name_female()
        assert name in EnINProvider.first_names_female

        name = self.fake.first_name_male()
        assert name in EnINProvider.first_names_male

        first_name = self.fake.first_name()
        assert first_name in EnINProvider.first_names

    def test_last_name(self):
        last_name = self.fake.last_name()
        assert last_name in EnINProvider.last_names


class TestEnPk(unittest.TestCase):
    def setUp(self):
        """Set up the Faker instance with the Pakistani locale."""
        self.fake = Faker("en_PK")

    def test_first_name(self):
        """Test if the first name is from the predefined list."""
        first_name = self.fake.first_name()
        self.assertIn(first_name, EnPKprovider.first_names)

    def test_last_name(self):
        """Test if the last name is from the predefined list."""
        last_name = self.fake.last_name()
        self.assertIn(last_name, EnPKprovider.last_names)

    def test_full_name(self):
        """Test if the generated full name follows the correct format."""
        full_name = self.fake.name()
        name_parts = full_name.split()
        self.assertIn(name_parts[0], EnPKprovider.first_names)
        self.assertIn(name_parts[-1], EnPKprovider.last_names)

    def test_name_format(self):
        """Test if the generated name format is as expected."""
        name = self.fake.name()
        name_parts = name.split()
        self.assertGreaterEqual(len(name_parts), 2, "Full name should have at least a first and last name.")
        self.assertIn(name_parts[0], EnPKprovider.first_names)
        self.assertIn(name_parts[-1], EnPKprovider.last_names)


class TestEnUS(unittest.TestCase):
    """Tests person in the en_US locale"""

    def setUp(self):
        self.fake = Faker("en_US")
        Faker.seed(0)

    def test_first_names(self):
        # General first name
        name = self.fake.first_name()
        self.assertIsInstance(name, str)
        assert name in EnUSProvider.first_names

        # Female first name
        name = self.fake.first_name_female()
        self.assertIsInstance(name, str)
        assert name in EnUSProvider.first_names
        assert name in EnUSProvider.first_names_female

        # Male first name
        name = self.fake.first_name_male()
        self.assertIsInstance(name, str)
        assert name in EnUSProvider.first_names
        assert name in EnUSProvider.first_names_male

        # Nonbinary first name
        name = self.fake.first_name_nonbinary()
        self.assertIsInstance(name, str)
        assert name in EnUSProvider.first_names
        assert name in EnUSProvider.first_names_nonbinary

    def test_last_names(self):
        # General last name
        name = self.fake.last_name()
        self.assertIsInstance(name, str)
        assert name in EnUSProvider.last_names

        # Female last name
        name = self.fake.last_name_female()
        self.assertIsInstance(name, str)
        assert name in EnUSProvider.last_names

        # Male last name
        name = self.fake.last_name_male()
        self.assertIsInstance(name, str)
        assert name in EnUSProvider.last_names

        # Nonbinary last name
        name = self.fake.last_name_nonbinary()
        self.assertIsInstance(name, str)
        assert name in EnUSProvider.last_names

    def test_prefix(self):
        # Nonbinary prefix
        prefix = self.fake.prefix_nonbinary()
        self.assertIsInstance(prefix, str)
        assert prefix in EnUSProvider.prefixes_nonbinary

    def test_suffix(self):
        # Nonbinary suffix
        suffix = self.fake.suffix_nonbinary()
        self.assertIsInstance(suffix, str)
        assert suffix in EnUSProvider.suffixes_nonbinary


class TestEs(unittest.TestCase):
    """Tests person in the es locale."""

    def setUp(self):
        self.fake = Faker("es")
        Faker.seed(0)

    def test_language_name(self):
        language_name = self.fake.language_name()
        assert language_name in EsProvider.language_names


class TestEsCO(unittest.TestCase):
    """Tests person in the es_CO locale"""

    def setUp(self):
        self.fake = Faker("es_CO")
        Faker.seed(0)

    def test_first_names(self):
        # General first name
        name = self.fake.first_name()
        self.assertIsInstance(name, str)
        assert name in EsCOProvider.first_names

        # Female first name
        name = self.fake.first_name_female()
        self.assertIsInstance(name, str)
        assert name in EsCOProvider.first_names
        assert name in EsCOProvider.first_names_female

        # Male first name
        name = self.fake.first_name_male()
        self.assertIsInstance(name, str)
        assert name in EsCOProvider.first_names
        assert name in EsCOProvider.first_names_male

    def test_last_names(self):
        # General last name
        name = self.fake.last_name()
        self.assertIsInstance(name, str)
        assert name in EsCOProvider.last_names

        # Female last name
        name = self.fake.last_name_female()
        self.assertIsInstance(name, str)
        assert name in EsCOProvider.last_names

        # Male last name
        name = self.fake.last_name_male()
        self.assertIsInstance(name, str)
        assert name in EsCOProvider.last_names

    def test_prefix(self):
        # Female prefix
        prefix = self.fake.prefix_female()
        self.assertIsInstance(prefix, str)
        assert prefix in EsCOProvider.prefixes_female

        # Male prefix
        prefix = self.fake.prefix_male()
        self.assertIsInstance(prefix, str)
        assert prefix in EsCOProvider.prefixes_male


class TestEtEE(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("et_EE")
        self.provider = EtEEProvider
        Faker.seed(0)

    def test_first_name(self):
        # General first name
        name = self.fake.first_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.first_names

        # Est first name
        name = self.fake.first_name_est()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.first_names
        assert name in self.provider.first_names_est

        # Rus first name
        name = self.fake.first_name_rus()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.first_names
        assert name in self.provider.first_names_rus

        # Females first name
        name = self.fake.first_name_female()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.first_names
        assert name in self.provider.first_names_female

        # Est females first name
        name = self.fake.first_name_female_est()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.first_names
        assert name in self.provider.first_names_female
        assert name in self.provider.first_names_female_est

        # Rus females first name
        name = self.fake.first_name_female_rus()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.first_names
        assert name in self.provider.first_names_female
        assert name in self.provider.first_names_female_rus

        # Male first name
        name = self.fake.first_name_male()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.first_names
        assert name in self.provider.first_names_male

        # Est male first name
        name = self.fake.first_name_male_est()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.first_names
        assert name in self.provider.first_names_male
        assert name in self.provider.first_names_male_est

        # Rus male first name
        name = self.fake.first_name_male_rus()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.first_names
        assert name in self.provider.first_names_male
        assert name in self.provider.first_names_male_rus

    def test_last_name(self):
        # General last name.
        name = self.fake.last_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.last_names

        # Est last name.
        name = self.fake.last_name_est()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.last_names
        assert name in self.provider.last_names_est

        # Rus last name.
        name = self.fake.last_name_rus()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.last_names
        assert name in self.provider.last_names_rus


class TestFiFI(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("fi_FI")
        Faker.seed(0)

    def test_gender_first_names(self):
        female_name = self.fake.first_name_female()
        self.assertIsInstance(female_name, str)
        assert female_name in FiProvider.first_names_female
        male_name = self.fake.first_name_male()
        self.assertIsInstance(male_name, str)
        assert male_name in FiProvider.first_names_male
        first_name = self.fake.first_name()
        self.assertIsInstance(first_name, str)
        assert first_name in FiProvider.first_names

    def test_last_names(self):
        last_name = self.fake.last_name()
        self.assertIsInstance(last_name, str)
        assert last_name in FiProvider.last_names


class TestFrBE(unittest.TestCase):
    """Tests person in the fr-BE locale"""

    def setUp(self):
        self.fake = Faker("fr-BE")
        self.provider = FrBEProvider
        Faker.seed(0)

    def test_first_name(self):
        # General first name
        name = self.fake.first_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.first_names

        # Females first name
        name = self.fake.first_name_female()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.first_names
        assert name in self.provider.first_names_female

        # Male first name
        name = self.fake.first_name_male()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.first_names
        assert name in self.provider.first_names_male

    def test_last_name(self):
        assert not hasattr(self.provider, "last_names_male")
        assert not hasattr(self.provider, "last_names_female")
        # All last names apply for all genders.
        assert hasattr(self.provider, "last_names")

        # General last name.
        name = self.fake.last_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.last_names

        # Females last name.
        name = self.fake.last_name_female()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.last_names
        assert name in self.provider.last_names

        # Male last name.
        name = self.fake.last_name_male()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.last_names


class TestGaIE(TestEnIE):
    """Tests person in the ga-IE locale"""

    def setUp(self):
        self.fake = Faker("ga-ie")
        self.provider = GaIEProvider
        Faker.seed(0)


class TestGuIN(unittest.TestCase):
    """Tests person in the gu_IN locale"""

    def setUp(self):
        self.fake = Faker("gu_IN")
        Faker.seed(0)

    """Verify that gender specific names are set correctly"""

    def test_first_name(self):
        name = self.fake.first_name()
        self.assertIsInstance(name, str)
        assert name in GuINProvider.first_names

    def test_first_name_male(self):
        name = self.fake.first_name_male()
        self.assertIsInstance(name, str)
        assert name in GuINProvider.first_names_male

    def test_first_name_female(self):
        name = self.fake.first_name_female()
        self.assertIsInstance(name, str)
        assert name in GuINProvider.first_names_female

    def test_last_name(self):
        last_name = self.fake.last_name()
        self.assertIsInstance(last_name, str)
        assert last_name in GuINProvider.last_names

    def test_name(self):
        name = self.fake.name().split()
        assert all(isinstance(n, str) for n in name)
        if len(name) == 3:
            assert all(
                [
                    name[0] in GuINProvider.prefixes,
                    name[1] in GuINProvider.first_names,
                    name[2] in GuINProvider.last_names,
                ]
            )
        else:
            assert name[0] in GuINProvider.first_names
            assert name[-1] in GuINProvider.last_names

    """Verify that gender specific prefixes are set correctly"""

    def test_prefix(self):
        prefix = self.fake.prefix()
        self.assertIsInstance(prefix, str)
        assert prefix in GuINProvider.prefixes

    def test_prefix_female(self):
        prefix = self.fake.prefix_female()
        self.assertIsInstance(prefix, str)
        assert prefix in GuINProvider.prefixes_female

    def test_prefix_male(self):
        prefix = self.fake.prefix_male()
        self.assertIsInstance(prefix, str)
        assert prefix in GuINProvider.prefixes_male


class TestHeIL(unittest.TestCase):
    """Tests person in the he_IL locale."""

    def setUp(self):
        self.fake = Faker("he_IL")
        Faker.seed(0)

    def test_language_name(self):
        language_name = self.fake.language_name()
        assert language_name in HeILProvider.language_names

    def test_male_first_name(self):
        first_name_male = self.fake.first_name_male()
        assert first_name_male in HeILProvider.first_names_male

    def test_female_first_name(self):
        first_name_female = self.fake.first_name_female()
        assert first_name_female in HeILProvider.first_names_female

    def test_last_name(self):
        last_name = self.fake.last_name()
        assert last_name in HeILProvider.last_names


class TestHiIN(unittest.TestCase):
    """Tests person in the hi_IN locale"""

    def setUp(self):
        self.fake = Faker("hi_IN")
        Faker.seed(0)

    def test_first_name(self):
        """Verify that gender specific names are set correctly"""

        name = self.fake.first_name_male()
        assert name in HiINProvider.first_names_male

        name = self.fake.first_name_female()
        assert name in HiINProvider.first_names_female

        name = self.fake.first_name()
        assert name in HiINProvider.first_names_male

    def test_last_name(self):
        last_name = self.fake.last_name()
        assert last_name in HiINProvider.last_names

    def test_name(self):
        name = self.fake.name().split()

        assert all(isinstance(n, str) for n in name)

        prefixes = HiINProvider.prefixes_male + HiINProvider.prefixes_female + HiINProvider.prefixes

        # name should always be 2-3 words. If 3, first word should be a prefix.
        if len(name) == 3:
            assert all(
                [
                    name[0] in prefixes,
                    name[1] in HiINProvider.first_names,
                    name[2] in HiINProvider.last_names,
                ]
            )
        else:
            assert name[0] in HiINProvider.first_names
            if name[-1].endswith(HiINProvider.suffixes):
                assert name[-1][:-1] in HiINProvider.last_names
                assert name[-1][-1] in HiINProvider.suffixes
            else:
                assert name[-1] in HiINProvider.last_names


class TestHyAM(unittest.TestCase):
    """Tests person in the hy_AM locale"""

    def setUp(self):
        self.fake = Faker("hy_AM")
        Faker.seed(0)

    def test_name(self):
        # General name
        name = self.fake.name()
        self.assertIsInstance(name, str)

        # Female name
        name = self.fake.name_female()
        self.assertIsInstance(name, str)

        # Male name
        name = self.fake.name_male()
        self.assertIsInstance(name, str)

    def test_first_name(self):
        # General first name
        name = self.fake.first_name()
        self.assertIsInstance(name, str)
        assert name in HyAmProvider.first_names

        # Female first name
        name = self.fake.first_name_female()
        self.assertIsInstance(name, str)
        assert name in HyAmProvider.first_names
        assert name in HyAmProvider.first_names_female

        # Male first name
        name = self.fake.first_name_male()
        self.assertIsInstance(name, str)
        assert name in HyAmProvider.first_names
        assert name in HyAmProvider.first_names_male

    def test_last_name(self):
        # There's no gender-specific last name in Armenian.
        assert not hasattr(HyAmProvider, "last_names_male")
        assert not hasattr(HyAmProvider, "last_names_female")
        # All last names apply for all genders.
        assert hasattr(HyAmProvider, "last_names")

        # General last name.
        name = self.fake.last_name()
        self.assertIsInstance(name, str)
        assert name in HyAmProvider.last_names

        # Females last name.
        name = self.fake.last_name_female()
        self.assertIsInstance(name, str)
        assert name in HyAmProvider.last_names

        # Male last name.
        name = self.fake.last_name_male()
        self.assertIsInstance(name, str)
        assert name in HyAmProvider.last_names


class TestJaJP(unittest.TestCase):
    """Tests person in the ja_JP locale"""

    def setUp(self):
        self.fake = Faker("ja")
        Faker.seed(0)

    def test_person(self):
        name = self.fake.name()
        assert name
        assert isinstance(name, str)

        first_name = self.fake.first_name()
        assert first_name
        assert isinstance(first_name, str)

        last_name = self.fake.last_name()
        assert last_name
        assert isinstance(last_name, str)

        kana_name = self.fake.kana_name()
        assert kana_name
        assert isinstance(kana_name, str)

        first_kana_name = self.fake.first_kana_name()
        assert first_kana_name
        assert isinstance(first_kana_name, str)

        first_kana_name_male = self.fake.first_kana_name_male()
        assert first_kana_name_male
        assert isinstance(first_kana_name_male, str)

        first_kana_name_female = self.fake.first_kana_name_female()
        assert first_kana_name_female
        assert isinstance(first_kana_name_female, str)

        last_kana_name = self.fake.last_kana_name()
        assert last_kana_name
        assert isinstance(last_kana_name, str)

        romanized_name = self.fake.romanized_name()
        assert romanized_name
        assert isinstance(romanized_name, str)

        first_romanized_name = self.fake.first_romanized_name()
        assert first_romanized_name
        assert isinstance(first_romanized_name, str)

        first_romanized_name_male = self.fake.first_romanized_name_male()
        assert first_romanized_name_male
        assert isinstance(first_romanized_name_male, str)

        first_romanized_name_female = self.fake.first_romanized_name_female()
        assert first_romanized_name_female
        assert isinstance(first_romanized_name_female, str)

        last_romanized_name = self.fake.last_romanized_name()
        assert last_romanized_name
        assert isinstance(last_romanized_name, str)

        first_name_pair = self.fake.first_name_pair()
        assert first_name_pair
        assert len(first_name_pair) == 3
        assert all(s for s in first_name_pair if isinstance(s, str))

        first_name_male_pair = self.fake.first_name_male_pair()
        assert first_name_male_pair
        assert len(first_name_male_pair) == 3
        assert all(s for s in first_name_male_pair if isinstance(s, str))

        first_name_female_pair = self.fake.first_name_female_pair()
        assert first_name_female_pair
        assert len(first_name_female_pair) == 3
        assert all(isinstance(s, str) for s in first_name_female_pair)

        last_name_pair = self.fake.last_name_pair()
        assert last_name_pair
        assert len(last_name_pair) == 3
        assert all(isinstance(s, str) for s in last_name_pair)


class TestLvLV(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("lv_LV")
        Faker.seed(0)

    def test_first_name(self):
        # General first name
        name = self.fake.first_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in LvProvider.first_names

        # Females first name
        name = self.fake.first_name_female()
        assert name
        self.assertIsInstance(name, str)
        assert name in LvProvider.first_names
        assert name in LvProvider.first_names_female

        # Male first name
        name = self.fake.first_name_male()
        assert name
        self.assertIsInstance(name, str)
        assert name in LvProvider.first_names
        assert name in LvProvider.first_names_male

    def test_last_name(self):
        # General last name.
        name = self.fake.last_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in LvProvider.last_names

        # Females last name.
        name = self.fake.last_name_female()
        assert name
        self.assertIsInstance(name, str)
        assert name in LvProvider.last_names_female + LvProvider.last_names_nonbinary

        # Females only last name.
        name = self.fake.last_name_female()
        assert name
        self.assertIsInstance(name, str)
        assert name in LvProvider.last_names_female

        # Male last name.
        name = self.fake.last_name_male()
        assert name
        self.assertIsInstance(name, str)
        assert name in LvProvider.last_names_male + LvProvider.last_names_nonbinary

        # Male only last name.
        name = self.fake.last_name_male()
        assert name
        self.assertIsInstance(name, str)
        assert name in LvProvider.last_names_male


class TestNeNP(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("ne_NP")
        Faker.seed(0)

    def test_names(self):
        name = self.fake.name().split()
        assert all(isinstance(n, str) for n in name)
        # name should always be 2-3 words. If 3, first word
        # should be a prefix.
        assert name[-2] in NeProvider.first_names
        assert name[-1] in NeProvider.last_names
        prefixes = NeProvider.prefixes_male + NeProvider.prefixes_female
        if len(name) == 3:
            assert name[0] in prefixes


class TestNlBE(unittest.TestCase):
    """Tests person in the nl-BE locale"""

    def setUp(self):
        self.fake = Faker("nl-BE")
        self.provider = NlBEProvider
        Faker.seed(0)

    def test_first_name(self):
        # General first name
        name = self.fake.first_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.first_names

        # Females first name
        name = self.fake.first_name_female()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.first_names
        assert name in self.provider.first_names_female

        # Male first name
        name = self.fake.first_name_male()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.first_names
        assert name in self.provider.first_names_male

    def test_last_name(self):
        assert not hasattr(self.provider, "last_names_male")
        assert not hasattr(self.provider, "last_names_female")
        # All last names apply for all genders.
        assert hasattr(self.provider, "last_names")

        # General last name.
        name = self.fake.last_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.last_names

        # Females last name.
        name = self.fake.last_name_female()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.last_names
        assert name in self.provider.last_names

        # Male last name.
        name = self.fake.last_name_male()
        assert name
        self.assertIsInstance(name, str)
        assert name in self.provider.last_names


class TestOrIN(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("or_IN")
        Faker.seed(0)

    def test_first_names(self):
        """simple test to verify that we are pulling gender specific names"""
        name = self.fake.first_name_female()
        assert name in OrINProvider.first_names_female

        name = self.fake.first_name_male()
        assert name in OrINProvider.first_names_male

        name = self.fake.first_name_unisex()
        assert name in OrINProvider.first_names_unisex

        name = self.fake.first_name()
        assert name in OrINProvider.first_names

    def test_middle_names(self):
        """test the middle name"""
        name = self.fake.middle_name()
        assert name in OrINProvider.middle_names

    def test_last_names(self):
        """test the last name is generating from the provided tuple"""
        last_name = self.fake.last_name()
        assert last_name in OrINProvider.last_names


class TestPlPL(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("pl_PL")
        Faker.seed(0)

    def test_identity_card_number_checksum(self):
        assert pl_checksum_identity_card_number(["A", "I", "S", 8, 5, 0, 2, 1, 4]) == 8
        assert pl_checksum_identity_card_number(["A", "U", "L", 9, 2, 7, 2, 8, 5]) == 9
        assert pl_checksum_identity_card_number(["A", "E", "I", 2, 5, 1, 8, 2, 4]) == 2
        assert pl_checksum_identity_card_number(["A", "H", "F", 2, 2, 0, 6, 8, 0]) == 2
        assert pl_checksum_identity_card_number(["A", "X", "E", 8, 2, 0, 3, 4, 0]) == 8

    def test_identity_card_number(self):
        for _ in range(100):
            assert re.search(r"^[A-Z]{3}\d{6}$", self.fake.identity_card_number())

    @mock.patch.object(PlPLProvider, "random_digit")
    def test_pesel_birth_date(self, mock_random_digit):
        mock_random_digit.side_effect = [
            3,
            5,
            8,
            8,
            3,
            5,
            8,
            8,
            7,
            9,
            9,
            3,
            7,
            9,
            9,
            3,
            7,
            9,
            9,
            3,
        ]
        assert self.fake.pesel(datetime.date(1899, 12, 31)) == "99923135889"
        assert self.fake.pesel(datetime.date(1999, 12, 31)) == "99123135885"
        assert self.fake.pesel(datetime.date(2000, 1, 1)) == "00210179936"
        assert self.fake.pesel(datetime.date(2100, 1, 1)) == "00410179932"
        assert self.fake.pesel(datetime.date(2200, 1, 1)) == "00610179938"

    @mock.patch.object(PlPLProvider, "random_digit")
    def test_pesel_sex_male(self, mock_random_digit):
        mock_random_digit.side_effect = [1, 3, 4, 5, 6, 1, 7, 0]
        assert self.fake.pesel(datetime.date(1909, 3, 3), "M") == "09030313454"
        assert self.fake.pesel(datetime.date(1913, 8, 16), "M") == "13081661718"

    @mock.patch.object(PlPLProvider, "random_digit")
    def test_pesel_sex_female(self, mock_random_digit):
        mock_random_digit.side_effect = [4, 9, 1, 6, 6, 1, 7, 3]
        assert self.fake.pesel(datetime.date(2007, 4, 13), "F") == "07241349161"
        assert self.fake.pesel(datetime.date(1933, 12, 16), "F") == "33121661744"

    def test_pesel_value_error(self):
        self.assertRaises(ValueError, self.fake.pesel, datetime.date(2300, 1, 1))
        self.assertRaises(ValueError, self.fake.pesel, datetime.date(1799, 12, 31))

    @mock.patch.object(PlPLProvider, "random_digit")
    def test_pwz_doctor(self, mock_random_digit):
        mock_random_digit.side_effect = [6, 9, 1, 9, 6, 5, 2, 7, 9, 9, 1, 5]
        assert self.fake.pwz_doctor() == "2691965"
        assert self.fake.pwz_doctor() == "4279915"

    @mock.patch.object(PlPLProvider, "random_digit")
    def test_pwz_doctor_check_digit_zero(self, mock_random_digit):
        mock_random_digit.side_effect = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 9, 9]
        assert self.fake.pwz_doctor() == "6000012"
        assert self.fake.pwz_doctor() == "1000090"

    @mock.patch.object(PlPLProvider, "random_int")
    @mock.patch.object(PlPLProvider, "random_digit")
    def test_pwz_nurse(self, mock_random_digit, mock_random_int):
        mock_random_digit.side_effect = [3, 4, 5, 6, 7, 1, 7, 5, 1, 2]
        mock_random_int.side_effect = [45, 3]
        assert self.fake.pwz_nurse(kind="nurse") == "4534567P"
        assert self.fake.pwz_nurse(kind="midwife") == "0317512A"

    @staticmethod
    def validate_nip(nip_str):
        """
        Validates NIP using recommended code
        https://pl.wikibooks.org/wiki/Kody_%C5%BAr%C3%B3d%C5%82owe/Implementacja_NIP
        """
        nip_str = nip_str.replace("-", "")
        if len(nip_str) != 10 or not nip_str.isdigit():
            return False
        digits = [int(i) for i in nip_str]
        weights = (6, 5, 7, 2, 3, 4, 5, 6, 7)
        check_sum = sum(d * w for d, w in zip(digits, weights)) % 11
        return check_sum == digits[9]

    def test_nip(self):
        for _ in range(100):
            assert self.validate_nip(self.fake.nip())


class TestPtPt(unittest.TestCase):
    """Tests person in the pt_PT locale."""

    def setUp(self):
        self.fake = Faker("pt_PT")
        Faker.seed(0)

    def test_male_first_name(self):
        first_name_male = self.fake.first_name_male()
        assert first_name_male in PtPtProvider.first_names_male

    def test_female_first_name(self):
        first_name_female = self.fake.first_name_female()
        assert first_name_female in PtPtProvider.first_names_female

    def test_last_name(self):
        last_name = self.fake.last_name()
        assert last_name in PtPtProvider.last_names


class TestRuRU(unittest.TestCase):
    """Tests person in the ru_RU locale"""

    def setUp(self):
        self.fake = Faker("ru_RU")
        Faker.seed(0)

    def test_translit(self):
        assert translit("Александр Сергеевич Пушкин") == "Aleksandr Sergeevich Pushkin"
        assert translit("Анна Андреевна Ахматова") == "Anna Andreevna Akhmatova"
        assert translit("Михаил") == "Mikhail"
        assert translit("Фёдор") == "Fedor"
        assert translit("Екатерина") == "Yekaterina"
        assert translit("Анастасия") == "Anastasiya"
        assert translit("Юрьевич") == "Yurevich"
        assert translit("Никитична") == "Nikitichna"
        assert translit("Щербакова") == "Shcherbakova"
        assert translit("Маяковский") == "Mayakovskiy"
        assert translit("Петров-Водкин") == "Petrov-Vodkin"
        assert translit("Воронцова-Дашкова") == "Vorontsova-Dashkova"
        assert translit("А.С.Пушкин") == "A.S.Pushkin"
        assert translit("А. С. Пушкин") == "A. S. Pushkin"
        assert translit("тов. И.И.Сидоров") == "tov. I.I.Sidorov"
        assert translit("г-н А.Б.Петров") == "g-n A.B.Petrov"
        assert translit("г-жа Ю.М.Петрова") == "g-zha Yu.M.Petrova"

    def test_name_female(self):
        first_name = self.fake.first_name_female()
        assert first_name in RuProvider.first_names_female
        middle_name = self.fake.middle_name_female()
        assert middle_name in RuProvider.middle_names_female
        last_name = self.fake.last_name_female()
        assert last_name in RuProvider.last_names_female

    def test_name_male(self):
        first_name = self.fake.first_name_male()
        assert first_name in RuProvider.first_names_male
        middle_name = self.fake.middle_name_male()
        assert middle_name in RuProvider.middle_names_male
        last_name = self.fake.last_name_male()
        assert last_name in RuProvider.last_names_male

    def test_language_name(self):
        language_name = self.fake.language_name()
        assert language_name in RuProvider.language_names

    def test_passport_owner(self):
        surname, given_name = self.fake.passport_owner()
        assert surname in RuProvider.last_names
        assert given_name in RuProvider.first_names


class TestSvSE(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("sv_SE")
        Faker.seed(0)

    def test_gender_first_names(self):
        """simple test to verify that we are pulling gender specific names"""
        name = self.fake.first_name_female()
        assert name in SvSEProvider.first_names_female
        name = self.fake.first_name_male()
        assert name in SvSEProvider.first_names_male
        name = self.fake.first_name()
        assert name in SvSEProvider.first_names


class TestSkSK(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("sk_SK")
        Faker.seed(0)

    def test_name_male(self):
        male_name = self.fake.name_male()
        name_parts = male_name.split(" ")
        first_name, last_name = "", ""
        if len(name_parts) == 2:
            first_name = name_parts[0]
            last_name = name_parts[1]
        elif len(name_parts) == 4:
            first_name = name_parts[1]
            last_name = name_parts[2]
        elif len(name_parts) == 3:
            if name_parts[-1] in SkSKProvider.suffixes:
                first_name = name_parts[0]
                last_name = name_parts[1]
            else:
                first_name = name_parts[1]
                last_name = name_parts[2]
        assert first_name in SkSKProvider.first_names_male
        assert last_name in SkSKProvider.last_names_male

    def test_name_female(self):
        female_name = self.fake.name_female()
        name_parts = female_name.split(" ")
        first_name, last_name = "", ""
        if len(name_parts) == 2:
            first_name = name_parts[0]
            last_name = name_parts[1]
        elif len(name_parts) == 4:
            first_name = name_parts[1]
            last_name = name_parts[2]
        elif len(name_parts) == 3:
            if name_parts[-1] in SkSKProvider.suffixes:
                first_name = name_parts[0]
                last_name = name_parts[1]
            else:
                first_name = name_parts[1]
                last_name = name_parts[2]
        assert first_name in SkSKProvider.first_names_female
        assert last_name in SkSKProvider.last_names_female


class TestSw(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("sw")
        Faker.seed(0)

    def test_last_name(self):
        """
        Test the generation of Swahili last names.
        """
        # There's no gender-specific last name in Swahili.
        self.assertTrue(hasattr(SwProvider, "last_names_male"))
        self.assertTrue(hasattr(SwProvider, "last_names_female"))

        # All last names apply to all genders.
        self.assertTrue(hasattr(SwProvider, "last_names"))

        # General last name.
        name = self.fake.last_name()
        self.assertIsInstance(name, str)
        self.assertIn(name, SwProvider.last_names)

        # Females last name.
        name = self.fake.last_name_female()
        self.assertIsInstance(name, str)
        self.assertIn(name, SwProvider.last_names)

        # Male last name.
        name = self.fake.last_name_male()
        self.assertIsInstance(name, str)
        self.assertIn(name, SwProvider.last_names)

    def test_first_name(self):
        """
        Test the generation of Swahili first names.
        """
        # General first name.
        name = self.fake.first_name()
        self.assertIsInstance(name, str)
        self.assertIn(name, SwProvider.first_names)

        # Female first name.
        name = self.fake.first_name_female()
        self.assertIsInstance(name, str)
        self.assertIn(name, SwProvider.first_names)
        self.assertIn(name, SwProvider.first_names_female)

        # Male first name.
        name = self.fake.first_name_male()
        self.assertIsInstance(name, str)
        self.assertIn(name, SwProvider.first_names)
        self.assertIn(name, SwProvider.first_names_male)

    def test_full_name(self):
        """
        Test the generation of full Swahili names.
        """
        # Full name.
        name = self.fake.name()
        self.assertIsInstance(name, str)

        full_name_parts = name.split()

        if len(full_name_parts) == 2:
            first_name = full_name_parts[0]
            last_name = full_name_parts[1]
            self.assertIn(first_name, SwProvider.first_names)
            self.assertIn(last_name, SwProvider.last_names)
        elif len(full_name_parts) == 3:
            prefix = full_name_parts[0]
            first_name = full_name_parts[1]
            last_name = full_name_parts[2]

            self.assertIn(prefix, SwProvider.prefixes_female + SwProvider.prefixes_male)
            self.assertIn(first_name, SwProvider.first_names)
            self.assertIn(last_name, SwProvider.last_names)
        else:
            raise AssertionError("Invalid number of name parts. Expected 2 or 3.")


class TestTaIN(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("ta_IN")
        Faker.seed(0)

    def test_gender_first_names(self):
        """simple test to verify that we are pulling gender specific names"""
        name = self.fake.first_name_female()
        assert name in TaINProvider.first_names_female
        name = self.fake.first_name_male()
        assert name in TaINProvider.first_names_male
        name = self.fake.first_name()
        assert name in TaINProvider.first_names


class TestThTh(unittest.TestCase):
    """Tests person in the th_TH locale"""

    def setUp(self):
        self.fake = Faker("th_TH")
        Faker.seed(0)

    def test_first_name(self):
        # General first name
        name = self.fake.first_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in ThThProvider.first_names

    def test_last_name(self):
        # There's no gender-specific last name in Thai.
        assert not hasattr(ThThProvider, "last_names_male")
        assert not hasattr(ThThProvider, "last_names_female")
        # All last names apply for all genders.
        assert hasattr(ThThProvider, "last_names")

        # General last name.
        name = self.fake.last_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in ThThProvider.last_names

    def test_name(self):
        # Full name
        name = self.fake.name()
        assert name
        self.assertIsInstance(name, str)


class TestUkUa(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("uk_UA")
        Faker.seed(0)
        self.provider = UkUAProvider
        self.translit = UkUATranslit

    def test_male_first_names(self):
        for _ in range(100):
            res = self.fake.first_name_male()
            assert res in self.provider.first_names_male

    def test_female_first_names(self):
        for _ in range(100):
            res = self.fake.first_name_female()
            assert res in self.provider.first_names_female

    def test_male_last_names(self):
        for _ in range(100):
            res = self.fake.last_name_male()
            assert res in self.provider.last_names_male

    def test_female_last_names(self):
        for _ in range(100):
            res = self.fake.last_name_female()
            assert res in self.provider.last_names_female

    def test_middle_names(self):
        for _ in range(100):
            res = self.fake.middle_name()
            assert res in self.provider.middle_names

    def test_male_middle_names(self):
        for _ in range(100):
            res = self.fake.middle_name_male()
            assert res in self.provider.middle_names_male

    def test_female_middle_names(self):
        for _ in range(100):
            res = self.fake.middle_name_female()
            assert res in self.provider.middle_names_female

    def test_language_name(self):
        for _ in range(100):
            language_name = self.fake.language_name()
            assert language_name in self.provider.language_names

    def test_transliteration(self):
        assert self.translit("Сергій") == "Serhii"
        assert self.translit("Лілія") == "Liliia"
        assert self.translit("Яся") == "Yasia"
        assert self.translit("Демʼян") == "Demian"
        assert self.translit("Марʼяна") == "Mariana"
        assert (
            self.translit("абвгґдеєжзиіїйклмнопрстуфхцчшщьюяєʼ'-") == "abvhgdeiezhzyiiiklmnoprstufkhtschshshchiuiaie'-"
        )
        assert self.translit("АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ") == "ABVHGDEYeZhZYIYiYKLMNOPRSTUFKhTsChShShchYuYa"

    def test_full_name_male(self):
        for _ in range(10):
            res = self.fake.full_name(gender="M")
            last_name, first_name, middle_name = res.split(" ")
            assert last_name in self.provider.last_names_male
            assert first_name in self.provider.first_names_male
            assert middle_name in self.provider.middle_names_male

    def test_full_name_female(self):
        for _ in range(1000):
            res = self.fake.full_name(gender="F")
            last_name, first_name, middle_name = res.split(" ")
            assert last_name in self.provider.last_names_female
            assert first_name in self.provider.first_names_female
            assert middle_name in self.provider.middle_names_female

    def test_full_name(self):
        for _ in range(10):
            res = self.fake.full_name()
            last_name, first_name, middle_name = res.split(" ")
            assert last_name in self.provider.last_names
            assert first_name in self.provider.first_names
            assert middle_name in self.provider.middle_names

    def test_short_full_name(self):
        res = self.fake.full_name(short=True)
        assert res.count(".") == 2
        assert res.count(" ") == 1


class TestViVn(unittest.TestCase):
    """Test vi_VN person provider methods"""

    def setUp(self):
        self.fake = Faker("vi_VN")
        Faker.seed(0)

    def test_first_names(self):
        """simple test to verify that we are pulling gender specific names"""
        name = self.fake.first_name_female()
        assert name in ViVNProvider.first_names_female

        name = self.fake.first_name_male()
        assert name in ViVNProvider.first_names_male

        name = self.fake.first_name_unisex()
        assert name in ViVNProvider.first_names_unisex

        name = self.fake.first_name()
        assert name in ViVNProvider.first_names

    def test_middle_names(self):
        """test the middle name"""
        name = self.fake.middle_name()
        assert name in ViVNProvider.middle_names

    def test_last_names(self):
        """test the last name is generating from the provided tuple"""
        last_name = self.fake.last_name()
        assert last_name in ViVNProvider.last_names


class TestYoNG(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("yo_NG")
        Faker.seed(0)

    def test_last_name(self):
        """
        Test the generation of Zulu last names.
        """
        # There's no gender-specific last name in Zulu.
        self.assertTrue(hasattr(YoNGProvider, "last_names_male"))
        self.assertTrue(hasattr(YoNGProvider, "last_names_female"))

        # All last names apply to all genders.
        self.assertTrue(hasattr(YoNGProvider, "last_names"))

        # General last name.
        name = self.fake.last_name()
        self.assertIsInstance(name, str)
        self.assertIn(name, YoNGProvider.last_names)

        # Females last name.
        name = self.fake.last_name_female()
        self.assertIsInstance(name, str)
        self.assertIn(name, YoNGProvider.last_names)

        # Male last name.
        name = self.fake.last_name_male()
        self.assertIsInstance(name, str)
        self.assertIn(name, YoNGProvider.last_names)

    def test_first_name(self):
        """
        Test the generation of Zulu first names.
        """
        # General first name.
        name = self.fake.first_name()
        self.assertIsInstance(name, str)
        self.assertIn(name, YoNGProvider.first_names)

        # Female first name.
        name = self.fake.first_name_female()
        self.assertIsInstance(name, str)
        self.assertIn(name, YoNGProvider.first_names)
        self.assertIn(name, YoNGProvider.first_names_female)

        # Male first name.
        name = self.fake.first_name_male()
        self.assertIsInstance(name, str)
        self.assertIn(name, YoNGProvider.first_names)
        self.assertIn(name, YoNGProvider.first_names_male)

    def test_full_name(self):
        """
        Test the generation of full Zulu names.
        """
        # Full name.
        name = self.fake.name()
        self.assertIsInstance(name, str)

        full_name_parts = name.split()

        if len(full_name_parts) == 2:
            first_name = full_name_parts[0]
            last_name = full_name_parts[1]
            self.assertIn(first_name, YoNGProvider.first_names)
            self.assertIn(last_name, YoNGProvider.last_names)
        elif len(full_name_parts) == 3:
            prefix = full_name_parts[0]
            first_name = full_name_parts[1]
            last_name = full_name_parts[2]

            self.assertIn(prefix, YoNGProvider.prefixes_female + YoNGProvider.prefixes_male)
            self.assertIn(first_name, YoNGProvider.first_names)
            self.assertIn(last_name, YoNGProvider.last_names)
        else:
            raise AssertionError("Invalid number of name parts. Expected 2 or 3.")


class TestZhCN(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("zh_CN")
        Faker.seed(0)

    def test_last_name(self):
        # There's no gender-specific last name in Chinese.
        assert not hasattr(ZhCNProvider, "last_names_male")
        assert not hasattr(ZhCNProvider, "last_names_female")
        assert not hasattr(ZhCNProvider, "last_romanized_names_male")
        assert not hasattr(ZhCNProvider, "last_romanized_names_female")
        # All last names apply for all genders.
        assert hasattr(ZhCNProvider, "last_names")

        # General last name.
        name = self.fake.last_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in ZhCNProvider.last_names

        # Females last name.
        name = self.fake.last_name_female()
        assert name
        self.assertIsInstance(name, str)
        assert name in ZhCNProvider.last_names

        # Male last name.
        name = self.fake.last_name_male()
        assert name
        self.assertIsInstance(name, str)
        assert name in ZhCNProvider.last_names

        # General last romanized name
        name = self.fake.last_romanized_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in ZhCNProvider.last_romanized_names

    def test_first_name(self):
        # General first name
        name = self.fake.first_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in ZhCNProvider.first_names

        # Females first name
        name = self.fake.first_name_female()
        assert name
        self.assertIsInstance(name, str)
        assert name in ZhCNProvider.first_names
        assert name in ZhCNProvider.first_names_female

        # Male first name
        name = self.fake.first_name_male()
        assert name
        self.assertIsInstance(name, str)
        assert name in ZhCNProvider.first_names
        assert name in ZhCNProvider.first_names_male

        # General first romanized name
        name = self.fake.first_romanized_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in ZhCNProvider.first_romanized_names

    def test_name(self):
        # Full name
        name = self.fake.name()
        assert name
        self.assertIsInstance(name, str)
        assert name[0] in ZhCNProvider.last_names or name[:2] in ZhCNProvider.last_names
        assert name[1:] in ZhCNProvider.first_names or name[2:] in ZhCNProvider.first_names

        # Full romanized name
        name = self.fake.romanized_name()
        assert name
        self.assertIsInstance(name, str)
        first_romanized_name, last_romanized_name = name.split(" ")
        assert first_romanized_name in ZhCNProvider.first_romanized_names
        assert last_romanized_name in ZhCNProvider.last_romanized_names


class TestZhTW(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("zh_TW")
        Faker.seed(0)

    def test_last_name(self):
        # There's no gender-specific last name in Chinese.
        assert not hasattr(ZhTWProvider, "last_names_male")
        assert not hasattr(ZhTWProvider, "last_names_female")
        assert not hasattr(ZhTWProvider, "last_romanized_names_male")
        assert not hasattr(ZhTWProvider, "last_romanized_names_female")
        # All last names apply for all genders.
        assert hasattr(ZhTWProvider, "last_names")

        # General last name.
        name = self.fake.last_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in ZhTWProvider.last_names

        # Females last name.
        name = self.fake.last_name_female()
        assert name
        self.assertIsInstance(name, str)
        assert name in ZhTWProvider.last_names

        # Male last name.
        name = self.fake.last_name_male()
        assert name
        self.assertIsInstance(name, str)
        assert name in ZhTWProvider.last_names

        # General last romanized name
        name = self.fake.last_romanized_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in ZhTWProvider.last_romanized_names

    def test_first_name(self):
        # General first name
        name = self.fake.first_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in ZhTWProvider.first_names

        # Females first name
        name = self.fake.first_name_female()
        assert name
        self.assertIsInstance(name, str)
        assert name in ZhTWProvider.first_names
        assert name in ZhTWProvider.first_names_female

        # Male first name
        name = self.fake.first_name_male()
        assert name
        self.assertIsInstance(name, str)
        assert name in ZhTWProvider.first_names
        assert name in ZhTWProvider.first_names_male

        # General first romanized name
        name = self.fake.first_romanized_name()
        assert name
        self.assertIsInstance(name, str)
        assert name in ZhTWProvider.first_romanized_names

    def test_name(self):
        # Full name
        name = self.fake.name()
        assert name
        self.assertIsInstance(name, str)
        assert name[0] in ZhTWProvider.last_names or name[:2] in ZhTWProvider.last_names
        assert name[1:] in ZhTWProvider.first_names or name[2:] in ZhTWProvider.first_names

        # Full romanized name
        name = self.fake.romanized_name()
        assert name
        self.assertIsInstance(name, str)
        first_romanized_name, last_romanized_name = name.split(" ")
        assert first_romanized_name in ZhTWProvider.first_romanized_names
        assert last_romanized_name in ZhTWProvider.last_romanized_names


class TestZuZa(unittest.TestCase):
    def setUp(self):
        self.fake = Faker("zu_ZA")
        Faker.seed(0)

    def test_last_name(self):
        """
        Test the generation of Zulu last names.
        """
        # There's no gender-specific last name in Zulu.
        self.assertTrue(hasattr(ZuZAProvider, "last_names_male"))
        self.assertTrue(hasattr(ZuZAProvider, "last_names_female"))

        # All last names apply to all genders.
        self.assertTrue(hasattr(ZuZAProvider, "last_names"))

        # General last name.
        name = self.fake.last_name()
        self.assertIsInstance(name, str)
        self.assertIn(name, ZuZAProvider.last_names)

        # Females last name.
        name = self.fake.last_name_female()
        self.assertIsInstance(name, str)
        self.assertIn(name, ZuZAProvider.last_names)

        # Male last name.
        name = self.fake.last_name_male()
        self.assertIsInstance(name, str)
        self.assertIn(name, ZuZAProvider.last_names)

    def test_first_name(self):
        """
        Test the generation of Zulu first names.
        """
        # General first name.
        name = self.fake.first_name()
        self.assertIsInstance(name, str)
        self.assertIn(name, ZuZAProvider.first_names)

        # Female first name.
        name = self.fake.first_name_female()
        self.assertIsInstance(name, str)
        self.assertIn(name, ZuZAProvider.first_names)
        self.assertIn(name, ZuZAProvider.first_names_female)

        # Male first name.
        name = self.fake.first_name_male()
        self.assertIsInstance(name, str)
        self.assertIn(name, ZuZAProvider.first_names)
        self.assertIn(name, ZuZAProvider.first_names_male)

    def test_full_name(self):
        """
        Test the generation of full Zulu names.
        """
        # Full name.
        name = self.fake.name()
        self.assertIsInstance(name, str)

        full_name_parts = name.split()

        if len(full_name_parts) == 2:
            first_name = full_name_parts[0]
            last_name = full_name_parts[1]
            self.assertIn(first_name, ZuZAProvider.first_names)
            self.assertIn(last_name, ZuZAProvider.last_names)
        elif len(full_name_parts) == 3:
            prefix = full_name_parts[0]
            first_name = full_name_parts[1]
            last_name = full_name_parts[2]

            self.assertIn(prefix, ZuZAProvider.prefixes_female + ZuZAProvider.prefixes_male)
            self.assertIn(first_name, ZuZAProvider.first_names)
            self.assertIn(last_name, ZuZAProvider.last_names)
        else:
            raise AssertionError("Invalid number of name parts. Expected 2 or 3.")


if __name__ == "__main__":
    unittest.main()
