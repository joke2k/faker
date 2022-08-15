from typing import Dict, Optional, Tuple, Union

from .. import BaseProvider, ElementsType

localized = True


class Provider(BaseProvider):
    formats: ElementsType = ["{{first_name}} {{last_name}}"]

    first_names: ElementsType = ["John", "Jane"]

    last_names: ElementsType = ["Doe"]

    # https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
    language_names: ElementsType = [
        "Afar",
        "Abkhazian",
        "Avestan",
        "Afrikaans",
        "Akan",
        "Amharic",
        "Aragonese",
        "Arabic",
        "Assamese",
        "Avaric",
        "Aymara",
        "Azerbaijani",
        "Bashkir",
        "Belarusian",
        "Bulgarian",
        "Bihari languages",
        "Bislama",
        "Bambara",
        "Bengali",
        "Tibetan",
        "Breton",
        "Bosnian",
        "Catalan",
        "Chechen",
        "Chamorro",
        "Corsican",
        "Cree",
        "Czech",
        "Church Slavic",
        "Chuvash",
        "Welsh",
        "Danish",
        "German",
        "Divehi",
        "Dzongkha",
        "Ewe",
        "Greek",
        "English",
        "Esperanto",
        "Spanish",
        "Estonian",
        "Basque",
        "Persian",
        "Fulah",
        "Finnish",
        "Fijian",
        "Faroese",
        "French",
        "Western Frisian",
        "Irish",
        "Gaelic",
        "Galician",
        "Guarani",
        "Gujarati",
        "Manx",
        "Hausa",
        "Hebrew",
        "Hindi",
        "Hiri Motu",
        "Croatian",
        "Haitian",
        "Hungarian",
        "Armenian",
        "Herero",
        "Interlingua",
        "Indonesian",
        "Interlingue",
        "Igbo",
        "Sichuan Yi",
        "Inupiaq",
        "Ido",
        "Icelandic",
        "Italian",
        "Inuktitut",
        "Japanese",
        "Javanese",
        "Georgian",
        "Kongo",
        "Kikuyu",
        "Kuanyama",
        "Kazakh",
        "Kalaallisut",
        "Central Khmer",
        "Kannada",
        "Korean",
        "Kanuri",
        "Kashmiri",
        "Kurdish",
        "Komi",
        "Cornish",
        "Kirghiz",
        "Latin",
        "Luxembourgish",
        "Ganda",
        "Limburgan",
        "Lingala",
        "Lao",
        "Lithuanian",
        "Luba-Katanga",
        "Latvian",
        "Malagasy",
        "Marshallese",
        "Maori",
        "Macedonian",
        "Malayalam",
        "Mongolian",
        "Marathi",
        "Malay",
        "Maltese",
        "Burmese",
        "Nauru",
        "North Ndebele",
        "Nepali",
        "Ndonga",
        "Dutch",
        "Norwegian Nynorsk",
        "Norwegian",
        "South Ndebele",
        "Navajo",
        "Chichewa",
        "Occitan",
        "Ojibwa",
        "Oromo",
        "Oriya",
        "Ossetian",
        "Panjabi",
        "Pali",
        "Polish",
        "Pushto",
        "Portuguese",
        "Quechua",
        "Romansh",
        "Rundi",
        "Romanian",
        "Russian",
        "Kinyarwanda",
        "Sanskrit",
        "Sardinian",
        "Sindhi",
        "Northern Sami",
        "Sango",
        "Sinhala",
        "Slovak",
        "Slovenian",
        "Samoan",
        "Shona",
        "Somali",
        "Albanian",
        "Serbian",
        "Swati",
        "Sotho, Southern",
        "Sundanese",
        "Swedish",
        "Swahili",
        "Tamil",
        "Telugu",
        "Tajik",
        "Thai",
        "Tigrinya",
        "Turkmen",
        "Tagalog",
        "Tswana",
        "Tonga",
        "Turkish",
        "Tsonga",
        "Tatar",
        "Twi",
        "Tahitian",
        "Uighur",
        "Ukrainian",
        "Urdu",
        "Uzbek",
        "Venda",
        "Vietnamese",
        "Walloon",
        "Wolof",
        "Xhosa",
        "Yiddish",
        "Yoruba",
        "Zhuang",
        "Chinese",
        "Zulu",
    ]

    def name(self) -> str:
        """
        :example 'John Doe'
        """
        pattern: str = self.random_element(self.formats)
        return self.generator.parse(pattern)

    def first_name(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        return self.random_element(self.first_names, min_length, max_length)

    def first_name_as_list(self) -> Union[Tuple[str, ...], Dict[str, float], Dict[str, float]]:
        return self.first_names  # type: ignore[return-value]

    def last_name(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        return self.random_element(self.last_names, min_length, max_length)

    def last_name_as_list(self) -> Union[Tuple[str, ...], Dict[str, float], Dict[str, float]]:
        return self.last_names  # type: ignore[return-value]

    def name_male(self) -> str:
        if hasattr(self, "formats_male"):
            formats = self.formats_male  # type: ignore[attr-defined]
        else:
            formats = self.formats
        pattern: str = self.random_element(formats)
        return self.generator.parse(pattern)

    def name_nonbinary(self) -> str:
        if hasattr(self, "formats_nonbinary"):
            formats = self.formats_nonbinary  # type: ignore[attr-defined]
        else:
            formats = self.formats
        pattern: str = self.random_element(formats)
        return self.generator.parse(pattern)

    def name_female(self) -> str:
        if hasattr(self, "formats_female"):
            formats = self.formats_female  # type: ignore[attr-defined]
        else:
            formats = self.formats
        pattern: str = self.random_element(formats)
        return self.generator.parse(pattern)

    def first_name_male(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        if hasattr(self, "first_names_male"):
            return self.random_element(self.first_names_male, min_length, max_length)  # type: ignore[attr-defined]
        return self.first_name(min_length, max_length)

    def first_name_male_as_list(self) -> Union[Tuple[str, ...], Dict[str, float], Dict[str, float]]:
        if hasattr(self, "first_names_male"):
            return self.first_names_male  # type: ignore[attr-defined]
        return self.first_name_as_list()

    def first_name_nonbinary(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        if hasattr(self, "first_names_nonbinary"):
            return self.random_element(self.first_names_nonbinary, min_length, max_length)  # type: ignore[attr-defined]
        return self.first_name(min_length, max_length)

    def first_name_nonbinary_as_list(self) -> Union[Tuple[str, ...], Dict[str, float], Dict[str, float]]:
        if hasattr(self, "first_names_nonbinary"):
            return self.first_names_nonbinary  # type: ignore[attr-defined]
        return self.first_name_as_list()

    def first_name_female(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        if hasattr(self, "first_names_female"):
            return self.random_element(self.first_names_female, min_length, max_length)  # type: ignore[attr-defined]
        return self.first_name(min_length, max_length)

    def first_name_female_as_list(self) -> Union[Tuple[str, ...], Dict[str, float], Dict[str, float]]:
        if hasattr(self, "first_names_female"):
            return self.first_names_female  # type: ignore[attr-defined]
        return self.first_name_as_list()

    def last_name_male(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        if hasattr(self, "last_names_male"):
            return self.random_element(self.last_names_male, min_length, max_length)  # type: ignore[attr-defined]
        return self.last_name(min_length, max_length)

    def last_name_male_as_list(self) -> Union[Tuple[str, ...], Dict[str, float], Dict[str, float]]:
        if hasattr(self, "last_names_male"):
            return self.last_names_male  # type: ignore[attr-defined]
        return self.first_name_as_list()

    def last_name_nonbinary(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        if hasattr(self, "last_names_nonbinary"):
            return self.random_element(self.last_names_nonbinary, min_length, max_length)  # type: ignore[attr-defined]
        return self.last_name(min_length, max_length)

    def last_name_nonbinary_as_list(self) -> Union[Tuple[str, ...], Dict[str, float], Dict[str, float]]:
        if hasattr(self, "last_names_nonbinary"):
            return self.last_names_nonbinary  # type: ignore[attr-defined]
        return self.first_name_as_list()

    def last_name_female(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        if hasattr(self, "last_names_female"):
            return self.random_element(self.last_names_female, min_length, max_length)  # type: ignore[attr-defined]
        return self.last_name(min_length, max_length)

    def last_name_female_as_list(self) -> Union[Tuple[str, ...], Dict[str, float], Dict[str, float]]:
        if hasattr(self, "last_names_female"):
            return self.last_names_female  # type: ignore[attr-defined]
        return self.first_name_as_list()

    def prefix(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        if hasattr(self, "prefixes"):
            return self.random_element(self.prefixes, min_length, max_length)  # type: ignore[attr-defined]
        if hasattr(self, "prefixes_male") and hasattr(self, "prefixes_female") and hasattr(self, "prefixes_nonbinary"):
            prefixes = (
                tuple(self.prefixes_male)  # type: ignore[attr-defined]
                + tuple(self.prefixes_female)  # type: ignore[attr-defined]
                + tuple(self.prefixes_nonbinary)  # type: ignore[attr-defined]
            )
            return self.random_element(prefixes, min_length, max_length)
        if hasattr(self, "prefixes_male") and hasattr(self, "prefixes_female"):
            prefixes = tuple(self.prefixes_male) + tuple(self.prefixes_female)  # type: ignore[attr-defined]
            return self.random_element(prefixes, min_length, max_length)
        return ""

    def prefix_as_list(self) -> Union[Tuple[str, ...], Dict[str, float], Dict[str, float]]:
        if hasattr(self, "prefixes"):
            return self.prefixes  # type: ignore[attr-defined]
        if hasattr(self, "prefixes_male") and hasattr(self, "prefixes_female") and hasattr(self, "prefixes_nonbinary"):
            prefixes = (
                tuple(self.prefixes_male)  # type: ignore[attr-defined]
                + tuple(self.prefixes_female)  # type: ignore[attr-defined]
                + tuple(self.prefixes_nonbinary)  # type: ignore[attr-defined]
            )
            return prefixes
        if hasattr(self, "prefixes_male") and hasattr(self, "prefixes_female"):
            prefixes = tuple(self.prefixes_male) + tuple(self.prefixes_female)  # type: ignore[attr-defined]
            return prefixes
        return ()

    def prefix_male(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        if hasattr(self, "prefixes_male"):
            return self.random_element(self.prefixes_male, min_length, max_length)  # type: ignore[attr-defined]
        return self.prefix(min_length, max_length)

    def prefix_male_as_list(self) -> Union[Tuple[str, ...], Dict[str, float], Dict[str, float]]:
        if hasattr(self, "prefixes_male"):
            return self.prefixes_male  # type: ignore[attr-defined]
        return self.prefix_as_list()

    def prefix_nonbinary(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        if hasattr(self, "prefixes_nonbinary"):
            return self.random_element(self.prefixes_nonbinary, min_length, max_length)  # type: ignore[attr-defined]
        return self.prefix(min_length, max_length)

    def prefix_nonbinary_as_list(self) -> Union[Tuple[str, ...], Dict[str, float], Dict[str, float]]:
        if hasattr(self, "prefixes_nonbinary"):
            return self.prefixes_nonbinary  # type: ignore[attr-defined]
        return self.prefix_as_list()

    def prefix_female(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        if hasattr(self, "prefixes_female"):
            return self.random_element(self.prefixes_female, min_length, max_length)  # type: ignore[attr-defined]
        return self.prefix(min_length, max_length)

    def prefix_female_as_list(self) -> Union[Tuple[str, ...], Dict[str, float], Dict[str, float]]:
        if hasattr(self, "prefixes_female"):
            return self.prefixes_female  # type: ignore[attr-defined]
        return self.prefix_as_list()

    def suffix(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        if hasattr(self, "suffixes"):
            return self.random_element(self.suffixes, min_length, max_length)  # type: ignore[attr-defined]
        if hasattr(self, "suffixes_male") and hasattr(self, "suffixes_female") and hasattr(self, "suffixes_nonbinary"):
            suffixes = (
                tuple(self.suffixes_male)  # type: ignore[attr-defined]
                + tuple(self.suffixes_female)  # type: ignore[attr-defined]
                + tuple(self.suffixes_nonbinary)  # type: ignore[attr-defined]
            )
            return self.random_element(suffixes, min_length, max_length)
        if hasattr(self, "suffixes_male") and hasattr(self, "suffixes_female"):
            suffixes = tuple(self.suffixes_male) + tuple(self.suffixes_female)  # type: ignore[attr-defined]
            return self.random_element(suffixes, min_length, max_length)
        return ""

    def suffix_as_list(self) -> Union[Tuple[str, ...], Dict[str, float], Dict[str, float]]:
        if hasattr(self, "suffixes"):
            return self.suffixes  # type: ignore[attr-defined]
        if hasattr(self, "suffixes_male") and hasattr(self, "suffixes_female") and hasattr(self, "suffixes_nonbinary"):
            suffixes = (
                tuple(self.suffixes_male)  # type: ignore[attr-defined]
                + tuple(self.suffixes_female)  # type: ignore[attr-defined]
                + tuple(self.suffixes_nonbinary)  # type: ignore[attr-defined]
            )
            return suffixes
        if hasattr(self, "suffixes_male") and hasattr(self, "suffixes_female"):
            suffixes = tuple(self.suffixes_male) + tuple(self.suffixes_female)  # type: ignore[attr-defined]
            return suffixes
        return ()

    def suffix_male(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        if hasattr(self, "suffixes_male"):
            return self.random_element(self.suffixes_male, min_length, max_length)  # type: ignore[attr-defined]
        return self.suffix(min_length, max_length)

    def suffix_male_as_list(self) -> Union[Tuple[str, ...], Dict[str, float], Dict[str, float]]:
        if hasattr(self, "suffixes_male"):
            return self.suffixes_male  # type: ignore[attr-defined]
        return self.suffix_as_list()

    def suffix_nonbinary(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        if hasattr(self, "suffixes_nonbinary"):
            return self.random_element(self.suffixes_nonbinary, min_length, max_length)  # type: ignore[attr-defined]
        return self.suffix(min_length, max_length)

    def suffix_nonbinary_as_list(self) -> Union[Tuple[str, ...], Dict[str, float], Dict[str, float]]:
        if hasattr(self, "suffixes_nonbinary"):
            return self.suffixes_nonbinary  # type: ignore[attr-defined]
        return self.suffix_as_list()

    def suffix_female(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        if hasattr(self, "suffixes_female"):
            return self.random_element(self.suffixes_female, min_length, max_length)  # type: ignore[attr-defined]
        return self.suffix(min_length, max_length)

    def suffix_female_as_list(self) -> Union[Tuple[str, ...], Dict[str, float], Dict[str, float]]:
        if hasattr(self, "suffixes_female"):
            return self.suffixes_female  # type: ignore[attr-defined]
        return self.suffix_as_list()

    def language_name(self, min_length: Optional[int] = None, max_length: Optional[int] = None) -> str:
        """Generate a random i18n language name (e.g. English)."""
        return self.random_element(self.language_names, min_length, max_length)
