import datetime

from typing import List, Optional

from ....typing import SexLiteral
from .. import Provider as SsnProvider


class Provider(SsnProvider):
    # Extracted from
    # https://en.wikipedia.org/wiki/Malaysian_identity_card
    place_of_birth_in_malaysia: dict[str] = {
        "johor": ["01", "21", "22", "23", "24"],
        "kedah": ["02", "25", "26", "27"],
        "kelantan": ["03", "28", "29"],
        "melaka": ["04", "30"],
        "nsembilan": ["05", "31", "59"],
        "pahang": ["06", "32", "33"],
        "penang": ["07", "35"],
        "perak": ["08", "36", "37", "38", "39"],
        "perlis": ["09", "40"],
        "selangor": ["10", "41", "42", "43", "44"],
        "terengganu": ["11", "45", "46"],
        "sabah": ["12", "47", "48", "49"],
        "sarawak": ["13", "50", "51", "52", "53"],
        "kl": ["14", "54", "55", "56", "57"],
        "labuan": ["15", "58"],
        "putrajaya": ["16"],
    }

    place_of_birth_outside_malaysia: dict[str] = {
        "brunei": ["60"],
        "indonesia": ["61"],
        "cambodia": ["62"],
        "democratic kampuchea": ["62"],
        "kampuchea": ["62"],
        "laos": ["63"],
        "myanmar": ["64"],
        "philippines": ["65"],
        "singapore": ["66"],
        "thailand": ["67"],
        "vietnam": ["68"],
        # Born outside malaysia before 2001
        "before_2001": ["71"],
        "china": ["74"],
        "india": ["75"],
        "pakistan": ["76"],
        "saudi arabia": ["77"],
        "sri lanka": ["78"],
        "bangladesh": ["79"],
        "unknown state": ["82"],
        # Asia Pasific: American Samoa / Australia / Christmas Island / Cocos (Keeling) Islands / Cook Islands / Fiji / French Polynesia / Guam / Heard Island and McDonald Islands / Marshall Islands / Micronesia / New Caledonia / New Zealand / Niue / Norfolk Island / Papua New Guinea / Timor Leste / Tokelau / United States Minor Outlying Islands / Wallis and Futuna Islands
        "asiap asific": ["83"],
        # South America: Anguilla / Argentina / Aruba / Bolivia / Brazil / Chile / Colombia / Ecuador / French Guinea / Guadeloupe / Guyana / Paraguay / Peru / South Georgia and the South Sandwich Islands / Suriname / Uruguay / Venezuela
        "south america": ["84"],
        # Africa: Algeria / Angola / Botswana / Burundi / Cameroon / Central African Republic / Chad / Congo-Brazzaville / Congo-Kinshasa / Djibouti / Egypt / Eritrea / Ethiopia / Gabon / Gambia / Ghana / Guinea / Kenya / Liberia / Malawi / Mali / Mauritania / Mayotte / Morocco / Mozambique / Namibia / Niger / Nigeria / Rwanda / Réunion / Senegal / Sierra Leone / Somalia / South Africa / Sudan / Swaziland / Tanzania / Togo / Tonga / Tunisia / Uganda / Western Sahara / Zaire / Zambia / Zimbabwe
        "africa": ["85"],
        # Europe: Armenia / Austria / Belgium / Cyprus / Denmark / Faroe Islands / France / Finland / Finland, Metropolitan / Germany / Germany, Democratic Republic / Germany, Federal Republic / Greece / Holy See (Vatican City) / Italy / Luxembourg / Malta / Mediterranean / Monaco / Netherlands / North Macedonia / Norway / Portugal / Republic of Moldova / Slovakia / Slovenia / Spain / Sweden / Switzerland / United Kingdom-Dependent Territories / United Kingdom-National Overseas / United Kingdom-Overseas Citizen / United Kingdom-Protected Person / United Kingdom-Subject
        "eorupe": ["86"],
        "britain": ["87"],
        "great britain": ["87"],
        "ireland": ["87"],
        # Middle East: Bahrain / Iran / Iraq / Palestine / Jordan / Kuwait / Lebanon / Oman / Qatar / Republic of Yemen / Syria / Turkey / United Arab Emirates / Yemen Arab Republic / Yemen People's Democratic Republic / Israel
        "middle east": ["88"],
        # Far East: Japan / North Korea / South Korea / Taiwan
        "far east": ["89"],
        # carribean: Bahamas / Barbados / Belize / Costa Rica / Cuba / Dominica / Dominican Republic / El Salvador / Grenada / Guatemala / Haiti / Honduras / Jamaica / Martinique / Mexico / Nicaragua / Panama / Puerto Rico / Saint Kitts and Nevis / Saint Lucia / Saint Vincent and the Grenadines / Trinidad and Tobago / Turks and Caicos Islands / Virgin Islands (USA)
        "caribbean": ["90"],
        # north america: Canada / Greenland / Netherlands Antilles / Saint Pierre and Miquelon / United States of America
        "north america": ["91"],
        # soviet union: Albania / Belarus / Bosnia and Herzegovina / Bulgaria / Byelorussia / Croatia / Czech Republic / Czechoslovakia / Estonia / Georgia / Hungary / Latvia / Lithuania / Montenegro / Poland / Republic of Kosovo / Romania / Russian Federation / Serbia / Ukraine
        "soviet union": ["92"],
        # Afghanistan / Andorra / Antarctica / Antigua and Barbuda / Azerbaijan / Benin / Bermuda / Bhutan / Bora Bora / Bouvet Island / British Indian Ocean Territory / Burkina Faso / Cape Verde / Cayman Islands / Comoros / Dahomey / Equatorial Guinea / Falkland Islands / French Southern Territories / Gibraltar / Guinea-Bissau / Hong Kong / Iceland / Ivory Coast / Kazakhstan / Kiribati / Kyrgyzstan / Lesotho / Libya / Liechtenstein / Macau / Madagascar / Maghribi / Malagasy / Maldives / Mauritius / Mongolia / Montserrat / Nauru / Nepal / Northern Marianas Islands / Outer Mongolia / Palau / Palestine / Pitcairn Islands / Saint Helena / Saint Lucia / Saint Vincent and the Grenadines / Samoa / San Marino / São Tomé and Príncipe / Seychelles / Solomon Islands / Svalbard and Jan Mayen Islands / Tajikistan / Turkmenistan / Tuvalu / Upper Volta / Uzbekistan / Vanuatu / Vatican City / Virgin Islands (British) / Western Samoa / Yugoslavia
        "": ["93"],
        # Stateless / Stateless Person Article 1/1954
        "stateless": ["98"],
        # Mecca / Neutral Zone / No Information / Refugee / Refugee Article 1/1951 / United Nations Specialized Agency / United Nations Organization / Unspecified Nationality
        "n/a": ["99"],
    }

    def ssn(
        self,
        date_of_birth=None,
        min_age: int = 18,
        max_age: int = 90,
        gender: Optional[SexLiteral] = None,
        state: str = None,
    ) -> str:
        """
        Return 12 character Malaysian Identification Card Number

        :param gender: F for female  M for male  None for default

        """
        if state:
            if state.lower() in self.place_of_birth_in_malaysia:
                state_code = self.generator.random.choice(self.place_of_birth_in_malaysia[state.lower()])
            else:
                state_list = ""
                for i in self.place_of_birth_in_malaysia.keys():
                    state_list += " " + i
                raise ValueError('Invalid state name: "' + state + '" available state name: ' + state_list)
        else:
            state, state_code_list = self.generator.random.choice(list(self.place_of_birth_in_malaysia.items()))
            state_code = self.generator.random.choice(state_code_list)

        if date_of_birth:
            birthday_str = date_of_birth.strftime("%y%m%d")
        else:
            age = datetime.timedelta(days=self.random_int(min_age * 365, max_age * 365))
            birthday = datetime.date.today() - age
            birthday_str = birthday.strftime("%y%m%d")

        _number = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        if gender:
            if gender in ("F", "f"):
                gender_num = self.generator.random.choice(_number[::2])
            elif gender in ("M", "m"):
                gender_num = self.generator.random.choice(_number[1::2])
            else:
                raise ValueError("Gender must be one of F or M.")
        else:
            gender_num = self.generator.random.choice(_number)

        ssn = birthday_str + state_code + str(self.random_int(0, 9)) + str(self.random_int(10, 99)) + str(gender_num)
        return ssn
