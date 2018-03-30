# coding=utf-8

from __future__ import unicode_literals

import re

from calendar import timegm
from datetime import timedelta
from time import time

from dateutil import relativedelta
from dateutil.tz import tzlocal, tzutc

from faker.utils.datetime_safe import date, datetime, real_date, real_datetime
from faker.utils import is_string

from .. import BaseProvider

localized = True


def datetime_to_timestamp(dt):
    if getattr(dt, 'tzinfo', None) is not None:
        dt = dt.astimezone(tzutc())
    return timegm(dt.timetuple())


def timestamp_to_datetime(timestamp, tzinfo):
    if tzinfo is None:
        pick = datetime.fromtimestamp(timestamp, tzlocal())
        pick = pick.astimezone(tzutc()).replace(tzinfo=None)
    else:
        pick = datetime.fromtimestamp(timestamp, tzinfo)

    return pick


class ParseError(ValueError):
    pass


timedelta_pattern = r''
for name, sym in [('years', 'y'), ('weeks', 'w'), ('days', 'd'),
                  ('hours', 'h'), ('minutes', 'm'), ('seconds', 's')]:
    timedelta_pattern += r'((?P<{0}>(?:\+|-)\d+?){1})?'.format(name, sym)


class Provider(BaseProvider):
    centuries = [
        'I',
        'II',
        'III',
        'IV',
        'V',
        'VI',
        'VII',
        'VIII',
        'IX',
        'X',
        'XI',
        'XII',
        'XIII',
        'XIV',
        'XV',
        'XVI',
        'XVII',
        'XVIII',
        'XIX',
        'XX',
        'XXI']

    countries = [{'timezones': ['Europe/Andorra'],
                  'code': 'AD',
                  'continent': 'Europe',
                  'name': 'Andorra',
                  'capital': 'Andorra la Vella'},
                 {'timezones': ['Asia/Kabul'],
                  'code': 'AF',
                  'continent': 'Asia',
                  'name': 'Afghanistan',
                  'capital': 'Kabul'},
                 {'timezones': ['America/Antigua'],
                  'code': 'AG',
                  'continent': 'North America',
                  'name': 'Antigua and Barbuda',
                  'capital': "St. John's"},
                 {'timezones': ['Europe/Tirane'],
                  'code': 'AL',
                  'continent': 'Europe',
                  'name': 'Albania',
                  'capital': 'Tirana'},
                 {'timezones': ['Asia/Yerevan'],
                  'code': 'AM',
                  'continent': 'Asia',
                  'name': 'Armenia',
                  'capital': 'Yerevan'},
                 {'timezones': ['Africa/Luanda'],
                  'code': 'AO',
                  'continent': 'Africa',
                  'name': 'Angola',
                  'capital': 'Luanda'},
                 {'timezones': ['America/Argentina/Buenos_Aires',
                                'America/Argentina/Cordoba',
                                'America/Argentina/Jujuy',
                                'America/Argentina/Tucuman',
                                'America/Argentina/Catamarca',
                                'America/Argentina/La_Rioja',
                                'America/Argentina/San_Juan',
                                'America/Argentina/Mendoza',
                                'America/Argentina/Rio_Gallegos',
                                'America/Argentina/Ushuaia'],
                  'code': 'AR',
                  'continent': 'South America',
                  'name': 'Argentina',
                  'capital': 'Buenos Aires'},
                 {'timezones': ['Europe/Vienna'],
                  'code': 'AT',
                  'continent': 'Europe',
                  'name': 'Austria',
                  'capital': 'Vienna'},
                 {'timezones': ['Australia/Lord_Howe',
                                'Australia/Hobart',
                                'Australia/Currie',
                                'Australia/Melbourne',
                                'Australia/Sydney',
                                'Australia/Broken_Hill',
                                'Australia/Brisbane',
                                'Australia/Lindeman',
                                'Australia/Adelaide',
                                'Australia/Darwin',
                                'Australia/Perth'],
                  'code': 'AU',
                  'continent': 'Oceania',
                  'name': 'Australia',
                  'capital': 'Canberra'},
                 {'timezones': ['Asia/Baku'],
                  'code': 'AZ',
                  'continent': 'Asia',
                  'name': 'Azerbaijan',
                  'capital': 'Baku'},
                 {'timezones': ['America/Barbados'],
                  'code': 'BB',
                  'continent': 'North America',
                  'name': 'Barbados',
                  'capital': 'Bridgetown'},
                 {'timezones': ['Asia/Dhaka'],
                  'code': 'BD',
                  'continent': 'Asia',
                  'name': 'Bangladesh',
                  'capital': 'Dhaka'},
                 {'timezones': ['Europe/Brussels'],
                  'code': 'BE',
                  'continent': 'Europe',
                  'name': 'Belgium',
                  'capital': 'Brussels'},
                 {'timezones': ['Africa/Ouagadougou'],
                  'code': 'BF',
                  'continent': 'Africa',
                  'name': 'Burkina Faso',
                  'capital': 'Ouagadougou'},
                 {'timezones': ['Europe/Sofia'],
                  'code': 'BG',
                  'continent': 'Europe',
                  'name': 'Bulgaria',
                  'capital': 'Sofia'},
                 {'timezones': ['Asia/Bahrain'],
                  'code': 'BH',
                  'continent': 'Asia',
                  'name': 'Bahrain',
                  'capital': 'Manama'},
                 {'timezones': ['Africa/Bujumbura'],
                  'code': 'BI',
                  'continent': 'Africa',
                  'name': 'Burundi',
                  'capital': 'Bujumbura'},
                 {'timezones': ['Africa/Porto-Novo'],
                  'code': 'BJ',
                  'continent': 'Africa',
                  'name': 'Benin',
                  'capital': 'Porto-Novo'},
                 {'timezones': ['Asia/Brunei'],
                  'code': 'BN',
                  'continent': 'Asia',
                  'name': 'Brunei Darussalam',
                  'capital': 'Bandar Seri Begawan'},
                 {'timezones': ['America/La_Paz'],
                  'code': 'BO',
                  'continent': 'South America',
                  'name': 'Bolivia',
                  'capital': 'Sucre'},
                 {'timezones': ['America/Noronha',
                                'America/Belem',
                                'America/Fortaleza',
                                'America/Recife',
                                'America/Araguaina',
                                'America/Maceio',
                                'America/Bahia',
                                'America/Sao_Paulo',
                                'America/Campo_Grande',
                                'America/Cuiaba',
                                'America/Porto_Velho',
                                'America/Boa_Vista',
                                'America/Manaus',
                                'America/Eirunepe',
                                'America/Rio_Branco'],
                  'code': 'BR',
                  'continent': 'South America',
                  'name': 'Brazil',
                  'capital': 'Bras\xc3\xadlia'},
                 {'timezones': ['America/Nassau'],
                  'code': 'BS',
                  'continent': 'North America',
                  'name': 'Bahamas',
                  'capital': 'Nassau'},
                 {'timezones': ['Asia/Thimphu'],
                  'code': 'BT',
                  'continent': 'Asia',
                  'name': 'Bhutan',
                  'capital': 'Thimphu'},
                 {'timezones': ['Africa/Gaborone'],
                  'code': 'BW',
                  'continent': 'Africa',
                  'name': 'Botswana',
                  'capital': 'Gaborone'},
                 {'timezones': ['Europe/Minsk'],
                  'code': 'BY',
                  'continent': 'Europe',
                  'name': 'Belarus',
                  'capital': 'Minsk'},
                 {'timezones': ['America/Belize'],
                  'code': 'BZ',
                  'continent': 'North America',
                  'name': 'Belize',
                  'capital': 'Belmopan'},
                 {'timezones': ['America/St_Johns',
                                'America/Halifax',
                                'America/Glace_Bay',
                                'America/Moncton',
                                'America/Goose_Bay',
                                'America/Blanc-Sablon',
                                'America/Montreal',
                                'America/Toronto',
                                'America/Nipigon',
                                'America/Thunder_Bay',
                                'America/Pangnirtung',
                                'America/Iqaluit',
                                'America/Atikokan',
                                'America/Rankin_Inlet',
                                'America/Winnipeg',
                                'America/Rainy_River',
                                'America/Cambridge_Bay',
                                'America/Regina',
                                'America/Swift_Current',
                                'America/Edmonton',
                                'America/Yellowknife',
                                'America/Inuvik',
                                'America/Dawson_Creek',
                                'America/Vancouver',
                                'America/Whitehorse',
                                'America/Dawson'],
                  'code': 'CA',
                  'continent': 'North America',
                  'name': 'Canada',
                  'capital': 'Ottawa'},
                 {'timezones': ['Africa/Kinshasa',
                                'Africa/Lubumbashi'],
                  'code': 'CD',
                  'continent': 'Africa',
                  'name': 'Democratic Republic of the Congo',
                  'capital': 'Kinshasa'},
                 {'timezones': ['Africa/Brazzaville'],
                  'code': 'CG',
                  'continent': 'Africa',
                  'name': 'Republic of the Congo',
                  'capital': 'Brazzaville'},
                 {'timezones': ['Africa/Abidjan'],
                  'code': 'CI',
                  'continent': 'Africa',
                  'name': "C\xc3\xb4te d'Ivoire",
                  'capital': 'Yamoussoukro'},
                 {'timezones': ['America/Santiago',
                                'Pacific/Easter'],
                  'code': 'CL',
                  'continent': 'South America',
                  'name': 'Chile',
                  'capital': 'Santiago'},
                 {'timezones': ['Africa/Douala'],
                  'code': 'CM',
                  'continent': 'Africa',
                  'name': 'Cameroon',
                  'capital': 'Yaound\xc3\xa9'},
                 {'timezones': ['Asia/Shanghai',
                                'Asia/Harbin',
                                'Asia/Chongqing',
                                'Asia/Urumqi',
                                'Asia/Kashgar'],
                  'code': 'CN',
                  'continent': 'Asia',
                  'name': "People's Republic of China",
                  'capital': 'Beijing'},
                 {'timezones': ['America/Bogota'],
                  'code': 'CO',
                  'continent': 'South America',
                  'name': 'Colombia',
                  'capital': 'Bogot\xc3\xa1'},
                 {'timezones': ['America/Costa_Rica'],
                  'code': 'CR',
                  'continent': 'North America',
                  'name': 'Costa Rica',
                  'capital': 'San Jos\xc3\xa9'},
                 {'timezones': ['America/Havana'],
                  'code': 'CU',
                  'continent': 'North America',
                  'name': 'Cuba',
                  'capital': 'Havana'},
                 {'timezones': ['Atlantic/Cape_Verde'],
                  'code': 'CV',
                  'continent': 'Africa',
                  'name': 'Cape Verde',
                  'capital': 'Praia'},
                 {'timezones': ['Asia/Nicosia'],
                  'code': 'CY',
                  'continent': 'Asia',
                  'name': 'Cyprus',
                  'capital': 'Nicosia'},
                 {'timezones': ['Europe/Prague'],
                  'code': 'CZ',
                  'continent': 'Europe',
                  'name': 'Czech Republic',
                  'capital': 'Prague'},
                 {'timezones': ['Europe/Berlin'],
                  'code': 'DE',
                  'continent': 'Europe',
                  'name': 'Germany',
                  'capital': 'Berlin'},
                 {'timezones': ['Africa/Djibouti'],
                  'code': 'DJ',
                  'continent': 'Africa',
                  'name': 'Djibouti',
                  'capital': 'Djibouti City'},
                 {'timezones': ['Europe/Copenhagen'],
                  'code': 'DK',
                  'continent': 'Europe',
                  'name': 'Denmark',
                  'capital': 'Copenhagen'},
                 {'timezones': ['America/Dominica'],
                  'code': 'DM',
                  'continent': 'North America',
                  'name': 'Dominica',
                  'capital': 'Roseau'},
                 {'timezones': ['America/Santo_Domingo'],
                  'code': 'DO',
                  'continent': 'North America',
                  'name': 'Dominican Republic',
                  'capital': 'Santo Domingo'},
                 {'timezones': ['America/Guayaquil',
                                'Pacific/Galapagos'],
                  'code': 'EC',
                  'continent': 'South America',
                  'name': 'Ecuador',
                  'capital': 'Quito'},
                 {'timezones': ['Europe/Tallinn'],
                  'code': 'EE',
                  'continent': 'Europe',
                  'name': 'Estonia',
                  'capital': 'Tallinn'},
                 {'timezones': ['Africa/Cairo'],
                  'code': 'EG',
                  'continent': 'Africa',
                  'name': 'Egypt',
                  'capital': 'Cairo'},
                 {'timezones': ['Africa/Asmera'],
                  'code': 'ER',
                  'continent': 'Africa',
                  'name': 'Eritrea',
                  'capital': 'Asmara'},
                 {'timezones': ['Africa/Addis_Ababa'],
                  'code': 'ET',
                  'continent': 'Africa',
                  'name': 'Ethiopia',
                  'capital': 'Addis Ababa'},
                 {'timezones': ['Europe/Helsinki'],
                  'code': 'FI',
                  'continent': 'Europe',
                  'name': 'Finland',
                  'capital': 'Helsinki'},
                 {'timezones': ['Pacific/Fiji'],
                  'code': 'FJ',
                  'continent': 'Oceania',
                  'name': 'Fiji',
                  'capital': 'Suva'},
                 {'timezones': ['Europe/Paris'],
                  'code': 'FR',
                  'continent': 'Europe',
                  'name': 'France',
                  'capital': 'Paris'},
                 {'timezones': ['Africa/Libreville'],
                  'code': 'GA',
                  'continent': 'Africa',
                  'name': 'Gabon',
                  'capital': 'Libreville'},
                 {'timezones': ['Asia/Tbilisi'],
                  'code': 'GE',
                  'continent': 'Asia',
                  'name': 'Georgia',
                  'capital': 'Tbilisi'},
                 {'timezones': ['Africa/Accra'],
                  'code': 'GH',
                  'continent': 'Africa',
                  'name': 'Ghana',
                  'capital': 'Accra'},
                 {'timezones': ['Africa/Banjul'],
                  'code': 'GM',
                  'continent': 'Africa',
                  'name': 'The Gambia',
                  'capital': 'Banjul'},
                 {'timezones': ['Africa/Conakry'],
                  'code': 'GN',
                  'continent': 'Africa',
                  'name': 'Guinea',
                  'capital': 'Conakry'},
                 {'timezones': ['Europe/Athens'],
                  'code': 'GR',
                  'continent': 'Europe',
                  'name': 'Greece',
                  'capital': 'Athens'},
                 {'timezones': ['America/Guatemala'],
                  'code': 'GT',
                  'continent': 'North America',
                  'name': 'Guatemala',
                  'capital': 'Guatemala City'},
                 {'timezones': ['America/Guatemala'],
                  'code': 'GT',
                  'continent': 'North America',
                  'name': 'Haiti',
                  'capital': 'Port-au-Prince'},
                 {'timezones': ['Africa/Bissau'],
                  'code': 'GW',
                  'continent': 'Africa',
                  'name': 'Guinea-Bissau',
                  'capital': 'Bissau'},
                 {'timezones': ['America/Guyana'],
                  'code': 'GY',
                  'continent': 'South America',
                  'name': 'Guyana',
                  'capital': 'Georgetown'},
                 {'timezones': ['America/Tegucigalpa'],
                  'code': 'HN',
                  'continent': 'North America',
                  'name': 'Honduras',
                  'capital': 'Tegucigalpa'},
                 {'timezones': ['Europe/Budapest'],
                  'code': 'HU',
                  'continent': 'Europe',
                  'name': 'Hungary',
                  'capital': 'Budapest'},
                 {'timezones': ['Asia/Jakarta',
                                'Asia/Pontianak',
                                'Asia/Makassar',
                                'Asia/Jayapura'],
                  'code': 'ID',
                  'continent': 'Asia',
                  'name': 'Indonesia',
                  'capital': 'Jakarta'},
                 {'timezones': ['Europe/Dublin'],
                  'code': 'IE',
                  'continent': 'Europe',
                  'name': 'Republic of Ireland',
                  'capital': 'Dublin'},
                 {'timezones': ['Asia/Jerusalem'],
                  'code': 'IL',
                  'continent': 'Asia',
                  'name': 'Israel',
                  'capital': 'Jerusalem'},
                 {'timezones': ['Asia/Calcutta'],
                  'code': 'IN',
                  'continent': 'Asia',
                  'name': 'India',
                  'capital': 'New Delhi'},
                 {'timezones': ['Asia/Baghdad'],
                  'code': 'IQ',
                  'continent': 'Asia',
                  'name': 'Iraq',
                  'capital': 'Baghdad'},
                 {'timezones': ['Asia/Tehran'],
                  'code': 'IR',
                  'continent': 'Asia',
                  'name': 'Iran',
                  'capital': 'Tehran'},
                 {'timezones': ['Atlantic/Reykjavik'],
                  'code': 'IS',
                  'continent': 'Europe',
                  'name': 'Iceland',
                  'capital': 'Reykjav\xc3\xadk'},
                 {'timezones': ['Europe/Rome'],
                  'code': 'IT',
                  'continent': 'Europe',
                  'name': 'Italy',
                  'capital': 'Rome'},
                 {'timezones': ['America/Jamaica'],
                  'code': 'JM',
                  'continent': 'North America',
                  'name': 'Jamaica',
                  'capital': 'Kingston'},
                 {'timezones': ['Asia/Amman'],
                  'code': 'JO',
                  'continent': 'Asia',
                  'name': 'Jordan',
                  'capital': 'Amman'},
                 {'timezones': ['Asia/Tokyo'],
                  'code': 'JP',
                  'continent': 'Asia',
                  'name': 'Japan',
                  'capital': 'Tokyo'},
                 {'timezones': ['Africa/Nairobi'],
                  'code': 'KE',
                  'continent': 'Africa',
                  'name': 'Kenya',
                  'capital': 'Nairobi'},
                 {'timezones': ['Asia/Bishkek'],
                  'code': 'KG',
                  'continent': 'Asia',
                  'name': 'Kyrgyzstan',
                  'capital': 'Bishkek'},
                 {'timezones': ['Pacific/Tarawa',
                                'Pacific/Enderbury',
                                'Pacific/Kiritimati'],
                  'code': 'KI',
                  'continent': 'Oceania',
                  'name': 'Kiribati',
                  'capital': 'Tarawa'},
                 {'timezones': ['Asia/Pyongyang'],
                  'code': 'KP',
                  'continent': 'Asia',
                  'name': 'North Korea',
                  'capital': 'Pyongyang'},
                 {'timezones': ['Asia/Seoul'],
                  'code': 'KR',
                  'continent': 'Asia',
                  'name': 'South Korea',
                  'capital': 'Seoul'},
                 {'timezones': ['Asia/Kuwait'],
                  'code': 'KW',
                  'continent': 'Asia',
                  'name': 'Kuwait',
                  'capital': 'Kuwait City'},
                 {'timezones': ['Asia/Beirut'],
                  'code': 'LB',
                  'continent': 'Asia',
                  'name': 'Lebanon',
                  'capital': 'Beirut'},
                 {'timezones': ['Europe/Vaduz'],
                  'code': 'LI',
                  'continent': 'Europe',
                  'name': 'Liechtenstein',
                  'capital': 'Vaduz'},
                 {'timezones': ['Africa/Monrovia'],
                  'code': 'LR',
                  'continent': 'Africa',
                  'name': 'Liberia',
                  'capital': 'Monrovia'},
                 {'timezones': ['Africa/Maseru'],
                  'code': 'LS',
                  'continent': 'Africa',
                  'name': 'Lesotho',
                  'capital': 'Maseru'},
                 {'timezones': ['Europe/Vilnius'],
                  'code': 'LT',
                  'continent': 'Europe',
                  'name': 'Lithuania',
                  'capital': 'Vilnius'},
                 {'timezones': ['Europe/Luxembourg'],
                  'code': 'LU',
                  'continent': 'Europe',
                  'name': 'Luxembourg',
                  'capital': 'Luxembourg City'},
                 {'timezones': ['Europe/Riga'],
                  'code': 'LV',
                  'continent': 'Europe',
                  'name': 'Latvia',
                  'capital': 'Riga'},
                 {'timezones': ['Africa/Tripoli'],
                  'code': 'LY',
                  'continent': 'Africa',
                  'name': 'Libya',
                  'capital': 'Tripoli'},
                 {'timezones': ['Indian/Antananarivo'],
                  'code': 'MG',
                  'continent': 'Africa',
                  'name': 'Madagascar',
                  'capital': 'Antananarivo'},
                 {'timezones': ['Pacific/Majuro',
                                'Pacific/Kwajalein'],
                  'code': 'MH',
                  'continent': 'Oceania',
                  'name': 'Marshall Islands',
                  'capital': 'Majuro'},
                 {'timezones': ['Europe/Skopje'],
                  'code': 'MK',
                  'continent': 'Europe',
                  'name': 'Macedonia',
                  'capital': 'Skopje'},
                 {'timezones': ['Africa/Bamako'],
                  'code': 'ML',
                  'continent': 'Africa',
                  'name': 'Mali',
                  'capital': 'Bamako'},
                 {'timezones': ['Asia/Rangoon'],
                  'code': 'MM',
                  'continent': 'Asia',
                  'name': 'Myanmar',
                  'capital': 'Naypyidaw'},
                 {'timezones': ['Asia/Ulaanbaatar',
                                'Asia/Hovd',
                                'Asia/Choibalsan'],
                  'code': 'MN',
                  'continent': 'Asia',
                  'name': 'Mongolia',
                  'capital': 'Ulaanbaatar'},
                 {'timezones': ['Africa/Nouakchott'],
                  'code': 'MR',
                  'continent': 'Africa',
                  'name': 'Mauritania',
                  'capital': 'Nouakchott'},
                 {'timezones': ['Europe/Malta'],
                  'code': 'MT',
                  'continent': 'Europe',
                  'name': 'Malta',
                  'capital': 'Valletta'},
                 {'timezones': ['Indian/Mauritius'],
                  'code': 'MU',
                  'continent': 'Africa',
                  'name': 'Mauritius',
                  'capital': 'Port Louis'},
                 {'timezones': ['Indian/Maldives'],
                  'code': 'MV',
                  'continent': 'Asia',
                  'name': 'Maldives',
                  'capital': 'Mal\xc3\xa9'},
                 {'timezones': ['Africa/Blantyre'],
                  'code': 'MW',
                  'continent': 'Africa',
                  'name': 'Malawi',
                  'capital': 'Lilongwe'},
                 {'timezones': ['America/Mexico_City',
                                'America/Cancun',
                                'America/Merida',
                                'America/Monterrey',
                                'America/Mazatlan',
                                'America/Chihuahua',
                                'America/Hermosillo',
                                'America/Tijuana'],
                  'code': 'MX',
                  'continent': 'North America',
                  'name': 'Mexico',
                  'capital': 'Mexico City'},
                 {'timezones': ['Asia/Kuala_Lumpur',
                                'Asia/Kuching'],
                  'code': 'MY',
                  'continent': 'Asia',
                  'name': 'Malaysia',
                  'capital': 'Kuala Lumpur'},
                 {'timezones': ['Africa/Maputo'],
                  'code': 'MZ',
                  'continent': 'Africa',
                  'name': 'Mozambique',
                  'capital': 'Maputo'},
                 {'timezones': ['Africa/Windhoek'],
                  'code': 'NA',
                  'continent': 'Africa',
                  'name': 'Namibia',
                  'capital': 'Windhoek'},
                 {'timezones': ['Africa/Niamey'],
                  'code': 'NE',
                  'continent': 'Africa',
                  'name': 'Niger',
                  'capital': 'Niamey'},
                 {'timezones': ['Africa/Lagos'],
                  'code': 'NG',
                  'continent': 'Africa',
                  'name': 'Nigeria',
                  'capital': 'Abuja'},
                 {'timezones': ['America/Managua'],
                  'code': 'NI',
                  'continent': 'North America',
                  'name': 'Nicaragua',
                  'capital': 'Managua'},
                 {'timezones': ['Europe/Amsterdam'],
                  'code': 'NL',
                  'continent': 'Europe',
                  'name': 'Kingdom of the Netherlands',
                  'capital': 'Amsterdam'},
                 {'timezones': ['Europe/Oslo'],
                  'code': 'NO',
                  'continent': 'Europe',
                  'name': 'Norway',
                  'capital': 'Oslo'},
                 {'timezones': ['Asia/Katmandu'],
                  'code': 'NP',
                  'continent': 'Asia',
                  'name': 'Nepal',
                  'capital': 'Kathmandu'},
                 {'timezones': ['Pacific/Nauru'],
                  'code': 'NR',
                  'continent': 'Oceania',
                  'name': 'Nauru',
                  'capital': 'Yaren'},
                 {'timezones': ['Pacific/Auckland',
                                'Pacific/Chatham'],
                  'code': 'NZ',
                  'continent': 'Oceania',
                  'name': 'New Zealand',
                  'capital': 'Wellington'},
                 {'timezones': ['Asia/Muscat'],
                  'code': 'OM',
                  'continent': 'Asia',
                  'name': 'Oman',
                  'capital': 'Muscat'},
                 {'timezones': ['America/Panama'],
                  'code': 'PA',
                  'continent': 'North America',
                  'name': 'Panama',
                  'capital': 'Panama City'},
                 {'timezones': ['America/Lima'],
                  'code': 'PE',
                  'continent': 'South America',
                  'name': 'Peru',
                  'capital': 'Lima'},
                 {'timezones': ['Pacific/Port_Moresby'],
                  'code': 'PG',
                  'continent': 'Oceania',
                  'name': 'Papua New Guinea',
                  'capital': 'Port Moresby'},
                 {'timezones': ['Asia/Manila'],
                  'code': 'PH',
                  'continent': 'Asia',
                  'name': 'Philippines',
                  'capital': 'Manila'},
                 {'timezones': ['Asia/Karachi'],
                  'code': 'PK',
                  'continent': 'Asia',
                  'name': 'Pakistan',
                  'capital': 'Islamabad'},
                 {'timezones': ['Europe/Warsaw'],
                  'code': 'PL',
                  'continent': 'Europe',
                  'name': 'Poland',
                  'capital': 'Warsaw'},
                 {'timezones': ['Europe/Lisbon',
                                'Atlantic/Madeira',
                                'Atlantic/Azores'],
                  'code': 'PT',
                  'continent': 'Europe',
                  'name': 'Portugal',
                  'capital': 'Lisbon'},
                 {'timezones': ['Pacific/Palau'],
                  'code': 'PW',
                  'continent': 'Oceania',
                  'name': 'Palau',
                  'capital': 'Ngerulmud'},
                 {'timezones': ['America/Asuncion'],
                  'code': 'PY',
                  'continent': 'South America',
                  'name': 'Paraguay',
                  'capital': 'Asunci\xc3\xb3n'},
                 {'timezones': ['Asia/Qatar'],
                  'code': 'QA',
                  'continent': 'Asia',
                  'name': 'Qatar',
                  'capital': 'Doha'},
                 {'timezones': ['Europe/Bucharest'],
                  'code': 'RO',
                  'continent': 'Europe',
                  'name': 'Romania',
                  'capital': 'Bucharest'},
                 {'timezones': ['Europe/Kaliningrad',
                                'Europe/Moscow',
                                'Europe/Volgograd',
                                'Europe/Samara',
                                'Asia/Yekaterinburg',
                                'Asia/Omsk',
                                'Asia/Novosibirsk',
                                'Asia/Krasnoyarsk',
                                'Asia/Irkutsk',
                                'Asia/Yakutsk',
                                'Asia/Vladivostok',
                                'Asia/Sakhalin',
                                'Asia/Magadan',
                                'Asia/Kamchatka',
                                'Asia/Anadyr'],
                  'code': 'RU',
                  'continent': 'Europe',
                  'name': 'Russia',
                  'capital': 'Moscow'},
                 {'timezones': ['Africa/Kigali'],
                  'code': 'RW',
                  'continent': 'Africa',
                  'name': 'Rwanda',
                  'capital': 'Kigali'},
                 {'timezones': ['Asia/Riyadh'],
                  'code': 'SA',
                  'continent': 'Asia',
                  'name': 'Saudi Arabia',
                  'capital': 'Riyadh'},
                 {'timezones': ['Pacific/Guadalcanal'],
                  'code': 'SB',
                  'continent': 'Oceania',
                  'name': 'Solomon Islands',
                  'capital': 'Honiara'},
                 {'timezones': ['Indian/Mahe'],
                  'code': 'SC',
                  'continent': 'Africa',
                  'name': 'Seychelles',
                  'capital': 'Victoria'},
                 {'timezones': ['Africa/Khartoum'],
                  'code': 'SD',
                  'continent': 'Africa',
                  'name': 'Sudan',
                  'capital': 'Khartoum'},
                 {'timezones': ['Europe/Stockholm'],
                  'code': 'SE',
                  'continent': 'Europe',
                  'name': 'Sweden',
                  'capital': 'Stockholm'},
                 {'timezones': ['Asia/Singapore'],
                  'code': 'SG',
                  'continent': 'Asia',
                  'name': 'Singapore',
                  'capital': 'Singapore'},
                 {'timezones': ['Europe/Ljubljana'],
                  'code': 'SI',
                  'continent': 'Europe',
                  'name': 'Slovenia',
                  'capital': 'Ljubljana'},
                 {'timezones': ['Europe/Bratislava'],
                  'code': 'SK',
                  'continent': 'Europe',
                  'name': 'Slovakia',
                  'capital': 'Bratislava'},
                 {'timezones': ['Africa/Freetown'],
                  'code': 'SL',
                  'continent': 'Africa',
                  'name': 'Sierra Leone',
                  'capital': 'Freetown'},
                 {'timezones': ['Europe/San_Marino'],
                  'code': 'SM',
                  'continent': 'Europe',
                  'name': 'San Marino',
                  'capital': 'San Marino'},
                 {'timezones': ['Africa/Dakar'],
                  'code': 'SN',
                  'continent': 'Africa',
                  'name': 'Senegal',
                  'capital': 'Dakar'},
                 {'timezones': ['Africa/Mogadishu'],
                  'code': 'SO',
                  'continent': 'Africa',
                  'name': 'Somalia',
                  'capital': 'Mogadishu'},
                 {'timezones': ['America/Paramaribo'],
                  'code': 'SR',
                  'continent': 'South America',
                  'name': 'Suriname',
                  'capital': 'Paramaribo'},
                 {'timezones': ['Africa/Sao_Tome'],
                  'code': 'ST',
                  'continent': 'Africa',
                  'name': 'S\xc3\xa3o Tom\xc3\xa9 and Pr\xc3\xadncipe',
                  'capital': 'S\xc3\xa3o Tom\xc3\xa9'},
                 {'timezones': ['Asia/Damascus'],
                  'code': 'SY',
                  'continent': 'Asia',
                  'name': 'Syria',
                  'capital': 'Damascus'},
                 {'timezones': ['Africa/Lome'],
                  'code': 'TG',
                  'continent': 'Africa',
                  'name': 'Togo',
                  'capital': 'Lom\xc3\xa9'},
                 {'timezones': ['Asia/Bangkok'],
                  'code': 'TH',
                  'continent': 'Asia',
                  'name': 'Thailand',
                  'capital': 'Bangkok'},
                 {'timezones': ['Asia/Dushanbe'],
                  'code': 'TJ',
                  'continent': 'Asia',
                  'name': 'Tajikistan',
                  'capital': 'Dushanbe'},
                 {'timezones': ['Asia/Ashgabat'],
                  'code': 'TM',
                  'continent': 'Asia',
                  'name': 'Turkmenistan',
                  'capital': 'Ashgabat'},
                 {'timezones': ['Africa/Tunis'],
                  'code': 'TN',
                  'continent': 'Africa',
                  'name': 'Tunisia',
                  'capital': 'Tunis'},
                 {'timezones': ['Pacific/Tongatapu'],
                  'code': 'TO',
                  'continent': 'Oceania',
                  'name': 'Tonga',
                  'capital': 'Nuku\xca\xbbalofa'},
                 {'timezones': ['Europe/Istanbul'],
                  'code': 'TR',
                  'continent': 'Asia',
                  'name': 'Turkey',
                  'capital': 'Ankara'},
                 {'timezones': ['America/Port_of_Spain'],
                  'code': 'TT',
                  'continent': 'North America',
                  'name': 'Trinidad and Tobago',
                  'capital': 'Port of Spain'},
                 {'timezones': ['Pacific/Funafuti'],
                  'code': 'TV',
                  'continent': 'Oceania',
                  'name': 'Tuvalu',
                  'capital': 'Funafuti'},
                 {'timezones': ['Africa/Dar_es_Salaam'],
                  'code': 'TZ',
                  'continent': 'Africa',
                  'name': 'Tanzania',
                  'capital': 'Dodoma'},
                 {'timezones': ['Europe/Kiev',
                                'Europe/Uzhgorod',
                                'Europe/Zaporozhye',
                                'Europe/Simferopol'],
                  'code': 'UA',
                  'continent': 'Europe',
                  'name': 'Ukraine',
                  'capital': 'Kiev'},
                 {'timezones': ['Africa/Kampala'],
                  'code': 'UG',
                  'continent': 'Africa',
                  'name': 'Uganda',
                  'capital': 'Kampala'},
                 {'timezones': ['America/New_York',
                                'America/Detroit',
                                'America/Kentucky/Louisville',
                                'America/Kentucky/Monticello',
                                'America/Indiana/Indianapolis',
                                'America/Indiana/Marengo',
                                'America/Indiana/Knox',
                                'America/Indiana/Vevay',
                                'America/Chicago',
                                'America/Indiana/Vincennes',
                                'America/Indiana/Petersburg',
                                'America/Menominee',
                                'America/North_Dakota/Center',
                                'America/North_Dakota/New_Salem',
                                'America/Denver',
                                'America/Boise',
                                'America/Shiprock',
                                'America/Phoenix',
                                'America/Los_Angeles',
                                'America/Anchorage',
                                'America/Juneau',
                                'America/Yakutat',
                                'America/Nome',
                                'America/Adak',
                                'Pacific/Honolulu'],
                  'code': 'US',
                  'continent': 'North America',
                  'name': 'United States',
                  'capital': 'Washington, D.C.'},
                 {'timezones': ['America/Montevideo'],
                  'code': 'UY',
                  'continent': 'South America',
                  'name': 'Uruguay',
                  'capital': 'Montevideo'},
                 {'timezones': ['Asia/Samarkand',
                                'Asia/Tashkent'],
                  'code': 'UZ',
                  'continent': 'Asia',
                  'name': 'Uzbekistan',
                  'capital': 'Tashkent'},
                 {'timezones': ['Europe/Vatican'],
                  'code': 'VA',
                  'continent': 'Europe',
                  'name': 'Vatican City',
                  'capital': 'Vatican City'},
                 {'timezones': ['America/Caracas'],
                  'code': 'VE',
                  'continent': 'South America',
                  'name': 'Venezuela',
                  'capital': 'Caracas'},
                 {'timezones': ['Asia/Saigon'],
                  'code': 'VN',
                  'continent': 'Asia',
                  'name': 'Vietnam',
                  'capital': 'Hanoi'},
                 {'timezones': ['Pacific/Efate'],
                  'code': 'VU',
                  'continent': 'Oceania',
                  'name': 'Vanuatu',
                  'capital': 'Port Vila'},
                 {'timezones': ['Asia/Aden'],
                  'code': 'YE',
                  'continent': 'Asia',
                  'name': 'Yemen',
                  'capital': "Sana'a"},
                 {'timezones': ['Africa/Lusaka'],
                  'code': 'ZM',
                  'continent': 'Africa',
                  'name': 'Zambia',
                  'capital': 'Lusaka'},
                 {'timezones': ['Africa/Harare'],
                  'code': 'ZW',
                  'continent': 'Africa',
                  'name': 'Zimbabwe',
                  'capital': 'Harare'},
                 {'timezones': ['Africa/Algiers'],
                  'code': 'DZ',
                  'continent': 'Africa',
                  'name': 'Algeria',
                  'capital': 'Algiers'},
                 {'timezones': ['Europe/Sarajevo'],
                  'code': 'BA',
                  'continent': 'Europe',
                  'name': 'Bosnia and Herzegovina',
                  'capital': 'Sarajevo'},
                 {'timezones': ['Asia/Phnom_Penh'],
                  'code': 'KH',
                  'continent': 'Asia',
                  'name': 'Cambodia',
                  'capital': 'Phnom Penh'},
                 {'timezones': ['Africa/Bangui'],
                  'code': 'CF',
                  'continent': 'Africa',
                  'name': 'Central African Republic',
                  'capital': 'Bangui'},
                 {'timezones': ['Africa/Ndjamena'],
                  'code': 'TD',
                  'continent': 'Africa',
                  'name': 'Chad',
                  'capital': "N'Djamena"},
                 {'timezones': ['Indian/Comoro'],
                  'code': 'KM',
                  'continent': 'Africa',
                  'name': 'Comoros',
                  'capital': 'Moroni'},
                 {'timezones': ['Europe/Zagreb'],
                  'code': 'HR',
                  'continent': 'Europe',
                  'name': 'Croatia',
                  'capital': 'Zagreb'},
                 {'timezones': ['Asia/Dili'],
                  'code': 'TL',
                  'continent': 'Asia',
                  'name': 'East Timor',
                  'capital': 'Dili'},
                 {'timezones': ['America/El_Salvador'],
                  'code': 'SV',
                  'continent': 'North America',
                  'name': 'El Salvador',
                  'capital': 'San Salvador'},
                 {'timezones': ['Africa/Malabo'],
                  'code': 'GQ',
                  'continent': 'Africa',
                  'name': 'Equatorial Guinea',
                  'capital': 'Malabo'},
                 {'timezones': ['America/Grenada'],
                  'code': 'GD',
                  'continent': 'North America',
                  'name': 'Grenada',
                  'capital': "St. George's"},
                 {'timezones': ['Asia/Almaty',
                                'Asia/Qyzylorda',
                                'Asia/Aqtobe',
                                'Asia/Aqtau',
                                'Asia/Oral'],
                  'code': 'KZ',
                  'continent': 'Asia',
                  'name': 'Kazakhstan',
                  'capital': 'Astana'},
                 {'timezones': ['Asia/Vientiane'],
                  'code': 'LA',
                  'continent': 'Asia',
                  'name': 'Laos',
                  'capital': 'Vientiane'},
                 {'timezones': ['Pacific/Truk',
                                'Pacific/Ponape',
                                'Pacific/Kosrae'],
                  'code': 'FM',
                  'continent': 'Oceania',
                  'name': 'Federated States of Micronesia',
                  'capital': 'Palikir'},
                 {'timezones': ['Europe/Chisinau'],
                  'code': 'MD',
                  'continent': 'Europe',
                  'name': 'Moldova',
                  'capital': 'Chi\xc5\x9fin\xc4\x83u'},
                 {'timezones': ['Europe/Monaco'],
                  'code': 'MC',
                  'continent': 'Europe',
                  'name': 'Monaco',
                  'capital': 'Monaco'},
                 {'timezones': ['Europe/Podgorica'],
                  'code': 'ME',
                  'continent': 'Europe',
                  'name': 'Montenegro',
                  'capital': 'Podgorica'},
                 {'timezones': ['Africa/Casablanca'],
                  'code': 'MA',
                  'continent': 'Africa',
                  'name': 'Morocco',
                  'capital': 'Rabat'},
                 {'timezones': ['America/St_Kitts'],
                  'code': 'KN',
                  'continent': 'North America',
                  'name': 'Saint Kitts and Nevis',
                  'capital': 'Basseterre'},
                 {'timezones': ['America/St_Lucia'],
                  'code': 'LC',
                  'continent': 'North America',
                  'name': 'Saint Lucia',
                  'capital': 'Castries'},
                 {'timezones': ['America/St_Vincent'],
                  'code': 'VC',
                  'continent': 'North America',
                  'name': 'Saint Vincent and the Grenadines',
                  'capital': 'Kingstown'},
                 {'timezones': ['Pacific/Apia'],
                  'code': 'WS',
                  'continent': 'Oceania',
                  'name': 'Samoa',
                  'capital': 'Apia'},
                 {'timezones': ['Europe/Belgrade'],
                  'code': 'RS',
                  'continent': 'Europe',
                  'name': 'Serbia',
                  'capital': 'Belgrade'},
                 {'timezones': ['Africa/Johannesburg'],
                  'code': 'ZA',
                  'continent': 'Africa',
                  'name': 'South Africa',
                  'capital': 'Pretoria'},
                 {'timezones': ['Europe/Madrid',
                                'Africa/Ceuta',
                                'Atlantic/Canary'],
                  'code': 'ES',
                  'continent': 'Europe',
                  'name': 'Spain',
                  'capital': 'Madrid'},
                 {'timezones': ['Asia/Colombo'],
                  'code': 'LK',
                  'continent': 'Asia',
                  'name': 'Sri Lanka',
                  'capital': 'Sri Jayewardenepura Kotte'},
                 {'timezones': ['Africa/Mbabane'],
                  'code': 'SZ',
                  'continent': 'Africa',
                  'name': 'Swaziland',
                  'capital': 'Mbabane'},
                 {'timezones': ['Europe/Zurich'],
                  'code': 'CH',
                  'continent': 'Europe',
                  'name': 'Switzerland',
                  'capital': 'Bern'},
                 {'timezones': ['Asia/Dubai'],
                  'code': 'AE',
                  'continent': 'Asia',
                  'name': 'United Arab Emirates',
                  'capital': 'Abu Dhabi'},
                 {'timezones': ['Europe/London'],
                  'code': 'GB',
                  'continent': 'Europe',
                  'name': 'United Kingdom',
                  'capital': 'London'},
                 ]

    regex = re.compile(timedelta_pattern)

    def unix_time(self, end_datetime=None):
        """
        Get a timestamp between January 1, 1970 and now
        :example 1061306726
        """
        end_datetime = self._parse_end_datetime(end_datetime)
        return self.generator.random.randint(0, end_datetime)

    def time_delta(self, end_datetime=None):
        """
        Get a timedelta object
        """
        end_datetime = self._parse_end_datetime(end_datetime)
        ts = self.generator.random.randint(0, end_datetime)
        return timedelta(seconds=ts)

    def date_time(self, tzinfo=None, end_datetime=None):
        """
        Get a datetime object for a date between January 1, 1970 and now
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example DateTime('2005-08-16 20:39:21')
        :return datetime
        """
        # NOTE: On windows, the lowest value you can get from windows is 86400
        #       on the first day. Known python issue:
        #       https://bugs.python.org/issue30684
        return datetime(1970, 1, 1, tzinfo=tzinfo) + \
            timedelta(seconds=self.unix_time(end_datetime=end_datetime))

    def date_time_ad(self, tzinfo=None, end_datetime=None):
        """
        Get a datetime object for a date between January 1, 001 and now
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example DateTime('1265-03-22 21:15:52')
        :return datetime
        """
        end_datetime = self._parse_end_datetime(end_datetime)
        ts = self.generator.random.randint(-62135596800, end_datetime)
        # NOTE: using datetime.fromtimestamp(ts) directly will raise
        #       a "ValueError: timestamp out of range for platform time_t"
        #       on some platforms due to system C functions;
        #       see http://stackoverflow.com/a/10588133/2315612
        # NOTE: On windows, the lowest value you can get from windows is 86400
        #       on the first day. Known python issue:
        #       https://bugs.python.org/issue30684
        return datetime(1970, 1, 1, tzinfo=tzinfo) + timedelta(seconds=ts)

    def iso8601(self, tzinfo=None, end_datetime=None):
        """
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example '2003-10-21T16:05:52+0000'
        """
        return self.date_time(tzinfo, end_datetime=end_datetime).isoformat()

    def date(self, pattern='%Y-%m-%d', end_datetime=None):
        """
        Get a date string between January 1, 1970 and now
        :param pattern format
        :example '2008-11-27'
        """
        return self.date_time(end_datetime=end_datetime).strftime(pattern)

    def date_object(self, end_datetime=None):
        """
        Get a date object between January 1, 1970 and now
        :example datetime.date(2016, 9, 20)
        """
        return self.date_time(end_datetime=end_datetime).date()

    def time(self, pattern='%H:%M:%S', end_datetime=None):
        """
        Get a time string (24h format by default)
        :param pattern format
        :example '15:02:34'
        """
        return self.date_time(
            end_datetime=end_datetime).time().strftime(pattern)

    def time_object(self, end_datetime=None):
        """
        Get a time object
        :example datetime.time(15, 56, 56, 772876)
        """
        return self.date_time(end_datetime=end_datetime).time()

    @classmethod
    def _parse_end_datetime(cls, value):
        if value is None:
            return int(time())

        return cls._parse_date_time(value)

    @classmethod
    def _parse_date_string(cls, value):
        parts = cls.regex.match(value)
        if not parts:
            raise ParseError("Can't parse date string `{}`.".format(value))
        parts = parts.groupdict()
        time_params = {}
        for (name_, param_) in parts.items():
            if param_:
                time_params[name_] = int(param_)

        if 'years' in time_params:
            if 'days' not in time_params:
                time_params['days'] = 0
            time_params['days'] += 365.24 * time_params.pop('years')

        if not time_params:
            raise ParseError("Can't parse date string `{}`.".format(value))
        return time_params

    @classmethod
    def _parse_timedelta(cls, value):
        if isinstance(value, timedelta):
            return value.total_seconds()
        if is_string(value):
            time_params = cls._parse_date_string(value)
            return timedelta(**time_params).total_seconds()
        if isinstance(value, (int, float)):
            return value
        raise ParseError("Invalid format for timedelta '{0}'".format(value))

    @classmethod
    def _parse_date_time(cls, text, tzinfo=None):
        if isinstance(text, (datetime, date, real_datetime, real_date)):
            return datetime_to_timestamp(text)
        now = datetime.now(tzinfo)
        if isinstance(text, timedelta):
            return datetime_to_timestamp(now - text)
        if is_string(text):
            if text == 'now':
                return datetime_to_timestamp(datetime.now(tzinfo))
            time_params = cls._parse_date_string(text)
            return datetime_to_timestamp(now + timedelta(**time_params))
        if isinstance(text, int):
            return datetime_to_timestamp(now + timedelta(text))
        raise ParseError("Invalid format for date '{0}'".format(text))

    @classmethod
    def _parse_date(cls, value):
        if isinstance(value, (datetime, real_datetime)):
            return value.date()
        elif isinstance(value, (date, real_date)):
            return value
        today = date.today()
        if isinstance(value, timedelta):
            return today - value
        if is_string(value):
            if value in ('today', 'now'):
                return today
            time_params = cls._parse_date_string(value)
            return today + timedelta(**time_params)
        if isinstance(value, int):
            return today + timedelta(value)
        raise ParseError("Invalid format for date '{0}'".format(value))

    def date_time_between(self, start_date='-30y', end_date='now', tzinfo=None):
        """
        Get a DateTime object based on a random date between two given dates.
        Accepts date strings that can be recognized by strtotime().

        :param start_date Defaults to 30 years ago
        :param end_date Defaults to "now"
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example DateTime('1999-02-02 11:42:52')
        :return DateTime
        """
        start_date = self._parse_date_time(start_date, tzinfo=tzinfo)
        end_date = self._parse_date_time(end_date, tzinfo=tzinfo)
        if end_date - start_date <= 1:
            ts = start_date + self.generator.random.random()
        else:
            ts = self.generator.random.randint(start_date, end_date)
        return datetime(1970, 1, 1, tzinfo=tzinfo) + timedelta(seconds=ts)

    def date_between(self, start_date='-30y', end_date='today'):
        """
        Get a Date object based on a random date between two given dates.
        Accepts date strings that can be recognized by strtotime().

        :param start_date Defaults to 30 years ago
        :param end_date Defaults to "today"
        :example Date('1999-02-02')
        :return Date
        """

        start_date = self._parse_date(start_date)
        end_date = self._parse_date(end_date)
        return self.date_between_dates(date_start=start_date, date_end=end_date)

    def future_datetime(self, end_date='+30d', tzinfo=None):
        """
        Get a DateTime object based on a random date between 1 second form now
        and a given date.
        Accepts date strings that can be recognized by strtotime().

        :param end_date Defaults to "+30d"
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example DateTime('1999-02-02 11:42:52')
        :return DateTime
        """
        return self.date_time_between(
            start_date='+1s', end_date=end_date, tzinfo=tzinfo,
        )

    def future_date(self, end_date='+30d', tzinfo=None):
        """
        Get a Date object based on a random date between 1 day from now and a
        given date.
        Accepts date strings that can be recognized by strtotime().

        :param end_date Defaults to "+30d"
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example DateTime('1999-02-02 11:42:52')
        :return DateTime
        """
        return self.date_between(start_date='+1d', end_date=end_date)

    def past_datetime(self, start_date='-30d', tzinfo=None):
        """
        Get a DateTime object based on a random date between a given date and 1
        second ago.
        Accepts date strings that can be recognized by strtotime().

        :param start_date Defaults to "-30d"
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example DateTime('1999-02-02 11:42:52')
        :return DateTime
        """
        return self.date_time_between(
            start_date=start_date, end_date='-1s', tzinfo=tzinfo,
        )

    def past_date(self, start_date='-30d', tzinfo=None):
        """
        Get a Date object based on a random date between a given date and 1 day
        ago.
        Accepts date strings that can be recognized by strtotime().

        :param start_date Defaults to "-30d"
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example DateTime('1999-02-02 11:42:52')
        :return DateTime
        """
        return self.date_between(start_date=start_date, end_date='-1d')

    def date_time_between_dates(
            self,
            datetime_start=None,
            datetime_end=None,
            tzinfo=None):
        """
        Takes two DateTime objects and returns a random datetime between the two
        given datetimes.
        Accepts DateTime objects.

        :param datetime_start: DateTime
        :param datetime_end: DateTime
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example DateTime('1999-02-02 11:42:52')
        :return DateTime
        """
        if datetime_start is None:
            datetime_start = datetime.now(tzinfo)

        if datetime_end is None:
            datetime_end = datetime.now(tzinfo)

        timestamp = self.generator.random.randint(
            datetime_to_timestamp(datetime_start),
            datetime_to_timestamp(datetime_end),
        )
        if tzinfo is None:
            pick = datetime.fromtimestamp(timestamp, tzlocal())
            pick = pick.astimezone(tzutc()).replace(tzinfo=None)
        else:
            pick = datetime.fromtimestamp(timestamp, tzinfo)
        return pick

    def date_between_dates(self, date_start=None, date_end=None):
        """
        Takes two Date objects and returns a random date between the two given dates.
        Accepts Date or Datetime objects

        :param date_start: Date
        :param date_end: Date
        :return Date
        """
        return self.date_time_between_dates(date_start, date_end).date()

    def date_time_this_century(
            self,
            before_now=True,
            after_now=False,
            tzinfo=None):
        """
        Gets a DateTime object for the current century.

        :param before_now: include days in current century before today
        :param after_now: include days in current century after today
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example DateTime('2012-04-04 11:02:02')
        :return DateTime
        """
        now = datetime.now(tzinfo)
        this_century_start = datetime(
            now.year - (now.year % 100), 1, 1, tzinfo=tzinfo)
        next_century_start = datetime(
            this_century_start.year + 100, 1, 1, tzinfo=tzinfo)

        if before_now and after_now:
            return self.date_time_between_dates(
                this_century_start, next_century_start, tzinfo)
        elif not before_now and after_now:
            return self.date_time_between_dates(now, next_century_start, tzinfo)
        elif not after_now and before_now:
            return self.date_time_between_dates(this_century_start, now, tzinfo)
        else:
            return now

    def date_time_this_decade(
            self,
            before_now=True,
            after_now=False,
            tzinfo=None):
        """
        Gets a DateTime object for the decade year.

        :param before_now: include days in current decade before today
        :param after_now: include days in current decade after today
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example DateTime('2012-04-04 11:02:02')
        :return DateTime
        """
        now = datetime.now(tzinfo)
        this_decade_start = datetime(
            now.year - (now.year % 10), 1, 1, tzinfo=tzinfo)
        next_decade_start = datetime(
            this_decade_start.year + 10, 1, 1, tzinfo=tzinfo)

        if before_now and after_now:
            return self.date_time_between_dates(
                this_decade_start, next_decade_start, tzinfo)
        elif not before_now and after_now:
            return self.date_time_between_dates(now, next_decade_start, tzinfo)
        elif not after_now and before_now:
            return self.date_time_between_dates(this_decade_start, now, tzinfo)
        else:
            return now

    def date_time_this_year(
            self,
            before_now=True,
            after_now=False,
            tzinfo=None):
        """
        Gets a DateTime object for the current year.

        :param before_now: include days in current year before today
        :param after_now: include days in current year after today
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example DateTime('2012-04-04 11:02:02')
        :return DateTime
        """
        now = datetime.now(tzinfo)
        this_year_start = now.replace(
            month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
        next_year_start = datetime(now.year + 1, 1, 1, tzinfo=tzinfo)

        if before_now and after_now:
            return self.date_time_between_dates(
                this_year_start, next_year_start, tzinfo)
        elif not before_now and after_now:
            return self.date_time_between_dates(now, next_year_start, tzinfo)
        elif not after_now and before_now:
            return self.date_time_between_dates(this_year_start, now, tzinfo)
        else:
            return now

    def date_time_this_month(
            self,
            before_now=True,
            after_now=False,
            tzinfo=None):
        """
        Gets a DateTime object for the current month.

        :param before_now: include days in current month before today
        :param after_now: include days in current month after today
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example DateTime('2012-04-04 11:02:02')
        :return DateTime
        """
        now = datetime.now(tzinfo)
        this_month_start = now.replace(
            day=1, hour=0, minute=0, second=0, microsecond=0)

        next_month_start = this_month_start + \
            relativedelta.relativedelta(months=1)
        if before_now and after_now:
            return self.date_time_between_dates(
                this_month_start, next_month_start, tzinfo)
        elif not before_now and after_now:
            return self.date_time_between_dates(now, next_month_start, tzinfo)
        elif not after_now and before_now:
            return self.date_time_between_dates(this_month_start, now, tzinfo)
        else:
            return now

    def date_this_century(self, before_today=True, after_today=False):
        """
        Gets a Date object for the current century.

        :param before_today: include days in current century before today
        :param after_today: include days in current century after today
        :example Date('2012-04-04')
        :return Date
        """
        today = date.today()
        this_century_start = date(today.year - (today.year % 100), 1, 1)
        next_century_start = date(this_century_start.year + 100, 1, 1)

        if before_today and after_today:
            return self.date_between_dates(
                this_century_start, next_century_start)
        elif not before_today and after_today:
            return self.date_between_dates(today, next_century_start)
        elif not after_today and before_today:
            return self.date_between_dates(this_century_start, today)
        else:
            return today

    def date_this_decade(self, before_today=True, after_today=False):
        """
        Gets a Date object for the decade year.

        :param before_today: include days in current decade before today
        :param after_today: include days in current decade after today
        :example Date('2012-04-04')
        :return Date
        """
        today = date.today()
        this_decade_start = date(today.year - (today.year % 10), 1, 1)
        next_decade_start = date(this_decade_start.year + 10, 1, 1)

        if before_today and after_today:
            return self.date_between_dates(this_decade_start, next_decade_start)
        elif not before_today and after_today:
            return self.date_between_dates(today, next_decade_start)
        elif not after_today and before_today:
            return self.date_between_dates(this_decade_start, today)
        else:
            return today

    def date_this_year(self, before_today=True, after_today=False):
        """
        Gets a Date object for the current year.

        :param before_today: include days in current year before today
        :param after_today: include days in current year after today
        :example Date('2012-04-04')
        :return Date
        """
        today = date.today()
        this_year_start = today.replace(month=1, day=1)
        next_year_start = date(today.year + 1, 1, 1)

        if before_today and after_today:
            return self.date_between_dates(this_year_start, next_year_start)
        elif not before_today and after_today:
            return self.date_between_dates(today, next_year_start)
        elif not after_today and before_today:
            return self.date_between_dates(this_year_start, today)
        else:
            return today

    def date_this_month(self, before_today=True, after_today=False):
        """
        Gets a Date object for the current month.

        :param before_today: include days in current month before today
        :param after_today: include days in current month after today
        :param tzinfo: timezone, instance of datetime.tzinfo subclass
        :example DateTime('2012-04-04 11:02:02')
        :return DateTime
        """
        today = date.today()
        this_month_start = today.replace(day=1)

        next_month_start = this_month_start + \
            relativedelta.relativedelta(months=1)
        if before_today and after_today:
            return self.date_between_dates(this_month_start, next_month_start)
        elif not before_today and after_today:
            return self.date_between_dates(today, next_month_start)
        elif not after_today and before_today:
            return self.date_between_dates(this_month_start, today)
        else:
            return today

    def time_series(
            self,
            start_date='-30d',
            end_date='now',
            precision=None,
            distrib=None,
            tzinfo=None):
        """
        Returns a generator yielding tuples of ``(<datetime>, <value>)``.

        The data points will start at ``start_date``, and be at every time interval specified by
        ``precision``.
        ``distrib`` is a callable that accepts ``<datetime>`` and returns ``<value>``

        """
        start_date = self._parse_date_time(start_date, tzinfo=tzinfo)
        end_date = self._parse_date_time(end_date, tzinfo=tzinfo)

        if end_date < start_date:
            raise ValueError("`end_date` must be greater than `start_date`.")

        if precision is None:
            precision = (end_date - start_date) / 30

        precision = self._parse_timedelta(precision)
        if distrib is None:
            def distrib(dt): return self.generator.random.uniform(0, precision)  # noqa

        if not callable(distrib):
            raise ValueError(
                "`distrib` must be a callable. Got {} instead.".format(distrib))

        datapoint = start_date
        while datapoint < end_date:
            dt = timestamp_to_datetime(datapoint, tzinfo)
            datapoint += precision
            yield (dt, distrib(dt))

    def am_pm(self):
        return self.date('%p')

    def day_of_month(self):
        return self.date('%d')

    def day_of_week(self):
        return self.date('%A')

    def month(self):
        return self.date('%m')

    def month_name(self):
        return self.date('%B')

    def year(self):
        return self.date('%Y')

    def century(self):
        """
        :example 'XVII'
        """
        return self.random_element(self.centuries)

    def timezone(self):
        return self.generator.random.choice(
            self.random_element(self.countries)['timezones'])
