# coding=utf-8
from ..Internet import Provider as InternetProvider

class Provider(InternetProvider):

    safeEmailTlds = ('com', 'net', 'fr', 'fr')
    freeEmailDomains = ('voila.fr', 'gmail.com', 'hotmail.fr', 'yahoo.fr', 'laposte.net', 'free.fr', 'sfr.fr', 'orange.fr', 'bouygtel.fr', 'club-internet.fr', 'dbmail.com', 'live.com', 'ifrance.com', 'noos.fr', 'tele2.fr', 'tiscali.fr', 'wanadoo.fr')
    tlds = ('com', 'com', 'com', 'net', 'org', 'fr', 'fr', 'fr')

    @staticmethod
    def _toAscii(string):
        replacements = (
            (u'à', u'a'), (u'À', u'A'), (u'ç', u'c'), (u'Ç', u'c'), (u'é', u'e'), (u'É', u'E'), (u'è', u'e'),
            (u'È', u'E'), (u'ë', u'e'), (u'Ë', u'E'), (u'ï', u'i'), (u'Ï', u'I'), (u'î', u'i'), (u'Î', u'I'),
            (u'ô', u'o'), (u'Ô', u'O'), (u'ù', u'u'), (u'Ù', u'U'),
        )
        for search, replace in replacements:
            string = string.replace(search,replace)

        return string

    def userName(self):
        format = self.randomElement( self.userNameFormats )
        return self._toAscii( self.bothify( self.generator.parse(format) ) ).lower()

    def domainWord(self):

        company = self.generator.format('company')
        companyElements = company.split(' ')
        company = companyElements[0]
        company = company.replace(" ","")

        return self._toAscii(company).lower()