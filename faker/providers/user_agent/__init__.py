# coding=utf-8

from __future__ import unicode_literals

import string
from datetime import datetime

from .. import BaseProvider


class Provider(BaseProvider):
    user_agents = (
        'chrome', 'firefox', 'internet_explorer', 'opera', 'safari',
    )

    windows_platform_tokens = (
        'Windows 95', 'Windows 98', 'Windows 98; Win 9x 4.90', 'Windows CE',
        'Windows NT 4.0', 'Windows NT 5.0', 'Windows NT 5.01',
        'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1',
        'Windows NT 6.2',
    )

    linux_processors = ('i686', 'x86_64')

    mac_processors = ('Intel', 'PPC', 'U; Intel', 'U; PPC')

    android_versions = (
        '1.0', '1.1', '1.5', '1.6', '2.0', '2.0.1', '2.1', '2.2', '2.2.1', '2.2.2', '2.2.3', '2.3', '2.3.1', '2.3.2',
        '2.3.3', '2.3.4', '2.3.5', '2.3.6', '2.3.7', '3.0', '3.1', '3.2', '3.2.1', '3.2.2', '3.2.3', '3.2.4', '3.2.5',
        '3.2.6', '4.0', '4.0.1', '4.0.2', '4.0.3', '4.0.4', '4.1', '4.1.1', '4.1.2', '4.2', '4.2.1', '4.2.2', '4.3',
        '4.3.1', '4.4', '4.4.1', '4.4.2', '4.4.3', '4.4.4', '5.0', '5.0.1', '5.0.2', '5.1', '5.1.1', '6.0', '6.0.1',
        '7.0', '7.1', '7.1.1', '7.1.2', '8.0.0', '8.1.0', '9',
    )

    apple_devices = ('iPhone', 'iPad')

    ios_versions = (
        '3.1.3', '4.2.1', '5.1.1', '6.1.6', '7.1.2', '9.3.5', '9.3.6', '10.3.3', '10.3.4', '12.4',
    )

    def mac_processor(self):
        return self.random_element(self.mac_processors)

    def linux_processor(self):
        return self.random_element(self.linux_processors)

    def user_agent(self):
        name = self.random_element(self.user_agents)
        return getattr(self, name)()

    def chrome(self, version_from=13, version_to=63,
               build_from=800, build_to=899):
        saf = '{0}.{1}'.format(self.generator.random.randint(531, 536),
                               self.generator.random.randint(0, 2))
        bld = self.lexify(self.numerify('##?###'), string.ascii_uppercase)
        tmplt = '({0}) AppleWebKit/{1} (KHTML, like Gecko)' \
                ' Chrome/{2}.0.{3}.0 Safari/{4}'
        tmplt_ios = '({0}) AppleWebKit/{1} (KHTML, like Gecko)' \
                    ' CriOS/{2}.0.{3}.0 Mobile/{4} Safari/{1}'
        platforms = (
            tmplt.format(self.linux_platform_token(),
                         saf,
                         self.generator.random.randint(version_from, version_to),
                         self.generator.random.randint(build_from, build_to),
                         saf),
            tmplt.format(self.windows_platform_token(),
                         saf,
                         self.generator.random.randint(version_from, version_to),
                         self.generator.random.randint(build_from, build_to),
                         saf),
            tmplt.format(self.mac_platform_token(),
                         saf,
                         self.generator.random.randint(version_from, version_to),
                         self.generator.random.randint(build_from, build_to),
                         saf),
            tmplt.format('Linux; {0}'.format(self.android_platform_token()),
                         saf,
                         self.generator.random.randint(version_from, version_to),
                         self.generator.random.randint(build_from, build_to),
                         saf),
            tmplt_ios.format(self.ios_platform_token(),
                             saf,
                             self.generator.random.randint(version_from, version_to),
                             self.generator.random.randint(build_from, build_to),
                             bld),
        )

        return 'Mozilla/5.0 ' + self.random_element(platforms)

    def firefox(self):
        ver = (
            'Gecko/{0} Firefox/{1}.0'.format(
                self.generator.date_time_between(
                    datetime(2011, 1, 1),
                ),
                self.generator.random.randint(4, 15),
            ),
            'Gecko/{0} Firefox/3.6.{1}'.format(
                self.generator.date_time_between(
                    datetime(2010, 1, 1),
                ),
                self.generator.random.randint(1, 20)),
            'Gecko/{0} Firefox/3.8'.format(
                self.generator.date_time_between(datetime(2010, 1, 1)),
            ),
        )
        tmplt_win = '({0}; {1}; rv:1.9.{2}.20) {3}'
        tmplt_lin = '({0}; rv:1.9.{1}.20) {2}'
        tmplt_mac = '({0}; rv:1.9.{1}.20) {2}'
        tmplt_and = '({0}; Mobile; rv:{1}.0) Gecko/{1}.0 Firefox/{1}.0'
        tmplt_ios = '({0}) AppleWebKit/{1} (KHTML, like Gecko) FxiOS/{2}.{3}.0 Mobile/{4} Safari/{1}'
        saf = '{0}.{1}'.format(self.generator.random.randint(531, 536),
                               self.generator.random.randint(0, 2))
        bld = self.lexify(self.numerify('##?###'), string.ascii_uppercase)
        bld2 = self.lexify(self.numerify('#?####'), string.ascii_lowercase)
        platforms = (
            tmplt_win.format(self.windows_platform_token(),
                             self.generator.locale().replace('_', '-'),
                             self.generator.random.randint(0, 2),
                             self.generator.random.choice(ver)),
            tmplt_lin.format(self.linux_platform_token(),
                             self.generator.random.randint(5, 7),
                             self.generator.random.choice(ver)),
            tmplt_mac.format(self.mac_platform_token(),
                             self.generator.random.randint(2, 6),
                             self.generator.random.choice(ver)),
            tmplt_and.format(self.android_platform_token(),
                             self.generator.random.randint(5, 68)),
            tmplt_ios.format(self.ios_platform_token(),
                             saf,
                             self.generator.random.randint(9, 18),
                             bld2,
                             bld),
        )

        return 'Mozilla/5.0 ' + self.random_element(platforms)

    def safari(self):
        saf = "{0}.{1}.{2}".format(self.generator.random.randint(531, 535),
                                   self.generator.random.randint(1, 50),
                                   self.generator.random.randint(1, 7))
        if not self.generator.random.getrandbits(1):
            ver = "{0}.{1}".format(self.generator.random.randint(4, 5),
                                   self.generator.random.randint(0, 1))
        else:
            ver = "{0}.0.{1}".format(self.generator.random.randint(4, 5),
                                     self.generator.random.randint(1, 5))
        tmplt_win = '(Windows; U; {0}) AppleWebKit/{1} (KHTML, like Gecko)' \
                    ' Version/{2} Safari/{3}'
        tmplt_mac = '({0} rv:{1}.0; {2}) AppleWebKit/{3} (KHTML, like Gecko)' \
                    ' Version/{4} Safari/{5}'
        tmplt_ipod = '(iPod; U; CPU iPhone OS {0}_{1} like Mac OS X; {2})' \
                     ' AppleWebKit/{3} (KHTML, like Gecko) Version/{4}.0.5' \
                     ' Mobile/8B{5} Safari/6{6}'
        locale = self.generator.locale().replace('_', '-')
        platforms = (
            tmplt_win.format(self.windows_platform_token(),
                             saf,
                             ver,
                             saf),
            tmplt_mac.format(self.mac_platform_token(),
                             self.generator.random.randint(2, 6),
                             locale,
                             saf,
                             ver,
                             saf),
            tmplt_ipod.format(self.generator.random.randint(3, 4),
                              self.generator.random.randint(0, 3),
                              locale,
                              saf,
                              self.generator.random.randint(3, 4),
                              self.generator.random.randint(111, 119),
                              saf),
        )

        return 'Mozilla/5.0 ' + self.random_element(platforms)

    def opera(self):
        platform = '({0}; {1}) Presto/2.9.{2} Version/{3}.00'.format(
            (
                self.linux_platform_token()
                if self.generator.random.getrandbits(1)
                else self.windows_platform_token()
            ),
            self.generator.locale().replace('_', '-'),
            self.generator.random.randint(160, 190),
            self.generator.random.randint(10, 12),
        )
        return 'Opera/{0}.{1}.{2}'.format(
            self.generator.random.randint(8, 9),
            self.generator.random.randint(10, 99),
            platform,
        )

    def internet_explorer(self):
        tmplt = 'Mozilla/5.0 (compatible; MSIE {0}.0; {1}; Trident/{2}.{3})'
        return tmplt.format(self.generator.random.randint(5, 9),
                            self.windows_platform_token(),
                            self.generator.random.randint(3, 5),
                            self.generator.random.randint(0, 1))

    def windows_platform_token(self):
        return self.random_element(self.windows_platform_tokens)

    def linux_platform_token(self):
        return 'X11; Linux {0}'.format(
            self.random_element(self.linux_processors))

    def mac_platform_token(self):
        return 'Macintosh; {0} Mac OS X 10_{1}_{2}'.format(
            self.random_element(self.mac_processors),
            self.generator.random.randint(5, 12),
            self.generator.random.randint(0, 9),
        )

    def android_platform_token(self):
        return 'Android {0}'.format(self.random_element(self.android_versions))

    def ios_platform_token(self):
        return '{0}; CPU {0} OS {1} like Mac OS X'.format(
            self.random_element(self.apple_devices),
            self.random_element(self.ios_versions).replace('.', '_'),
        )
