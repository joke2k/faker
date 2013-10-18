from __future__ import unicode_literals
from . import BaseProvider
import random
import re
from faker.providers.lorem import Provider as Lorem


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

    def user_name(self):
        pattern = self.random_element(self.user_name_formats)
        return self.bothify(self.generator.parse(pattern)).lower()

    def domain_name(self):
        return self.domain_word() + '.' + self.tld()

    def domain_word(self):
        company = self.generator.format('company')
        company_elements = company.split(' ')
        company = company_elements.pop(0)
        return re.sub(r'\W', '', company).lower()

    def tld(self):
        return self.random_element(self.tlds)

    def url(self):
        pattern = self.random_element(self.url_formats)
        return self.generator.parse(pattern)

    def ipv4(self):
        """
        Convert 32-bit integer to dotted IPv4 address.
        """
        return ".".join(map(lambda n: str(random.randint(-2147483648, 2147483647) >> n & 0xFF), [24, 16, 8, 0]))

    def ipv6(self):
        res = []
        for i in range(0, 8):
            res.append(hex(random.randint(0, 65535))[2:].zfill(4))
        return ":".join(res)

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
    def slug(cls, value=None):
        """
        Django algorithm
        """
        import unicodedata

        #value = unicode(value or Lorem.text(20))
        #value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
        #value = unicode(re.sub(r'[^\w\s-]', '', value).strip().lower())
        #return re.sub('[-\s]+', '-', value)
        value = unicodedata.normalize('NFKD', value or Lorem.text(20)).encode('ascii', 'ignore').decode('ascii')
        value = re.sub('[^\w\s-]', '', value).strip().lower()
        return re.sub('[-\s]+', '-', value)


