from . import BaseProvider
from . import DateTime
from datetime import datetime
import random


class Provider(BaseProvider):

    userAgents = ('firefox','chrome','internetExplorer','opera','safari')

    windowsPlatformTokens = (
        'Windows NT 6.2', 'Windows NT 6.1', 'Windows NT 6.0', 'Windows NT 5.2', 'Windows NT 5.1',
        'Windows NT 5.01', 'Windows NT 5.0', 'Windows NT 4.0', 'Windows 98; Win 9x 4.90',
        'Windows 98', 'Windows 95', 'Windows CE'
        )

    linuxProcessors = ('i686', 'x86_64',)

    macProcessors = ('Intel', 'PPC', 'U; Intel', 'U; PPC')

    langs = ('en-US', 'sl-SI', 'it-IT')

    @classmethod
    def macProcessor(cls):
        return cls.randomElement( cls.macProcessors )

    @classmethod
    def linuxProcessor(cls):
        return cls.randomElement( cls.linuxProcessors )

    @classmethod
    def userAgent(cls):
        userAgentName = cls.randomElement( cls.userAgents )
        return getattr(cls, userAgentName)()

    @classmethod
    def chrome(cls):
        saf = str(random.randint(531,536)) + str(random.randint(0,2))

        platforms = (
            "(%s) AppleWebKit/%s (KHTML, like Gecko) Chrome/%s.0.%s.0 Safari/%s" % (cls.linuxPlatformToken(), saf, random.randint(13,15),random.randint(800,899), saf),
            "(%s) AppleWebKit/%s (KHTML, like Gecko) Chrome/%s.0.%s.0 Safari/%s" % (cls.windowsPlatformToken(), saf, random.randint(13,15),random.randint(800,899), saf),
            "(%s) AppleWebKit/%s (KHTML, like Gecko) Chrome/%s.0.%s.0 Safari/%s" % (cls.macPlatformToken(), saf, random.randint(13,15),random.randint(800,899), saf),
        )

        return 'Mozilla/5.0 ' + cls.randomElement( platforms )

    @classmethod
    def firefox(cls):
        ver = (
            'Gecko/%s Firefox/%s.0' % (DateTime.Provider.dateTimeBetween(datetime(2011,1,1)), random.randint(4,15)),
            'Gecko/%s Firefox/3.6.%s' % (DateTime.Provider.dateTimeBetween(datetime(2010,1,1)), random.randint(1,20)),
            'Gecko/%s Firefox/3.8' % (DateTime.Provider.dateTimeBetween(datetime(2010,1,1)), ),
        )

        platforms = (
            "(%s; %s; rv:1.9.%s.20) %s" % (cls.windowsPlatformToken(), cls.randomElement(cls.langs), random.randint(0,2),random.choice(ver)),
            "(%s; rv:1.9.%s.20) %s" % (cls.linuxPlatformToken(), random.randint(5,7),random.choice(ver)),
            "(%s; rv:1.9.%s.20) %s" % (cls.macPlatformToken(), random.randint(2,6),random.choice(ver)),
        )

        return 'Mozilla/5.0 ' + cls.randomElement( platforms )

    @classmethod
    def safari(cls):
        saf = "%s.%s.%s" % (random.randint(531,535),random.randint(1,50),random.randint(1,7))
        if random.randint(0,1) == 0:
            ver = "%s.%s" % (random.randint(4,5),random.randint(0,1))
        else:
            ver = "%s.0.%s" % (random.randint(4,5),random.randint(1,5))

        platforms = (
            '(Windows; U; %s) AppleWebKit/%s (KHTML, like Gecko) Version/%s Safari/%s' % (cls.windowsPlatformToken(), saf, ver, saf),
            '(%s rv:%s.0; %s) AppleWebKit/%s (KHTML, like Gecko) Version/%s Safari/%s' % (cls.macPlatformToken(), random.randint(2,6), cls.randomElement(cls.langs), saf, ver, saf),
            '(iPod; U; CPU iPhone OS %s_%s like Mac OS X; %s) AppleWebKit/%s (KHTML, like Gecko) Version/%s.0.5 Mobile/8B%s Safari/6%s' % (
                random.randint(3,4), random.randint(0,3), cls.randomElement(cls.langs), saf,random.randint(3,4), random.randint(111,119), saf
            )
        )

        return 'Mozilla/5.0 ' + cls.randomElement( platforms )

    @classmethod
    def opera(cls):

        platforms = (
            '(%s; %s) Presto/2.9.%s Version/%s.00' % (cls.linuxPlatformToken(), cls.randomElement(cls.langs), random.randint(160,190), random.randint(10,12)),
            '(%s; %s) Presto/2.9.%s Version/%s.00' % (cls.windowsPlatformToken(), cls.randomElement(cls.langs), random.randint(160,190), random.randint(10,12)),
        )

        return 'Opera/%s.%s %s' % (random.randint(8,9),random.randint(10,99),cls.randomElement(platforms))

    @classmethod
    def internetExplorer(cls):
        return 'Mozilla/5.0 (compatible; MSIE %s.0; %s; Trident/%s.%s)' % (
            random.randint(5,9),
            cls.windowsPlatformToken(),
            random.randint(3,5),
            random.randint(0,1)
        )

    @classmethod
    def windowsPlatformToken(cls):
        return cls.randomElement(cls.windowsPlatformTokens)

    @classmethod
    def linuxPlatformToken(cls):
        return 'X11; Linux %s' % cls.randomElement( cls.linuxProcessors )

    @classmethod
    def macPlatformToken(cls):
        return 'Macintosh; %s Mac OS X 10_%s_%s' % ( cls.randomElement(cls.macProcessors), random.randint(5,8), random.randint(0,9) )
