import datetime as dt
import re

from typing import Pattern

from freezegun import freeze_time

from faker import Faker
from faker.providers.user_agent import Provider as UaProvider


class TestUserAgentProvider:
    """Test user agent provider methods"""

    num_samples = 1000
    android_token_pattern: Pattern = re.compile(r"Android (?P<android_version>\d+(?:\.\d){0,2})")
    ios_token_pattern: Pattern = re.compile(
        r"^(?P<apple_device>.*?); CPU \1 OS " + r"(?P<ios_version>\d+(?:_\d){0,2}) like Mac OS X"
    )
    mac_token_pattern: Pattern = re.compile(r"Macintosh; (?P<mac_processor>.*?) Mac OS X 10_([5-9]|1[0-2])_(\d)")
    one_day = dt.timedelta(1.0)

    def test_android_platform_token(self, faker, num_samples):
        for _ in range(num_samples):
            match = self.android_token_pattern.fullmatch(faker.android_platform_token())
            assert match.group("android_version") in UaProvider.android_versions

    def test_ios_platform_token(self, faker, num_samples):
        for _ in range(num_samples):
            match = self.ios_token_pattern.fullmatch(faker.ios_platform_token())
            assert match.group("apple_device") in UaProvider.apple_devices
            assert match.group("ios_version").replace("_", ".") in UaProvider.ios_versions

    def test_mac_platform_token(self, faker, num_samples):
        for _ in range(num_samples):
            match = self.mac_token_pattern.fullmatch(faker.mac_platform_token())
            assert match.group("mac_processor") in UaProvider.mac_processors

    def test_firefox_deterministic_output(self, faker: Faker, num_samples: int) -> None:
        """Check whether ``faker.firefox()`` is deterministic, given the same seed."""

        for _ in range(num_samples):
            # GIVEN a (new) random seed
            seed = faker.random.random()

            # AND a DevOpsTester using a Faker instance seeded with this seed

            # It is a bit tricky to feed the faker with its own random
            # value, but it is sufficient for this particular test
            faker.seed_instance(seed)

            # AND the DevOpsTester using the fake library tomorrow
            with freeze_time(dt.datetime.now() + self.one_day):
                # AND the DevOpsTester requests a faked Mozilla Firefox web browser user agent (str)
                fake_firefox_ua_output_tomorrow = faker.firefox()

            # WHEN the DevOpsTester would use the fake library with the same seed
            faker.seed_instance(seed)

            # AND the DevOpsTester would use the fake library some time later
            with freeze_time(dt.datetime.max - self.one_day):
                # AND the DevOpsTester requests again faked Mozilla Firefox web browser user agent
                fake_firefox_ua_output_much_later = faker.firefox()

            # THEN the later Firefox U/A output should (always) be equal to the previous one
            assert fake_firefox_ua_output_much_later == fake_firefox_ua_output_tomorrow
