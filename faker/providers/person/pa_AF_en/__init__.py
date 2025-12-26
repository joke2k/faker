from faker.providers.person import Provider as PersonProvider
import random
"""
Afghanistan Pashto (English Transliteration) Locale for Faker

This package provides Afghan Pashto and Tajik personal names written in English
transliteration, including support for male and female first names, last names,
prefixes, and suffixes.
"""


class Provider(PersonProvider):

    prefixes_male = [ 'Mir', 'Sardar', 'Malik', 'Khan', 'Haji', 'Mullah', 'Ustad', 'Mawlawi', 'Sheikh', 'Amir',
        'Sultan', 'Shah', 'Padshah', 'Wazir', 'Mufti', 'Qazi', 'Hafiz', 'Maulvi', 'Al-Haj', 'Sayyid',
        'Mirza', 'Baba', 'Pir', 'Ghazi', 'Sahib', 'Jan', 'Agha', 'Dost', 'Aziz', 'Karim']
    prefixes_female = [
        "Peghla",  # Miss (used for unmarried young women)
        "Mairman",  # Mrs./Madam (formal title for a married or adult woman)
        "Aghele",  # Formal prefix equivalent to 'Lady' or 'Madam'
        "Bibi",  # Respectful title for older women or maternal figures
        "Jan",  # Respectful suffix added after a name (e.g., 'Malala Jan')
        "Tror",  # 'Aunt' (maternal or paternal); used respectfully for older women
        "Nia",  # 'Grandmother'; used as an honorific for elderly women
        "Khor",  # 'Sister'; a common respectful way to address a peer
        "Mor",  # 'Mother'; used to address senior women with high respect
        "Muhtarama"  # 'Respected' (feminine form); used in highly formal contexts
    ]

    suffixes = [ 'zai', 'khel', 'wal', 'dost', 'ullah', 'uddin', 'bakhsh', 'yar', 'jan', 'dad',
        'pur', 'zada', 'i', 'ian', 'far', 'niaz', 'mand', 'yar', 'baz', 'war',
        'dil', 'gul', 'noor', 'bahar', 'shah', 'khan', 'malik', 'sardar', 'wazir', 'amir']

    pashto_male_first_names = [
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
        'Zaman', 'Aminullah', 'Baz', 'Chinar', 'Dilawar', 'Ehsanullah', 'Fazal', 'Gulzar', 'Haji', 'Ilyas','Abasin', 'Abdul',
        'Ahmed', 'Aimal', 'Ali', 'Alam', 'Alamzeb', 'Amail', 'Amu', 'Andam', 'Angar', 'Armaghan', 'Arman', 'Arsalan',
        'Aryan', 'Asfand', 'Asfandyar', 'Atal', 'Atsak', 'Aurang', 'Awalmir', 'Azlan', 'Azmaray', 'Babak', 'Babrak',
        'Bacha', 'Badam', 'Bahram', 'Bahramand', 'Bahrawar', 'Bakht', 'Bakht Rawan', 'Bakht Awar', 'Balach', 'Balay',
        'Barlas', 'Baryal', 'Baryalai', 'Baseer', 'Batoor', 'Baz', 'Bazgar', 'Bazir', 'Behroz', 'Beltoon', 'Beroj',
        'Chargul', 'Chinar', 'Dagar', 'Darab', 'Darman', 'Darwesh', 'Darya', 'Daryab', 'Daulat', 'Dawar', 'Diar',
        'Dilawar', 'Droon', 'Elam', 'Farhang', 'Farihund', 'Gahez', 'Gedi', 'Ghairat', 'Ghakhtalay', 'Ghalji', 'Ghamay',
        'Gharsanay', 'Ghatool', 'Ghazan', 'Ghazin', 'Ghorzang', 'Ghunchagul', 'Ghurghusht', 'Gogal', 'Gorbat', 'Grant',
        'Gul', 'Gul Baz', 'Gul Jan', 'Gul Mast', 'Gul Rang', 'Gul Yar', 'Gul Zaman', 'Gulab', 'Gulzar', 'Hask',
        'Helmand', 'Hewand', 'Hukam', 'Izat', 'Janan', 'Janat Gul', 'Jandol', "Kakay'", 'Karlani', 'Karmal', 'Karwan',
        'Khagalay', 'Khaista', 'Khak', 'Khalo', 'Khan', 'Khandawar', 'Khialay', 'Khog', 'Khushal', 'Khushdil',
        'Khwazun', 'Khyber', 'Kochai', 'Kushan', 'Lajbar', 'Lashkar', 'Lal', 'Lawang', 'Lawangin', 'Lmar', 'Liwal',
        'Mairanay', 'Maiwand', 'Malang', 'Malook', 'Malyar', 'Manan', 'Mangal', 'Marghoz', 'Marjan', 'Marwand',
        'Mashal', 'Mateen', 'Mehtar', 'Minatbar', 'Mirwais', 'Mirzal', 'Mohambar', 'Muhammad', 'Nang', 'Nangial',
        'Noomyalay', 'Nufail', 'Olas', 'Olasyar', 'Paiman', 'Pamir', 'Pashtoon', 'Pason', 'Pasoon', 'Patang', 'Patman',
        'Patwal', 'Patyal', 'Paywastun', 'Pelabo', 'Perzo', 'Pohand', 'Pordal', 'Powneda', 'Psarlay', 'Qajeer Gul',
        'Qalandar', 'Rahamdil', 'Rangeen', 'Reday', 'Reshteen', 'Roshan', 'Rustam', 'Sabawoon', 'Sadin', 'Sahar',
        'Sahar Gul', 'Sahim', 'Saifur', 'Salar', 'Samandar', 'Samoon', 'Samsor', 'Sangar', 'Sangin', 'Sangrez',
        'Sanobar', 'Sarban', 'Sarbaz', 'Sardar', 'Sartor', 'Sayel', 'Selab', 'Selani', 'Shahsawar', 'Shahzar', 'Shamal',
        'Shamshad', 'Sher', 'Sherdil', 'Sherin', 'Shin Gul', 'Shindi Gul', 'Shino', 'Shpol', 'Shpoon', 'Shuja',
        'Sibghatullah', 'Sifat', 'Sikandar', 'Sohrab', 'Sparlay', 'Spetselay', 'Spin', 'Spin Gul', 'Spinzar', 'Storay',
        'Sur Gul', 'Suweil', 'Syal', 'Taban', 'Tanim', 'Taroon', 'Tawas', 'Teri', 'Tofan', 'Tolwak', 'Tor Gul',
        'Toryal', 'Toti', 'Turan', 'Turialai', 'Wadaan', 'Wais', 'Wakdar', 'Wakman', 'Wali', 'Yama', 'Yaqut', 'Yoon',
        'Zafran', 'Zalaan', 'Zaland', 'Zalmay', 'Zapran', 'Zar Gul', 'Zarwali', 'Zarak', 'Zaram', 'Zarang', 'Zarbat',
        'Zardab', 'Zardad', 'Zargar', 'Zarghun', 'Zarhawar', 'Zarhgay', 'Zarin', 'Zarkanay', 'Zarlesh', 'Zarmast',
        'Zarnosh', 'Zaryab', 'Zawaar', 'Zawar', 'Zgard', 'Ziar', 'Ziarmal', 'Zigar', 'Zmarak', 'Zmaray', 'Zorak',
        'Zorawar', 'Zwak', 'Zwandun', 'Afia', 'Aghala', 'Ambrin', 'Angeza', 'Anar', 'Ara', 'Apana', 'Aryana', 'Badrai',
        'Bakht Awara', 'Bala Nashta', 'Balbala', 'Banafsha', 'Barsala', 'Bazira', 'Benazira', 'Bibi', 'Bibi Rokhana',
        'Brekhna', 'Diwa', 'Durkhanai', 'Farishta', 'Gabina', 'Galai', 'Ghatola', 'Ghorashka', 'Ghotai', 'Ghuncha',
        'Gorgora', 'Grana', 'Gul Bano', 'Gul Ghotai', 'Gul Lakhta', 'Gul Makai', 'Gul Mina', 'Gul Panrha', 'Gul Sangha',
        'Gul Warin', 'Gulalai', 'Gulchin', 'Gulnar', 'Hala', 'Helai', 'Hila', 'Hina', 'Husay', 'Kashmala', 'Khaista',
        'Khaperai', 'Kharo', 'Khatol', 'Khkulay', 'Khush Bakhta', 'Khwaga', 'Kochai', 'Kontara', 'Laila', 'Lailuma',
        'Lakhta', 'Lalma', 'Lalzari', 'Lamba', 'Lawanga', 'Lema', 'Mahjabin', 'Mahnur', 'Mahzala', 'Malalai',
        'Malghalara', 'Mina', 'Mukai', 'Munawara', 'Murchakai', 'Muska', 'Naghma', 'Nangialai', 'Narenja', 'Natkai',
        'Nawyata', 'Nazanina', 'Nazdana', 'Nazo', 'Niazmina', 'Orbakhta', 'Orbala', 'Orzala', 'Palwasha', 'Panra',
        'Parghunda', 'Pariwash', 'Parkha', 'Pashmina', 'Patasa', 'Peghra', 'Perkha', 'Pokha', 'Ranrha', 'Rayan',
        'Rekhmina', 'Reshtina', 'Roshina', 'Saba', 'Salgay', 'Sandara', 'Sanga', 'Sangina', 'Selai', 'Senzela',
        'Shahgalay', 'Shahay', 'Shahlalai', 'Shamla', 'Shandana', 'Shanzai', 'Shaperai', 'Shastai', 'Shazmina',
        'Sherin', 'Shinkai', 'Shinogai', 'Shughla', 'Spalmay', 'Sparghai', 'Spezala', 'Spozmai', 'Storai', 'Tabana',
        'Talwasa', 'Tanima', 'Tor Pikai', 'Ugay', 'Wadaana', 'Wagma', 'Wahida', 'Wajia', 'Warda', 'Wawrina', 'Wranga',
        'Wreshmin', 'Zainba', 'Zaituna', 'Zakia', 'Zala', 'Zalanda', 'Zaloba', 'Zamba', 'Zar Bibi', 'Zar Masta',
        'Zar Mina', 'Zar Wareen', 'Zarbaha', 'Zareena', 'Zareesh', 'Zarghuna', 'Zarka', 'Zar Lakhta', 'Zar Sanga',
        'Zarshala', 'Zartaj', 'Zhala', 'Zhalai', 'Zohal', 'Zufash'
    ]

    pashto_female_first_names = [
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
        'Afia', 'Badrai', 'Diwa', 'Farishta', 'Gabina', 'Hala', 'Kashmala', 'Laila', 'Mahjabin',
        'Naghma', 'Orbakhta', 'Palwasha', 'Ranrha', 'Saba', 'Tabana', 'Ugay', 'Wadaana', 'Zainba'
    ]

    tajik_male_first_names = [
        'Farhad', 'Rustam', 'Babur', 'Jamshid', 'Kawoon', 'Sohrab', 'Bahram', 'Khosrow', 'Nadir', 'Yama',
        'Abdul', 'Ali', 'Hassan', 'Hussein', 'Jafar', 'Mahdi', 'Mustafa', 'Reza', 'Said', 'Yasin',
        'Farid', 'Hafiz', 'Iqbal', 'Jalal', 'Khalil', 'Latif', 'Nazar', 'Qasim', 'Rahim', 'Samir',
        'Ahmad', 'Bashir', 'Davlat', 'Ehsan', 'Fahim', 'Ghaffar', 'Habib', 'Iskandar', 'Jamshed', 'Kamran',
        'Lutfullah', 'Mansur', 'Nemat', 'Omid', 'Parviz', 'Qodir', 'Rahmat', 'Safar', 'Taj', 'Umar',
        'Vohid', 'Wahid', 'Yaqub', 'Zafar', 'Anwar', 'Bakhtiar', 'Daler', 'Eraj', 'Firuz', 'Gul',
        'Hamza', 'Iraj', 'Jawid', 'Karam', 'Lutf', 'Matin', 'Nur', 'Otabek', 'Payam', 'Qais',
        'Rashid', 'Said', 'Tahir', 'Umed', 'Vali', 'Wasi', 'Yusuf', 'Zubair', 'Aslam', 'Bismillah',
        'Daud', 'Emon', 'Fayz', 'Ghiyas', 'Hadi', 'Ismoil', 'Javohir', 'Khalid', 'Lal', 'Muhsin',
        'Nasim', 'Obid', 'Parwaiz', 'Qurban', 'Rauf', 'Sabur', 'Tawhid', 'Ubayd', 'Vafo', 'Wajid',
        'Yahyo', 'Zayn', 'Abror', 'Bahrom', 'Davron', 'Elyor', 'Farkhod', 'Gulom', 'Hikmat', 'Ilhom',
        'Jahongir', 'Khurshed', 'Loik', 'Murod', 'Nizom', 'Olim', 'Pardaev', 'Qobil', 'Ravshan', 'Safar',
        'Tojiddin', 'Ulugbek', 'Vosil', 'Wahdat', 'Yorqin', 'Zafar', 'Alisher', 'Bekzod', 'Dilshod', 'Eshon',
        'Firdavs', 'Gulbahor', 'Hoshim', 'Ibrohim', 'Jalol', 'Komron', 'Laziz', 'Mirzo', 'Nozim', 'Otabek',
        'Parviz', 'Qahhor', 'Rustam', 'Sardor', 'Temur', 'Uchqun', 'Vahob', 'Wahob', 'Yodgor', 'Ziyo',
        'Akmal', 'Bobur', 'Doston', 'Erkin', 'Fayoz', 'Gulnazar', 'Husan', 'Isfandiyor', 'Javlon', 'Kamol',
        'Lutfi', 'Muhammad', 'Nurali', 'Otabek', 'Pahlavon', 'Qodir', 'Rahim', 'Siroj', 'Tolib', 'Umid',
        'Vahid', 'Wahid', 'Yigitali', 'Zafar', 'Abdullo', 'Bahodir', 'Davlat', 'Eshmurod', 'Farkhod', 'Gul',
        'Hamid', 'Ixtiyor', 'Jahongir', 'Khayot', 'Laziz', 'Muhammad', 'Nizom', 'Olimjon', 'Parviz', 'Qobil',
        'Rashid', 'Safar', 'Tohir', 'Umidjon', 'Vohid', 'Wahid', 'Yodgor', 'Zafar', 'Akbar', 'Bobojon',
        'Dilshod', 'Eraj', 'Fayzullo', 'Gulom', 'Hoshim', 'Ibrohim', 'Jalol', 'Komron', 'Laziz', 'Mirzo',
        'Nozim', 'Otabek', 'Parviz', 'Qahhor', 'Rustam', 'Sardor', 'Temur', 'Uchqun', 'Vahob', 'Wahob',
        'Yodgor', 'Ziyo', 'Akmal', 'Bobur', 'Doston', 'Erkin', 'Fayoz', 'Gulnazar', 'Husan', 'Isfandiyor',
        'Javlon', 'Kamol', 'Lutfi', 'Muhammad', 'Nurali', 'Otabek', 'Pahlavon', 'Qodir', 'Rahim', 'Siroj',
        'Tolib', 'Umid', 'Vahid', 'Wahid', 'Yigitali', 'Zafar', 'Abdullo', 'Bahodir', 'Davlat', 'Eshmurod',
        'Farkhod', 'Gul', 'Hamid', 'Ixtiyor', 'Jahongir', 'Khayot', 'Laziz', 'Muhammad', 'Nizom', 'Olimjon',
        'Parviz', 'Qobil', 'Rashid', 'Safar', 'Tohir', 'Umidjon', 'Vohid', 'Wahid', 'Yodgor', 'Zafar',
        'Akbar', 'Bobojon', 'Dilshod', 'Eraj', 'Fayzullo', 'Gulom', 'Hoshim', 'Ibrohim', 'Jalol', 'Komron',
        'Laziz', 'Mirzo', 'Nozim', 'Otabek', 'Parviz', 'Qahhor', 'Rustam', 'Sardor', 'Temur', 'Uchqun',
        'Vahob', 'Wahob', 'Yodgor', 'Ziyo', 'Akmal', 'Bobur', 'Doston', 'Erkin', 'Fayoz', 'Gulnazar',
        'Husan', 'Isfandiyor', 'Javlon', 'Kamol', 'Lutfi', 'Muhammad', 'Nurali', 'Otabek', 'Pahlavon', 'Qodir',
        'Rahim', 'Siroj', 'Tolib', 'Umid', 'Vahid', 'Wahid', 'Yigitali', 'Zafar', 'Abdullo', 'Bahodir',
        'Davlat', 'Eshmurod', 'Farkhod', 'Gul', 'Hamid', 'Ixtiyor', 'Jahongir', 'Khayot', 'Laziz', 'Muhammad',
        'Nizom', 'Olimjon', 'Parviz', 'Qobil', 'Rashid', 'Safar', 'Tohir', 'Umidjon', 'Vohid', 'Wahid',
        'Yodgor', 'Zafar', 'Akbar', 'Bobojon', 'Dilshod', 'Eraj', 'Fayzullo', 'Gulom', 'Hoshim', 'Ibrohim',
        'Jalol', 'Komron', 'Laziz', 'Mirzo', 'Nozim', 'Otabek', 'Parviz', 'Qahhor', 'Rustam', 'Sardor',
        'Temur', 'Uchqun', 'Vahob', 'Wahob', 'Yodgor', 'Ziyo', 'Akmal', 'Bobur', 'Doston', 'Erkin',
        'Fayoz', 'Gulnazar', 'Husan', 'Isfandiyor', 'Javlon', 'Kamol', 'Lutfi', 'Muhammad', 'Nurali', 'Otabek',
        'Pahlavon', 'Qodir', 'Rahim', 'Siroj', 'Tolib', 'Umid', 'Vahid', 'Wahid', 'Yigitali', 'Zafar',
        'Abdullo', 'Bahodir', 'Davlat', 'Eshmurod', 'Farkhod', 'Gul', 'Hamid', 'Ixtiyor', 'Jahongir', 'Khayot',
        'Laziz', 'Muhammad', 'Nizom', 'Olimjon', 'Parviz', 'Qobil', 'Rashid', 'Safar', 'Tohir', 'Umidjon',
        'Vohid', 'Wahid', 'Yodgor', 'Zafar', 'Akbar', 'Bobojon', 'Dilshod', 'Eraj', 'Fayzullo', 'Gulom',
        'Hoshim', 'Ibrohim', 'Jalol', 'Komron', 'Laziz', 'Mirzo', 'Nozim', 'Otabek', 'Parviz', 'Qahhor',
        'Rustam', 'Sardor', 'Temur', 'Uchqun', 'Vahob', 'Wahob', 'Yodgor', 'Ziyo', 'Akmal', 'Bobur',
        'Doston', 'Erkin', 'Fayoz', 'Gulnazar', 'Husan', 'Isfandiyor', 'Javlon', 'Kamol', 'Lutfi', 'Muhammad',
        'Nurali', 'Otabek', 'Pahlavon', 'Qodir', 'Rahim', 'Siroj', 'Tolib', 'Umid', 'Vahid', 'Wahid',
        'Yigitali', 'Zafar', 'Abdullo', 'Bahodir', 'Davlat', 'Eshmurod', 'Farkhod', 'Gul', 'Hamid', 'Ixtiyor',
        'Jahongir', 'Khayot', 'Laziz', 'Muhammad', 'Nizom', 'Olimjon', 'Parviz', 'Qobil', 'Rashid', 'Safar',
        'Tohir', 'Umidjon', 'Vohid', 'Wahid', 'Yodgor', 'Zafar', 'Akbar', 'Bobojon', 'Dilshod', 'Eraj',
        'Fayzullo', 'Gulom', 'Hoshim', 'Ibrohim', 'Jalol', 'Komron', 'Laziz', 'Mirzo', 'Nozim', 'Otabek',
        'Parviz', 'Qahhor', 'Rustam', 'Sardor', 'Temur', 'Uchqun', 'Vahob', 'Wahob', 'Yodgor', 'Ziyo',
        'Akmal', 'Bobur', 'Doston', 'Erkin', 'Fayoz', 'Gulnazar', 'Husan', 'Isfandiyor', 'Javlon', 'Kamol',
        'Lutfi', 'Muhammad', 'Nurali', 'Otabek', 'Pahlavon', 'Qodir', 'Rahim', 'Siroj', 'Tolib', 'Umid',
        'Vahid', 'Wahid', 'Yigitali', 'Zafar', 'Abdullo', 'Bahodir', 'Davlat', 'Eshmurod', 'Farkhod', 'Gul',
        'Hamid', 'Ixtiyor', 'Jahongir', 'Khayot', 'Laziz', 'Muhammad', 'Nizom', 'Olimjon', 'Parviz', 'Qobil',
        'Rashid', 'Safar', 'Tohir', 'Umidjon', 'Vohid', 'Wahid', 'Yodgor', 'Zafar', 'Akbar', 'Bobojon',
        'Dilshod', 'Eraj', 'Fayzullo', 'Gulom', 'Hoshim', 'Ibrohim', 'Jalol', 'Komron', 'Laziz', 'Mirzo',
        'Nozim', 'Otabek', 'Parviz', 'Qahhor', 'Rustam', 'Sardor', 'Temur', 'Uchqun', 'Vahob', 'Wahob',
        'Yodgor', 'Ziyo', 'Akmal', 'Bobur', 'Doston', 'Erkin', 'Fayoz', 'Gulnazar', 'Husan', 'Isfandiyor',
        'Javlon', 'Kamol', 'Lutfi', 'Muhammad', 'Nurali', 'Otabek', 'Pahlavon', 'Qodir', 'Rahim', 'Siroj',
        'Tolib', 'Umid', 'Vahid', 'Wahid', 'Yigitali', 'Zafar', 'Abdullo', 'Bahodir', 'Davlat', 'Eshmurod',
        'Farkhod', 'Gul', 'Hamid', 'Ixtiyor', 'Jahongir', 'Khayot', 'Laziz', 'Muhammad', 'Nizom', 'Olimjon',
        'Parviz', 'Qobil', 'Rashid', 'Safar', 'Tohir', 'Umidjon', 'Vohid', 'Wahid', 'Yodgor', 'Zafar'
    ]

    tajik_female_first_names = [
        'Farzana', 'Shabnam', 'Nahid', 'Parwin', 'Roxana', 'Scheherazade', 'Gohar', 'Laleh', 'Mahnaz', 'Niloofar',
        'Masooma', 'Nafisa', 'Rahima', 'Sakina', 'Zainab', 'Mursal', 'Fahima', 'Habiba', 'Khadija', 'Laila',
        'Maryam', 'Nadia', 'Razia', 'Saida', 'Yasmin', 'Aisha', 'Bibi', 'Dilafruz', 'Eram', 'Farahnaz',
        'Gul', 'Hadiya', 'Iram', 'Jahanara', 'Khalida', 'Lalzari', 'Mahnaz', 'Nabila', 'Ozra', 'Parwana',
        'Qamar', 'Rahila', 'Sahar', 'Tabasum', 'Uzma', 'Vida', 'Wahida', 'Yalda', 'Zainab', 'Afsana',
        'Bakht', 'Chaman', 'Durdana', 'Eram', 'Fauzia', 'Gulshan', 'Hawa', 'Iffat', 'Jamilah', 'Kalsoom',
        'Laila', 'Masooma', 'Najiba', 'Omarah', 'Palwasha', 'Qubra', 'Rahima', 'Sakina', 'Tahira', 'Urooj',
        'Vida', 'Wajma', 'Yasira', 'Zarqa', 'Aqila', 'Bushra', 'Chinar', 'Dilruba', 'Eshal', 'Faryal',
        'Gulnar', 'Hena', 'Inayat', 'Jawhara', 'Kawish', 'Lamar', 'Munira', 'Nasreen', 'Omaid', 'Parisa',
        'Qudsia', 'Razia', 'Sadaf', 'Taslima', 'Umaira', 'Vasila', 'Wazira', 'Yumna', 'Zeba', 'Anisa',
        'Bahar', 'Cheen', 'Darya', 'Elham', 'Farkhunda', 'Gulrukh', 'Hira', 'Iqra', 'Joya', 'Kiran',
        'Lailuma', 'Mahro', 'Nazia', 'Orana', 'Pari', 'Qirat', 'Rahmat', 'Saima', 'Tahera', 'Uzma',
        'Vida', 'Warsa', 'Yasamin', 'Zulekha', 'Arooj', 'Bano', 'Chamanara', 'Dilshad', 'Eman', 'Farzana',
        'Gulbanu', 'Huma', 'Iram', 'Jannat', 'Kashmala', 'Laili', 'Mahwish', 'Nargis', 'Omaima', 'Paiman',
        'Qamaria', 'Roshna', 'Sughra', 'Tara', 'Ulfat', 'Vida', 'Wahida', 'Yasmeen', 'Zara', 'Aalia',
        'Bahar', 'Chaman', 'Dilbar', 'Ema', 'Fahima', 'Gulbahar', 'Hina', 'Iram', 'Javeria', 'Khalida',
        'Laila', 'Mahira', 'Naseem', 'Omaidah', 'Parizad', 'Qudsia', 'Rukhsana', 'Saba', 'Tasneem', 'Uroosa',
        'Vasima', 'Wajdan', 'Yasmin', 'Zareen', 'Amina', 'Bibi', 'Chaman', 'Durdana', 'Eram', 'Fauzia',
        'Gul', 'Hawa', 'Iffat', 'Jamilah', 'Kalsoom', 'Laila', 'Masooma', 'Najiba', 'Omarah', 'Palwasha',
        'Qubra', 'Rahima', 'Sakina', 'Tahira', 'Urooj', 'Vida', 'Wajma', 'Yasira', 'Zarqa', 'Aqila',
        'Bushra', 'Chinar', 'Dilruba', 'Eshal', 'Faryal', 'Gulnar', 'Hena', 'Inayat', 'Jawhara', 'Kawish',
        'Lamar', 'Munira', 'Nasreen', 'Omaid', 'Parisa', 'Qudsia', 'Razia', 'Sadaf', 'Taslima', 'Umaira',
        'Vasila', 'Wazira', 'Yumna', 'Zeba', 'Anisa', 'Bahar', 'Cheen', 'Darya', 'Elham', 'Farkhunda',
        'Gulrukh', 'Hira', 'Iqra', 'Joya', 'Kiran', 'Lailuma', 'Mahro', 'Nazia', 'Orana', 'Pari',
        'Qirat', 'Rahmat', 'Saima', 'Tahera', 'Uzma', 'Vida', 'Warsa', 'Yasamin', 'Zulekha', 'Arooj',
        'Bano', 'Chamanara', 'Dilshad', 'Eman', 'Farzana', 'Gulbanu', 'Huma', 'Iram', 'Jannat', 'Kashmala',
        'Laili', 'Mahwish', 'Nargis', 'Omaima', 'Paiman', 'Qamaria', 'Roshna', 'Sughra', 'Tara', 'Ulfat',
        'Vida', 'Wahida', 'Yasmeen', 'Zara', 'Aalia', 'Bahar', 'Chaman', 'Dilbar', 'Ema', 'Fahima',
        'Gulbahar', 'Hina', 'Iram', 'Javeria', 'Khalida', 'Laila', 'Mahira', 'Naseem', 'Omaidah', 'Parizad',
        'Qudsia', 'Rukhsana', 'Saba', 'Tasneem', 'Uroosa', 'Vasima', 'Wajdan', 'Yasmin', 'Zareen', 'Amina',
        'Bibi', 'Chaman', 'Durdana', 'Eram', 'Fauzia', 'Gul', 'Hawa', 'Iffat', 'Jamilah', 'Kalsoom',
        'Laila', 'Masooma', 'Najiba', 'Omarah', 'Palwasha', 'Qubra', 'Rahima', 'Sakina', 'Tahira', 'Urooj',
        'Vida', 'Wajma', 'Yasira', 'Zarqa', 'Aqila', 'Bushra', 'Chinar', 'Dilruba', 'Eshal', 'Faryal',
        'Gulnar', 'Hena', 'Inayat', 'Jawhara', 'Kawish', 'Lamar', 'Munira', 'Nasreen', 'Omaid', 'Parisa',
        'Qudsia', 'Razia', 'Sadaf', 'Taslima', 'Umaira', 'Vasila', 'Wazira', 'Yumna', 'Zeba', 'Anisa',
        'Bahar', 'Cheen', 'Darya', 'Elham', 'Farkhunda', 'Gulrukh', 'Hira', 'Iqra', 'Joya', 'Kiran',
        'Lailuma', 'Mahro', 'Nazia', 'Orana', 'Pari', 'Qirat', 'Rahmat', 'Saima', 'Tahera', 'Uzma',
        'Vida', 'Warsa', 'Yasamin', 'Zulekha', 'Arooj', 'Bano', 'Chamanara', 'Dilshad', 'Eman', 'Farzana',
        'Gulbanu', 'Huma', 'Iram', 'Jannat', 'Kashmala', 'Laili', 'Mahwish', 'Nargis', 'Omaima', 'Paiman',
        'Qamaria', 'Roshna', 'Sughra', 'Tara', 'Ulfat', 'Vida', 'Wahida', 'Yasmeen', 'Zara', 'Aalia',
        'Bahar', 'Chaman', 'Dilbar', 'Ema', 'Fahima', 'Gulbahar', 'Hina', 'Iram', 'Javeria', 'Khalida',
        'Laila', 'Mahira', 'Naseem', 'Omaidah', 'Parizad', 'Qudsia', 'Rukhsana', 'Saba', 'Tasneem', 'Uroosa',
        'Vasima', 'Wajdan', 'Yasmin', 'Zareen', 'Amina', 'Bibi', 'Chaman', 'Durdana', 'Eram', 'Fauzia',
        'Gul', 'Hawa', 'Iffat', 'Jamilah', 'Kalsoom', 'Laila', 'Masooma', 'Najiba', 'Omarah', 'Palwasha',
        'Qubra', 'Rahima', 'Sakina', 'Tahira', 'Urooj', 'Vida', 'Wajma', 'Yasira', 'Zarqa', 'Aqila',
        'Bushra', 'Chinar', 'Dilruba', 'Eshal', 'Faryal', 'Gulnar', 'Hena', 'Inayat', 'Jawhara', 'Kawish'
    ]

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
        'Lutf', 'Miran', 'Nur', 'Obaid', 'Parwiz', 'Qudrat', 'Rahimullah', 'Sabir', 'Tawfiq', 'Umar',
        'Vedat', 'Wahab', 'Yahya', 'Zalmai', 'Aimal', 'Babar', 'Chinar', 'Dil', 'Emal', 'Farhad',
        'Gulbuddin', 'Haji', 'Irfan', 'Jahangir', 'Khalid', 'Lal', 'Miran', 'Nek', 'Omar', 'Pacha',
        'Qais', 'Rahmatullah', 'Sahil', 'Tahir', 'Ubaidullah', 'Vasef', 'Waliullah', 'Yahya', 'Zaki', 'Arif',
        'Bilal', 'Chamanullah', 'Daud', 'Ehsan', 'Fazlullah', 'Gul', 'Hakim', 'Ibrahim', 'Jamshed', 'Khalilullah',
        'Latifullah', 'Momin', 'Nazir', 'Obaid', 'Pir', 'Qurban', 'Rahim', 'Samiullah', 'Tajuddin', 'Usman',
        'Vakil', 'Waris', 'Yasin', 'Zabih', 'Aslam', 'Bismillah', 'Chiragh', 'Dilawar', 'Eid', 'Farooz',
        'Herati', 'Kabuli', 'Mazar', 'Nangarhari', 'Panjshiri', 'Parwani', 'Samarqandi', 'Wardaki', 'Badakhshi',
        'Balkhi',
        'Dari', 'Farsi', 'Ghazni', 'Hazarajat', 'Istalif', 'Jowzjan', 'Kunar', 'Logar', 'Maimana', 'Nimruz',
        'Oruzgan', 'Parwan', 'Qandahar', 'Rostaq', 'Sarobi', 'Takhar', 'Uruzgan', 'Waras', 'Yawan', 'Zaranj',
        'Ahmadi', 'Alavi', 'Bahrami', 'Davlat', 'Emami', 'Farahi', 'Gulistani', 'Hashemi', 'Ibrahimi', 'Jafari',
        'Kazemi', 'Lahori', 'Mahdavi', 'Nasiri', 'Omidi', 'Parvizi', 'Qasemi', 'Rahimi', 'Sadeghi', 'Tavakoli',
        'Vahidi', 'Wahidi', 'Yazdani', 'Zamani', 'Abidi', 'Barani', 'Chaman', 'Danesh', 'Esfahani', 'Fahim',
        'Gharibi', 'Hosseini', 'Izadi', 'Jalali', 'Kermani', 'Lashgari', 'Mashhadi', 'Nadiri', 'Omidvar', 'Pour',
        'Qobadi', 'Rashidi', 'Shirazi', 'Tabrizi', 'Vahedi', 'Wahdat', 'Yaghoubi', 'Zahedi', 'Abbasi', 'Bonyadi',
        'Chitsaz', 'Dehqani', 'Eftekhari', 'Fouladi', 'Gorgani', 'Hamidi', 'Isfandiyari', 'Javan', 'Karimi', 'Lari',
        'Mojaddedi', 'Nabawi', 'Ostadi', 'Pahlavan', 'Qazvini', 'Ranjbar', 'Saberi', 'Tehrani', 'Vaziri', 'Waseqi',
        'Yasini', 'Zand', 'Ashna', 'Bahar', 'Choubineh', 'Daryaee', 'Ebrahimi', 'Farrokh', 'Golestani', 'Hakimi',
        'Iraj', 'Javanmard', 'Khorasani', 'Lavasan', 'Mirdamadi', 'Nouri', 'Ostad', 'Pirzadeh', 'Qomi', 'Rostami',
        'Safavi', 'Tousi', 'Vafaei', 'Wahhabi', 'Yousefi', 'Zarrabi', 'Abrishami', 'Bakhtiari', 'Chamran', 'Dolatabadi',
        'Eshghi', 'Faramarzi', 'Goudarzi', 'Hamedani', 'Imani', 'Jahan', 'Kashani', 'Lahijani', 'Mofidi', 'Nazari',
        'Olia', 'Pishva', 'Qashqai', 'Rahmani', 'Safari', 'Taba', 'Vahdati', 'Wahdat', 'Yazdi', 'Zarif',
        'Amini', 'Bozorg', 'Cheraghi', 'Darvish', 'Eskandari', 'Fars', 'Ghasemi', 'Hekmat', 'Ishraqi', 'Javid',
        'Khalaj', 'Lashkari', 'Moghadam', 'Nazemi', 'Oveisi', 'Pouya', 'Qahraman', 'Rashid', 'Sajjadi', 'Tajik',
        'Vafadar', 'Wafai', 'Yaghouti', 'Zakeri', 'Akbari', 'Bijan', 'Chooka', 'Daneshvar', 'Eshraghi', 'Fazeli',
        'Gilan', 'Haghighi', 'Irani', 'Jalili', 'Khomeini', 'Lotfi', 'Moshiri', 'Nadimi', 'Ostad', 'Parsi',
        'Qavami', 'Ranjbar', 'Salami', 'Tavassoli', 'Vaziri', 'Wafadar', 'Yazdan', 'Zarghami', 'Ardabili', 'Bahar',
        'Chitsaz', 'Deilami', 'Ebrahimi', 'Farahani', 'Gilan', 'Hosseinzadeh', 'Izadi', 'Jahanbin', 'Kashani',
        'Lashgari',
        'Mansouri', 'Nadimi', 'Ostad', 'Pahlavi', 'Qazvini', 'Rahnavard', 'Sadegh', 'Tabatabaei', 'Vahidi', 'Wahdat',
        'Yazdani', 'Zamani', 'Ahmadi', 'Bani', 'Chaman', 'Dari', 'Esfandiari', 'Farrokh', 'Gholami', 'Hashemi',
        'Imani', 'Jafari', 'Kazemi', 'Lahori', 'Mahdavi', 'Nasiri', 'Omidi', 'Parvizi', 'Qasemi', 'Rahimi',
        'Sadeghi', 'Tavakoli', 'Vahidi', 'Wahidi', 'Yazdani', 'Zamani', 'Abidi', 'Barani', 'Chaman', 'Danesh',
        'Esfahani', 'Fahim', 'Gharibi', 'Hosseini', 'Izadi', 'Jalali', 'Kermani', 'Lashgari', 'Mashhadi', 'Nadiri',
        'Omidvar', 'Pour', 'Qobadi', 'Rashidi', 'Shirazi', 'Tabrizi', 'Vahedi', 'Wahdat', 'Yaghoubi', 'Zahedi',
        'Abbasi', 'Bonyadi', 'Chitsaz', 'Dehqani', 'Eftekhari', 'Fouladi', 'Gorgani', 'Hamidi', 'Isfandiyari', 'Javan',
        'Karimi', 'Lari', 'Mojaddedi', 'Nabawi', 'Ostadi', 'Pahlavan', 'Qazvini', 'Ranjbar', 'Saberi', 'Tehrani',
        'Vaziri', 'Waseqi', 'Yasini', 'Zand', 'Ashna', 'Bahar', 'Choubineh', 'Daryaee', 'Ebrahimi', 'Farrokh',
        'Golestani', 'Hakimi', 'Iraj', 'Javanmard', 'Khorasani', 'Lavasan', 'Mirdamadi', 'Nouri', 'Ostad', 'Pirzadeh',
        'Qomi', 'Rostami', 'Safavi', 'Tousi', 'Vafaei', 'Wahhabi', 'Yousefi', 'Zarrabi', 'Abrishami', 'Bakhtiari',
        'Chamran', 'Dolatabadi', 'Eshghi', 'Faramarzi', 'Goudarzi', 'Hamedani', 'Imani', 'Jahan', 'Kashani', 'Lahijani',
        'Mofidi', 'Nazari', 'Olia', 'Pishva', 'Qashqai', 'Rahmani', 'Safari', 'Taba', 'Vahdati', 'Wahdat',
        'Yazdi', 'Zarif', 'Amini', 'Bozorg', 'Cheraghi', 'Darvish', 'Eskandari', 'Fars', 'Ghasemi', 'Hekmat',
        'Ishraqi', 'Javid', 'Khalaj', 'Lashkari', 'Moghadam', 'Nazemi', 'Oveisi', 'Pouya', 'Qahraman', 'Rashid',
        'Sajjadi', 'Tajik', 'Vafadar', 'Wafai', 'Yaghouti', 'Zakeri', 'Akbari', 'Bijan', 'Chooka', 'Daneshvar',
        'Eshraghi', 'Fazeli', 'Gilan', 'Haghighi', 'Irani', 'Jalili', 'Khomeini', 'Lotfi', 'Moshiri', 'Nadimi',
        'Ostad', 'Parsi', 'Qavami', 'Ranjbar', 'Salami', 'Tavassoli', 'Vaziri', 'Wafadar', 'Yazdan', 'Zarghami'
    ]


    # ================ Email section =====================
    domains = [
        "gmail.com", "yahoo.com", "outlook.com", "afghanmail.com", "mail.com"
    ]

    def username(self, gender=None):
        """Random Afghan-style username"""
        if gender == "female":
            first = random.choice(self.pashto_female_first_names).lower()
        elif gender == "male":
            first = random.choice(self.pashto_male_first_names).lower()
        else:
            first = random.choice(self.pashto_male_first_names + self.pashto_female_first_names).lower()

        last = random.choice(self.last_names).lower()
        number = str(random.randint(1, 999))
        return f"{first}.{last}{number}"

    def email(self, gender=None):
        """Full email address"""
        return f"{self.username(gender)}@{random.choice(self.domains)}"

# =================End of the email section ==============

    # ---------- BASIC PARTS ----------

    def first_name_male(self):
        return random.choice(self.pashto_male_first_names + self.tajik_male_first_names)

    def first_name_female(self):
        return random.choice(self.pashto_female_first_names + self.tajik_female_first_names)

    def last_name(self):
        return random.choice(self.last_names)

    def first_name(self):
        return random.choice([self.first_name_male(), self.first_name_female()])

    # ---------- FULL NAME ----------

    def name(self):
        gender = random.choice(["male", "female"])

        if gender == "male":
            prefix = random.choice(self.prefixes_male)
            first = self.first_name_male()
        else:
            prefix = random.choice(self.prefixes_female)
            first = self.first_name_female()

        last = self.last_name()
        suffix = random.choice(self.suffixes)

        return f"{prefix} {first} {last} {suffix}"



