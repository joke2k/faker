import re

from ipaddress import ip_address, ip_network
from itertools import cycle
from unittest.mock import PropertyMock, patch

import pytest

from validators import domain as validate_domain
from validators import email as validate_email

from faker.providers.internet import Provider as InternetProvider
from faker.providers.internet.en_GB import Provider as EnGbInternetProvider
from faker.providers.internet.es_ES import Provider as EsEsInternetProvider
from faker.providers.internet.pl_PL import Provider as PlPlInternetProvider
from faker.providers.internet.ro_RO import Provider as RoRoInternetProvider
from faker.providers.internet.th_TH import Provider as ThThInternetProvider
from faker.providers.internet.zh_CN import Provider as ZhCnInternetProvider
from faker.providers.person.ja_JP import Provider as JaPersonProvider
from faker.utils import text


class TestInternetProvider:
    """Test internet provider methods"""
    num_samples = 100
    ipv4_pattern = re.compile(
        r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}'
        r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
    )
    ipv4_network_pattern = re.compile(
        r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}'
        r'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
        r'/(?:\d|[12]\d|3[0-2])$',
    )

    def test_email(self, faker, num_samples):
        for _ in range(num_samples):
            email = faker.email()
            assert '@' in email

    def test_email_with_domain(self, faker):
        domain = 'example.com'
        email = faker.email(domain=domain)
        assert email.split('@')[1] == domain

    def test_safe_email(self, faker, num_samples):
        expected_domains = ['example.com', 'example.org', 'example.net']
        for _ in range(num_samples):
            email = faker.safe_email()
            assert email.split('@')[1] in expected_domains

    def test_safe_domain_names(self, faker, num_samples):
        expected_domains = ['example.com', 'example.org', 'example.net']
        for _ in range(num_samples):
            safe_domain_name = faker.safe_domain_name()
            assert safe_domain_name in expected_domains

    @patch(
        'faker.providers.internet.Provider.image_placeholder_services',
        {'https://dummyimage.com/{width}x{height}'},
    )
    def test_image_url(self, faker):
        my_width = 500
        my_height = 1024
        url = faker.image_url(my_width, my_height)
        assert f'https://dummyimage.com/{my_width}x{my_height}' == url
        url = faker.image_url()
        assert 'https://dummyimage.com/' in url

    def test_hostname(self, faker):
        hostname_1_level = faker.hostname(levels=1)
        hostname_parts = hostname_1_level.split('.')
        assert hostname_1_level and isinstance(hostname_1_level, str)
        assert len(hostname_parts) == 3

        hostname_0_level = faker.hostname(levels=0)
        assert hostname_0_level and isinstance(hostname_0_level, str)

    def test_ipv4(self, faker, num_samples):
        for _ in range(num_samples):
            address = faker.ipv4()
            assert 7 <= len(address) <= 15
            assert self.ipv4_pattern.fullmatch(address)

        for _ in range(num_samples):
            address = faker.ipv4(network=True)
            assert 9 <= len(address) <= 18
            assert self.ipv4_network_pattern.fullmatch(address)

        for _ in range(num_samples):
            address = faker.ipv4(private=True)
            assert 7 <= len(address) <= 15
            assert self.ipv4_pattern.fullmatch(address)
            assert ip_address(address).is_private

        for _ in range(num_samples):
            address = faker.ipv4(private=False)
            assert 7 <= len(address) <= 15
            assert self.ipv4_pattern.fullmatch(address)
            assert not ip_address(address).is_private

    def test_ipv4_caching(self, faker):
        from faker.providers.internet import _IPv4Constants

        # The extra [None] here is to test code path involving whole IPv4 pool
        for address_class in list(_IPv4Constants._network_classes.keys()) + [None]:
            if address_class is None:
                networks_attr = '_cached_all_networks'
            else:
                networks_attr = f'_cached_all_class_{address_class}_networks'
            weights_attr = f'{networks_attr}_weights'
            provider = InternetProvider(faker)

            # First, test cache creation
            assert not hasattr(provider, networks_attr)
            assert not hasattr(provider, weights_attr)
            provider.ipv4(address_class=address_class)
            assert hasattr(provider, networks_attr)
            assert hasattr(provider, weights_attr)

            # Then, test cache access on subsequent calls
            with patch.object(InternetProvider, networks_attr, create=True,
                              new_callable=PropertyMock) as mock_networks_cache:
                with patch.object(InternetProvider, weights_attr, create=True,
                                  new_callable=PropertyMock) as mock_weights_cache:
                    # Keep test fast by patching the cache attributes to return something simple
                    mock_networks_cache.return_value = [ip_network('10.0.0.0/24')]
                    mock_weights_cache.return_value = [10]
                    for _ in range(100):
                        provider.ipv4(address_class=address_class)

                    # Python's hasattr() internally calls getattr()
                    # So each call to ipv4() accesses the cache attributes twice
                    assert mock_networks_cache.call_count == 200
                    assert mock_weights_cache.call_count == 200

    def test_ipv4_network_class(self, faker, num_samples):
        for _ in range(num_samples):
            klass = faker.ipv4_network_class()
            assert klass in 'abc'

    def test_ipv4_private(self, faker, num_samples):
        for _ in range(num_samples):
            address = faker.ipv4_private()
            assert 7 <= len(address) <= 15
            assert self.ipv4_pattern.fullmatch(address)
            assert ip_address(address).is_private

        for _ in range(num_samples):
            address = faker.ipv4_private(network=True)
            assert 9 <= len(address) <= 18
            assert self.ipv4_network_pattern.fullmatch(address)
            assert ip_network(address)[0].is_private

    def test_ipv4_private_class(self, faker, num_samples):
        from faker.providers.internet import _IPv4Constants
        for clas in 'abc':
            class_network = _IPv4Constants._network_classes[clas]
            class_min = class_network.network_address
            class_max = class_network.broadcast_address

            for _ in range(num_samples):
                address = faker.ipv4_private(address_class=clas)
                assert 7 <= len(address) <= 15
                assert self.ipv4_pattern.fullmatch(address)
                assert ip_address(address).is_private
                assert class_min <= ip_address(address) <= class_max

    def test_ipv4_public_caching(self, faker):
        from faker.providers.internet import _IPv4Constants

        for address_class in _IPv4Constants._network_classes.keys():
            networks_attr = f'_cached_public_class_{address_class}_networks'
            weights_attr = f'{networks_attr}_weights'
            provider = InternetProvider(faker)

            # First, test cache creation
            assert not hasattr(provider, networks_attr)
            assert not hasattr(provider, weights_attr)
            provider.ipv4_public(address_class=address_class)
            assert hasattr(provider, networks_attr)
            assert hasattr(provider, weights_attr)

            # Then, test cache access on subsequent calls
            with patch.object(InternetProvider, networks_attr, create=True,
                              new_callable=PropertyMock) as mock_networks_cache:
                with patch.object(InternetProvider, weights_attr, create=True,
                                  new_callable=PropertyMock) as mock_weights_cache:
                    # Keep test fast by patching the cache attributes to return something simple
                    mock_networks_cache.return_value = [ip_network('10.0.0.0/24')]
                    mock_weights_cache.return_value = [10]
                    for _ in range(100):
                        provider.ipv4_public(address_class=address_class)

                    # Python's hasattr() internally calls getattr()
                    # So each call to ipv4_public() accesses the cache attributes twice
                    assert mock_networks_cache.call_count == 200
                    assert mock_weights_cache.call_count == 200

    def test_ipv4_public(self, faker, num_samples):
        for _ in range(num_samples):
            address = faker.ipv4_public()
            assert 7 <= len(address) <= 15
            assert self.ipv4_pattern.fullmatch(address)
            assert not ip_address(address).is_private

        for _ in range(num_samples):
            address = faker.ipv4_public(network=True)
            assert 9 <= len(address) <= 18
            assert self.ipv4_network_pattern.fullmatch(address)
            # Hack around ipaddress module
            # As 192.0.0.0 is net addr of many 192.0.0.0/* nets
            # ipaddress considers them as private
            if ip_network(address).network_address != ip_address('192.0.0.0'):
                assert not ip_network(address)[0].is_private

    def test_ipv4_public_class(self, faker, num_samples):
        from faker.providers.internet import _IPv4Constants
        for clas in 'abc':
            class_network = _IPv4Constants._network_classes[clas]
            class_min = class_network.network_address
            class_max = class_network.broadcast_address

            for _ in range(num_samples):
                address = faker.ipv4_public(address_class=clas)
                assert 7 <= len(address) <= 15
                assert not ip_address(address).is_private
                assert class_min <= ip_address(address) <= class_max
                assert self.ipv4_pattern.fullmatch(address)

    def test_ipv4_distribution_selection(self):
        from faker.generator import Generator, random
        from faker.utils.distribution import choices_distribution
        provider = InternetProvider(Generator())

        subnets = [ip_network('10.0.0.0/8'), ip_network('11.0.0.0/8')]
        valid_weights = [1, 1]
        list_of_invalid_weights = [
            [1, 2, 3],   # List size does not match subnet list size
            ['a', 'b'],  # List size matches, but elements are invalid
            11,        # Not a list or valid iterable
        ]

        with patch('faker.providers.internet.choices_distribution',
                   wraps=choices_distribution) as mock_choices_fn:
            with patch('faker.generator.random.choice',
                       wraps=random.choice) as mock_random_choice:
                # If weights argument is valid, only `choices_distribution` should be called
                provider._random_ipv4_address_from_subnets(subnets, valid_weights)
                assert mock_choices_fn.call_count == 1
                assert mock_random_choice.call_count == 0

                # If weights argument is invalid, calls to `choices_distribution` will fail
                # and calls to `random.choice` will be made as failover behavior
                for invalid_weights in list_of_invalid_weights:
                    # Reset mock objects for each iteration
                    mock_random_choice.reset_mock()
                    mock_choices_fn.reset_mock()

                    provider._random_ipv4_address_from_subnets(subnets, invalid_weights)
                    assert mock_choices_fn.call_count == 1
                    assert mock_random_choice.call_count == 1

    def test_ipv6(self, faker, num_samples):
        provider = InternetProvider(faker)

        for _ in range(num_samples):
            address = provider.ipv6()
            assert len(address) >= 3  # ::1
            assert len(address) <= 39
            assert (
                re.compile(r'^([0-9a-f]{0,4}:){2,7}[0-9a-f]{1,4}$').search(address))

        for _ in range(num_samples):
            address = provider.ipv6(network=True)
            assert len(address) >= 4  # ::/8
            assert len(address) <= 39 + 4
            assert (
                re.compile(r'^([0-9a-f]{0,4}:){2,7}[0-9a-f]{0,4}/\d{1,3}$').search(
                    address))

    def test_port_number(self, faker, num_samples):
        for _ in range(num_samples):
            assert 0 <= faker.port_number() <= 65535
            assert 0 <= faker.port_number(is_system=True) <= 1023
            assert 1024 <= faker.port_number(is_user=True) <= 49151
            assert 49152 <= faker.port_number(is_dynamic=True) <= 65535

    def test_http_method(self, faker, num_samples):
        expected_methods = [
            'CONNECT', 'DELETE', 'GET', 'HEAD', 'OPTIONS', 'PATCH', 'POST',
            'PUT', 'TRACE',
        ]

        got_methods = set()
        for _ in range(num_samples):
            got_methods.add(faker.http_method())

        assert expected_methods == sorted(got_methods)

    def test_dga(self, faker):
        assert faker.dga() != faker.dga()

        expected_domain = 'cqphixmpdfpptskr.com'
        assert faker.dga(day=1, month=1, year=1000, tld='com', length=16) == expected_domain

    def test_iana_id(self, faker, num_samples):
        for _ in range(num_samples):
            assert 1 <= int(faker.iana_id()) <= 8888888


class TestInternetProviderUrl:
    """ Test internet url generation """

    @staticmethod
    def is_correct_scheme(url, schemes):
        return any(url.startswith(f'{scheme}://') for scheme in schemes)

    def test_url_default_schemes(self, faker):
        for _ in range(100):
            url = faker.url()
            assert self.is_correct_scheme(url, ['http', 'https'])

    def test_url_custom_schemes(self, faker):
        schemes_sets = [
            ['usb'],
            ['ftp', 'file'],
            ['usb', 'telnet', 'http'],
        ]
        for _, schemes in zip(range(100), cycle(schemes_sets)):
            url = faker.url(schemes=schemes)
            assert self.is_correct_scheme(url, schemes)

    def test_url_empty_schemes_list_generate_schemeless_urls(self, faker):
        for _ in range(100):
            url = faker.url(schemes=[])
            assert not url.startswith('http')
            assert url.startswith('://')


class TestJaJp:
    """Test ja_JP internet provider methods"""

    def test_internet(self, faker):
        names = JaPersonProvider.last_romanized_names

        domain_word = faker.domain_word()
        assert isinstance(domain_word, str)
        assert any(domain_word == text.slugify(name) for name in names)

        domain_name = faker.domain_name()
        deep_domain_name = faker.domain_name(3)
        assert isinstance(domain_name, str)
        assert isinstance(deep_domain_name, str)
        assert deep_domain_name.count('.') == 3
        with pytest.raises(ValueError):
            faker.domain_name(-1)

        user_name = faker.user_name()
        assert isinstance(user_name, str)

        tld = faker.tld()
        assert isinstance(tld, str)


class TestZhCn:
    """Test zh_CN internet provider methods"""

    def test_email(self, faker):
        email = faker.email()
        validate_email(email)

    def test_domain_word(self, faker):
        domain_word = faker.domain_word()
        assert len(domain_word) > 1

    @patch(
        'faker.providers.internet.Provider.tld',
        lambda x: 'cn',
    )
    def test_domain_name(self, faker):
        domain_name_1_level = faker.domain_name(levels=1)
        domain_parts = domain_name_1_level.split(".")
        assert len(domain_parts) == 2
        assert domain_parts[-1] == 'cn'
        domain_name_2_level = faker.domain_name(levels=2)
        domain_parts = domain_name_2_level.split(".")
        assert len(domain_parts) == 3
        assert domain_parts[-1] == 'cn'
        assert domain_parts[1] in ['ac', 'com', 'edu', 'gov', 'mil',
                                   'net', 'org', 'ah', 'bj', 'cq',
                                   'fj', 'gd', 'gs', 'gz', 'gx', 'ha',
                                   'hb', 'he', 'hi', 'hk', 'hl', 'hn',
                                   'jl', 'js', 'jx', 'ln', 'mo', 'nm',
                                   'nx', 'qh', 'sc', 'sd', 'sh', 'sn',
                                   'sx', 'tj', 'xj', 'xz', 'yn', 'zj']

    def test_domain_name_one_level_after_tld(self, faker):
        provider = ZhCnInternetProvider(faker)
        for _ in range(100):
            domain_name = faker.domain_name(levels=1)
            domain_parts = domain_name.split('.')
            assert len(domain_parts) == 2
            assert domain_parts[-1] in provider.tlds.keys()
            assert domain_parts[0] not in provider.second_level_domains

    @patch('faker.providers.internet.zh_CN.Provider.domain_word')
    @patch('faker.providers.internet.Provider.tld')
    def test_domain_name_two_levels_after_cn_tld(self, mock_tld, mock_domain_word, faker):
        provider = ZhCnInternetProvider(faker)

        # If tld() returns cn, second level name should be selected from second_level_domains
        # and domain_word() will only be called once which will be used for the third level
        mock_tld.return_value = 'cn'
        mock_domain_word.return_value = 'li'
        for _ in range(100):
            mock_domain_word.reset_mock()
            domain_name = faker.domain_name(levels=2)
            domain_parts = domain_name.split('.')
            assert len(domain_parts) == 3
            assert domain_parts[-1] == 'cn'
            assert domain_parts[-2] in provider.second_level_domains
            assert domain_parts[0] == 'li'
            assert mock_domain_word.call_count == 1

    @patch('faker.providers.internet.zh_CN.Provider.domain_word')
    @patch('faker.providers.internet.Provider.tld')
    def test_domain_name_two_levels_after_non_cn_tld(self, mock_tld, mock_domain_word, faker):
        # If tld() does not return cn, domain_word() will be called twice
        mock_domain_word.reset_mock()
        mock_tld.return_value = 'net'
        mock_domain_word.return_value = 'li'
        domain_name = faker.domain_name(levels=2)
        assert domain_name == 'li.li.net'
        assert mock_domain_word.call_count == 2

    @patch('faker.providers.internet.zh_CN.Provider.domain_word')
    @patch('faker.providers.internet.Provider.tld')
    def test_domain_name_more_than_two_levels_after_cn_tld(self, mock_tld, mock_domain_word, faker):
        provider = ZhCnInternetProvider(faker)

        mock_tld.return_value = 'cn'
        mock_domain_word.return_value = 'li'
        for levels in range(3, 10):
            with patch('faker.providers.internet.zh_CN.Provider.domain_name',
                       wraps=faker.domain_name) as mock_domain_name:
                mock_tld.reset_mock()
                mock_domain_word.reset_mock()
                mock_domain_name.reset_mock()
                domain_name = faker.domain_name(levels=levels)
                domain_parts = domain_name.split('.')

                # Same assertions as levels=2 for tld and second level if tld is cn
                # But every level henceforth should return the mocked value
                assert domain_parts[-1] == 'cn'
                assert domain_parts[-2] in provider.second_level_domains
                assert all(domain_part == 'li' for domain_part in domain_parts[:-2])

                # tld() method should only be called once, domain_word() will be called for each
                # level after tld except the second, and recursive calls to domain_name() will be
                # made for each level starting from the third level after tld
                assert mock_tld.call_count == 1
                assert mock_domain_word.call_count == levels - 1
                assert mock_domain_name.call_count == levels - 2

    @patch('faker.providers.internet.zh_CN.Provider.domain_word')
    @patch('faker.providers.internet.Provider.tld')
    def test_domain_name_more_than_two_levels_after_non_cn_tld(self, mock_tld, mock_domain_word, faker):
        mock_tld.return_value = 'net'
        mock_domain_word.return_value = 'li'
        for levels in range(3, 10):
            with patch('faker.providers.internet.zh_CN.Provider.domain_name',
                       wraps=faker.domain_name) as mock_domain_name:
                mock_tld.reset_mock()
                mock_domain_word.reset_mock()
                mock_domain_name.reset_mock()
                domain_name = faker.domain_name(levels=levels)
                domain_parts = domain_name.split('.')

                # Same assertions as levels=2 for non cn tld and
                # every level henceforth should return the mocked value
                assert domain_parts[-1] == 'net'
                assert all(domain_part == 'li' for domain_part in domain_parts[:-1])

                # tld() method should only be called once, domain_word() will be called for each
                # level after tld, and recursive calls to domain_name() will be made for each
                # level starting from the third level after tld
                assert mock_tld.call_count == 1
                assert mock_domain_word.call_count == levels
                assert mock_domain_name.call_count == levels - 2

    def test_domain_name_bad_level(self, faker):
        with pytest.raises(ValueError):
            faker.domain_name(levels=0)


class TestZhTw:
    """Test zh_TW internet provider methods"""

    def test_email(self, faker):
        email = faker.email()
        validate_email(email)


class TestHuHu:
    """Test hu_HU internet provider methods"""

    def test_internet(self, faker):
        domain_name = faker.domain_name()
        assert isinstance(domain_name, str)
        tld = faker.tld()
        assert isinstance(tld, str)
        email = faker.email()
        assert isinstance(email, str)


class TestPlPl:
    """Test pl_PL internet provider methods"""

    def test_free_email_domain(self, faker):
        domain = faker.free_email_domain()
        assert domain in PlPlInternetProvider.free_email_domains

    def test_tld(self, faker):
        tld = faker.tld()
        assert tld in PlPlInternetProvider.tlds


class TestNlNl:
    """Test nl_NL internet provider methods"""

    @patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'fabiënné',
    )
    def test_ascii_safe_email(self, faker):
        email = faker.ascii_safe_email()
        validate_email(email)
        assert email.split('@')[0] == 'fabienne'

    @patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'fabiënné',
    )
    def test_ascii_free_email(self, faker):
        email = faker.ascii_free_email()
        validate_email(email)
        assert email.split('@')[0] == 'fabienne'

    @patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'fabiënné',
    )
    def test_ascii_company_email(self, faker):
        email = faker.ascii_company_email()
        validate_email(email)
        assert email.split('@')[0] == 'fabienne'


class TestArAa:
    """Test ar_AA internet provider methods"""

    @patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'اصيل',
    )
    def test_ascii_safe_email(self, faker):
        email = faker.ascii_safe_email()
        validate_email(email)
        assert email.split('@')[0] == 'asyl'

    @patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'اصيل',
    )
    def test_ascii_free_email(self, faker):
        email = faker.ascii_free_email()
        validate_email(email)
        assert email.split('@')[0] == 'asyl'

    @patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'اصيل',
    )
    def test_ascii_company_email(self, faker):
        email = faker.ascii_company_email()
        validate_email(email)
        assert email.split('@')[0] == 'asyl'


class TestPtBr:
    """Test pt_BR internet provider methods"""

    @patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'VitóriaMagalhães',
    )
    def test_ascii_safe_email(self, faker):
        email = faker.ascii_safe_email()
        validate_email(email)
        assert email.split('@')[0] == 'vitoriamagalhaes'

    @patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'JoãoSimões',
    )
    def test_ascii_free_email(self, faker):
        email = faker.ascii_free_email()
        validate_email(email)
        assert email.split('@')[0] == 'joaosimoes'

    @patch(
        'faker.providers.internet.Provider.user_name',
        lambda x: 'AndréCauã',
    )
    def test_ascii_company_email(self, faker):
        email = faker.ascii_company_email()
        validate_email(email)
        assert email.split('@')[0] == 'andrecaua'


class TestEnPh:
    """Test en_PH internet provider methods"""
    num_samples = 100

    def test_domain_name(self, faker, num_samples):
        for i in range(num_samples):
            domain = faker.domain_name()
            validate_domain(domain)


class TestFilPh(TestEnPh):
    """Test fil_PH internet provider methods"""
    pass


class TestTlPh(TestFilPh):
    """Test tl_PH internet provider methods"""
    pass


class TestEnGb:
    """Tests for the en_GB locale."""

    def test_free_email_domain(self, faker):
        domain = faker.free_email_domain()
        assert domain in EnGbInternetProvider.free_email_domains

    def test_tld(self, faker):
        tld = faker.tld()
        assert tld in EnGbInternetProvider.tlds


class TestEsEs:
    """Tests for the es_ES locale."""

    def test_tld(self, faker):
        tld = faker.tld()
        assert tld in EsEsInternetProvider.tlds


class TestRoRo:
    """Test ro_RO internet provider methods"""

    def test_free_email_domain(self, faker):
        domain = faker.free_email_domain()
        assert domain in RoRoInternetProvider.free_email_domains

    def test_tld(self, faker):
        tld = faker.tld()
        assert tld in PlPlInternetProvider.tlds


class TestThTh:
    """Test th_TH internet provider methods"""

    def test_tld(self, faker):
        tld = faker.tld()
        assert tld in ThThInternetProvider.tlds
