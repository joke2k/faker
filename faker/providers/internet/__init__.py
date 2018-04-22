# coding=utf-8
from __future__ import unicode_literals

from text_unidecode import unidecode

from .. import BaseProvider

from ipaddress import ip_address, ip_network, IPV4LENGTH, IPV6LENGTH

# from faker.generator import random
# from faker.providers.lorem.la import Provider as Lorem
from faker.utils.decorators import lowercase, slugify, slugify_unicode


localized = True


IPV4_PUBLIC_NETS = {
    'a': ip_network('0.0.0.0/1'),
    'b': ip_network('128.0.0.0/2'),
    'c': ip_network('192.0.0.0/3')
}
IPV4_PRIVATE_NET_BLOCKS = {
    'a': (
        ip_network('0.0.0.0/8'),
        ip_network('10.0.0.0/8'),
        ip_network('127.0.0.0/8'),
    ),
    'b': (
        ip_network('169.254.0.0/16'),
        ip_network('172.16.0.0/12')
    ),
    'c': (
        ip_network('192.0.0.0/29'),
        ip_network('192.0.0.170/31'),
        ip_network('192.0.2.0/24'),
        ip_network('192.168.0.0/16'),
        ip_network('198.18.0.0/15'),
        ip_network('198.51.100.0/24'),
        ip_network('203.0.113.0/24')
    ),
}
IPV4_NET_CLASSES = {
    'a': (167772160, 184549375, 24),
    'b': (2886729728, 2887778303, 20),
    'c': (3232235520, 3232301055, 16)
}


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
        if address_class is None:
            ip_range = (0, (2 ** IPV4LENGTH) - 1)
        else:
            net = IPV4_PUBLIC_NETS[address_class]
            ip_range = (net._ip[0], net.ip[-1])
        address = str(ip_address(self.generator.random.randint(*ip_range)))
        if network:
            address += '/' + str(self.generator.random.randint(0, IPV4LENGTH))
            address = str(ip_network(address, strict=False))
        return address

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
        address_class = address_class or self.ipv4_network_class()
        min_, max_, netmask = IPV4_NET_CLASSES[address_class]
        address = str(ip_address(
            self.generator.random.randint(min_, max_)))
        if network:
            address += '/' + str(self.generator.random.randint(netmask, 31))
            address = str(ip_network(address, strict=False))
        return address

    def ipv4_public(self, network=False, address_class=None):
        """
        Returns a public IPv4 excluding private blocks.

        :param network: Network address
        :param address_class: IPv4 address class (a, b, or c)
        :returns: Public IPv4
        """
        address_class = address_class or self.ipv4_network_class()
        public_net = IPV4_PUBLIC_NETS[address_class]
        private_blocks = IPV4_PRIVATE_NET_BLOCKS[address_class]
        # Make valid IP ranges, created from private block exclusion
        net_ranges = []
        ## Starts at end of 1st block if it's 1st of class
        if public_net[0] != private_blocks[0][0]:
            net_ranges = [(public_net[0]._ip, private_blocks[0][0]._ip-1)]
        ## Loop on private blocks and guess available ranges
        for i, block in enumerate(private_blocks):
            if i+1 == len(private_blocks):
                break
            net_range = (block[-1]._ip+1, private_blocks[i+1][0]._ip-1)
            net_ranges.append(net_range)
        ## Add last range
        net_ranges.append((private_blocks[-1][-1]._ip-1, public_net[-1]._ip-1))
        net_ranges = [(i, j) for i, j in net_ranges if (j-i) > 0]
        # Choose a range
        min_, max_ = self.generator.random.choice(net_ranges)
        address = str(ip_address(
            self.generator.random.randint(min_, max_)))
        # Add network mask
        if network:
            net_masks = {'a': 8, 'b': 16, 'c': 24}
            min_net_mask = net_masks[address_class]
            address += '/' + str(self.generator.random.randint(min_net_mask, 31))
            address = str(ip_network(address, strict=False))
        return address

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
            [self.random_element(self.uri_paths) for _ in range(0, deep)]
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
