# coding=utf-8
from __future__ import unicode_literals

from text_unidecode import unidecode

from .. import BaseProvider

from ipaddress import ip_address, ip_network, IPv4Address, IPV4LENGTH, IPV6LENGTH

# from faker.generator import random
# from faker.providers.lorem.la import Provider as Lorem
from faker.utils.decorators import lowercase, slugify, slugify_unicode


localized = True


IPV4_NETWORK_CLASSES = {
    'a': ip_network('0.0.0.0/1'),
    'b': ip_network('128.0.0.0/2'),
    'c': ip_network('192.0.0.0/3')
}
IPV4_PRIVATE_NETWORKS = IPv4Address._constants._private_networks.copy()

# Remove 0.0.0.0/8 "This host on this network" [RFC1122], Section 3.2.1.3
# as no IP from this range can be used in local or global traffic
IPV4_PRIVATE_NETWORKS.remove(ip_network('0.0.0.0/8'))

# Add IANA reserved ranges missing from Python ipaddress module
# https://www.iana.org/assignments/iana-ipv4-special-registry/iana-ipv4-special-registry.xhtml
IPV4_PRIVATE_NETWORKS += [
    ip_network('192.0.0.0/24'),
    ip_network('100.64.0.0/10'),
    ip_network('192.0.0.0/24'),
    ip_network('192.0.0.0/29'),
    ip_network('192.0.0.8/32'),
    ip_network('192.0.0.9/32'),
    ip_network('192.0.0.10/32'),
    ip_network('192.31.196.0/24'),
    ip_network('192.52.193.0/24'),
    ip_network('192.88.99.0/24'),
    ip_network('192.175.48.0/24')
]


class Provider(BaseProvider):
    safe_email_tlds = ('org', 'com', 'net')
    free_email_domains = ('gmail.com', 'yahoo.com', 'hotmail.com')
    tlds = (
        'com', 'com', 'com', 'com', 'com', 'com', 'biz', 'info', 'net', 'org'
    )

    uri_pages = (
        'index', 'home', 'search', 'main', 'post', 'homepage', 'category',
        'register', 'login', 'faq', 'about', 'terms', 'privacy', 'author'
    )
    uri_paths = (
        'app', 'main', 'wp-content', 'search', 'category', 'tag', 'categories',
        'tags', 'blog', 'posts', 'list', 'explore'
    )
    uri_extensions = (
        '.html', '.html', '.html', '.htm', '.htm', '.php', '.php', '.jsp',
        '.asp'
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
        'https://placeholdit.imgix.net/~text'
        '?txtsize=55&txt={width}x{height}&w={width}&h={height}',
        'https://www.lorempixel.com/{width}/{height}',
        'https://dummyimage.com/{width}x{height}',
    )

    replacements = tuple()

    def _to_ascii(self, string):
        for search, replace in self.replacements:
            string = string.replace(search, replace)

        string = unidecode(string)
        return string

    @lowercase
    def email(self, domain=None):
        if domain:
            email = '{0}@{1}'.format(self.user_name(), domain)
        else:
            pattern = self.random_element(self.email_formats)
            email = "".join(self.generator.parse(pattern).split(" "))
        return email

    @lowercase
    def safe_email(self):
        return '{}@example.{}'.format(
            self.user_name(), self.random_element(self.safe_email_tlds)
        )

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
            "".join(self.generator.parse(pattern).split(" "))
        )

    @lowercase
    def ascii_safe_email(self):
        return self._to_ascii(
            self.user_name() +
            '@example.' +
            self.random_element(self.safe_email_tlds)
        )

    @lowercase
    def ascii_free_email(self):
        return self._to_ascii(
            self.user_name() + '@' + self.free_email_domain()
        )

    @lowercase
    def ascii_company_email(self):
        return self._to_ascii(
            self.user_name() + '@' + self.domain_name()
        )

    @slugify_unicode
    def user_name(self):
        pattern = self.random_element(self.user_name_formats)
        username = self._to_ascii(
            self.bothify(self.generator.parse(pattern)).lower()
        )
        return username

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
    def domain_word(self,):
        company = self.generator.format('company')
        company_elements = company.split(' ')
        company = self._to_ascii(company_elements.pop(0))
        return company

    def tld(self):
        return self.random_element(self.tlds)

    def url(self, schemes=None):
        """
        :param schemes: a list of strings to use as schemes, one will chosen randomly.
        If None, it will generate http and https urls.
        Passing an empty list will result in schemeless url generation like "://domain.com".

        :returns: a random url string.
        """
        if schemes is None:
            schemes = ['http', 'https']

        pattern = '{}://{}'.format(
            self.random_element(schemes) if schemes else "",
            self.random_element(self.url_formats)
        )

        return self.generator.parse(pattern)

    def _random_ipv4_address_from_subnet(self, subnet, network=False):
        """
        Produces a random IPv4 address or network with a valid CIDR
        from within a given subnet.

        :param subnet: IPv4Network to choose from within
        :param network: Return a network address, and not an IP address
        """
        address = str(
            subnet[self.generator.random.randint(
                0, subnet.num_addresses - 1
            )]
        )

        if network:
            address += '/' + str(self.generator.random.randint(
                subnet.prefixlen,
                subnet.max_prefixlen
            ))
            address = str(ip_network(address, strict=False))

        return address

    def ipv4(self, network=False, address_class=None, private=None):
        """
        Produce a random IPv4 address or network with a valid CIDR.

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

        if address_class:
            subnet = IPV4_NETWORK_CLASSES[address_class]
        else:
            # if no address class is choosen, use whole IPv4 pool
            subnet = ip_network('0.0.0.0/0')

        return self._random_ipv4_address_from_subnet(subnet, network)

    def ipv4_network_class(self):
        """
        Returns a IPv4 network class 'a', 'b' or 'c'.

        :returns: IPv4 network class
        """
        return self.random_element('abc')

    def ipv4_private(self, network=False, address_class=None):
        """
        Returns a private IPv4.

        :param network: Network address
        :param address_class: IPv4 address class (a, b, or c)
        :returns: Private IPv4
        """
        # compute private networks
        supernet = IPV4_NETWORK_CLASSES[
            address_class or self.ipv4_network_class()
        ]

        private_networks = [
            subnet for subnet in IPV4_PRIVATE_NETWORKS
            if subnet.overlaps(supernet)
        ]

        # choose private network
        subnet = self.generator.random.choice(private_networks)

        return self._random_ipv4_address_from_subnet(subnet, network)

    def ipv4_public(self, network=False, address_class=None):
        """
        Returns a public IPv4 excluding private blocks.

        :param network: Network address
        :param address_class: IPv4 address class (a, b, or c)
        :returns: Public IPv4
        """
        # compute public networks
        public_networks = [IPV4_NETWORK_CLASSES[
            address_class or self.ipv4_network_class()
        ]]

        for private_network in IPV4_PRIVATE_NETWORKS:
            try:
                public_networks = list(map(
                    lambda net: list(net.address_exclude(private_network)),
                    public_networks)
                )

                # flatten list of lists
                public_networks = [
                    item for nested in public_networks for item in nested
                ]
            except ValueError:
                # excluded private network is not within our supernet
                pass

        # choose public network
        subnet = self.generator.random.choice(public_networks)

        return self._random_ipv4_address_from_subnet(subnet, network)

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

    def uri_page(self):
        return self.random_element(self.uri_pages)

    def uri_path(self, deep=None):
        deep = deep if deep else self.generator.random.randint(1, 3)
        return "/".join(
            self.random_elements(self.uri_paths, length=deep)
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
