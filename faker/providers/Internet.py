from . import BaseProvider
import random

class Provider(BaseProvider):

    safeEmailTlds = ('org','com','net')
    freeEmailDomains = ('gmail.com','yahoo.com','hotmail.com')
    tlds = ('com','com','com','com','com','com','biz','info','net','org')

    userNameFormats = (
        '{{lastName}}.{{firstName}}',
        '{{firstName}}.{{lastName}}',
        '{{firstName}}##',
        '?{{lastName}}',
    )
    emailFormats = (
        '{{userName}}@{{domainName}}',
        '{{userName}}@{{freeEmailDomain}}',
    )
    urlFormats = (
        'http://www.{{domainName}}/',
        'http://{{domainName}}/',
    )

    def email(self):
        format = self.randomElement( self.emailFormats )
        return "".join(self.generator.parse(format).split(" "))

    def safeEmail(self):
        return self.userName() + '@example.' + self.randomElement( self.safeEmailTlds )

    def freeEmail(self):
        return self.userName() + '@' + self.freeEmailDomain()

    def companyEmail(self):
        return self.userName() + '@' + self.domainName()

    @classmethod
    def freeEmailDomain(cls):
        return cls.randomElement( cls.freeEmailDomains )

    def userName(self):
        format = self.randomElement(self.userNameFormats)
        return self.bothify( self.generator.parse(format) ).lower()

    def domainName(self):
        return self.domainWord() + '.' + self.tld()

    def domainWord(self):
        company = self.generator.format('company')()
        companyElements = company.split(' ')
        company = companyElements.pop(0)
        return company.replace(r'\W','').lower()

    def tld(self):
        return self.randomElement( self.tlds )

    def url(self):
        format = self.randomElement( self.urlFormats )
        return self.generator.parse( format )

    def ipv4(self):
        "Convert 32-bit integer to dotted IPv4 address."
        return ".".join(map(lambda n: str( random.randint(-2147483648,2147483647) >>n & 0xFF), [24,16,8,0]))

    def ipv6(self):
        res = []
        for i in range(0,8):
            res.append( hex(random.randint(0,65535))[2:].zfill(4) )
        return ":".join(res)


