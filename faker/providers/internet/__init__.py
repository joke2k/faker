from ipaddress import IPV4LENGTH, IPV6LENGTH, ip_address, ip_network

from text_unidecode import unidecode

# from faker.generator import random
# from faker.providers.lorem.la import Provider as Lorem
from faker.utils.decorators import lowercase, slugify, slugify_unicode
from faker.utils.distribution import choices_distribution

from .. import BaseProvider

localized = True


class _IPv4Constants:
    """
    IPv4 network constants used to group networks into different categories.
    Structure derived from `ipaddress._IPv4Constants`.

    Excluded network list is updated to comply with current IANA list of
    private and reserved networks.
    """
    _network_classes = {
        'a': ip_network('0.0.0.0/1'),
        'b': ip_network('128.0.0.0/2'),
        'c': ip_network('192.0.0.0/3'),
    }

    # Three common private networks from class A, B and CIDR
    # to generate private addresses from.
    _private_networks = [
        ip_network('10.0.0.0/8'),
        ip_network('172.16.0.0/12'),
        ip_network('192.168.0.0/16'),
    ]

    # List of networks from which IP addresses will never be generated,
    # includes other private IANA and reserved networks from
    # ttps://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml
    _excluded_networks = [
        ip_network('0.0.0.0/8'),
        ip_network('100.64.0.0/10'),
        ip_network('127.0.0.0/8'),  # loopback network
        ip_network('169.254.0.0/16'),  # linklocal network
        ip_network('192.0.0.0/24'),
        ip_network('192.0.2.0/24'),
        ip_network('192.31.196.0/24'),
        ip_network('192.52.193.0/24'),
        ip_network('192.88.99.0/24'),
        ip_network('192.175.48.0/24'),
        ip_network('198.18.0.0/15'),
        ip_network('198.51.100.0/24'),
        ip_network('203.0.113.0/24'),
        ip_network('224.0.0.0/4'),  # multicast network
        ip_network('240.0.0.0/4'),
        ip_network('255.255.255.255/32'),
    ]


class Provider(BaseProvider):
    safe_domain_names = ('example.org', 'example.com', 'example.net')
    free_email_domains = ('gmail.com', 'yahoo.com', 'hotmail.com')
    tlds = (
        'com', 'com', 'com', 'com', 'com', 'com', 'biz', 'info', 'net', 'org',
    )
    hostname_prefixes = ('db', 'srv', 'desktop', 'laptop', 'lt', 'email', 'web')
    uri_pages = (
        'index', 'home', 'search', 'main', 'post', 'homepage', 'category',
        'register', 'login', 'faq', 'about', 'terms', 'privacy', 'author',
    )
    uri_paths = (
        'app', 'main', 'wp-content', 'search', 'category', 'tag', 'categories',
        'tags', 'blog', 'posts', 'list', 'explore',
    )
    uri_extensions = (
        '.html', '.html', '.html', '.htm', '.htm', '.php', '.php', '.jsp',
        '.asp',
    )
    http_methods = (
        'GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE',
        'PATCH',
    )

    user_name_formats = (
        '{{last_name}}.{{first_name}}',
        '{{first_name}}.{{last_name}}',
        '{{first_name}}##',
        '?{{last_name}}',
    )
    email_formats = (
        '{{user_name}}@{{domain_name}}',
        '{{user_name}}@{{free_email_domain}}',
    )
    url_formats = (
        'www.{{domain_name}}/',
        '{{domain_name}}/',
    )
    uri_formats = (
        '{{url}}',
        '{{url}}{{uri_page}}/',
        '{{url}}{{uri_page}}{{uri_extension}}',
        '{{url}}{{uri_path}}/{{uri_page}}/',
        '{{url}}{{uri_path}}/{{uri_page}}{{uri_extension}}',
    )
    image_placeholder_services = (
        'https://www.lorempixel.com/{width}/{height}',
        'https://dummyimage.com/{width}x{height}',
        'https://placekitten.com/{width}/{height}',
        'https://placeimg.com/{width}/{height}/any',
    )

    replacements = ()

    def _to_ascii(self, string):
        for search, replace in self.replacements:
            string = string.replace(search, replace)

        string = unidecode(string)
        return string

    @lowercase
    def email(self, domain=None):
        if domain:
            email = f'{self.user_name()}@{domain}'
        else:
            pattern = self.random_element(self.email_formats)
            email = "".join(self.generator.parse(pattern).split(" "))
        return email

    @lowercase
    def safe_domain_name(self):
        return self.random_element(self.safe_domain_names)

    @lowercase
    def safe_email(self):
        return self.user_name() + '@' + self.safe_domain_name()

    @lowercase
    def free_email(self):
        return self.user_name() + '@' + self.free_email_domain()

    @lowercase
    def company_email(self):
        return self.user_name() + '@' + self.domain_name()

    @lowercase
    def free_email_domain(self):
        return self.random_element(self.free_email_domains)

    @lowercase
    def ascii_email(self):
        pattern = self.random_element(self.email_formats)
        return self._to_ascii(
            "".join(self.generator.parse(pattern).split(" ")),
        )

    @lowercase
    def ascii_safe_email(self):
        return self._to_ascii(self.user_name() + '@' + self.safe_domain_name())

    @lowercase
    def ascii_free_email(self):
        return self._to_ascii(
            self.user_name() + '@' + self.free_email_domain(),
        )

    @lowercase
    def ascii_company_email(self):
        return self._to_ascii(
            self.user_name() + '@' + self.domain_name(),
        )

    @slugify_unicode
    def user_name(self):
        pattern = self.random_element(self.user_name_formats)
        username = self._to_ascii(
            self.bothify(self.generator.parse(pattern)).lower(),
        )
        return username

    @lowercase
    def hostname(self, levels=1):
        """
        Produce a hostname with specified number of subdomain levels.

        >>> hostname()
        db-01.nichols-phillips.com
        >>> hostname(0)
        laptop-56
        >>> hostname(2)
        web-12.williamson-hopkins.jackson.com
        """
        if levels < 1:
            return self.random_element(self.hostname_prefixes) + '-' + self.numerify('##')
        return self.random_element(self.hostname_prefixes) + '-' + self.numerify('##') + '.' + self.domain_name(levels)

    @lowercase
    def domain_name(self, levels=1):
        """
        Produce an Internet domain name with the specified number of
        subdomain levels.

        >>> domain_name()
        nichols-phillips.com
        >>> domain_name(2)
        williamson-hopkins.jackson.com
        """
        if levels < 1:
            raise ValueError("levels must be greater than or equal to 1")
        if levels == 1:
            return self.domain_word() + '.' + self.tld()
        else:
            return self.domain_word() + '.' + self.domain_name(levels - 1)

    @lowercase
    @slugify_unicode
    def domain_word(self):
        company = self.generator.format('company')
        company_elements = company.split(' ')
        company = self._to_ascii(company_elements.pop(0))
        return company

    def dga(self, year=None, month=None, day=None, tld=None, length=None):
        """Generates a domain name by given date
        https://en.wikipedia.org/wiki/Domain_generation_algorithm

        :type year: int
        :type month: int
        :type day: int
        :type tld: str
        :type length: int
        :rtype: str
        """

        domain = ''
        year = year or self.random_int(min=1, max=9999)
        month = month or self.random_int(min=1, max=12)
        day = day or self.random_int(min=1, max=30)
        tld = tld or self.tld()
        length = length or self.random_int(min=2, max=63)

        for _ in range(length):
            year = ((year ^ 8 * year) >> 11) ^ ((year & 0xFFFFFFF0) << 17)
            month = ((month ^ 4 * month) >> 25) ^ 16 * (month & 0xFFFFFFF8)
            day = ((day ^ (day << 13)) >> 19) ^ ((day & 0xFFFFFFFE) << 12)
            domain += chr(((year ^ month ^ day) % 25) + 97)

        return domain + '.' + tld

    def tld(self):
        return self.random_element(self.tlds)

    def http_method(self):
        """Returns random HTTP method
        https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

        :rtype: str
        """

        return self.random_element(self.http_methods)

    def url(self, schemes=None):
        """
        :param schemes: a list of strings to use as schemes, one will chosen randomly.
        If None, it will generate http and https urls.
        Passing an empty list will result in schemeless url generation like "://domain.com".

        :returns: a random url string.
        """
        if schemes is None:
            schemes = ['http', 'https']

        pattern = f'{self.random_element(schemes) if schemes else ""}://{self.random_element(self.url_formats)}'

        return self.generator.parse(pattern)

    def _get_all_networks_and_weights(self, address_class=None):
        """
        Produces a 2-tuple of valid IPv4 networks and corresponding relative weights

        :param address_class: IPv4 address class (a, b, or c)
        """
        # If `address_class` has an unexpected value, use the whole IPv4 pool
        if address_class in _IPv4Constants._network_classes.keys():
            networks_attr = f'_cached_all_class_{address_class}_networks'
            all_networks = [_IPv4Constants._network_classes[address_class]]
        else:
            networks_attr = '_cached_all_networks'
            all_networks = [ip_network('0.0.0.0/0')]

        # Return cached network and weight data if available
        weights_attr = f'{networks_attr}_weights'
        if hasattr(self, networks_attr) and hasattr(self, weights_attr):
            return getattr(self, networks_attr), getattr(self, weights_attr)

        # Otherwise, compute for list of networks (excluding special networks)
        all_networks = self._exclude_ipv4_networks(
            all_networks,
            _IPv4Constants._excluded_networks,
        )

        # Then compute for list of corresponding relative weights
        weights = [network.num_addresses for network in all_networks]

        # Then cache and return results
        setattr(self, networks_attr, all_networks)
        setattr(self, weights_attr, weights)
        return all_networks, weights

    def _get_private_networks_and_weights(self, address_class=None):
        """
        Produces an OrderedDict of valid private IPv4 networks and corresponding relative weights

        :param address_class: IPv4 address class (a, b, or c)
        """
        # If `address_class` has an unexpected value, choose a valid value at random
        if address_class not in _IPv4Constants._network_classes.keys():
            address_class = self.ipv4_network_class()

        # Return cached network and weight data if available for a specific address class
        networks_attr = f'_cached_private_class_{address_class}_networks'
        weights_attr = f'{networks_attr}_weights'
        if hasattr(self, networks_attr) and hasattr(self, weights_attr):
            return getattr(self, networks_attr), getattr(self, weights_attr)

        # Otherwise, compute for list of private networks (excluding special networks)
        supernet = _IPv4Constants._network_classes[address_class]
        private_networks = [
            subnet for subnet in _IPv4Constants._private_networks
            if subnet.overlaps(supernet)
        ]
        private_networks = self._exclude_ipv4_networks(
            private_networks,
            _IPv4Constants._excluded_networks,
        )

        # Then compute for list of corresponding relative weights
        weights = [network.num_addresses for network in private_networks]

        # Then cache and return results
        setattr(self, networks_attr, private_networks)
        setattr(self, weights_attr, weights)
        return private_networks, weights

    def _get_public_networks_and_weights(self, address_class=None):
        """
        Produces a 2-tuple of valid public IPv4 networks and corresponding relative weights

        :param address_class: IPv4 address class (a, b, or c)
        """
        # If `address_class` has an unexpected value, choose a valid value at random
        if address_class not in _IPv4Constants._network_classes.keys():
            address_class = self.ipv4_network_class()

        # Return cached network and weight data if available for a specific address class
        networks_attr = f'_cached_public_class_{address_class}_networks'
        weights_attr = f'{networks_attr}_weights'
        if hasattr(self, networks_attr) and hasattr(self, weights_attr):
            return getattr(self, networks_attr), getattr(self, weights_attr)

        # Otherwise, compute for list of public networks (excluding private and special networks)
        public_networks = [_IPv4Constants._network_classes[address_class]]
        public_networks = self._exclude_ipv4_networks(
            public_networks,
            _IPv4Constants._private_networks +
            _IPv4Constants._excluded_networks,
        )

        # Then compute for list of corresponding relative weights
        weights = [network.num_addresses for network in public_networks]

        # Then cache and return results
        setattr(self, networks_attr, public_networks)
        setattr(self, weights_attr, weights)
        return public_networks, weights

    def _random_ipv4_address_from_subnets(self, subnets, weights=None, network=False):
        """
        Produces a random IPv4 address or network with a valid CIDR
        from within the given subnets using a distribution described
        by weights.

        :param subnets: List of IPv4Networks to choose from within
        :param weights: List of weights corresponding to the individual IPv4Networks
        :param network: Return a network address, and not an IP address
        :return:
        """
        # If the weights argument has an invalid value, default to equal distribution
        try:
            subnet = choices_distribution(subnets, weights, random=self.generator.random, length=1)[0]
        except (AssertionError, TypeError):
            subnet = self.generator.random.choice(subnets)

        address = str(
            subnet[self.generator.random.randint(
                0, subnet.num_addresses - 1,
            )],
        )

        if network:
            address += '/' + str(self.generator.random.randint(
                subnet.prefixlen,
                subnet.max_prefixlen,
            ))
            address = str(ip_network(address, strict=False))

        return address

    def _exclude_ipv4_networks(self, networks, networks_to_exclude):
        """
        Exclude the list of networks from another list of networks
        and return a flat list of new networks.

        :param networks: List of IPv4 networks to exclude from
        :param networks_to_exclude: List of IPv4 networks to exclude
        :returns: Flat list of IPv4 networks
        """
        networks_to_exclude.sort(key=lambda x: x.prefixlen)
        for network_to_exclude in networks_to_exclude:
            def _exclude_ipv4_network(network):
                """
                Exclude a single network from another single network
                and return a list of networks. Network to exclude
                comes from the outer scope.

                :param network: Network to exclude from
                :returns: Flat list of IPv4 networks after exclusion.
                          If exclude fails because networks do not
                          overlap, a single element list with the
                          orignal network is returned. If it overlaps,
                          even partially, the network is excluded.
                """
                try:
                    return list(network.address_exclude(network_to_exclude))
                except ValueError:
                    # If networks overlap partially, `address_exclude`
                    # will fail, but the network still must not be used
                    # in generation.
                    if network.overlaps(network_to_exclude):
                        return []
                    else:
                        return [network]

            networks = list(map(_exclude_ipv4_network, networks))

            # flatten list of lists
            networks = [
                item for nested in networks for item in nested
            ]

        return networks

    def ipv4_network_class(self):
        """
        Returns a IPv4 network class 'a', 'b' or 'c'.

        :returns: IPv4 network class
        """
        return self.random_element('abc')

    def ipv4(self, network=False, address_class=None, private=None):
        """
        Returns a random IPv4 address or network with a valid CIDR.

        :param network: Network address
        :param address_class: IPv4 address class (a, b, or c)
        :param private: Public or private
        :returns: IPv4
        """
        if private is True:
            return self.ipv4_private(address_class=address_class,
                                     network=network)
        elif private is False:
            return self.ipv4_public(address_class=address_class,
                                    network=network)
        else:
            all_networks, weights = self._get_all_networks_and_weights(address_class=address_class)
            return self._random_ipv4_address_from_subnets(all_networks, weights=weights, network=network)

    def ipv4_private(self, network=False, address_class=None):
        """
        Returns a private IPv4.

        :param network: Network address
        :param address_class: IPv4 address class (a, b, or c)
        :returns: Private IPv4
        """
        private_networks, weights = self._get_private_networks_and_weights(address_class=address_class)
        return self._random_ipv4_address_from_subnets(private_networks, weights=weights, network=network)

    def ipv4_public(self, network=False, address_class=None):
        """
        Returns a public IPv4 excluding private blocks.

        :param network: Network address
        :param address_class: IPv4 address class (a, b, or c)
        :returns: Public IPv4
        """
        public_networks, weights = self._get_public_networks_and_weights(address_class=address_class)
        return self._random_ipv4_address_from_subnets(public_networks, weights=weights, network=network)

    def ipv6(self, network=False):
        """Produce a random IPv6 address or network with a valid CIDR"""
        address = str(ip_address(self.generator.random.randint(
            2 ** IPV4LENGTH, (2 ** IPV6LENGTH) - 1)))
        if network:
            address += '/' + str(self.generator.random.randint(0, IPV6LENGTH))
            address = str(ip_network(address, strict=False))
        return address

    def mac_address(self):
        mac = [self.generator.random.randint(0x00, 0xff) for _ in range(0, 6)]
        return ":".join(map(lambda x: "%02x" % x, mac))

    def port_number(self, is_system=False, is_user=False, is_dynamic=False):
        """Returns a network port number
        https://tools.ietf.org/html/rfc6335

        :param is_system: System or well-known ports
        :param is_user: User or registered ports
        :param is_dynamic: Dynamic / private / ephemeral ports
        :rtype: int
        """

        if is_system:
            return self.random_int(min=0, max=1023)
        elif is_user:
            return self.random_int(min=1024, max=49151)
        elif is_dynamic:
            return self.random_int(min=49152, max=65535)

        return self.random_int(min=0, max=65535)

    def uri_page(self):
        return self.random_element(self.uri_pages)

    def uri_path(self, deep=None):
        deep = deep if deep else self.generator.random.randint(1, 3)
        return "/".join(
            self.random_elements(self.uri_paths, length=deep),
        )

    def uri_extension(self):
        return self.random_element(self.uri_extensions)

    def uri(self):
        pattern = self.random_element(self.uri_formats)
        return self.generator.parse(pattern)

    @slugify
    def slug(self, value=None):
        """Django algorithm"""
        if value is None:
            value = self.generator.text(20)
        return value

    def image_url(self, width=None, height=None):
        """
        Returns URL to placeholder image
        Example: http://placehold.it/640x480
        """
        width_ = width or self.random_int(max=1024)
        height_ = height or self.random_int(max=1024)
        placeholder_url = self.random_element(self.image_placeholder_services)
        return placeholder_url.format(width=width_, height=height_)

    def iana_id(self):
        """Returns IANA Registrar ID
        https://www.iana.org/assignments/registrar-ids/registrar-ids.xhtml

        :rtype: str
        """

        return str(self.random_int(min=1, max=8888888))

    def ripe_id(self):
        """Returns RIPE Organization ID
        https://www.ripe.net/manage-ips-and-asns/db/support/organisation-object-in-the-ripe-database

        :rtype: str
        """

        lex = '?' * self.random_int(min=2, max=4)
        num = '%' * self.random_int(min=1, max=5)
        return self.bothify(f'ORG-{lex}{num}-RIPE').upper()

    def nic_handle(self, suffix='FAKE'):
        """Returns NIC Handle ID
        https://www.apnic.net/manage-ip/using-whois/guide/person/

        :rtype: str
        """

        if len(suffix) < 2:
            raise ValueError('suffix length must be greater than or equal to 2')

        lex = '?' * self.random_int(min=2, max=4)
        num = '%' * self.random_int(min=1, max=5)
        return self.bothify(f'{lex}{num}-{suffix}').upper()

    def nic_handles(self, count=1, suffix='????'):
        """Returns NIC Handle ID list

        :rtype: list[str]
        """

        return [self.nic_handle(suffix=suffix) for _ in range(count)]
