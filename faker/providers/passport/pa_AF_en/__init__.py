import random
from datetime import date, timedelta
from typing import Tuple, Optional

from faker.typing import SexLiteral
from .. import Provider as PassportProvider


class Provider(PassportProvider):
    """Implement passport provider for ``pa_AF`` locale in English."""

    # Afghan passport number formats
    passport_number_formats = (
        "A########",  # alphanumeric starting with A
        "P########",  # alphanumeric starting with P
        "########",  # numeric only
        "###-######",  # formatted with dash
    )

    # Afghan first names in English transliteration
    first_names = {
        "M": [

            'Ahmad', 'Mohammad', 'Abdullah', 'Noorullah', 'Khalid', 'Rahim', 'Farid', 'Nasir', 'Jamal', 'Tariq',
            'Wali', 'Yusuf', 'Zahir', 'Bashir', 'Daoud', 'Faisal', 'Gul', 'Hamid', 'Ismail', 'Javed',
            'Karim', 'Latif', 'Massoud', 'Noor', 'Omar', 'Qadir', 'Rashid', 'Safi', 'Talib', 'Wahid',
            'Baryalai', 'Spin', 'Tor', 'Zmarak', 'Khostai', 'Wazir', 'Miran', 'Sangar', 'Shinwari', 'Ghilzai',
            'Amanullah', 'Aziz', 'Bashir', 'Dawood', 'Ehsan', 'Fahim', 'Ghulam', 'Habib', 'Ibrahim', 'Jalal',
            'Kabeer', 'Lutfullah', 'Mansoor', 'Naim', 'Obaid', 'Pacha', 'Qais', 'Rahmat', 'Sattar', 'Tawab',
            'Umar', 'Valli', 'Wais', 'Yaqub', 'Zabi', 'Abdul', 'Ataullah', 'Bismillah', 'Chaman', 'Dastagir',
            'Ezat', 'Farooz', 'Ghaus', 'Hafiz', 'Inayat', 'Jahan', 'Khalil', 'Lal', 'Matin', 'Nazar',
            'Omar', 'Pir', 'Qurban', 'Rahim', 'Sami', 'Tahir', 'Ubaid', 'Vakil', 'Wali', 'Yar',
            'Zaman', 'Amin', 'Baz', 'Chinar', 'Dilawar', 'Ehsanullah', 'Fazal', 'Gulzar', 'Haji', 'Ilyas',
            'Juma', 'Khal', 'Lala', 'Mullah', 'Nek', 'Omid', 'Pacha', 'Qader', 'Rahman', 'Sadiq',
            'Talib', 'Ustad', 'Vafadar', 'Wazir', 'Younis', 'Zubair', 'Aashiq', 'Badar', 'Chiragh', 'Darya',
            'Eid', 'Faiz', 'Gohar', 'Hakim', 'Iqbal', 'Jamil', 'Khan', 'Liaqat', 'Momin', 'Nawab',
            'Obaidullah', 'Paiman', 'Qasim', 'Rafiq', 'Sahib', 'Taj', 'Usman', 'Vakel', 'Watan', 'Yaftali',
            'Zardad', 'Asad', 'Bahram', 'Chaman', 'Dost', 'Ebad', 'Fateh', 'Ghausuddin', 'Hidayat', 'Ishaq',
            'Jawad', 'Kamal', 'Lutf', 'Miran', 'Nur', 'Obaid', 'Parwiz', 'Qudrat', 'Rahimullah', 'Sabir',
            'Tawfiq', 'Umar', 'Vedat', 'Wahab', 'Yahya', 'Zalmai', 'Aimal', 'Babar', 'Chinar', 'Dil',
            'Emal', 'Farhad', 'Gulbuddin', 'Haji', 'Irfan', 'Jahangir', 'Khalid', 'Lal', 'Miran', 'Nek',
            'Omar', 'Pacha', 'Qais', 'Rahmatullah', 'Sahil', 'Tahir', 'Ubaidullah', 'Vasef', 'Waliullah', 'Yahya',
            'Zaki', 'Arif', 'Bilal', 'Chamanullah', 'Daud', 'Ehsan', 'Fazlullah', 'Gul', 'Hakim', 'Ibrahim',
            'Jamshed', 'Khalilullah', 'Latifullah', 'Momin', 'Nazir', 'Obaid', 'Pir', 'Qurban', 'Rahim', 'Samiullah',
            'Tajuddin', 'Usman', 'Vakil', 'Waris', 'Yasin', 'Zabih', 'Aslam', 'Bismillah', 'Chiragh', 'Dilawar',
            'Eid', 'Farooz', 'Ghaus', 'Hafizullah', 'Inayatullah', 'Jahan', 'Khalid', 'Lal', 'Matin', 'Nazar',
            'Obaidullah', 'Pacha', 'Qais', 'Rahim', 'Sami', 'Tahir', 'Ubaid', 'Vakil', 'Wali', 'Yar',
            'Zaman', 'Aminullah', 'Baz', 'Chinar', 'Dilawar', 'Ehsanullah', 'Fazal', 'Gulzar', 'Haji', 'Ilyas',
            'Juma', 'Khal', 'Lala', 'Mullah', 'Nek', 'Omid', 'Pacha', 'Qader', 'Rahman', 'Sadiq',
            'Talib', 'Ustad', 'Vafadar', 'Wazir', 'Younis', 'Zubair', 'Aashiq', 'Badar', 'Chiragh', 'Darya',
            'Eid', 'Faiz', 'Gohar', 'Hakim', 'Iqbal', 'Jamil', 'Khan', 'Liaqat', 'Momin', 'Nawab',
            'Obaidullah', 'Paiman', 'Qasim', 'Rafiq', 'Sahib', 'Taj', 'Usman', 'Vakel', 'Watan', 'Yaftali',
            'Zardad', 'Asad', 'Bahram', 'Chaman', 'Dost', 'Ebad', 'Fateh', 'Ghausuddin', 'Hidayat', 'Ishaq',
            'Jawad', 'Kamal', 'Lutf', 'Miran', 'Nur', 'Obaid', 'Parwiz', 'Qudrat', 'Rahimullah', 'Sabir',
            'Tawfiq', 'Umar', 'Vedat', 'Wahab', 'Yahya', 'Zalmai', 'Aimal', 'Babar', 'Chinar', 'Dil',
            'Emal', 'Farhad', 'Gulbuddin', 'Haji', 'Irfan', 'Jahangir', 'Khalid', 'Lal', 'Miran', 'Nek',
            'Omar', 'Pacha', 'Qais', 'Rahmatullah', 'Sahil', 'Tahir', 'Ubaidullah', 'Vasef', 'Waliullah', 'Yahya',
            'Zaki', 'Arif', 'Bilal', 'Chamanullah', 'Daud', 'Ehsan', 'Fazlullah', 'Gul', 'Hakim', 'Ibrahim',
            'Jamshed', 'Khalilullah', 'Latifullah', 'Momin', 'Nazir', 'Obaid', 'Pir', 'Qurban', 'Rahim', 'Samiullah',
            'Tajuddin', 'Usman', 'Vakil', 'Waris', 'Yasin', 'Zabih', 'Aslam', 'Bismillah', 'Chiragh', 'Dilawar',
            'Eid', 'Farooz', 'Ghaus', 'Hafizullah', 'Inayatullah', 'Jahan', 'Khalid', 'Lal', 'Matin', 'Nazar',
            'Obaidullah', 'Pacha', 'Qais', 'Rahim', 'Sami', 'Tahir', 'Ubaid', 'Vakil', 'Wali', 'Yar',
            'Zaman', 'Aminullah', 'Baz', 'Chinar', 'Dilawar', 'Ehsanullah', 'Fazal', 'Gulzar', 'Haji', 'Ilyas',
            'Juma', 'Khal', 'Lala', 'Mullah', 'Nek', 'Omid', 'Pacha', 'Qader', 'Rahman', 'Sadiq',
            'Talib', 'Ustad', 'Vafadar', 'Wazir', 'Younis', 'Zubair', 'Aashiq', 'Badar', 'Chiragh', 'Darya',
            'Eid', 'Faiz', 'Gohar', 'Hakim', 'Iqbal', 'Jamil', 'Khan', 'Liaqat', 'Momin', 'Nawab',
            'Obaidullah', 'Paiman', 'Qasim', 'Rafiq', 'Sahib', 'Taj', 'Usman', 'Vakel', 'Watan', 'Yaftali',
            'Zardad', 'Asad', 'Bahram', 'Chaman', 'Dost', 'Ebad', 'Fateh', 'Ghausuddin', 'Hidayat', 'Ishaq',
            'Jawad', 'Kamal', 'Lutf', 'Miran', 'Nur', 'Obaid', 'Parwiz', 'Qudrat', 'Rahimullah', 'Sabir',
            'Tawfiq', 'Umar', 'Vedat', 'Wahab', 'Yahya', 'Zalmai', 'Aimal', 'Babar', 'Chinar', 'Dil',
            'Emal', 'Farhad', 'Gulbuddin', 'Haji', 'Irfan',

         ],
        "F": [

            'Mariam', 'Fatima', 'Zahra', 'Laila', 'Nadia', 'Sabrina', 'Soraya', 'Parwin', 'Shukria', 'Fereshta',
            'Hadia', 'Jamila', 'Kamila', 'Nargis', 'Razia', 'Safia', 'Tamanna', 'Wajiha', 'Yasmin', 'Zarmina',
            'Gulalai', 'Mairman', 'SpinGul', 'Torpekai', 'Wazhma', 'Shamsia', 'Naghma', 'Mishal', 'Sanga', 'Zarghuna',
            'Aisha', 'Bibi', 'Chaman', 'Dilafroz', 'Emaan', 'Farahnaz', 'Gul', 'Hadiya', 'Iram', 'Jahanara',
            'Khadija', 'Lalzari', 'Mahnaz', 'Nabila', 'Ozra', 'Parwana', 'Qamar', 'Rahila', 'Sahar', 'Tabasum',
            'Uzma', 'Vida', 'Wahida', 'Yalda', 'Zainab', 'Afsana', 'Bakht', 'Chaman', 'Durdana', 'Eram',
            'Fauzia', 'Gulshan', 'Hawa', 'Iffat', 'Jamilah', 'Kalsoom', 'Laila', 'Masooma', 'Najiba', 'Omarah',
            'Palwasha', 'Qubra', 'Rahima', 'Sakina', 'Tahira', 'Urooj', 'Vida', 'Wajma', 'Yasira', 'Zarqa',
            'Aqila', 'Bushra', 'Chinar', 'Dilruba', 'Eshal', 'Faryal', 'Gulnar', 'Hena', 'Inayat', 'Jawhara',
            'Kawish', 'Lamar', 'Munira', 'Nasreen', 'Omaid', 'Parisa', 'Qudsia', 'Razia', 'Sadaf', 'Taslima',
            'Umaira', 'Vasila', 'Wazira', 'Yumna', 'Zeba', 'Anisa', 'Bahar', 'Cheen', 'Darya', 'Elham',
            'Farkhunda', 'Gulrukh', 'Hira', 'Iqra', 'Joya', 'Kiran', 'Lailuma', 'Mahro', 'Nazia', 'Orana',
            'Pari', 'Qirat', 'Rahmat', 'Saima', 'Tahera', 'Uzma', 'Vida', 'Warsa', 'Yasamin', 'Zulekha',
            'Arooj', 'Bano', 'Chamanara', 'Dilshad', 'Eman', 'Farzana', 'Gulbanu', 'Huma', 'Iram', 'Jannat',
            'Kashmala', 'Laili', 'Mahwish', 'Nargis', 'Omaima', 'Paiman', 'Qamaria', 'Roshna', 'Sughra', 'Tara',
            'Ulfat', 'Vida', 'Wahida', 'Yasmeen', 'Zara', 'Aalia', 'Bahar', 'Chaman', 'Dilbar', 'Ema',
            'Fahima', 'Gulbahar', 'Hina', 'Iram', 'Javeria', 'Khalida', 'Laila', 'Mahira', 'Naseem', 'Omaidah',
            'Parizad', 'Qudsia', 'Rukhsana', 'Saba', 'Tasneem', 'Uroosa', 'Vasima', 'Wajdan', 'Yasmin', 'Zareen',
            'Amina', 'Bibi', 'Chaman', 'Durdana', 'Eram', 'Fauzia', 'Gul', 'Hawa', 'Iffat', 'Jamilah',
            'Kalsoom', 'Laila', 'Masooma', 'Najiba', 'Omarah', 'Palwasha', 'Qubra', 'Rahima', 'Sakina', 'Tahira',
            'Urooj', 'Vida', 'Wajma', 'Yasira', 'Zarqa', 'Aqila', 'Bushra', 'Chinar', 'Dilruba', 'Eshal',
            'Faryal', 'Gulnar', 'Hena', 'Inayat', 'Jawhara', 'Kawish', 'Lamar', 'Munira', 'Nasreen', 'Omaid',
            'Parisa', 'Qudsia', 'Razia', 'Sadaf', 'Taslima', 'Umaira', 'Vasila', 'Wazira', 'Yumna', 'Zeba',
            'Anisa', 'Bahar', 'Cheen', 'Darya', 'Elham', 'Farkhunda', 'Gulrukh', 'Hira', 'Iqra', 'Joya',
            'Kiran', 'Lailuma', 'Mahro', 'Nazia', 'Orana', 'Pari', 'Qirat', 'Rahmat', 'Saima', 'Tahera',
            'Uzma', 'Vida', 'Warsa', 'Yasamin', 'Zulekha', 'Arooj', 'Bano', 'Chamanara', 'Dilshad', 'Eman',
            'Farzana', 'Gulbanu', 'Huma', 'Iram', 'Jannat', 'Kashmala', 'Laili', 'Mahwish', 'Nargis', 'Omaima',
            'Paiman', 'Qamaria', 'Roshna', 'Sughra', 'Tara', 'Ulfat', 'Vida', 'Wahida', 'Yasmeen', 'Zara',
            'Aalia', 'Bahar', 'Chaman', 'Dilbar', 'Ema', 'Fahima', 'Gulbahar', 'Hina', 'Iram', 'Javeria',
            'Khalida', 'Laila', 'Mahira', 'Naseem', 'Omaidah', 'Parizad', 'Qudsia', 'Rukhsana', 'Saba', 'Tasneem',
            'Uroosa', 'Vasima', 'Wajdan', 'Yasmin', 'Zareen', 'Amina', 'Bibi', 'Chaman', 'Durdana', 'Eram',
            'Fauzia', 'Gul', 'Hawa', 'Iffat', 'Jamilah', 'Kalsoom', 'Laila', 'Masooma', 'Najiba', 'Omarah',
            'Palwasha', 'Qubra', 'Rahima', 'Sakina', 'Tahira', 'Urooj', 'Vida', 'Wajma', 'Yasira', 'Zarqa',
            'Aqila', 'Bushra', 'Chinar', 'Dilruba', 'Eshal', 'Faryal', 'Gulnar', 'Hena', 'Inayat', 'Jawhara',
            'Kawish', 'Lamar', 'Munira', 'Nasreen', 'Omaid', 'Parisa', 'Qudsia',

         ]
    }

    # Afghan last names in English transliteration
    last_names = [

        'Khan', 'Ahmadzai', 'Mohammadi', 'Karimi', 'Hussaini', 'Rahmani', 'Sadiqi', 'Yousafzai', 'Popal', 'Ghilzai',
        'Durrani', 'Barakzai', 'Noori', 'Alkozai', 'Stanikzai', 'Zazai', 'Wardak', 'Kharoti', 'Hotak', 'Taraki',
        'Ahmadi', 'Alami', 'Balkhi', 'Danish', 'Ebrahimi', 'Faruqi', 'Ghani', 'Hakimi', 'Ibrahimi', 'Jami',
        'Arsalai', 'Atmar', 'Azizi', 'Bakhtari', 'Charkhi', 'Dost', 'Ehsas', 'Faqiri', 'Gul', 'Haidari',
        'Ismail', 'Jabarkhel', 'Kakar', 'Lodin', 'Mangal', 'Niazi', 'Omar', 'Paktin', 'Qaderi', 'Rasuli',
        'Safi', 'Tani', 'Umar', 'Wafa', 'Yaftali', 'Zadran', 'Achakzai', 'Babrakzai', 'Chamkani', 'Dawlatzai',
        'Esmat', 'Fahim', 'Ghafor', 'Habibi', 'Ishaqzai', 'Jalalzai', 'Kandahari', 'Lakanwal', 'Mahmood', 'Nazar',
        'Obaidullah', 'Parwani', 'Qaisrani', 'Rohani', 'Sangin', 'Tarakai', 'Usmani', 'Waziri', 'Yaqubi', 'Zabuli',
        'Afridi', 'Bangash', 'Chitrali', 'Daudzai', 'Eid', 'Farooz', 'Ghalib', 'Hassanzai', 'Ibrahimkhel', 'Jalalabad',
        'Khattak', 'Lashkari', 'Marwat', 'Nangarhar', 'Orakzai', 'Peshawari', 'Qandahari', 'Rahim', 'Shinwari', 'Turi',
        'Uthmanzai', 'Wazir', 'Yousuf', 'Zakhil', 'Amin', 'Babar', 'Chaman', 'Dawood', 'Eidgah', 'Farooq',
        'Ghaznavi', 'Habibullah', 'Ilyas', 'Jamal', 'Khalil', 'Latif', 'Miran', 'Nek', 'Obaid', 'Pacha',
        'Qais', 'Rahimullah', 'Sahib', 'Taj', 'Ubaid', 'Vakil', 'Wali', 'Yar', 'Zaman', 'Aminullah',
        'Baz', 'Chinar', 'Dilawar', 'Ehsanullah', 'Fazal', 'Gulzar', 'Haji', 'Ilyas', 'Juma', 'Khal',
        'Lala', 'Mullah', 'Nek', 'Omid', 'Pacha', 'Qader', 'Rahman', 'Sadiq', 'Talib', 'Ustad',
        'Vafadar', 'Wazir', 'Younis', 'Zubair', 'Aashiq', 'Badar', 'Chiragh', 'Darya', 'Eid', 'Faiz',
        'Gohar', 'Hakim', 'Iqbal', 'Jamil', 'Khan', 'Liaqat', 'Momin', 'Nawab', 'Obaidullah', 'Paiman',
        'Qasim', 'Rafiq', 'Sahib', 'Taj', 'Usman', 'Vakel', 'Watan', 'Yaftali', 'Zardad', 'Asad',
        'Bahram', 'Chaman', 'Dost', 'Ebad', 'Fateh', 'Ghausuddin', 'Hidayat', 'Ishaq', 'Jawad', 'Kamal',
        'Lutf', 'Miran', 'Nur', 'Obaid', 'Parwiz', 'Qudrat', 'Rahimullah', 'Sabir', 'Tawfiq', 'Umar',
        'Vedat', 'Wahab', 'Yahya', 'Zalmai', 'Aimal', 'Babar', 'Chinar', 'Dil', 'Emal', 'Farhad',
        'Gulbuddin', 'Haji', 'Irfan', 'Jahangir', 'Khalid', 'Lal', 'Miran', 'Nek', 'Omar', 'Pacha',
        'Qais', 'Rahmatullah', 'Sahil', 'Tahir', 'Ubaidullah', 'Vasef', 'Waliullah', 'Yahya', 'Zaki', 'Arif',
        'Bilal', 'Chamanullah', 'Daud', 'Ehsan', 'Fazlullah', 'Gul', 'Hakim', 'Ibrahim', 'Jamshed', 'Khalilullah',
        'Latifullah', 'Momin', 'Nazir', 'Obaid', 'Pir', 'Qurban', 'Rahim', 'Samiullah', 'Tajuddin', 'Usman',
        'Vakil', 'Waris', 'Yasin', 'Zabih', 'Aslam', 'Bismillah', 'Chiragh', 'Dilawar', 'Eid', 'Farooz',
        'Ghaus', 'Hafizullah', 'Inayatullah', 'Jahan', 'Khalid', 'Lal', 'Matin', 'Nazar', 'Obaidullah', 'Pacha',
        'Qais', 'Rahim', 'Sami', 'Tahir', 'Ubaid', 'Vakil', 'Wali', 'Yar', 'Zaman', 'Aminullah',
        'Baz', 'Chinar', 'Dilawar', 'Ehsanullah', 'Fazal', 'Gulzar', 'Haji', 'Ilyas', 'Juma', 'Khal',
        'Lala', 'Mullah', 'Nek', 'Omid', 'Pacha', 'Qader', 'Rahman', 'Sadiq', 'Talib', 'Ustad',
        'Vafadar', 'Wazir', 'Younis', 'Zubair', 'Aashiq', 'Badar', 'Chiragh', 'Darya', 'Eid', 'Faiz',
        'Gohar', 'Hakim', 'Iqbal', 'Jamil', 'Khan', 'Liaqat', 'Momin', 'Nawab', 'Obaidullah', 'Paiman',
        'Qasim', 'Rafiq', 'Sahib', 'Taj', 'Usman', 'Vakel', 'Watan', 'Yaftali', 'Zardad', 'Asad',
        'Bahram', 'Chaman', 'Dost', 'Ebad', 'Fateh', 'Ghausuddin', 'Hidayat', 'Ishaq', 'Jawad', 'Kamal',
        'Lutf', 'Miran', 'Nur', 'Obaid', 'Parwiz', 'Qudrat',

     ]

    def passport_owner(self, gender: SexLiteral = "M") -> Tuple[str, str]:
        first_name = random.choice(self.first_names.get(gender, self.first_names["M"]))
        last_name = random.choice(self.last_names)
        return first_name, last_name

    def passport_dates(self, birthday: date = date.today()) -> Tuple[date, date]:
        """Generate issue and expiry dates for Afghan passport."""
        today = date.today()
        age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

        if age < 5:
            expiry_years = 5
            issue_date = self.generator.date_between_dates(birthday, today)
        elif age < 16:
            expiry_years = 5
            min_issue = birthday + timedelta(days=5 * 365)
            issue_date = self.generator.date_between_dates(min_issue, today)
        elif age >= 26:
            expiry_years = 10
            min_issue = today - timedelta(days=expiry_years * 365)
            issue_date = self.generator.date_between_dates(min_issue, today)
        else:
            expiry_years = 26 - age
            min_issue = birthday + timedelta(days=16 * 365)
            issue_date = self.generator.date_between_dates(min_issue, today)

        expiry_date = issue_date.replace(year=issue_date.year + expiry_years)

        # Adjust Feb 29 for non-leap years
        if issue_date.month == 2 and issue_date.day == 29:
            if not self._is_leap_year(expiry_date.year):
                expiry_date = expiry_date.replace(day=28)

        return issue_date, expiry_date

    def _is_leap_year(self, year: int) -> bool:
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def passport_gender(self, seed: int = 0) -> SexLiteral:
        if seed != 0:
            random.seed(seed)
        genders: list[SexLiteral] = ["M", "F", "X"]
        return random.choices(genders, weights=[0.493, 0.493, 0.014], k=1)[0]