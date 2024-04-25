import string

from datetime import datetime, timedelta

from .. import BaseProvider, ElementsType

_DT_ALMOST_MAX = datetime.max - timedelta(1.0)


class Provider(BaseProvider):
    """Implement default user agent provider for Faker."""

    user_agents: ElementsType[str] = (
        "chrome",
        "firefox",
        "internet_explorer",
        "opera",
        "safari",
    )

    # source
    # https://en.wikipedia.org/wiki/Microsoft_Windows
    windows_platform_tokens: ElementsType[str] = (
        "Windows 95",
        "Windows 98",
        "Windows 98; Win 9x 4.90",
        "Windows CE",
        "Windows NT 4.0",
        "Windows NT 5.0",
        "Windows NT 5.01",
        "Windows NT 5.1",
        "Windows NT 5.2",
        "Windows NT 6.0",
        "Windows NT 6.1",
        "Windows NT 6.2",
        "Windows NT 10.0",
        "Windows NT 11.0",
    )

    linux_processors: ElementsType[str] = ("i686", "x86_64")

    mac_processors: ElementsType[str] = ("Intel", "PPC", "U; Intel", "U; PPC")

    # source
    # https://en.wikipedia.org/wiki/Android_version_history
    android_versions: ElementsType[str] = (
        "1.0",
        "1.1",
        "1.5",
        "1.6",
        "2.0",
        "2.0.1",
        "2.1",
        "2.2",
        "2.2.1",
        "2.2.2",
        "2.2.3",
        "2.3",
        "2.3.1",
        "2.3.2",
        "2.3.3",
        "2.3.4",
        "2.3.5",
        "2.3.6",
        "2.3.7",
        "3.0",
        "3.1",
        "3.2",
        "3.2.1",
        "3.2.2",
        "3.2.3",
        "3.2.4",
        "3.2.5",
        "3.2.6",
        "4.0",
        "4.0.1",
        "4.0.2",
        "4.0.3",
        "4.0.4",
        "4.1",
        "4.1.1",
        "4.1.2",
        "4.2",
        "4.2.1",
        "4.2.2",
        "4.3",
        "4.3.1",
        "4.4",
        "4.4.1",
        "4.4.2",
        "4.4.3",
        "4.4.4",
        "5.0",
        "5.0.1",
        "5.0.2",
        "5.1",
        "5.1.1",
        "6.0",
        "6.0.1",
        "7.0",
        "7.1",
        "7.1.1",
        "7.1.2",
        "8.0.0",
        "8.1.0",
        "9",
        "10",
        "11",
        "12",
        "12.1",
        "13",
        "14",
    )

    apple_devices: ElementsType[str] = ("iPhone", "iPad")

    # sources
    # https://en.wikipedia.org/wiki/IOS_version_history
    ios_versions: ElementsType[str] = (
        "3.1.3",
        "4.2.1",
        "5.1.1",
        "6.1.6",
        "7.1.2",
        "9.3.5",
        "9.3.6",
        "10.3.3",
        "10.3.4",
        "11.4.1",
        "12.4.4",
        "12.4.8",
        "13.5.1",
        "14.2",
        "14.2.1",
        "14.8.1",
        "15.8.2",
        "16.7.6",
        "17.1",
        "17.1.1",
        "17.1.2",
        "17.2",
        "17.2.1",
        "17.3",
        "17.3.1",
        "17.4",
    )

    def mac_processor(self) -> str:
        """Generate a MacOS processor token used in user agent strings."""
        return self.random_element(self.mac_processors)

    def linux_processor(self) -> str:
        """Generate a Linux processor token used in user agent strings."""
        return self.random_element(self.linux_processors)

    def user_agent(self) -> str:
        """Generate a random web browser user agent string."""
        name: str = self.random_element(self.user_agents)
        return getattr(self, name)()

    def chrome(
        self,
        version_from: int = 13,
        version_to: int = 63,
        build_from: int = 800,
        build_to: int = 899,
    ) -> str:
        """Generate a Chrome web browser user agent string."""
        saf: str = f"{self.generator.random.randint(531, 536)}.{self.generator.random.randint(0, 2)}"
        bld: str = self.lexify(self.numerify("##?###"), string.ascii_uppercase)
        tmplt: str = "({0}) AppleWebKit/{1} (KHTML, like Gecko)" " Chrome/{2}.0.{3}.0 Safari/{4}"
        tmplt_ios: str = "({0}) AppleWebKit/{1} (KHTML, like Gecko)" " CriOS/{2}.0.{3}.0 Mobile/{4} Safari/{1}"
        platforms: ElementsType[str] = (
            tmplt.format(
                self.linux_platform_token(),
                saf,
                self.generator.random.randint(version_from, version_to),
                self.generator.random.randint(build_from, build_to),
                saf,
            ),
            tmplt.format(
                self.windows_platform_token(),
                saf,
                self.generator.random.randint(version_from, version_to),
                self.generator.random.randint(build_from, build_to),
                saf,
            ),
            tmplt.format(
                self.mac_platform_token(),
                saf,
                self.generator.random.randint(version_from, version_to),
                self.generator.random.randint(build_from, build_to),
                saf,
            ),
            tmplt.format(
                f"Linux; {self.android_platform_token()}",
                saf,
                self.generator.random.randint(version_from, version_to),
                self.generator.random.randint(build_from, build_to),
                saf,
            ),
            tmplt_ios.format(
                self.ios_platform_token(),
                saf,
                self.generator.random.randint(version_from, version_to),
                self.generator.random.randint(build_from, build_to),
                bld,
            ),
        )

        return "Mozilla/5.0 " + self.random_element(platforms)

    def firefox(self) -> str:
        """Generate a Mozilla Firefox web browser user agent string."""
        ver: ElementsType[str] = (
            (
                f"Gecko/{self.generator.date_time_between(datetime(2011, 1, 1), _DT_ALMOST_MAX)} "
                f"Firefox/{self.generator.random.randint(4, 15)}.0"
            ),
            (
                f"Gecko/{self.generator.date_time_between(datetime(2010, 1, 1), _DT_ALMOST_MAX)} "
                f"Firefox/3.6.{self.generator.random.randint(1, 20)}"
            ),
            f"Gecko/{self.generator.date_time_between(datetime(2010, 1, 1), _DT_ALMOST_MAX)} Firefox/3.8",
        )
        tmplt_win: str = "({0}; {1}; rv:1.9.{2}.20) {3}"
        tmplt_lin: str = "({0}; rv:1.9.{1}.20) {2}"
        tmplt_mac: str = "({0}; rv:1.9.{1}.20) {2}"
        tmplt_and: str = "({0}; Mobile; rv:{1}.0) Gecko/{1}.0 Firefox/{1}.0"
        tmplt_ios: str = "({0}) AppleWebKit/{1} (KHTML, like Gecko) FxiOS/{2}.{3}.0 Mobile/{4} Safari/{1}"
        saf: str = f"{self.generator.random.randint(531, 536)}.{self.generator.random.randint(0, 2)}"
        bld: str = self.lexify(self.numerify("##?###"), string.ascii_uppercase)
        bld2: str = self.lexify(self.numerify("#?####"), string.ascii_lowercase)
        platforms: ElementsType[str] = (
            tmplt_win.format(
                self.windows_platform_token(),
                self.generator.locale().replace("_", "-"),
                self.generator.random.randint(0, 2),
                self.generator.random.choice(ver),
            ),
            tmplt_lin.format(
                self.linux_platform_token(),
                self.generator.random.randint(5, 7),
                self.generator.random.choice(ver),
            ),
            tmplt_mac.format(
                self.mac_platform_token(),
                self.generator.random.randint(2, 6),
                self.generator.random.choice(ver),
            ),
            tmplt_and.format(self.android_platform_token(), self.generator.random.randint(5, 68)),
            tmplt_ios.format(
                self.ios_platform_token(),
                saf,
                self.generator.random.randint(9, 18),
                bld2,
                bld,
            ),
        )

        return "Mozilla/5.0 " + self.random_element(platforms)

    def safari(self) -> str:
        """Generate a Safari web browser user agent string."""
        saf: str = (
            f"{self.generator.random.randint(531, 535)}."
            f"{self.generator.random.randint(1, 50)}."
            f"{self.generator.random.randint(1, 7)}"
        )

        ver: str = (
            f"{self.generator.random.randint(4, 5)}.{self.generator.random.randint(0, 1)}"
            if not self.generator.random.getrandbits(1)
            else f"{self.generator.random.randint(4, 5)}.0.{self.generator.random.randint(1, 5)}"
        )

        tmplt_win: str = "(Windows; U; {0}) AppleWebKit/{1} (KHTML, like Gecko)" " Version/{2} Safari/{3}"
        tmplt_mac: str = "({0} rv:{1}.0; {2}) AppleWebKit/{3} (KHTML, like Gecko)" " Version/{4} Safari/{5}"
        tmplt_ipod: str = (
            "(iPod; U; CPU iPhone OS {0}_{1} like Mac OS X; {2})"
            " AppleWebKit/{3} (KHTML, like Gecko) Version/{4}.0.5"
            " Mobile/8B{5} Safari/6{6}"
        )
        locale: str = self.generator.locale().replace("_", "-")
        platforms: ElementsType[str] = (
            tmplt_win.format(self.windows_platform_token(), saf, ver, saf),
            tmplt_mac.format(
                self.mac_platform_token(),
                self.generator.random.randint(2, 6),
                locale,
                saf,
                ver,
                saf,
            ),
            tmplt_ipod.format(
                self.generator.random.randint(3, 4),
                self.generator.random.randint(0, 3),
                locale,
                saf,
                self.generator.random.randint(3, 4),
                self.generator.random.randint(111, 119),
                saf,
            ),
        )

        return "Mozilla/5.0 " + self.random_element(platforms)

    def opera(self) -> str:
        """Generate an Opera web browser user agent string."""
        token: str = (
            self.linux_platform_token() if self.generator.random.getrandbits(1) else self.windows_platform_token()
        )
        locale: str = self.generator.locale().replace("_", "-")
        platform: str = (
            f"({token}; {locale}) Presto/2.9.{self.generator.random.randint(160, 190)} "
            f"Version/{self.generator.random.randint(10, 12)}.00"
        )
        return f"Opera/{self.generator.random.randint(8, 9)}.{self.generator.random.randint(10, 99)}.{platform}"

    def internet_explorer(self) -> str:
        """Generate an IE web browser user agent string."""
        return (
            f"Mozilla/5.0 (compatible; MSIE {self.generator.random.randint(5, 9)}.0; "
            f"{self.windows_platform_token()}; "
            f"Trident/{self.generator.random.randint(3, 5)}.{self.generator.random.randint(0, 1)})"
        )

    def windows_platform_token(self) -> str:
        """Generate a Windows platform token used in user agent strings."""
        return self.random_element(self.windows_platform_tokens)

    def linux_platform_token(self) -> str:
        """Generate a Linux platform token used in user agent strings."""
        return f"X11; Linux {self.random_element(self.linux_processors)}"

    def mac_platform_token(self) -> str:
        """Generate a MacOS platform token used in user agent strings."""
        return (
            f"Macintosh; {self.random_element(self.mac_processors)} Mac OS X 10_"
            f"{self.generator.random.randint(5, 12)}_{self.generator.random.randint(0, 9)}"
        )

    def android_platform_token(self) -> str:
        """Generate an Android platform token used in user agent strings."""
        return f"Android {self.random_element(self.android_versions)}"

    def ios_platform_token(self) -> str:
        """Generate an iOS platform token used in user agent strings."""
        apple_device: str = self.random_element(self.apple_devices)
        ios_version: str = self.random_element(self.ios_versions)
        return f"{apple_device}; CPU {apple_device} " f'OS {ios_version.replace(".", "_")} like Mac OS X'
