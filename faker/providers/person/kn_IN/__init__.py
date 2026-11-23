from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats_male = (
        "{{first_name_male}} {{last_name}}",
        "{{prefix_male}} {{first_name_male}} {{last_name}}",
    )

    formats_female = (
        "{{first_name_female}} {{last_name}}",
        "{{prefix_female}} {{first_name_female}} {{last_name}}",
    )

    formats = formats_male + formats_female

    # Source references (accessed 2026-11-23):
    # - https://www.behindthename.com/names/usage/kannada (given names)
    # - https://en.wikipedia.org/wiki/Category:Kannada-language_surnames (surnames)
    # Names are common, generic given names and family names written in Kannada script,
    # manually filtered for synthetic test-data suitability.

    first_names_female = (
        "ಅಕ್ಷತಾ",
        "ಅನಿತಾ",
        "ಅನುಷಾ",
        "ಅರ್ಚನಾ",
        "ಆಶಾ",
        "ಐಶ್ವರ್ಯ",
        "ಕವಿತಾ",
        "ಕಾವ್ಯ",
        "ಗಾಯತ್ರಿ",
        "ಗೀತಾ",
        "ಚೈತ್ರಾ",
        "ಜ್ಯೋತಿ",
        "ದಿವ್ಯ",
        "ದೀಪಾ",
        "ನಂದಿನಿ",
        "ನಯನಾ",
        "ಪದ್ಮಾ",
        "ಪವಿತ್ರಾ",
        "ಪೂಜಾ",
        "ಪ್ರಿಯಾ",
        "ಭಾರತಿ",
        "ಮಮತಾ",
        "ಮಾಲತಿ",
        "ಮೇಘನಾ",
        "ರಕ್ಷಿತಾ",
        "ರಂಜಿತಾ",
        "ರಮ್ಯಾ",
        "ರಶ್ಮಿ",
        "ರೇಖಾ",
        "ಲಕ್ಷ್ಮಿ",
        "ವಾಣಿ",
        "ವಿದ್ಯಾ",
        "ಶಾರದಾ",
        "ಶ್ರುತಿ",
        "ಸಹನಾ",
        "ಸುಧಾ",
        "ಸುಮಾ",
        "ಸೌಮ್ಯ",
        "ಸ್ಪಂದನಾ",
        "ಹೇಮಾ",
    )

    first_names_male = (
        "ಅನಿಲ್",
        "ಅಭಿಷೇಕ್",
        "ಅರುಣ್",
        "ಆನಂದ್",
        "ಉಮೇಶ್",
        "ಕಿರಣ್",
        "ಗಣೇಶ್",
        "ಗಿರೀಶ್",
        "ಚಂದ್ರಶೇಖರ್",
        "ದರ್ಶನ್",
        "ದೀಪಕ್",
        "ನಾಗರಾಜ್",
        "ನಿತಿನ್",
        "ಪುನೀತ್",
        "ಪ್ರಕಾಶ್",
        "ಪ್ರಜ್ವಲ್",
        "ಪ್ರವೀಣ್",
        "ಬಸವರಾಜ್",
        "ಮಂಜುನಾಥ್",
        "ಮಹೇಶ್",
        "ಮೋಹನ್",
        "ರಮೇಶ್",
        "ರವಿ",
        "ರಾಘವೇಂದ್ರ",
        "ರಾಜೇಶ್",
        "ರಾಹುಲ್",
        "ಲೋಕೇಶ್",
        "ವಸಂತ್",
        "ವಿನಯ್",
        "ವಿಶ್ವನಾಥ್",
        "ಶಿವಕುಮಾರ್",
        "ಶ್ರೀನಿವಾಸ್",
        "ಸಂತೋಷ್",
        "ಸಂದೀಪ್",
        "ಸತೀಶ್",
        "ಸುದೀಪ್",
        "ಸುರೇಶ್",
        "ಹರೀಶ್",
        "ಹನುಮಂತ",
    )

    first_names = first_names_female + first_names_male

    last_names = (
        "ಅಂಗಡಿ",
        "ಆಚಾರ್ಯ",
        "ಉಪಾಧ್ಯ",
        "ಕಾಮತ್",
        "ಕಾರಂತ",
        "ಕುಲಕರ್ಣಿ",
        "ಗೌಡ",
        "ಜೋಶಿ",
        "ದೇಶಪಾಂಡೆ",
        "ದೇಸಾಯಿ",
        "ನಾಯಕ್",
        "ಪಾಟೀಲ",
        "ಪೂಜಾರಿ",
        "ಪೈ",
        "ಪ್ರಭು",
        "ಬಂಗೇರ",
        "ಬಿರಾದಾರ",
        "ಭಟ್",
        "ಮಲ್ಯ",
        "ಮೂರ್ತಿ",
        "ರಾವ್",
        "ರೆಡ್ಡಿ",
        "ಶಾಸ್ತ್ರಿ",
        "ಶೆಟ್ಟಿ",
        "ಶೆಣೈ",
        "ಸುವರ್ಣ",
        "ಹಿರೇಮಠ",
        "ಹೆಗಡೆ",
        "ಹೆಬ್ಬಾರ್",
        "ಹೊಳ್ಳ",
    )

    prefixes_female = (
        "ಶ್ರೀಮತಿ",
        "ಕುಮಾರಿ",
    )

    prefixes_male = ("ಶ್ರೀ",)

    prefixes = prefixes_female + prefixes_male
