# coding=utf-8

from __future__ import unicode_literals
from .. import BaseProvider

from faker.generator import random
from faker.providers.lorem.la import Provider as Lorem
from faker.utils.decorators import slugify, slugify_unicode

localized = True


class Provider(BaseProvider):
    safe_email_tlds = ('org', 'com', 'net')
    free_email_domains = ('gmail.com', 'yahoo.com', 'hotmail.com')
    tlds = ('com', 'com', 'com', 'com', 'com', 'com', 'biz', 'info', 'net', 'org')

    uri_pages = (
    'index', 'home', 'search', 'main', 'post', 'homepage', 'category', 'register', 'login', 'faq', 'about', 'terms',
    'privacy', 'author')
    uri_paths = (
    'app', 'main', 'wp-content', 'search', 'category', 'tag', 'categories', 'tags', 'blog', 'posts', 'list', 'explore')
    uri_extensions = ('.html', '.html', '.html', '.htm', '.htm', '.php', '.php', '.jsp', '.asp')

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
        'http://www.{{domain_name}}/',
        'http://{{domain_name}}/',
    )
    uri_formats = (
        '{{url}}',
        '{{url}}{{uri_page}}/',
        '{{url}}{{uri_page}}{{uri_extension}}',
        '{{url}}{{uri_path}}/{{uri_page}}/',
        '{{url}}{{uri_path}}/{{uri_page}}{{uri_extension}}',
    )
    image_placeholder_services = (
        'https://placeholdit.imgix.net/~text?txtsize=55&txt={width}×{height}&w={width}&h={height}',
        'http://www.lorempixel.com/{width}/{height}',
        'http://dummyimage.com/{width}x{height}',
     )

    replacements = tuple()

    IPV4LENGTH = 32
    IPV6LENGTH = 128

    def _to_ascii(self, string):
        for search, replace in self.replacements:
            string = string.replace(search, replace)

        return string

    def email(self):
        pattern = self.random_element(self.email_formats)
        return "".join(self.generator.parse(pattern).split(" "))

    def safe_email(self):
        return self.user_name() + '@example.' + self.random_element(self.safe_email_tlds)

    def free_email(self):
        return self.user_name() + '@' + self.free_email_domain()

    def company_email(self):
        return self.user_name() + '@' + self.domain_name()

    @classmethod
    def free_email_domain(cls):
        return cls.random_element(cls.free_email_domains)

    @slugify_unicode
    def user_name(self):
        pattern = self.random_element(self.user_name_formats)
        username = self._to_ascii(
            self.bothify(self.generator.parse(pattern)
        ).lower())
        return username

    def domain_name(self):
        return self.domain_word() + '.' + self.tld()

    @slugify_unicode
    def domain_word(self,):
        company = self.generator.format('company')
        company_elements = company.split(' ')
        company = self._to_ascii(company_elements.pop(0))
        return company.lower()

    def tld(self):
        return self.random_element(self.tlds)

    def url(self):
        pattern = self.random_element(self.url_formats)
        return self.generator.parse(pattern)

    def ipv4(self, network=False):
        """ Produce a random IPv4 address or network with a valid CIDR.

        IP code generation inspired by ipaddress module: https://github.com/phihag/ipaddress
        """
        ip_int = random.randint(0, (2 ** self.IPV4LENGTH) - 1)
        if network:
            prefixlen = random.randint(0, self.IPV4LENGTH)
            ALL_ONES = (2 ** self.IPV4LENGTH) - 1
            netmask = ALL_ONES ^ (ALL_ONES >> prefixlen)
            ip_int = int(ip_int) & int(netmask)
        ip_str = '.'.join([str(ip_int >> n & 0xFF) for n in [24, 16, 8, 0]])
        if network:
            ip_str += '/' + str(prefixlen)
        return ip_str

    def ipv6(self, network=False):
        """ Produce a random IPv6 address or network with a valid CIDR.

        IP code generation inspired by ipaddress module: https://github.com/phihag/ipaddress
        """
        ip_int = random.randint(2 ** self.IPV4LENGTH, (2 ** self.IPV6LENGTH) - 1)
        if network:
            prefixlen = random.randint(0, self.IPV6LENGTH)
            ALL_ONES = (2 ** self.IPV6LENGTH) - 1
            netmask = ALL_ONES ^ (ALL_ONES >> prefixlen)
            ip_int = int(ip_int) & int(netmask)
        hex_str = '%032x' % ip_int
        hextets = ['%x' % int(hex_str[x:x + 4], 16) for x in range(0, 32, 4)]
        ip_str = ':'.join([h.zfill(4) for h in hextets])
        if network:
            ip_str += '/' + str(prefixlen)
        return ip_str

    def mac_address(self):
        mac = [random.randint(0x00, 0xff) for i in range(0, 6)]
        return ":".join(map(lambda x: "%02x" % x, mac))

    @classmethod
    def uri_page(cls):
        return cls.random_element(cls.uri_pages)

    @classmethod
    def uri_path(cls, deep=None):
        deep = deep if deep else random.randint(1, 3)
        return "/".join([cls.random_element(cls.uri_paths) for _ in range(0, deep)])

    @classmethod
    def uri_extension(cls):
        return cls.random_element(cls.uri_extensions)

    def uri(self):
        pattern = self.random_element(self.uri_formats)
        return self.generator.parse(pattern)

    @classmethod
    @slugify
    def slug(cls, value=None):
        """
        Django algorithm
        """
        if value is None:
            value = Lorem.text(20)
        return value

    @classmethod
    def image_url(cls, width=None, height=None):
        """
        Returns URL to placeholder image
        Example: http://placehold.it/640x480
        """
        width_ = width or cls.random_int(max=1024)
        height_ = height or cls.random_int(max=1024)
        placeholder_url = cls.random_element(cls.image_placeholder_services)
        return placeholder_url.format(width=width_, height=height_)
