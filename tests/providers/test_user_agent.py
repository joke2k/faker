import re

from faker.providers.user_agent import Provider as UaProvider


class TestUserAgentProvider:
    """Test user agent provider methods"""
    num_samples = 1000
    android_token_pattern = re.compile(r'Android (?P<android_version>\d+(?:\.\d){0,2})')
    ios_token_pattern = re.compile(r'^(?P<apple_device>.*?); CPU \1 OS (?P<ios_version>\d+(?:_\d){0,2}) like Mac OS X')
    mac_token_pattern = re.compile(r'Macintosh; (?P<mac_processor>.*?) Mac OS X 10_([5-9]|1[0-2])_(\d)')

    def test_android_platform_token(self, faker, num_samples):
        for _ in range(num_samples):
            match = self.android_token_pattern.fullmatch(faker.android_platform_token())
            assert match.group('android_version') in UaProvider.android_versions

    def test_ios_platform_token(self, faker, num_samples):
        for _ in range(num_samples):
            match = self.ios_token_pattern.fullmatch(faker.ios_platform_token())
            assert match.group('apple_device') in UaProvider.apple_devices
            assert match.group('ios_version').replace('_', '.') in UaProvider.ios_versions

    def test_mac_platform_token(self, faker, num_samples):
        for _ in range(num_samples):
            match = self.mac_token_pattern.fullmatch(faker.mac_platform_token())
            assert match.group('mac_processor') in UaProvider.mac_processors
