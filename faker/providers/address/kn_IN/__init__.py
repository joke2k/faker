from .. import Provider as AddressProvider


class Provider(AddressProvider):
    city_formats = ("{{city_name}}",)

    street_name_formats = (
        "{{first_name}} {{street_suffix}}",
        "{{last_name}} {{street_suffix}}",
    )

    street_address_formats = (
        "{{building_number}}, {{street_name}}",
        "{{building_number}}, %ನೇ ಅಡ್ಡರಸ್ತೆ, {{street_name}}",
    )

    # All cities below are in Karnataka, so full addresses name Karnataka as the state.
    address_formats = (
        "{{street_address}}\n{{city}} - {{postcode}}",
        "{{street_address}}\n{{city}} - {{postcode}}, ಕರ್ನಾಟಕ",
    )

    building_number_formats = (
        "#",
        "##",
        "###",
        "#/#",
        "##/#",
    )

    # Karnataka PIN codes fall in the 560xxx-591xxx range (India Post, Karnataka postal circle).
    postcode_formats = (
        "56####",
        "57####",
        "58####",
        "590###",
        "591###",
    )

    street_suffixes = (
        "ರಸ್ತೆ",
        "ಮುಖ್ಯರಸ್ತೆ",
        "ನಗರ",
        "ಬಡಾವಣೆ",
        "ಲೇಔಟ್",
        "ವೃತ್ತ",
    )

    # Source references (accessed 2026-11-23):
    # - https://en.wikipedia.org/wiki/List_of_cities_in_Karnataka_by_population (cities)
    # - https://www.indiapost.gov.in/ (Karnataka postal circle PIN code range)
    # - https://github.com/unicode-org/cldr-json/blob/main/cldr-json/cldr-localenames-full/main/kn/territories.json
    #   (Kannada territory/country names)
    # Data is manually filtered and normalized for Faker synthetic generation.

    cities = (
        "ಉಡುಪಿ",
        "ಕಲಬುರಗಿ",
        "ಕಾರವಾರ",
        "ಕೊಪ್ಪಳ",
        "ಕೋಲಾರ",
        "ಗದಗ",
        "ಚಾಮರಾಜನಗರ",
        "ಚಿಕ್ಕಬಳ್ಳಾಪುರ",
        "ಚಿಕ್ಕಮಗಳೂರು",
        "ಚಿತ್ರದುರ್ಗ",
        "ತುಮಕೂರು",
        "ದಾವಣಗೆರೆ",
        "ಧಾರವಾಡ",
        "ಬಳ್ಳಾರಿ",
        "ಬಾಗಲಕೋಟೆ",
        "ಬೀದರ್",
        "ಬೆಂಗಳೂರು",
        "ಬೆಳಗಾವಿ",
        "ಭದ್ರಾವತಿ",
        "ಮಂಗಳೂರು",
        "ಮಂಡ್ಯ",
        "ಮಡಿಕೇರಿ",
        "ಮೈಸೂರು",
        "ಯಾದಗಿರಿ",
        "ರಾಮನಗರ",
        "ರಾಯಚೂರು",
        "ವಿಜಯಪುರ",
        "ಶಿವಮೊಗ್ಗ",
        "ಹಾವೇರಿ",
        "ಹಾಸನ",
        "ಹುಬ್ಬಳ್ಳಿ",
        "ಹೊಸಪೇಟೆ",
    )

    states = (
        "ಅರುಣಾಚಲ ಪ್ರದೇಶ",
        "ಅಸ್ಸಾಂ",
        "ಆಂಧ್ರ ಪ್ರದೇಶ",
        "ಉತ್ತರ ಪ್ರದೇಶ",
        "ಉತ್ತರಾಖಂಡ",
        "ಒಡಿಶಾ",
        "ಕರ್ನಾಟಕ",
        "ಕೇರಳ",
        "ಗುಜರಾತ್",
        "ಗೋವಾ",
        "ಛತ್ತೀಸಗಢ",
        "ಜಾರ್ಖಂಡ್",
        "ತಮಿಳುನಾಡು",
        "ತೆಲಂಗಾಣ",
        "ತ್ರಿಪುರ",
        "ನಾಗಾಲ್ಯಾಂಡ್",
        "ಪಂಜಾಬ್",
        "ಪಶ್ಚಿಮ ಬಂಗಾಳ",
        "ಬಿಹಾರ",
        "ಮಣಿಪುರ",
        "ಮಧ್ಯ ಪ್ರದೇಶ",
        "ಮಹಾರಾಷ್ಟ್ರ",
        "ಮಿಜೋರಾಂ",
        "ಮೇಘಾಲಯ",
        "ರಾಜಸ್ಥಾನ",
        "ಸಿಕ್ಕಿಂ",
        "ಹರಿಯಾಣ",
        "ಹಿಮಾಚಲ ಪ್ರದೇಶ",
    )

    countries = (
        "ಆಸ್ಟ್ರೇಲಿಯಾ",
        "ಇಟಲಿ",
        "ಕೆನಡಾ",
        "ಚೀನಾ",
        "ಜಪಾನ್",
        "ಜರ್ಮನಿ",
        "ನೇಪಾಳ",
        "ಪಾಕಿಸ್ತಾನ",
        "ಫ್ರಾನ್ಸ್",
        "ಬಾಂಗ್ಲಾದೇಶ",
        "ಭಾರತ",
        "ಭೂತಾನ್",
        "ರಷ್ಯಾ",
        "ಶ್ರೀಲಂಕಾ",
        "ಸಿಂಗಾಪುರ",
    )

    def city_name(self) -> str:
        return self.random_element(self.cities)

    def street_address(self) -> str:
        # Numerify after parsing so formats can include a cross-road number ("%ನೇ ಅಡ್ಡರಸ್ತೆ" = "Nth cross"),
        # a common part of addresses in Karnataka.
        pattern: str = self.random_element(self.street_address_formats)
        return self.numerify(self.generator.parse(pattern))

    def administrative_unit(self) -> str:
        return self.random_element(self.states)

    state = administrative_unit
