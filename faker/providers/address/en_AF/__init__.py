from faker.providers import BaseProvider
import random


class Provider(BaseProvider):
    """Afghan complete address provider in English."""

    provinces = [
        "Badakhshan", "Badghis", "Baghlan", "Balkh", "Bamyan", "Paktia", "Paktika",
        "Parwan", "Panjshir", "Takhar", "Daykundi", "Jowzjan", "Uruzgan", "Zabul",
        "Samangan", "Sar-e Pol", "Ghor", "Ghazni", "Faryab", "Farah", "Kabul",
        "Kapisa", "Kandahar", "Kunduz", "Kunar", "Laghman", "Logar", "Maidan Wardak",
        "Nimroz", "Nangarhar", "Nuristan", "Helmand", "Herat", "Khost"
    ]

    cities = {
        "Badakhshan": ["Fayzabad"],
        "Badghis": ["Qala-e Naw"],
        "Baghlan": ["Pul-e Khumri"],
        "Balkh": ["Mazar-e Sharif"],
        "Bamyan": ["Bamyan"],
        "Daykundi": ["Nili"],
        "Farah": ["Farah"],
        "Faryab": ["Maymana"],
        "Ghor": ["Chaghcharan"],
        "Ghazni": ["Ghazni"],
        "Helmand": ["Lashkargah"],
        "Herat": ["Herat"],
        "Jowzjan": ["Sheberghan"],
        "Kabul": ["Kabul"],
        "Kapisa": ["Mahmud Raqi"],
        "Kandahar": ["Kandahar"],
        "Kunduz": ["Kunduz"],
        "Kunar": ["Asadabad"],
        "Khost": ["Khost"],
        "Laghman": ["Mihtarlam"],
        "Logar": ["Pul-e Alam"],
        "Maidan Wardak": ["Maidan Shar"],
        "Nimroz": ["Zaranj"],
        "Nangarhar": ["Jalalabad"],
        "Nuristan": ["Parun"],
        "Uruzgan": ["Tarin Kot"],
        "Paktia": ["Gardez"],
        "Paktika": ["Sharan"],
        "Panjshir": ["Bazarak"],
        "Parwan": ["Charikar"],
        "Samangan": ["Aybak"],
        "Sar-e Pol": ["Sar-e Pol"],
        "Takhar": ["Taloqan"],
        "Zabul": ["Qalat"]
    }

    # Districts for all provinces (English transliterations)
    districts = {
        "Kabul": ["Kabul City", "Sarayi Shamali", "Surobi", "Qarabagh", "Bagrami",
                  "Deh Sabz", "Paghman", "Istalif", "Farza", "Guldara", "Khawaja Rawash",
                  "Kalakan", "Mir Bacha Kot", "Musahi", "Shakardara", "Chisht-e Sharif",
                  "Musayi"],
        "Parwan": ["Charikar", "Jabal-us-Siraj", "Siyahgird", "Shinwari", "Kohistan",
                   "Surkhi Parsa", "Salang", "Sheikh Ali", "Ghorband", "Bagram"],
        "Kapisa": ["Mahmud Raqi", "Nijrab", "Tagab", "Koh Band", "Hisa-e Awali Kohistan",
                   "Hisa-e Duwum Kohistan", "Ala Sai"],
        "Panjshir": ["Bazarak", "Paryan", "Darah", "Anaba", "Rokha", "Pashghor",
                     "Shtal", "Abdullah Khel"],
        "Baghlan": ["Pul-e Khumri", "Dahana-e Ghori", "Andarab", "Burka", "Baghlan-e Jadid",
                    "Doshi", "Farang wa Gharu", "Guzargah-e Nur", "Khinjan", "Khost wa Fereng",
                    "Nahrin", "Pul-e Hisar", "Tala wa Barfak", "Kalgai"],
        "Badghis": ["Qala-e Naw", "Ab Kamari", "Bala Murghab", "Jawand", "Ghormach",
                    "Muqur", "Qadis"],
        "Badakhshan": ["Fayzabad", "Argo", "Arghanch Khwa", "Baharak", "Darayim", "Ishkashim",
                       "Jurm", "Khash", "Khwan", "Kishim", "Kuf Ab", "Koran wa Munjan",
                       "Maimay", "Nusay", "Raghistan", "Shuhada", "Shighnan", "Shiki",
                       "Shuhada", "Tagab", "Tishkan", "Wakhan", "Warduj", "Yaftali Sufla",
                       "Yawan", "Yawan", "Zibak"],
        "Balkh": ["Mazar-e Sharif", "Balkhab", "Chimtal", "Charbolak", "Charkent",
                  "Dehdadi", "Dawlatabad", "Sholgara", "Kaldar", "Khulm",
                  "Kishindeh Rabat Sangi", "Marmul", "Nahr-e Shahi", "Shortepa", "Zari"],
        "Bamyan": ["Bamyan", "Yakawlang", "Koh Mard", "Panjab", "Sayghan", "Shibar",
                   "Waras", "Saydabad"],
        "Daykundi": ["Nili", "Ishtarlay", "Khedir", "Gizab", "Miramor", "Nawur",
                     "Sang-e Takht", "Kajran", "Sharistan"],
        "Farah": ["Farah", "Anar Dara", "Bala Buluk", "Bakwa", "Gulistan", "Khaki Safed",
                  "Lash wa Juwayn", "Pur Chaman", "Pusht Rod", "Qala-e Kah", "Shib Koh"],
        "Faryab": ["Maymana", "Almar", "Andkhoy", "Bilchiragh", "Dawlatabad", "Ghormach",
                   "Khan Char Bagh", "Khwaja Sabz Posh", "Qarghan", "Qaramqol", "Qaysar",
                   "Shirintagab", "Pashtun Kot", "Gurziwan"],
        "Ghor": ["Chaghcharan", "Du Layna", "Dushi Qala", "Lal wa Sarjangal", "Marghab",
                 "Pasaband", "Saghar", "Shahrak", "Taywara", "Tulak"],
        "Ghazni": ["Ghazni", "Ab Band", "Ajristan", "Andar", "Deh Yak", "Giro", "Jaghori",
                   "Jaghatu", "Khwaja Umari", "Malistan", "Muqur", "Nawur", "Nawa",
                   "Qarabagh", "Rashidan", "Zanakhan", "Abas Band", "Waghaz"],
        "Helmand": ["Lashkargah", "Nahr-e Saraj", "Nad Ali", "Nawa-e Barakzayi", "Garmser",
                    "Dishu", "Sangin", "Washir", "Kajaki", "Musa Qala", "Baghran",
                    "Reg", "Nawzad"],
        "Herat": ["Herat", "Adraskan", "Injil", "Chisht-e Sharif", "Farsi", "Ghoryan",
                  "Gulran", "Guzara", "Gozara", "Zinda Jan", "Karukh", "Kushk Rabat Sangi",
                  "Kushk-e Kuhna", "Obe", "Pashtun Zarghun", "Tirpul"],
        "Jowzjan": ["Sheberghan", "Aqcha", "Darzab", "Fayzabad", "Khanaqa", "Khamyab",
                    "Khwaja Du Koh", "Mardyan", "Mingajik", "Qarqin", "Qush Tepa"],
        "Kandahar": ["Kandahar", "Arghandab", "Arghistan", "Dand", "Ghorak", "Khakrez",
                     "Maruf", "Miyanishin", "Nesh", "Panjwayi", "Shah Wali Kot",
                     "Shorabak", "Takhta Pul", "Zheray", "Spin Boldak"],
        "Kunduz": ["Kunduz", "Imam Sahib", "Aliabad", "Archi", "Chardara", "Khanabad",
                   "Qala-e Zal"],
        "Kunar": ["Asadabad", "Barkunar", "Chawki", "Dangam", "Dara-e Pech", "Ghaziabad",
                  "Kama", "Marawara", "Narang", "Nurgal", "Shiltan", "Sarkani",
                  "Nari", "Watapur"],
        "Khost": ["Khost", "Bak", "Gurbuz", "Ismail Khel wa Manduzai", "Musa Khel",
                  "Nad Shah Kot", "Qalandar", "Sabari", "Shamul", "Spera", "Tani",
                  "Terezayi"],
        "Laghman": ["Mihtarlam", "Alishing", "Alingar", "Dawlat Shah", "Qarghayi",
                    "Badpash"],
        "Logar": ["Pul-e Alam", "Azra", "Baraki Barak", "Kharwar", "Khushi",
                  "Mohammad Agha", "Charkh"],
        "Maidan Wardak": ["Maidan Shar", "Chak", "Hisa-e Awali Behsud", "Hisa-e Duwum Behsud",
                          "Jalrez", "Markaz Behsud", "Nirkh", "Saydabad", "Day Mirdad"],
        "Nangarhar": ["Jalalabad", "Achin", "Bati Kot", "Behsud", "Chaparhar", "Darbaba",
                      "Dur Baba", "Ghani Khel", "Goshta", "Hisarak", "Khogyani",
                      "Kuz Kunar", "Kot", "Lal Pur", "Muhmand Dara", "Nazyan",
                      "Pachir Agam", "Rodat", "Sherzad", "Shinwar", "Surkh Rod"],
        "Nimroz": ["Zaranj", "Chakhansur", "Char Burjak", "Khash Rod", "Kang", "Dilaram"],
        "Nuristan": ["Parun", "Barg-e Matal", "Du Ab", "Kamdesh", "Mandol", "Nurgaram",
                     "Waygal", "Wama"],
        "Paktia": ["Gardez", "Ahmadabad", "Chamkani", "Dand Patan", "Garda Serai",
                   "Jaji", "Jani Khel", "Laja Mangal", "Mirzaka", "Patan", "Rohani Baba",
                   "Sayyid Karam", "Shwak", "Waza Zadran", "Zadran", "Zarmat"],
        "Paktika": ["Sharan", "Barmal", "Dila", "Gayan", "Gomal", "Jani Khel", "Mata Khan",
                    "Nika", "Urgun", "Sar Hawza", "Terwa", "Arghistan", "Wormamay",
                    "Wazakhwa", "Yusuf Khel", "Zarghun Shar", "Ziruk"],
        "Samangan": ["Aybak", "Dara-e Suf Bala", "Dara-e Suf Payin", "Fayzabad",
                     "Hazrati Sultan", "Khuram wa Sarbagh", "Ruyi Du Ab"],
        "Sar-e Pol": ["Sar-e Pol", "Balkhab", "Gosfandi", "Sozma Qala", "Sangcharak",
                      "Kohistanat", "Shirintagab"],
        "Takhar": ["Taloqan", "Ishkamish", "Bangui", "Baharak", "Chah Ab", "Chal",
                   "Dasht-e Qala", "Farkhar", "Hazar Sumuch", "Khwaja Bahauddin",
                   "Khwaja Ghar", "Namak Ab", "Rustaq", "Warsaj", "Yangi Qala"],
        "Uruzgan": ["Tarin Kot", "Chora", "Dehrawud", "Gizab", "Khas Uruzgan",
                    "Shahid Hassas", "Chenartu"],
        "Zabul": ["Qalat", "Arghandab", "Atghar", "Daychopan", "Mizan", "Naw Bahar",
                  "Shamulzayi", "Shinkay", "Shahjoy", "Tarnak wa Jaldak", "Sewri"]
    }

    streets = [
        "Main Road", "Bazaar Road", "University Road", "School Road", "Hospital Road",
        "Square Road", "Four-Way Junction", "Street No. 1", "Street No. 2",
        "District Road", "Administrative Road", "Mosque Road", "Karta Road",
        "Maiwand Avenue", "Ahmad Shah Baba Road", "Darulaman Road",
        "Khushal Khan Road", "Shahid Street", "Nader Khan Road", "Bazaar Alley",
        "Gul Froshi Street", "Pul-e Mahmud Khan Road", "Jalalabad Road",
        "Company Road", "Wazir Akbar Khan Street", "Shir Shah Suri Road",
        "Macrorayan Street", "District Block Road"
    ]

    def province(self):
        return random.choice(self.provinces)

    def city(self, province=None):
        if province is None:
            province = self.province()
        return random.choice(self.cities.get(province, [province]))

    def district(self, province=None):
        if province is None:
            province = self.province()
        return random.choice(self.districts.get(province, [province]))

    def street(self):
        return random.choice(self.streets)

    def postalcode(self):
        return str(random.randint(10000, 99999))

    def address(self):
        province = self.province()
        city = self.city(province)
        district = self.district(province)
        street = self.street()
        postal = self.postalcode()
        return f"{street}, District {district}, City {city}, {province}, {postal}"
